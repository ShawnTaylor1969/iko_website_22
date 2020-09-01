from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from api_members.models import Member
from api_notifications.models import Notification
from api_configurations.models import Configuration
from api_spaces.models import Space
from .tables import MemberTable, SisterTable
from .forms import Member_EditForm, User_EditForm, Member_ReadForm, Member_Sister_Filter_Form, CreateUser_Login_Form, CreateUser_Member_Form, Edit_MemberForm, Edit_UserForm
from .utils import addToQueryString, createCommaDelimitedString, convertCommaDelimitedList, addZeros
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date
from dateutil.relativedelta import relativedelta

def SisterListView(request):
    template_name = "web_members/member_sisters.html"
    members = Member.objects.filter(status='ACTIVATED').order_by('user__first_name', 'user__last_name')
    members = members.exclude(type='INDEPENDENT')

    search = request.GET.get("search", "")
    if not search == "":
        # members = members.filter(Q(user__first_name__icontains=search) | \
        #                    Q(summary__icontains=search) | \
        #                    Q(body__icontains=search) | \
        #                    Q(comments__body__icontains=search))
        pass
    else:
        # name = request.GET.get("name", "")
        # if not name == "":
        #     members = members.filter(Q(first_name__icontains=name) | \
        #                             Q(last_name__icontains=name))

        pledge_class = request.GET.get("pledge_class", "")
        if not pledge_class == "":
            members = members.filter(pledge_class=pledge_class)

        graduation_year = request.GET.get("graduation_year", "")
        if not graduation_year == "":
            members = members.filter(graduation_year=graduation_year)

    table = SisterTable(members)
    context = {"table": table}
    return render(request, template_name, context)

def sisters_filters(request):
    template_name = 'web_members/member_sisters_filters.html'

    data = dict()
    if request.method == 'POST':
        filter_form = Member_Sister_Filter_Form(request.POST)

        if filter_form.is_valid():
            queryString = ""
            queryString = addToQueryString(queryString, 'search', filter_form.cleaned_data['search'])
            queryString = addToQueryString(queryString, 'name', filter_form.cleaned_data['name'])
            queryString = addToQueryString(queryString, 'pledge_class', filter_form.cleaned_data['pledge_class'])
            queryString = addToQueryString(queryString, 'graduation_year', filter_form.cleaned_data['graduation_year'])
            data['queryString'] = '/members/sisters' + queryString
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        filter_form = Member_Sister_Filter_Form(initial={'search': request.GET.get("search",""), \
                                                    'name': request.GET.get("name",""), \
                                                    'pledge_class': request.GET.get("pledge_class",""), \
                                                    'graduation_year': request.GET.get("graduation_year","")})
    context = {'filter_form': filter_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def MemberListView(request):
    template_name = "web_members/member_list.html"
    members = Member.objects.all().order_by('user__username')
    table = MemberTable(members)
    context = {"table": table}
    return render(request, template_name, context)

def MemberReadView(request, pk):
    template_name = 'web_members/member_read.html'
    data = dict()
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        return redirect(reverse('web_members:list'))
    else:
        member_form = Member_ReadForm(instance=member)
    context = {'member_form': member_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

# Used as part of the Site Administration
def MemberEditView(request, pk):
    template_name = 'web_members/member_edit.html'
    data = dict()
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member_form = Member_EditForm(request.POST, request.FILES or None, instance=member)
        user = member.user
        user_form = User_EditForm(request.POST, instance=user)
        if member_form.is_valid() and user_form.is_valid():
            member.save()
            user.save()
            return redirect(reverse('web_members:list'))
    else:
        member_form = Member_EditForm(instance=member)
        user_form = User_EditForm(instance=member.user)

    context = {'member_form': member_form, 'user_form': user_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

# Used by a member to update their own profile
def EditMemberView(request, pk):
    template_name = 'web_members/edit_member.html'
    data = dict()
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member_form = Edit_MemberForm(request.POST, request.FILES or None, instance=member)
        user = member.user
        user_form = Edit_UserForm(request.POST, instance=user)
        if member_form.is_valid() and user_form.is_valid():
            member.save()
            user.save()
            return redirect(reverse('home'))
    else:
        member_form = Edit_MemberForm(instance=member)
        user_form = Edit_UserForm(instance=member.user)

    context = {'member_form': member_form, 'user_form': user_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def MemberDeleteView(request, pk):
    template_name = 'web_members/modal_member_delete.html'
    data = dict()
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'member': member, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def MemberMultipleDeleteView(request):
    template_name = 'web_members/modal_member_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    members = Member.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for member in members:
            member.delete()
        data['form_is_valid'] = True
    else:
        context ={'members': members,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

# Create your views here.
class CreateUser_View(View):
    template_name = "web_members/signup.html"

    def get(self, request, *args, **kwargs):
        isErrorMessage = False
        errorMessage = ""

        user_form = CreateUser_Login_Form()
        type = "SISTER"
        pledge_class = date.today().year
        graduation_year =date.today().year
        birth_date_default = date.today() - relativedelta(years=17)

        member_form = CreateUser_Member_Form(initial={'type': type, 'pledgeClass': str(pledge_class), 'graduationYear': str(graduation_year), 'birth_date': birth_date_default})
        context = {"user_form": user_form, "member_form": member_form, "registered": False, "isErrorMessage": isErrorMessage, "errorMessage": errorMessage}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        isErrorMessage = False
        errorMessage = ""
        registered = False

        user_form = CreateUser_Login_Form(request.POST)
        member_form = CreateUser_Member_Form(request.POST)

        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()

            configurations = Configuration.objects.all()
            configuration = configurations.first()
            Notification.add_notification(notify_user=user, source_user=user, message="Welcome to the " + configuration.organization_name + " website!")
            member = member_form.save(commit=False)
            member.user = user
            member.created_dateTime = date.today()
            member.pledge_class = int(member_form.data['pledgeClass'])
            member.graduation_year = int(member_form.data['graduationYear'])
            member.save()
            registered = True

            # Create user space
            space_title = title=user.first_name + " " + user.last_name
            space = Space(title=space_title, summary=space_title, body=space_title, show_application_menu=False, show_space_menu=True, \
                            status='INACTIVE', admin_method='USER', admin_user=user, user_space=True, system_space=True)
            space.save()
        else:
            isErrorMessage = True
            errorMessage = user_form.errors
        context = {"user_form": user_form, "member_form": member_form, "registered": registered, "isErrorMessage": isErrorMessage, "errorMessage": errorMessage}
        return render(request, self.template_name, context)

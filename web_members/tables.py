import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_members.models import Member

class MemberTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    member = tables.TemplateColumn(template_name='web_members/avatar_sm.html', orderable=False)
    name = tables.Column(empty_values=())
    member_type = tables.Column(empty_values=())
    email = tables.Column(empty_values=())

    class Meta:
        model = Member
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "member", "name", "status", "member_type", "pledge_class", "graduation_year", "house_positions")

    def render_name(self, record):
        return format_html("<a href='{}'>{}</a>", "/members/" + str(record.pk) + "/read", record.user.first_name + " " + record.user.last_name)

    def render_email(self, record):
        return record.user.email

    def render_member_type(self, record):
        if record.type == "ALUMNI":
            return "Alumni"
        if record.type == "NEWBLOOD":
            return "New Blood"
        if record.type == "ACTIVE":
            return "Active"
        if record.type == "INDEPENDENT":
            return "Independent"
        return "Unknown"

class SisterTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    member = tables.TemplateColumn(template_name='web_members/avatar_sm.html', orderable=False)
    name = tables.Column(empty_values=())
    type_name = tables.Column(empty_values=())
    email = tables.Column(empty_values=())

    class Meta:
        model = Member
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "member", "name", "email", "type_name", "pledge_class", "graduation_year", "house_positions")

    def render_name(self, record):
        return format_html("<a href='{}'>{}</a>", "/members/" + str(record.pk) + "/read", record.user.first_name + " " + record.user.last_name)

    def render_email(self, record):
        return record.user.email

    def render_type_name(self, record):
        if record.type == "ALUMNI":
            return "Alumni"
        if record.type == "NEWBLOOD":
            return "New Blood"
        if record.type == "ACTIVE":
            return "Active"
        if record.type == "INDEPENDENT":
            return "Independent"
        return "Unknown"

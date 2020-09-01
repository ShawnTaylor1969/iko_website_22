import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_spaces.models import Space

class SpaceTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    description = tables.Column(empty_values=())
    administration = tables.Column(empty_values=())
    access = tables.Column(empty_values=())
    types_of_content = tables.Column(empty_values=())

    class Meta:
        model = Space
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "description", "status", "type", "administration", "access", "types_of_content", "created_dateTime" )

    def render_description(self, record):
        return format_html("<a href='{}'><strong>{}</strong><br><small>{}</a><br>slug: {}</small>", "/spaces/" + str(record.pk) + "/read", record.title, record.summary, record.slug)

    def render_administration(self, record):
        retval = ""
        try:
            if record.admin_method == "POSITION":
                retval = "Position based: " + record.admin_position.title;
            else:
                if record.admin_method == "USER":
                    retval = "Member based: " + record.admin_user.first_name + " " + record.admin_user.last_name;
                else:
                    retval = "Website Administrator"
        except Exception as e:
            pass
        return retval

    def render_access(self, record):
        retval = ""
        if record.public_access and record.private_access:
            retval = "Public and Private access"
        else:
            if record.public_access:
                retval = "Public access only"
            else:
                if record.private_access:
                    retval = "Private access only"
                else:
                    for position in record.restricted_to_positions.all():
                        if retval != "":
                            retval = retval + ", "
                        retval = retval + position.title;
                    for group in record.restricted_to_groups.all():
                        if retval != "":
                            retval = retval + ", "
                        retval = retval + group.title;
                    if retval == "":
                        retval = "None"
        return retval

    def render_types_of_content(self, record):
        retval = ""
        for content_type in record.content_types.all():
            if retval != "":
                retval = retval + ", "
            retval = retval + content_type.title;
        if retval == "":
            retval = "None"
        return retval

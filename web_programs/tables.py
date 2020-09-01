import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_programs.models import Program

class ProgramTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    description = tables.Column(empty_values=())
    access = tables.Column(empty_values=())

    class Meta:
        model = Program
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "description", "status", "type", "url", "access")

    def render_description(self, record):
        return format_html("<a href='{}'><strong>{}</strong><br><small>{}</small></a>", "/programs/" + str(record.pk) + "/read", record.title, record.summary)

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

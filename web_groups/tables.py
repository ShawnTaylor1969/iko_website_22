import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_groups.models import Group

class GroupTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    
    class Meta:
        model = Group
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "title", "positions")

    def render_title(self, record):
        return format_html("<a href='{}'>{}</a>", "/groups/" + str(record.pk) + "/read", record.title)

    def render_email(self, record):
        return record.user.email

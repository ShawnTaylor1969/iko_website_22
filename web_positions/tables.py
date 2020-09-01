import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_positions.models import Position

class PositionTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    title_link = tables.Column("Title", empty_values=())

    class Meta:
        model = Position
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "title_link", "is_top_five", "parent_position")

    def render_title_link(self, record):
        return format_html("<a href='{}'>{}</a>", "/positions/" + str(record.pk) + "/read", record.title)

import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_eventtypes.models import EventType

class EventTypeTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)

    class Meta:
        model = EventType
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "title")

import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_eventschedules.models import EventSchedule

class EventScheduleTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    type = tables.Column(empty_values=())

    class Meta:
        model = EventSchedule
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "title", "type", "organizer", "is_active")

    def render_title(self, record):
        return format_html("<a href='{}'>{}</a>", "/eventschedules/" + str(record.pk) + "/read", record.title)

    def render_type(self, record):
        return record.event_type.title

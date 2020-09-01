import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_calendars.models import Calendar

class CalendarTable(tables.Table):
    X = tables.TemplateColumn('<input name="opt_{{ record.pk }}" slug="{{ record.slug }}" pk="{{ record.pk }}" type="checkbox">', orderable=False)
    cover = tables.TemplateColumn('<a href="/eventschedules/{{ record.pk }}/list"><img src="{% if record.picture %}{{ record.picture.url }}{% else%}/static/img/calendar.svg{% endif %}" height="75px" width="75px"></a>')

    class Meta:
        model = Calendar
        template_name = "django_tables2/bootstrap4.html"
        fields = ("X", "cover", "title", "summary", "organizer")

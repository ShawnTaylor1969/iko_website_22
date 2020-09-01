import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_timelines.models import Timeline

class TimelineTable(tables.Table):
    media = tables.TemplateColumn(template_name='web_timelines/timeline_media.html', orderable=False, verbose_name='Timelinex', attrs={"th": {"style": "display:none"}})

    class Meta:
        model = Timeline
        template_name = "django_tables2/bootstrap4.html"
        fields = ("media",)

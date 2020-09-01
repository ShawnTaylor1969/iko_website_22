import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from api_walls.models import Wall

class WallTable(tables.Table):
    media = tables.TemplateColumn(template_name='web_walls/wall_media.html', orderable=False, verbose_name='Timeline', attrs={"th": {"style": "display:none"}})

    class Meta:
        model = Wall
        template_name = "django_tables2/bootstrap4.html"
        fields = ("media",)

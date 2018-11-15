from django.contrib import admin
from .models import Post, Client

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from django_object_actions import DjangoObjectActions


admin.site.register(Post)
# admin.site.register(Client)


@admin.register(Client)
class ClientAdmin(DjangoObjectActions, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'email', 'address')

    def generate_pdf(self, request, obj):
        html_string = render_to_string('blog/client_pdf.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Gerar PDF'
    generate_pdf.short_description = 'Clique para gerar o PDF dessa ordem de serviço'

    change_actions = ('generate_pdf',)

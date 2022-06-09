from django.views.generic.base import View
from django.http import FileResponse, HttpResponse
from django.conf import settings

from PIL import Image as PILImage
# -*- coding:utf-8 -*-
import io, os
from functools import partial
#Importamos algunas librerias: SimpleDocTemplate, es una plantilla de documento
#predefinida; getSampleStyleSheet, contiene una hoja de estilos de ejemplo;
#inch es una pulgada
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm

from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus.flowables import Image, ParagraphAndImage

PAGE_WIDTH = A4[0]
PAGE_HEIGHT = A4[1]

styles = getSampleStyleSheet()

from ..models.receipt import Receipt

ACTIVITIES = [
    {
        'date':'01/04/2022',
        'activities':[
            {
                "activity":"DEscripription activity",
                "time":4
            }
        ],
        'hours':4
    },
    {
        'date':'04/04/2022',
        'activities':[
            {
                "activity":"DEscripription activity 1",
                "time":3
            }
        ],
        'hours':2
    }    
]


def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold', 11)
    # canvas.drawInlineImage(empresa.logo.path, 40, PAGE_HEIGHT - 80, 65, 65)
    canvas.drawString(75, PAGE_HEIGHT - 40, 'Juan Perex')
    canvas.setFont('Helvetica', 9)
    canvas.drawString(75, PAGE_HEIGHT - 54, 'Urb. Tupac Amaru 9000')
    canvas.drawString(75, PAGE_HEIGHT - 68, 'San Sebastian Cusco Peru')
    canvas.drawString(75, PAGE_HEIGHT - 82, 'Telf: +51 935000600')
    canvas.drawString(75, PAGE_HEIGHT - 96, 'Correo: juan@gmail.com')
    # canvas.setFont('Times-Roman', 10)
    canvas.setFont('Helvetica', 10)
    canvas.drawCentredString(450, PAGE_HEIGHT-45, 'RUC: 10888886440')
    canvas.drawCentredString(450, PAGE_HEIGHT-60, 'INVOICE')
    canvas.drawCentredString(450, PAGE_HEIGHT-75, '20220001')
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch, "Página %d / %s" %(doc.page, 8))
    canvas.restoreState()


class MyReceiptView(View):

    def get(self, request, pk, *args, **kwargs):
        buffer = io.BytesIO()
        receipt = Receipt.objects.get(id=pk)
        print('VVVVVVVVVVVVVVVVVVV')
        print(receipt)
        #Creamos un documento basándonos en una plantilla
        doc = SimpleDocTemplate(buffer, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        story = []
        estilo = styles['Normal']
        # estilo.fontSize=10
        story.append(Spacer(0, 20))
        story.append(Paragraph("BILL TO:", styles['Heading4']))
        story.append(Paragraph("Christiane Castellon", estilo))
        story.append(Paragraph("Easymgt", estilo))
        story.append(Paragraph("2681 sw 156 pl", estilo))
        story.append(Paragraph("Miami, FL, 33185", estilo))
        story.append(Paragraph("United States", estilo))
        story.append(Paragraph("Fecha: 15-04-2022", estilo))
        story.append(Spacer(0, 12))
        
        #Definimos un estilo
        header = ['#', 'Description', 'Hours', 'Amount']
        body = self.table_body(ACTIVITIES)
        body.insert(0, header)
        table=Table(body, colWidths=([1*cm, 11*cm, 2.2*cm, 2.2*cm]))
        table.setStyle(TableStyle([('BACKGROUND',(0,0),(4,0), colors.lightblue),('TEXTCOLOR',(0,0),(3,0), colors.black)]))
        
        story.append(table)
        story.append(Spacer(0, 12))
        
        doc.build(story, onFirstPage=partial(myFirstPage), onLaterPages = myLaterPages)
        
        response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = "attachment; filename=Cotización {}.pdf".format(cotizacion.cliente.numero,)
        response['Content-Disposition'] = 'attachment; filename=Receipt.pdf'
        response.write(buffer.getvalue())
        buffer.close()
        return response

    def table_body(self, activities):
        body = []
        style = ParagraphStyle('BodyText')
        style.alignment = 0
        style.fontSize = 9
        normal = styles['Normal']
        for index, d in enumerate(activities, start=1):
            body.append([index, Table(self.build_descriptions(d, normal)) , d['hours'], ''])
        h5 = styles['Heading5']
        h5.alignment = 2
        total_hours = sum([x['hours'] for x in activities])
        totales = ['', Paragraph('Total', h5), total_hours, '']
        body.append(totales)
        return body

    def build_descriptions(self, item, style):
        lis = [[Paragraph(item['date'], styles['Heading4'])]]
        for d in item['activities']:
            lis.append([Paragraph(d['activity'], style)])
        return lis
    

# http://menteleal.blogspot.com/2014/02/report-lab-platypus-entendiendo-la.html


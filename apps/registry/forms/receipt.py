
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Field

from django import forms

from ..models.receipt import Receipt
from apps.utils.forms import smtSave, btnCancel, btnReset


class ReceiptModelForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ("date", "discount", "total")
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre de la Receipt'}),
        # }

    def __init__(self, *args, **kwargs):
        super(ReceiptModelForm, self).__init__(*args, **kwargs)
        # self.fields['imagen'].help_text = "Las dimensiones de la imagen deben ser 900px X 650px"
        self.fields['date'].label = "Fecha"

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.helper.form_class = 'js-validate'
        self.helper.layout = Layout(
            Div(Field('date', css_class='input-required')),
            Div(Field('discount')),
            Div(Field('total')),
            Row(
                FormActions(
                    Div(
                        smtSave(),
                        btnCancel(),
                        css_class='btn-group')
                ),
            ),
        )


from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Field

from django import forms

from ..models.service import Service
from apps.utils.forms import smtSave, btnCancel, btnReset


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("code", "description", "cost", 'is_public')
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'Ingrese el código del servicio'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese la descripción del servicio'}),
            'cost': forms.NumberInput(attrs={'placeholder': 'Ingrese el costo', 'step':'any'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServiceModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(Field('code', css_class='input-required')),
            Div(Field('description')),
            Div(Field('cost')),
            Div(Field('is_public')),
            Row(
                FormActions(
                    Div(
                        smtSave(),
                        btnReset(),
                        btnCancel(),
                        css_class='btn-group')
                ),
            ),
        )

from django import forms
from django.forms.widgets import Select
from .models import Curator, CuratorQuartCosts

class CuratorForm(forms.ModelForm):
    class Meta:
        model = Curator
        fields = ('title', 'total_for_all_quart')
        labels = {'title': 'Название куратора',
                'total_for_all_quart': 'сумма по одному куратору за 4 квартала' 
        }
        widgets = {'curator': Select(attrs={'size': 8})}

class CuratorQuartCostsForm(forms.ModelForm):
    quart_0 = forms.FloatField(label = "Квартал 1")
    quart_1 = forms.FloatField(label = "Квартал 2")
    quart_2 = forms.FloatField(label = "Квартал 3")
    quart_3 = forms.FloatField(label = "Квартал 4")
    delete = forms.BooleanField(label = 'Удалить', required=False)
    
    class Meta:
        model = CuratorQuartCosts
        fields = ('curator', )
        labels = {
            'curator':'Куратор: '
        }
        widgets = {'cqc': Select(attrs={'size': 8})}

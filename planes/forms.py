from django.forms import ModelForm
from django.forms.widgets import Select
from .models import Curator

class CuratorForm(ModelForm):
    class Meta:
        model = Curator
        fields = ('title', 'total_for_all_quart')
        labels = {'title': 'Название куратора',
                'total_for_all_quart': 'сумма по одному куратору за 4 квартала' 
        }
        widgets = {'curator': Select(attrs={'size': 20})}

from django import forms
from .models import Vagas

class dadosVagas(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = ['nome_gestor', 'abertura_para_o_departamento', 'nome_vaga',
                   'data_inicio', 'quantidades_de_vagas', 'motivo_vaga',
                   'nome_do_substituido', 'sexo', 'escola', 'observacao']
        widgets = {
            'nome_gestor': forms.TextInput(attrs={'class': 'form-control'}),
            'abertura_para_o_departamento': forms.Select(attrs={'class': 'form-control'}),
            'nome_vaga': forms.TextInput(attrs={'class': 'form-control'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'quantidades_de_vagas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'motivo_vaga': forms.Select(attrs={'class': 'form-control'}),
            'nome_do_substituido': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'escola': forms.Select(attrs={'class': 'form-control'}),
            'observacao': forms.TextInput(attrs={'class': 'form-control', 'rows': 5})
        }
        
class avaliacaoRH(forms.ModelForm):
    class Meta:
        model= Vagas
        fields = ['status', 'observacao_rh', 'ativa']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'observacao_rh': forms.TextInput(attrs={'class': 'form-control', 'rows': 4}),
            'ativa': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
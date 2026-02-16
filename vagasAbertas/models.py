from django.db import models
from django.contrib.auth.models import User

class Vagas(models.Model):
    STATUS_CHOICES = [
        ('em_analise', 'Em Analise'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado')
    ]
    DEPARTAMENTOS = [
            ('comercial', 'Comercial'),
            ('compras', 'Compras'),
            ('diretoria', 'Diretoria'),
            ('financeiro', 'Financeiro'),
            ('rh', 'Recursos Humanos'),
            ('obra', 'Obras'),
            ('orcamento', 'Orçamento'),
            ('planejamento', 'Planejamento Processos e Qualidade'),
            ('producao', 'Produção'),  
            ('projetos', 'Projetos'),
            ('ti', 'Tecnologia de Informação')
        ]
    
    #solicitante
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome_gestor = models.CharField(max_length=200, blank=True)
    data_solic = models.DateField(auto_now_add=True)
    abertura_para_o_departamento = models.CharField(max_length=200, choices=DEPARTAMENTOS)

    #detalhes da vaga
    nome_vaga = models.CharField(max_length=200, blank=True, help_text="Soldador, Projetista, etc.")
    data_inicio = models.DateField()
    quantidades_de_vagas = models.PositiveBigIntegerField(help_text="Digite a quantidade de vagas que gostaria de abrir, exemplo: 2")
    motivo_vaga = models.CharField(max_length=100, choices=[
        ('substitucao', 'Substituição'),
        ('nova_vaga', 'Novas Vagas')
    ])

    #informação de substituto
    nome_do_substituido = models.CharField(max_length=200)
    sexo = models.CharField(max_length=100, choices=[
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('naoexp', 'Prefiro não especificar.')
    ])
    escola = models.CharField(max_length=100, choices=[
        ('fundamental', 'Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Superior'),
        ('tecnico', 'Técnico')
    ])
    observacao = models.TextField(blank=False, help_text="Digite aqui alguma observação que queira fazer sobre o candidato substituto, exemplo: 'O candidato tem experiência prévia na função.'")

    # Controle de criação
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = 'em_analise')
    ativa = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    observacao_rh = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"{self.nome_vaga} - {self.departamento}"
        
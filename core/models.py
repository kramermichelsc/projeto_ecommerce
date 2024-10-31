from django.db import models

from stdimage.models import StdImageField

class Produtos(models.Model):
    codigo = models.IntegerField('Código Produto', primary_key=True, auto_created=True, unique=True, blank=True)
    nome = models.CharField('Nome Produto', max_length=100, blank=False)
    descricao = models.CharField('Descrição', max_length=100, blank=False)
    quantidade = models.IntegerField('Quantidade', blank=False)
    valor = models.DecimalField('Valor', max_digits=9, decimal_places=2)
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb':(125,125)})

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    cpf = models.IntegerField('CPF', primary_key=True, unique=True, blank=False)
    nome = models.CharField('Nome do Cliente', max_length=100, blank=False)
    data_nascimento = models.DateField('Data deNascimento')
    codigo_produto = models.OneToOneField(Produtos, on_delete=models.CASCADE)
    #codigo_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    email = models.EmailField('E-mail', max_length=100, blank=False)
    telefone = models.BigIntegerField('Telefone', help_text='Inserir númro com DD')

    def __str__(self):
        return self.nome





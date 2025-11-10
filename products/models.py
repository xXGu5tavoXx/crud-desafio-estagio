from django.db import models

class Produto(models.Model):
    # O campo 'id' é criado automaticamente pelo Django
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    # DecimalField é o tipo mais adequado para valores monetários (preço)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        # Define o nome da tabela no banco de dados como 'produtos'
        db_table = 'produtos'

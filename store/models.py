from django.db import models
from django.contrib.auth.models import User 

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    imagem = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    completo = models.BooleanField(default=False) 
    id_transacao = models.CharField(max_length=100, null=True)
    @property
    def get_cart_total(self):
        itens = self.itempedido_set.all()
        total = sum([item.get_total for item in itens])
        return total

    @property
    def get_cart_items(self):
        itens = self.itempedido_set.all()
        total = sum([item.quantidade for item in itens])
        return total
    
    

    def __str__(self):
        return str(self.id)

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        return self.produto.preco * self.quantidade
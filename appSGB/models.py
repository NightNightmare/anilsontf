from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)

class Livro(models.Model):
    DISPONIBILIDADE_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
    ]

    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    ano_publicacao = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    disponibilidade = models.CharField(max_length=20, choices=DISPONIBILIDADE_CHOICES)
    def __str__(self):
        return self.titulo




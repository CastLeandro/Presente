from tortoise import fields
from tortoise.models import Model

class Usuario(Model):
    id = fields.IntField(primary_key=True)
    user = fields.CharField(max_length=100, unique=True)
    senha = fields.CharField(max_length=100)

    def __str__(self):
        return self.user
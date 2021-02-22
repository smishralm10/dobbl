from django.db import models
from uuid import UUID

# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length=32)
    client_id = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)

class Strategy(models.Model):
    name = models.CharField(max_length=32)

class Order(models.Model):
    id = models.UUIDField(UUID, primary_key=True)
    transaction_type = models.CharField(max_length=3)
    qty = models.IntegerField()
    price = models.FloatField()
    broker = models.ForeignKey(Broker)
    strategy = models.ForeignKey(Strategy)
    intrument = models.CharField(max_length=255)



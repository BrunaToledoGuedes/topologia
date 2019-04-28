from django.db import models
from django.utils import timezone

class Rede(models.Model):
    NomeRede =  models.CharField(max_length=30)
    RoteadorIP1 = models.CharField(max_length=20)
    RoteadorNetmask1 = models.CharField(max_length=20)
    RoteadorIP2 = models.CharField(max_length=20)
    RoteadorNetmask2 = models.CharField(max_length=20)
    HostIP1   = models.CharField(max_length=20)
    HostIP2   = models.CharField(max_length=20)
    HostIP3   = models.CharField(max_length=20)
    HostIP4   = models.CharField(max_length=20)
    HostNetmask1   = models.CharField(max_length=20)
    HostNetmask2   = models.CharField(max_length=20)
    HostNetmask3   = models.CharField(max_length=20)
    HostNetmask4   = models.CharField(max_length=20)
    HostGateway1   = models.CharField(max_length=20)
    HostGateway2   = models.CharField(max_length=20)
    HostGateway3   = models.CharField(max_length=20)
    HostGateway4   = models.CharField(max_length=20)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.NomeRede
		

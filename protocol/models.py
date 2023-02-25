from django.db import models


class IndexInfo(models.Model):
    objects = None
    phone = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)


class MetamaskAccount(models.Model):
    objects = None
    user_wallet_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    objects = None
    account = models.CharField(max_length=250, null=True, blank=True)
    res_hash = models.CharField(max_length=250, null=True, blank=True)
    data = models.CharField(max_length=5000, null=True, blank=True)


class IPFS(models.Model):
    objects = None
    file = models.FileField(null=True, blank=True, default=None)
    result_hash = models.CharField(max_length=250, null=True, blank=True)
    account = models.CharField(max_length=250, null=True, blank=True)
    text = models.CharField(max_length=5000, null=True, blank=True)
    hash_ipfs = models.CharField(max_length=250, null=True, blank=True)



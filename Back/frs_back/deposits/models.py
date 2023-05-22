from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    id = models.IntegerField(primary_key=True)
    fin_prdt_cd = models.TextField(unique=True)
    dcls_month = models.CharField(max_length=6)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField(null = True)
    dcls_strt_day = models.CharField(max_length=8)

class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

    class Meta:
        unique_together = ['fin_prdt_cd', 'intr_rate_type_nm', 'save_trm']


class SavingProducts(models.Model):
    id = models.IntegerField(primary_key=True)
    fin_prdt_cd = models.TextField(unique=True)
    dcls_month = models.CharField(max_length=6)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField(null = True)
    dcls_strt_day = models.CharField(max_length=8)

class SavingOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(SavingProducts,on_delete=models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    rsrv_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
    
    class Meta:
        unique_together = ['fin_prdt_cd', 'intr_rate_type_nm', 'save_trm']
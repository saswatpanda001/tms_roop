from django.db import models
from django.utils import timezone
# Create your models here.


class items(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class spent(models.Model):
    datetime = models.DateTimeField(default=timezone.now, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    spent_on = models.ForeignKey(items,on_delete=models.SET_NULL, blank=True, null=True)
    item_category = models.ForeignKey(category,on_delete=models.SET_NULL, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)



    def save(self, *args, **kwargs):
        if self.item_name != self.spent_on.name:
            self.item_name = self.spent_on.name
        if self.category_name != self.item_category.name:
            self.category_name = self.item_category.name
            
        return super().save(*args, **kwargs)

    

    def __str__(self):
        return f"{str(self.datetime)[:10]}- {self.spent_on.name} - {str(self.amount)}"  


    
from django.db import models

class CustomerQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Customer queries"

    def __str__(self):
        return self.name
    
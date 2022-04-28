from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'categories'

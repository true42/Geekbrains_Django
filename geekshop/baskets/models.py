from django.db import models

from authapp.models import User
from mainapp.models import Product

#
# class BasketsQuerySet(models.QuerySet):
#     def delete(self, *args, **kwargs):
#         for item in self:
#             item.product.quantity +=item.quantity
#             item.product.save()
#         super(BasketsQuerySet, self).delete(*args, **kwargs)
#

class Baskets(models.Model):
    # objects = BasketsQuerySet.as_manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        baskets = Baskets.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        baskets = Baskets.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    # def delete(self, using=None, keep_parents=False, *args, **kwargs):
    #     self.product.quantity +=self.quantity
    #     self.save()
    #     super(Baskets, self).delete(*args, **kwargs)
    #
    #
    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
    #     if self.pk:
    #         get_item = self.get_item(int(self.pk))
    #         self.product.quantity -= self.quantity-get_item
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(Baskets, self).save(*args, **kwargs)


    @staticmethod
    def get_item(pk):
        return Baskets.objects.get(pk=pk).quantity


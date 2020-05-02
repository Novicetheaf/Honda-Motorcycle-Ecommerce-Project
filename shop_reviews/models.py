from django.db import models
from django.utils import timezone


# Create your models here.
class ShopReview(models.Model):
      """
      Customers Reviews
      """
      review_title = models.CharField(max_length=100)
      reviewer_name = models.CharField(default='', max_length=50)
      review_description = models.TextField(max_length=200)
      review_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
      review_views = models.IntegerField(default=0)

      def __unicode__(self):
          return self.review_title

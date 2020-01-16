from django.db import models
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
import mptt


class Category(MPTTModel):
    """
    Simple model for categorizing entries.
    """

    title = models.CharField(
        ('title'), max_length=255)
    is_leaf = models.BooleanField(default=True)

    parent = TreeForeignKey(
        'self',
        related_name='children',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name=('parent category'))

    @property
    def has_children(self):
        return len(self.get_children()) > 0

    def save(self, *args, **kwargs):
        if self.is_leaf_node():
            self.is_leaf = True
        else:
            self.is_leaf = False
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # class Meta:
    #     """
    #     Category's meta informations.
    #     """
    #     ordering = ['title']
    #     verbose_name = _('category')
    #     verbose_name_plural = _('categories')

    class MPTTMeta:
        """
        Category MPTT's meta informations.
        """
        order_insertion_by = ['title']


mptt.register(Category, order_insertion_by=['title'])

DELIVERY_CHOICES = [

        ('Immediate', 'Immediate'),
        ('Standard', 'Standard'),
        ('Advanced', 'Advanced'),


]


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Image')
    title = models.CharField(max_length=34)
    desc = models.TextField(max_length=50)
    our_price = models.FloatField(null=True, blank=True)
    mandi_price = models.FloatField(blank=True)
    status = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='Standard')
    Standard_availability = models.BooleanField(null=True)
    Immediate_availability = models.BooleanField(null=True)
    Advanced_availabilty = models.BooleanField(null=True)

    class Meta:
        db_table = "Product"

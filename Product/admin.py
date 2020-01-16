
from django.contrib import admin
from django.utils.html import mark_safe
from mptt.admin import DraggableMPTTAdmin

from .models import  Category, Product

admin.site.site_header = 'Blog Admin'


class CategoryAdmin(DraggableMPTTAdmin):
    fields = ('title',)
    list_display = ('indented_title', 'tree_actions', 'title',
                    )
    list_filter = ('parent',)
    list_display_links = (
                             'indented_title',
                         ),
    expand_tree_by_default = True


from django import forms

from django.contrib.admin.widgets import FilteredSelectMultiple


class EquipmentModelForm(forms.ModelForm):
    pizzas = forms.ModelMultipleChoiceField(
        queryset=Category.objects.filter(is_leaf=False),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=('Pizzas'),
            is_stacked=False

        )
    )
class EquipmentModelForm(forms.ModelForm):
    pizzas = forms.ModelMultipleChoiceField(
        queryset=Category.objects.filter(is_leaf=False),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=('Pizzas'),
            is_stacked=False
        ))


admin.site.register(Category, CategoryAdmin, list_display_links=('indented_title',), )

admin.site.register(Product)


class Product_Admin(admin.ModelAdmin):
 search_fields = ['title']

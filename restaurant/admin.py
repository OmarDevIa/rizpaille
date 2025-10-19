from django.contrib import admin
from .models import Meal,OrderTransaction 
# Register your models here.

from django.utils.html import format_html
from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """
    Admin View for Meal
    description: The description of the meal admin.
    Author: Omar
    """
    list_display = ('name', 'description', 'price', 'available', 'stock', 'image_tag')
    search_fields = ('name', 'description')

    def image_tag(self, obj):
        if obj.image:  # Vérifie que l'image existe
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "Pas d'image"

    image_tag.short_description = 'Aperçu'


@admin.register(OrderTransaction)
class OrderTransactionAdmin(admin.ModelAdmin):
    list_display = ('meal', 'customer', 'amount', 'status', 'created_at')

    search_fields = ('meal', 'customer',"amount","status")


from django.contrib import admin
from .models import *

class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ['Acknowledge']
    search_fields = ['Email']
    list_display = ['Email', 'Acknowledge']


# Register your models here.
admin.site.register(Newsletter,NewsletterAdmin)
admin.site.register(Meals)
admin.site.register(Category)
admin.site.register(AllItems)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Contact)
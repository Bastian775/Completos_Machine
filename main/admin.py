from django.contrib import admin
from .models import  Usuario, Completo
# Register your models here.

class Completoadmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio')
    search_fields = ('nombre', 'tipo')
    list_per_page = 10

admin.site.register(Usuario)
admin.site.register(Completo, Completoadmin)
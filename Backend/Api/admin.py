from django.contrib import admin
from .models import User, Fichier, Categorie, Classe

# Register your models here.

admin.site.register(User)
admin.site.register(Fichier)
admin.site.register(Categorie)
admin.site.register(Classe)
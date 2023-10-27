from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Fichier(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='fichiers/')
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
    
class Classe(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
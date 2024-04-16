from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    Brief = models.TextField(default="Add the required text brief")
    roles = (
        ('ui/ux', 'ui/ux'),
        ('frontend', 'frontend'),
        ('backend', 'backend'),
        ('product-manager', 'product-manager')
    )
    industries = (
        ('Technology', 'techology'),
        ('Fashion', 'fashion'),
        ('Food & Beverages', 'food & beverages'),
        ('Health & wellness', 'health & wellness'),
        ('Entertainment', 'entertainment'),
        ('Travel & hospitality', 'travel & hospitality')
    )
    difficulties = (
        ('Easy', 'easy'),
        ('Intermidiate', 'intermidiate'),
        ('Hard', 'hard'),
    )
    Role = models.CharField(max_length=200, choices=roles)
    Industry = models.CharField(max_length=200, choices=industries)
    Difficulty = models.CharField(max_length=200, choices=difficulties)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

class Taskgenerator(models.Model):
    roles = (
        ('ui/ux', 'ui/ux'),
        ('frontend', 'frontend'),
        ('backend', 'backend'),
        ('product-manager', 'product-manager')
    )
    industries = (
        ('Technology', 'techology'),
        ('Fashion', 'fashion'),
        ('Food & Beverages', 'food & beverages'),
        ('Health & wellness', 'health & wellness'),
        ('Entertainment', 'entertainment'),
        ('Travel & hospitality', 'travel & hospitality')
    )
    difficulties = (
        ('Easy', 'easy'),
        ('Intermidiate', 'intermidiate'),
        ('Hard', 'hard'),
    )
    Role = models.CharField(max_length=200, choices=roles)
    Industry = models.CharField(max_length=200, choices=industries)
    Difficulty = models.CharField(max_length=200, choices=difficulties)

    Brief = models.TextField(editable=False, default='add a brief')

    


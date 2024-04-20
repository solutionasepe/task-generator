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
    duration = (
        ('1 day', '1 day'),
        ('1 week', '1 week'),
        ('1 month', '1 month')
    )
    Role = models.CharField(max_length=200, choices=roles)
    Industry = models.CharField(max_length=200, choices=industries)
    Difficulty = models.CharField(max_length=200, choices=difficulties)
    Duration = models.CharField(max_length=200, default="pick the duration you want to work on", choices=duration)

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
    duration = (
        ('1 day', '1 day'),
        ('1 week', '1 week'),
        ('1 month', '1 month')
    )
    Role = models.CharField(max_length=200, choices=roles)
    Industry = models.CharField(max_length=200, choices=industries)
    Difficulty = models.CharField(max_length=200, choices=difficulties)
    Duration = models.CharField(max_length=200, default="pick the duration you want to work on", choices=duration)
    Brief = models.TextField(editable=False, default='add a brief')

    


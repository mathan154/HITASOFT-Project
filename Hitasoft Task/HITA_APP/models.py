from django.db import models

# Create your models here.
class Task(models.Model):
    
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    
    PRIORITY_CHOICES = [ ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    
    STATUS_CHOICES = [ ('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

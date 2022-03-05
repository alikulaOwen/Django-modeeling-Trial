from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.



class Document(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    content = models.TextField()
    comment = models.ForeignKey('Comment', related_name='document', on_delete=models.CASCADE)
    notification = models.ForeignKey('Notification', related_name='document', on_delete=models.CASCADE)

    def clean(self):
        from django.utils.html import strip_tags
        cleaned_content = strip_tags(self.content)
        return self.cleaned_content
        ###
       
    def __str__(self):
        return self.created_by, self.date_created, self.date_modified
        


class ProteinSequence(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    amino = models.TextField()
    dna_string = models.TextField()
    comment = models.ForeignKey('Comment', related_name='protein_sequence', null= True,on_delete=models.CASCADE)
    notification = models.ForeignKey('Notification', related_name='protein_sequence', null=True, on_delete=models.CASCADE)

    #validates if dna string is 3 time amino string
    def clean(self):
        from django.core.exceptions import ValidationError
        dna_len =len(self.dna_string)
        amino_len = len(self.amino)
        if  dna_len != 3 * amino_len :
            raise ValidationError('Invalid dna string. it is not three times amino')

    def save(self, *args, **kwargs):
        super(ProteinSequence, self).save(*args, **kwargs)

class Comment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    content = models.TextField()
    notification = models.ForeignKey('Notification', related_name='comment', on_delete=models.CASCADE)
    
    
    def clean(self):
        from django.utils.html import strip_tags
        cleaned_content = strip_tags(content)
        return str(self.cleaned_content)

    def __str__(self):
        return self.created_by, self.date_created, self.date_modified




class Link(models.Model):
    link =models.TextField()
    notification = models.ForeignKey('Notification', related_name='link', on_delete=models.CASCADE)

    def __str__(self):
        return self.link, self.message, self.icon_Name




class NotificationType(models.Model):
    NOTIFICATION_TYPE = (
        ('Link', 'Link'),
        ('Static', 'Static'),
        ('System', 'System'),
    )
    NotificationType = models.CharField(max_length=25, choices=NOTIFICATION_TYPE)
    #slug = models.SlugField(max_length=255, unique = True)


    def __str__(self):
        return self.NotificationType


class Notification(models.Model):
    notification_type = models.ForeignKey(NotificationType, related_name='notification', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    icon_name= models.CharField(max_length=25)
    
   
    # notification_type = models.OneToOneField(NotificationType, on_delete=models.CASCADE)
  
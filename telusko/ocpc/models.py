
from django.db import models

class Contest(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#000000') 
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=100)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='universities')
    def __str__(self):
        return self.name
    
class Coach(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Female', 'Female'), ('Male', 'Male')])
    official_phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    tshirt_size = models.CharField(max_length=20, choices=[
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('not required', 'T-Shirt is not required')
    ])
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='teams')
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='teams')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    full_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Female', 'Female'), ('Male', 'Male')])
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    tshirt_size = models.CharField(max_length=20, choices=[
        ('XS', 'XS'), 
        ('S', 'S'), 
        ('M', 'M'), 
        ('L', 'L'), 
        ('XL', 'XL'), 
        ('XXL', 'XXL'), 
        ('not required', 'T-Shirt is not required')
    ])

    def __str__(self):
        return f"{self.full_name} - {self.team.name}"

class Document(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='document')
    file = models.FileField(upload_to='document_upload/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
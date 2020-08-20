from django.db import models

# Create your models here.
class Varsity(models.Model):
    varsity_id=models.AutoField(primary_key=True)
    univarsity_name=models.CharField(max_length=100, help_text='Enter varsity full name (e.g. Dhaka University')
    univarsity_nickname=models.CharField(max_length=10, help_text='Enter varsity nickname (e.g. DU/BUET/AUST)')
    foundation=models.IntegerField(help_text='Enter foundation date (e.g. 1921)')
    location=models.CharField(max_length=20, help_text='Enter district (e.g. Dhaka)')
    division=models.CharField(max_length=20, help_text='Enter division (e.g. Dhaka)')
    specailization=models.CharField(max_length=50, help_text='Enter speciality  (e.g. Engineering/Medical/Agricultural)')
    phdgranting=models.CharField(max_length=10, help_text='Enter PhD availability(e.g Yes/No)')
    category=models.CharField(max_length=20, help_text='Enter Public/Private/International')
    link=models.CharField(max_length=100, help_text='Enter varsity website (e.g. https://www.buet.ac.bd)')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['univarsity_name', 'univarsity_nickname'], name='name_nick')
        ]
        ordering=['univarsity_name']

    def __str__(self):
        return self.univarsity_name+','+self.univarsity_nickname
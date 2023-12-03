from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfle(AbstractUser):
    """ Обыкновенный пользователь. """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]


    date_of_birth = models.DateField(blank=False)
    photo = models.ImageField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)



class Representative(models.Model):
    """ Представитель больницы. """
    # hospital = 
    # 

    pass

class AuthorReview(UserProfle):
    """ Автор отзыва. """

    pass

class AuthorRecord(Representative):
    """ Автор записи. """
    pass

from django.db import models
# from user.models import User
# from account import models

# Create your models here.

class MainCategory(models.Model):

    """

    We will store our main Categories Like :
    1. Study 
    2. Sport
    3. Hobbies
    ...

    """
    name = models.CharField(max_length = 50)

class SubCategory(models.Model):

    """
    We will user`s custom categories like i.g : 
    1. Algorithm
    ...

    """
    name = models.CharField(max_length = 50)
    is_active = models.BooleanField(default=True)
    main_id = models.ForeignKey(MainCategory, on_delete = models.CASCADE, related_name = 'SubCategories')
    # user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'UsersCategories')

class Activity(models.Model):

    """
    #
    """
    start_time = models.PositiveSmallIntegerField(blank=False, null=False)
    end_time = models.PositiveSmallIntegerField(blank=False, null=False)
    date = models.DateField() # date of the activity itself
    modified_time = models.DateTimeField()
    focus_percentage = models.PositiveSmallIntegerField()
    description = models.TextField()
    sub_category_id = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    main_category_id = models.ForeignKey(MainCategory, on_delete = models.CASCADE)

    #day_of_the_week = models.PositiveSmallIntegerField()
    # user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'UsersCategories')



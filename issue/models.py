from django.db import models
# from accounts.models import Account
# from category.models import Category

# Create your models here.
class Incharge (models.Model):
    incharge_name   = models.CharField(max_length=100, unique=True)
    description     = models.TextField(max_length=300, blank=True)
    images          = models.ImageField(upload_to='photos/products', blank=True,)
    is_available    = models.BooleanField(default=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.incharge_name

class Room (models.Model):
    incharge_name   = models.ForeignKey(Incharge, on_delete=models.DO_NOTHING, blank=True, null=True)
    room_name       = models.CharField(max_length=100, blank=True, unique=True)
    room_no         = models.IntegerField(unique=True)
    description     = models.TextField(max_length=300, blank=True)
    images          = models.ImageField(upload_to='photos/products', blank=True,)
    is_available    = models.BooleanField(default=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_name


class Token (models.Model):
    token_name      = models.CharField(max_length=100, blank=True)
    room            = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    tok_no          = models.IntegerField(null=True)
    is_priority     = models.BooleanField(default=False)
    is_called       = models.BooleanField(default=False)
    is_served       = models.BooleanField(default=False)
    is_missed       = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add=True)
    call_time       = models.DateTimeField(auto_now_add=True)
    served_time     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token_name

class Display_call (models.Model):
    d_room_no       = models.CharField(max_length=100, blank=True, unique=True)
    d_tok_no       = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.d_room_no

from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
Type_Choices = (
    ('Bedsitter', 'BEDSITTER'),
    ('Single-room', 'SINGLE-ROOM'),
    ('Double-room', 'DOUBLE-ROOM'),
    ('Apartment', 'APARTMENT'),
    ('1-bedroom', '1-BEDROOM'),
    ('2-bedroom', '2-BEDROOM'),
    ('3-bedroom', '3-BEDROOM'),
    ('4-bedroom', '4+BEDROOM'),
    ('Hostel', 'HOSTEL'),
)

Extra_Choices = (
    ('Parking', 'PARKING'),
    ('Drawers', 'DRAWERS'),
    ('Sink', 'SINK'),
    ('Electricity', 'ELECTRICITY'),
    ('Security', 'SECURITY'),
    ('Wardrobe', 'WARDROBE'),
    ('Furnishing', 'FURNISHING')
)


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)


    class Meta:
        swappable = "AUTH_USER_MODEL"
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
User._meta.get_field("groups").related_name = "custom_user_set"
User._meta.get_field("user_permissions").related_name = "custom_user_set"



class Listing(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=12, choices=Type_Choices, default=[], blank=False)
    town = models.CharField(max_length=200)
    specific_location = models.CharField(max_length=200)
    monthly_cost = models.IntegerField()
    description = models.CharField(max_length=200)  # Add parentheses () to specify max_length
    extras = MultiSelectField(max_length=256, choices=Extra_Choices, default=[], blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    class Meta:
        ordering = ['-created', '-type', 'monthly_cost']

    def __str__(self):
        return self.type

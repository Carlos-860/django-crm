from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\d{5}(-\d{4})?$',
            message="ZIP code must be entered in the format: '12345' or '12345-6789'"
        )]
    )

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
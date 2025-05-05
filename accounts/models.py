from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator

# Custom manager that will manage creation of custom user objects
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)
    
# Custom user
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('pharmacist', 'Pharmacist')
    ]
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, choices=ROLES, default = 'patient')
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return f'Username: {self.username}'

# Profile extending Custom user for additional user fields
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$', 'Invalid phone number')])
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile."
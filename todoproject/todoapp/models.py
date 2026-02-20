from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    pass

class MainCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Főkategória")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Főkategória"
        verbose_name_plural = "Főkategóriák"

class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Alkategória")
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='subcategories', verbose_name="Főkategória")

    def __str__(self):
        return f"{self.main_category.name} - {self.name}"

    class Meta:
        verbose_name = "Alkategória"
        verbose_name_plural = "Alkategóriák"

class Person(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Név")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefonszám")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Személy"
        verbose_name_plural = "Személyek"

class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Esemény/Okmány neve")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='events', verbose_name="Érintett személy")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='events', verbose_name="Kategória")
    deadline = models.DateField(verbose_name="Érvényesség vége (határidő)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.person.full_name}"
    @property
    def is_valid(self):
        # A határidő az érvényesség utolsó napja. Ma éjfélkor még érvényes.
        return self.deadline >= timezone.now().date()

    class Meta:
        verbose_name = "Esemény"
        verbose_name_plural = "Események"
        ordering = ['deadline']

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from .models import CustomUser, MainCategory, SubCategory, Person, Event

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_category')
    list_filter = ('main_category',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'person', 'subcategory', 'deadline', 'is_valid')
    list_filter = ('subcategory', 'person', 'deadline')
    search_fields = ('name', 'person__full_name')

    def is_valid(self, obj):
        # A határidő az érvényesség utolsó napja. Ma éjfélkor még érvényes.
        return obj.deadline >= timezone.now().date()
    
    is_valid.boolean = True
    is_valid.short_description = 'Érvényes?'

admin.site.register(CustomUser, UserAdmin)

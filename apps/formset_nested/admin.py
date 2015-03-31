from django.contrib import admin
from .models import Contact, CellPhone, Email

# Register your models here.


class CellPhoneInLine(admin.TabularInline):
    model = CellPhone
    extra = 0


class EmailInLine(admin.TabularInline):
    model = Email
    extra = 0

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name',
    inlines = [CellPhoneInLine, EmailInLine]
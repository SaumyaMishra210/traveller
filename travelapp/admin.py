from django.contrib import admin
from travelapp.models import  Bookingmodel ,SignUpmodel ,Login , Register

# Register your models here.
def get_all_field_names(model):
    return [field.name for field in model._meta.fields]

@admin.register(SignUpmodel)
class signupAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(SignUpmodel)
@admin.register(Bookingmodel)
class bookingAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(Bookingmodel)

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(Login)

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(Register)

# admin.site.register(SignUp,signupAdmin)
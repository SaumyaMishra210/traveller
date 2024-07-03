from django.contrib import admin
from travelapp.models import SignUpmodel , Bookingmodel

# Register your models here.
@admin.register(SignUpmodel)
class signupAdmin(admin.ModelAdmin):
    list_display = ('name','email')
@admin.register(Bookingmodel)
class bookingAdmin(admin.ModelAdmin):
    list_display = ('destination',)


# admin.site.register(SignUp,signupAdmin)
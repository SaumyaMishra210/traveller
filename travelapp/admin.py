from django.contrib import admin
from travelapp.models import SignUp

# Register your models here.
@admin.register(SignUp)
class signupAdmin(admin.ModelAdmin):
    list_display = ('name','email')



# admin.site.register(SignUp,signupAdmin)
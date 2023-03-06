from django.contrib import admin
from .views import sign_up

# Register your models here.
# from django.urls import path

class sign_upAdmin(admin.ModelAdmin):
    list_display =("username","email","password")

admin.site.register(sign_upAdmin, sign_up)

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
# ]


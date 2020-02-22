from django.contrib import admin

# Register your models here.
from .models import Profile, Room_comment,Rom
@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Room_comment)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Rom)
class PostAdmin(admin.ModelAdmin):
    pass
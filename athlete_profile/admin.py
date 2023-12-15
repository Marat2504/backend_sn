from django.contrib import admin

from .models import Profile, ProfilePhoto


class ProfileAdmin(admin.ModelAdmin):
    pass


class ProfilePhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfilePhoto, ProfilePhotoAdmin)



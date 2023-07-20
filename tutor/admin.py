from django.contrib import admin
from .models import Tutor

# Register your models here.


# admin.site.register(Tutor)

class TutorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tutor,TutorAdmin)
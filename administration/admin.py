from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserTypes, Curator, UserActivityJournal


# Register your models here.
admin.site.register(UserTypes)
admin.site.register(Curator)
admin.site.register(UserActivityJournal)
admin.site.register(get_user_model())
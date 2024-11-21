from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import *


class IncorrectWordInline(admin.StackedInline):
    model = IncorrectWord
    extra = 1


class CorrectWordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    inlines = (IncorrectWordInline,)


admin.site.register(CorrectWord, CorrectWordAdmin)
admin.site.register(IncorrectWord)

admin.site.unregister(Group)
admin.site.unregister(User)

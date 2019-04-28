from django.contrib import admin
from .models import Rede
from django.forms import TextInput
from django.db import models

class RedeAdmin(admin.ModelAdmin):

    formfield_overrides = {models.CharField: {'widget' : TextInput(attrs={'size':'50'})},
	}

admin.site.register(Rede, RedeAdmin)

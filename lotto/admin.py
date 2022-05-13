from django.contrib import admin
from .models import GuessNumbers # .은 현재 파일이 위치한 폴더 자체를 의미

# Register your models here.
admin.site.register(GuessNumbers)

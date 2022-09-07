from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(User, UserAdmin)# 외우는법 : 어드민 사이트에 등록한다 
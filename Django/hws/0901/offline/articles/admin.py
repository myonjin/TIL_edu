from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

# 관리자.사이트.등록(모델)
admin.site.register(Article, ArticleAdmin)
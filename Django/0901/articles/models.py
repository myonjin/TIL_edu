from django.db import models

# Create your models here.

class Article(models.Model):
    # 제목과 내용 filed (column) 생성
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title        
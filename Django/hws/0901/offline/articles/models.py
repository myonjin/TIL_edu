from django.db import models

# Create your models here.
# article table 생성하기 위한 class 하나 정의
class Article(models.Model):
    # 제목과 내용 field (column) 생성
    # schema title  Text(50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    

    def __str__(self):
        return self.title
    
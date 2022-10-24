from rest_framework import serializers
from .models import Book, Comment


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class OnlybookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title,')

class CommentSerializer(serializers.ModelSerializer):

    book=OnlybookSerializer(serializers.ModelSerializer)
    # # book id값에대한 title을 출력해준다 
    class Meta:
        model = Comment
        fields = ('id','content','created_at','updated_at',)
        


class BookSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = CommentSerializer(source='.count',read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

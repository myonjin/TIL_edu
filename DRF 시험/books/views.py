from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # books정보를 담아서 출력해준다
    books=Book.objects.all()
    if request.method == 'GET':
        serializer = BookListSerializer(books,many=True)
        return Response(serializer.data)
    # 요청보낸 데이터를 저장한다
    elif request.method == 'POST':
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):

    book = get_object_or_404(Book, pk= book_pk)
    # book 에대한 pk값을 가져와서 불러온다
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    #삭제한다
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #책에대한 데이터와 요청한값을 들고와서 수정한다
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    pass

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    if request.method == 'GET':
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    pass
    



@api_view(['POST'])
def comment_create(request, book_pk):
    comment = get_object_or_404(Comment,pk=book_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    pass

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    
    comment = get_object_or_404(Comment, pk= comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    pass


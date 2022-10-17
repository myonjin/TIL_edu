from rest_framework.response import Response
from rest_framework.decorators import api_view
from stack_data import Serializer

from .models import Article
from .serializer import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    Serializer = ArticleListSerializer(articles, many=True)
    return Response(Serializer.data)

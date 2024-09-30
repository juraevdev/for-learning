from django.shortcuts import render
from rest_framework import viewsets
from .models import Article, Book
from .serializers import ArticleSerializer

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    serializer_class = ArticleSerializer

def book_search(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Book.objects.filter(title__icontains=query)

    return render(request, 'search.html', {'results': results, 'query': query})
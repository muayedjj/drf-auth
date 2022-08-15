from django.urls import path
from .views import BookCreateListView, BookDetailView

urlpatterns = [
    path('', BookCreateListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_details'),
]

from django.conf.urls.static import static
from django.urls import path
from .views import NewsList, NewsDetail, UserLoginView
from django.conf import settings

urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('login/', UserLoginView.as_view(), name='user-login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

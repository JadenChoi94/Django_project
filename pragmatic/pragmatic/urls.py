from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from articleapp.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

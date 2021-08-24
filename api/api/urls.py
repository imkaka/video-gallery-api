# django/rest_framework imports
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

# project level imports
from gallery import views as gallery_views


router = SimpleRouter()

# register gallery app urls with router
router.register(r'video', gallery_views.VideoGalleryViewSet, basename='gallery')

# urlpatterns
urlpatterns = [
    path('api/v1/', include((router.urls, 'api'), namespace='v1')),
    path('admin/', admin.site.urls),
]

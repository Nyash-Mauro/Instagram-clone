from django.conf.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path(r'^$',views.home,name='home'),
    path(r'^image/', views.image_upload,name='upload'),
    path('profile/', views.profile_info,name='profile'),
    path(r'^edit/$',views.profile_edit,name='edit'),
    path(r'^new_comment/(\d+)/$' ,views.add_comment,name='newComment'),
    path(r'^comment/(\d+)/$' ,views.comments,name='comments'),
    path(r'^likes/(\d+)/$' , views.like_images, name='likes'),
     path(r'^user/$',views.search_user,name='search_user')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home,name='home'),
    path('image/', views.image_upload,name='upload'),
    path('profile/', views.profile_info,name='profile'),
    path('edit/',views.profile_edit,name='edit'),
    path('new_comment/' ,views.add_comment,name='newComment'),
    path('comment/' ,views.comments,name='comments'),
    path('likes/' , views.like_images, name='likes'),
    path('user/',views.search_user,name='search_user')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

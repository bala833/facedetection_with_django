from django.urls import path
from django.conf.urls import url
from face2.views import upload_video,display,track_image,TakeImages,download,TrainImages,load_page,face,add_face
 
from django.conf.urls.static import static
from django.conf import  settings
 
 
 
urlpatterns = [
    
    # path('',load_page,name='page-load'),
    path('',load_page,name='home'),
    url(r'upload/(?P<id>\d+)/(?P<name>[\w-]+)$', TakeImages, name='TakeImages'),
    path('upload',upload_video,name='upload'),
    path('videos/',display,name='videos'),
	url(r'^trackimages/$', track_image, name='track_image'),
	url(r'^TakeImages/$', TakeImages, name='TakeImages'),
	url(r'^TrainImages/$', TrainImages, name='TrainImages'),
	url(r'^download/$', download, name='download'),
	url(r'^face/$', face, name='face'),
	url(r'^add_face/$', add_face, name='add_face'),

 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
     
# urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/', views.profile, name='profile'),
    url('^neighbourhood', views.neighbourhood, name='neighbourhood'),
    url('^addneighbourhood',views.addneighbourhood,name="addneighbourhood"),
    url(r'^detail/(?P<neighbourhood_id>\d+)/$' , views.neighbourhood_details, name='detail' ),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

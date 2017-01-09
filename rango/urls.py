from django.conf.urls import url
from rango import views


urlpatterns = [

    url(r'^$',views.index, name='index'),
    url(r'^catagory/(?P<catagory_name_slug>[\w\-]+)/$', views.catagory, name='catagory'),  # New!
    url(r'^add_catagory/$', views.add_catagory, name='add_catagory'), # NEW MAPPING!
    url(r'^catagory/(?P<catagory_name_slug>[\w\-]+)/add_page/$',views.add_page, name='add_page'),
   # url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
   # url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^goto/$', views.track_url, name='goto'),
    url(r'^like_catagory/$', views.like_catagory, name='like_catagory'),
]

from django.conf.urls import url
from . import views



urlpatterns = [
   
    url(r'^$', views.homepage, name='homepage'),
    url(r'^CCI/$', views.institute, name='institute'),
    url(r'^CCI/special homes/$', views.special, name='Special Homes'),
    url(r'^CCI/children homes/$', views.children, name='Children Homes'),
    url(r'^CCI/place for safety/$', views.place, name='Place For Safety'),
    url(r'^CCI/Observation home/$', views.observation, name='Observation Homes'),
    url(r'^CCI/childlistsp/', views.childlistdl, name='listdl'),
    url(r'^CCI/childlistpl/', views.childlistjp, name='listjp'),
    url(r'^CCI/childlistol/', views.childlistmb, name='listmb'),
    url(r'^CCI/childlistch/', views.childlistkl, name='listkl'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^lostportal/$',views.lost,name='lost'),
    url(r'^addlostchild/$',views.addlost,name="addlost"),
    url(r'^addnewchild/$',views.addchild,name="addchild"),
    url(r'^adoptionlist/$',views.adoptionlist,name="adoption"),
    url(r'^adoptionlist/parentform/$',views.parentform,name="parentform"),
    url(r'^donorform/$',views.donorform,name="donor"),
    url(r'^CWC/$', views.post_list, name='post_list'),
     url(r'^CWC/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^CWC/post/new/$', views.post_new, name='post_new'),
     url(r'^CWC/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

     url(r'^CWC/post/(?P<pk>\d+)/remove/$',views.post_remove, name="post_remove"),
     url(r'^CWC/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
     url(r'^CWC/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
     url(r'^CWC/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
     url(r'^CWC/index/$',views.index,name='index'),
     url(r'^CWC/(?P<pk>[0-9]+)/$',views.detail,name="detail"),
    
    ]
   
  

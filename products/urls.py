from django.conf.urls import url
#from django.urls import path

from .views import Home
app_name = 'products'
urlpatterns = [
    #path('', Home.as_view(), name='home'),
    url(r'^$', Home.as_view(), name='home'),    
    #url(r'^categories/$', views.CategoryListView.as_view(), name='category_list'),
    #url(r'^categories/(?P<slug>[\w-]+)/$', views.CategoryDetail.as_view(), name='category_detail'),
    #url(r'^(?P<id>[\w-]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    #url(r'^(?P<id>[\w-]+)/variation/?', views.VariationListView.as_view(), name='variation_list'),
]


#url(r'^$', views.home, name='home'),
 #   url(r'^login/$',  views.login, name='login'),
  #  url(r'^logout/$', views.logout, name='logout'),
   # url(r'^signup$', views.signup, name='signup'),
    #url(r'^contact$', views.contact, name='contact'),
    #url(r'^message$', views.message, name='message'),

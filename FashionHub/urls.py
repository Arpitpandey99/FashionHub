"""Fashion_Hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from shopping.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Home,name='home'),
    url(r'^about/$',About,name='about'),
    url(r'^contact/$',Contact,name='contact'),
    url(r'^products/(?P<cat_id>[0-9]+)/$',products,name='products'),
    url(r'^product_details/(?P<p_id>[0-9]+)/$',product_details,name='product_details'),
    url(r'^login/$',Login,name='login'),
    url(r'^Add_to_cart/(?P<pid>[0-9]+)/$',AddToCart,name='cart'),
    url(r'^mycart',MyCart,name='mycart'),
    url(r'^remove_product/(?P<cid>[0-9]+)/$',Delete_item_from_cart,name='remove'),
    url(r'^signup',Signup,name='signup'),
    url(r'^order_product/(?P<pid>[0-9]+)/$',Order,name='order'),
    url(r'^clear_cart/$',Clear_Cart,name='clearcart'),
##Amin urls##
    url(r'^admin_home/$',Admin_home,name='admin_panel'),
    url(r'^All_Cat/$', AllCategory, name='all_cat'),
    url(r'^Add_Category/$', Add_Category, name='add_categoty'),
    url(r'^All_SubCat/$', AllSubcategory, name='all_subcat'),
    url(r'^Add_SubCat/$', Add_Subcategory, name='add_subcat'),
    url(r'^Add_product/$', AllProduct, name='all_product'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from adminApp.views import *
from userApp.views import *


urlpatterns = [
    #admin url start
    path('admin/', admin.site.urls),
    path('admin_home_page/', admin_home_page, name="admin_home_page"),

    path('apr/', admin_signup_page, name="admin_signup_page"),
    path('admin_register_message/', admin_register_message, name="admin_register_message"),
    path('apl/', admin_login_page, name="admin_login_page"),

    path('add_medicine/', add_medicine, name='add_medicine'),
    path('add_blog/', add_blog, name="add_blog"),

    path('admin_profile/<int:id>/', admin_profile, name="admin_profile"),
    path('admin_logout/', admin_logout, name="admin_logout"),
    
    path('view_medicine_information/', view_medicine_info, name="view_medicine_info"),

    path('update_med_info/<str:myid>', update_med_info, name="update_med_info"),
    path('delete_med_info/<str:myid>', delete_med_info, name="delete_med_info"),


    path('update_blog/<str:myid>', update_blog, name="update_blog"),
    path('delete_blog/<str:myid>', delete_blog, name="delete_blog"),

    path('view_blog/', view_blog, name="view_blog"),
    #admin url end



#user url start
    path('', home_page, name="home_page"),
    path('signup/', user_signup_page, name="user_signup_page"),
    path('login/', user_login_page, name="user_login_page"),

    path('about/', about_page, name="about_page"),
    path('categories/', category_page, name="category_page"),
    path('medicine/', medicine_page, name="medicine_page"),
    path('blog/', blog_page, name="blog_page"),
    path('contact/', contact_page, name="contact_page"),



    path('product_order/<str:myid>', product_order_page, name="product_order_page"),
    path('add_to_cart/<str:myid>', add_to_cart, name="add_to_cart"),
    path('search_results/', search_results, name="search_results"),
#user url start
    path('user_logout/', user_logout, name="user_logout"),
    path('user_profile/<int:id>/', user_profile, name="user_profile"),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

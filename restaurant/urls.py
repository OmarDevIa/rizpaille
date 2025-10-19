from django.urls import path,re_path
from .views import index,order,details,login_user,logout_user

from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path('order/<int:pk>/',order,name='order'),
    path('details/',details,name='details'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('about/',TemplateView.as_view(template_name='restaurant/about.html'),name='about'),
]

urlpatterns += [
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='restaurant/robots.txt', content_type='text/plain')),


]


handler404 = 'restaurant.views.page_not_found'
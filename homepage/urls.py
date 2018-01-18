from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
  url(r'^$',views.homepage),
  url(r'^login/$',login,{'template_name':'homepage/login.html'}),
]

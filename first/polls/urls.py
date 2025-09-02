import django.urls
from . import views
urlpatterns=[
    django.urls.path("",views.main,name="main")
]
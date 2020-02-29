from django.urls import path, include,re_path
from boke import views
urlpatterns = [
    # path('index/',views.index),
    path('detail/',views.detail),
    path('sousuo/',views.sousuo),
    path('about/',views.about),
    path('liuyan/',views.liuyan),

]
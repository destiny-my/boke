from django.urls import path, include,re_path
from user import views
urlpatterns = [
    path('newslistpic/',views.newlistpic),
    path('detail_con/',views.detail_con),
    path('listpic/',views.listpic)
]

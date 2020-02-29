from django.shortcuts import render
from user.models import User

def newlistpic(request):
    user_list = User.objects.all()
    return render(request, 'newslistpic.html',{'user_list':user_list})
# Create your views here.

def detail_con(request):
    id = request.GET.get('id')
    detail_list = User.objects.get(id=id)
    return render(request, 'detail_con.html', {'detail_list': detail_list})


def listpic(request):
    return render(request,'listpic.html')
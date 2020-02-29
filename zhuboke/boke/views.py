from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from boke.models import Post
import math
# Create your views here.
def base(request):
    return render(request,'base.html')





def index2(request):
    #获取当前页码数
    num = request.GET.get('num',1)
    n = int(num)
    post_list = Post.objects.all()
    #创建分页器对象
    pages = Paginator(post_list,7)
    #获取当前页的数据
    try:
        perpage_data = pages.page(n)
    except PageNotAnInteger:
        perpage_data = pages.page(1)
    except EmptyPage:
        perpage_data = pages.page(pages.num_pages)


    begin = (n-int(math.ceil(10.0/2)))
    if begin<1:
        begin = 1
    end = begin+9
    if end > pages.num_pages:
        end = pages.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end-9
    pagelist = range(begin,end+1)


    return render(request,'index.html',{"perpage_data":perpage_data,'pages':pages,'pagelist':pagelist,'current':n})


#首页
def index(request):
    #接受请求参数num
    num = request.GET.get('num',1)
    #处理分页请求
    post_list,n = page(num)
    #上一页
    pre_page = int(n)-1
    #下一页
    next_page = int(n)+1
    return render(request,'index.html',{'post_list':post_list,'pre_page':pre_page,'next_page':next_page})



def page(num,size=7):
    #接收当前的页码数
    num = int(num)
    #总记录数
    totalRecords = Post.objects.count()
    #总页数
    totalPages = int(math.ceil(totalRecords*1.0/size))
    #判断是否越界
    if num <1:
        num = 1
    if num > totalPages:
        num = totalPages
    #计算每页显示的记录
    posts = Post.objects.all()[((num-1)*size):(num*size)]

    return posts,num

#详情页


def detail(request):
    id = request.GET.get('id')
    print(id)
    detail_list = Post.objects.get(id=id)

    return render(request,'detail.html',{'detail_list':detail_list})

#搜索网页
def sousuo(request):
    name = request.GET.get('sousuo')
    print(name)
    if name:
        print('收到')
        sousuo_list = Post.objects.filter(title__contains = name)
        print(sousuo_list)
    else:
        sousuo_list = Post.objects.all()[:10]
    return render(request,'sousuo.html',{'sousuo_list':sousuo_list})



# def add_list(request):
#     return render(request)


def about(request):
    return render(request,'about.html')


def liuyan(request):
    return render(request,'liyan.html')


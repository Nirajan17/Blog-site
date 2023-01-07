from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'in_posts':posts})

def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'post.html',{'po_posts':posts})

def add_blog(request):# html files named as this functions are directed to this function.
    if request.method == 'POST':
        title_text = request.POST['title_text']
        des_text = request.POST['des_text']
        print(title_text)
        pst = Post()
        pst = Post.objects.create(title = title_text,body = des_text)
        pst.save()
        return redirect('/')
    return render(request, 'add_blog.html')

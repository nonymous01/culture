from django.shortcuts import render,HttpResponse
from .form import ActicleForm
from .models import Article
# Create your views here.

#ajouter un Article dans la db
def add_user(request):
    context={}
    form = ActicleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request, "my_app/index.html", context)

#afficher la liste
def list_view(resquest):
    context={}
    context["datas"]=Article.objects.all()
    return render(resquest, "my_app/list.html" ,context)
def blog(request):
    context={}
    context["datas"]=Article.objects.all()
    return render(request, "my_app/blog.html",context)

#delete
def delete(request,id):
    context={}
    context["datas"]=Article.objects.all()
    rm = Article.objects.get(id=id)
    rm.delete()
    return render(request, "my_app/list.html" ,context)


#updete

def update(request,id):
    context={}
    up=Article.objects.get(id=id)
    form = ActicleForm(request.POST)
    up.description = str(form["description"].value())
    up.titre = str(form["titre"].value())
    up.save()
    context["form"]=form
    return render(request, "my_app/update.html",context)
    


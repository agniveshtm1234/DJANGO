from django.shortcuts import render,redirect
from .models import animeinfo
from .forms import animeform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import os
# Create your views here.

def home_page(request):
    visits =int(request.COOKIES.get('visits',0))
    visits+=1
    response = render(request,'index.html',{'visits':visits})
    response.set_cookie('visits',visits)
    return response

@login_required(login_url='user_login')
def create(request):
    if request.method == "POST":
        frm = animeform(request.POST,request.FILES)
        if frm.is_valid():
            anime = frm.save(commit=False)
            anime.user = request.user
            anime.save()
            messages.success(request,"Anime Added Successfully")
            return redirect('list')
    else:
        frm=animeform()
    return render(request,"create.html",{"frm":frm}) #passed to the html file

@login_required(login_url='user_login')
@never_cache
def list(request):  
    anime_set = animeinfo.objects.filter(user=request.user)#took entire records based on user
    response = render(request,"list.html",{"animes":anime_set})
    return response
#print(anime_set) --> prints the entire dataset from database in a query set

@login_required(login_url='user_login')
def edit(request,pk):
    instance_edited = animeinfo.objects.get(pk=pk,user=request.user)
    if request.method == "POST":
        frm = animeform(request.POST,request.FILES,instance=instance_edited) #updates the fields after submission
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
        frm = animeform(instance=instance_edited)
    return render(request,'create.html',{"frm":frm})

@login_required(login_url='login/')
def delete(request,pk):
    instance=animeinfo.objects.get(pk=pk,user=request.user) #collect the record
    if instance.img:  # Replace 'image' with your ImageField name
        image_path = instance.img.path
        if os.path.exists(image_path):
            os.remove(image_path) #deletes the user added images from media folder
    instance.delete()#deleted the record from the server
    anime_set=animeinfo.objects.all()
    return render(request,"list.html",{"animes":anime_set})





''' this was inside  edit() function 

        recent_visits = request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits

'''
'''this was inside list() function 
      
    recent_visits = request.session.get('recent_visits',[])
    count = int(request.session.get('count',0))
    count+=1
    request.session['count']=count
    recent_anime_set = animeinfo.objects.filter(pk__in=recent_visits)
    anime_set = animeinfo.objects.all()#took entire records
    response = render(request,"list.html",{"animes":anime_set,'visits':count,"recent_animes":recent_anime_set})
    return response

'''
from django.shortcuts import render,redirect,get_object_or_404
from .models import animeinfo
from .forms import animeform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.cache import cache
import os
# Create your views here.
# Main Views.py
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
            frm.instance.user = request.user
            frm.save()
            cache.delete(f"anime_list_{request.user.id}")
            messages.success(request,"Anime Added Successfully")
            return redirect('list')
    else:
        frm=animeform()
    return render(request,"create.html",{"frm":frm}) #passed to the html file

@never_cache
@login_required(login_url='user_login')
def list(request):  
    cache_key = f"anime_list_{request.user.id}" #unique key per user
    anime_set = cache.get(cache_key)
    if not anime_set:
        print("Fetching from database.......")
        anime_set = animeinfo.objects.filter(user=request.user)#took entire records based on user
        cache.set(cache_key,anime_set,120)
    response = render(request,"list.html",{"animes":anime_set})
    return response
#print(anime_set) --> prints the entire dataset from database in a query set

@login_required(login_url='user_login')
def edit(request,pk):
    #instance_edited = animeinfo.objects.get(pk=pk,user=request.user)  --> might raise Doesnot Exist exception to the user,(bad UX)
    instance_edited = get_object_or_404(animeinfo,pk=pk,user=request.user) #Shows error 404 page handling the error carefully
    if request.method == "POST":
        frm = animeform(request.POST,request.FILES,instance=instance_edited) #updates the fields after submission
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
        frm = animeform(instance=instance_edited)
    return render(request,'create.html',{"frm":frm})

@login_required(login_url='user_login')
def delete(request,pk):
    #instance=animeinfo.objects.get(pk=pk,user=request.user) #collect the record
    instance_deleted = get_object_or_404(animeinfo,pk=pk,user=request.user)
    if instance_deleted.img and os.path.exists(instance_deleted.img.path):  # Replace 'image' with your ImageField name
        try:
            os.remove(instance_deleted.img.path) #deletes the user added images from media folder
        except OSError:
            pass
    instance_deleted.delete()#deleted the record from the server
    cache.delete(f"anime_list_{request.user.id}")
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

''' anime = frm.save(commit=False)
            anime.user = request.user
            anime.save()
            messages.success(request,"Anime Added Successfully")
            return redirect('list')
            
            for user specificness use this.'''
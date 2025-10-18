"""from django.shortcuts import render
from .models import animeinfo
from .forms import animeform
# Create your views here.
def home_page(request):
    frm = animeform()
    if request.method == "POST":
        print(request.POST)  #data passed from the forms inside index.html is passed with a method called 'post'
        print(request.POST.get("title")) #its a query dictionary , ie why <dict>.get() is used to get the value using keys
        print(request.POST.get("year"))
        print(request.POST.get('summary'))

        title = request.POST.get('title')   
        year = request.POST.get('year')   #collecting these in variables for uploading
        summary = request.POST.get('summary') # to Database using ORM method
        Big3 = request.POST.get('Big3')
        animeobj=animeinfo(title=title,year=year,summary=summary,Big3=Big3) #uploaded to models.py
        animeobj.save() #saved the object , django internally converts this into an INSERT Query in RDBMS 
    anime_set=animeinfo.objects.all()  #took entire records
    return render(request,"index.html",{"animes":anime_set,"frm":frm}) #passed to the html file"""


"""here .get() method is used because the response come as a query dictionary
    ,we can also use POST['<key>'] but this method raises a Key Error if 
    the specified key isnt inside POST, instead we use .get() where if 
    Key is not found the function then returns None, which is safer.
"""
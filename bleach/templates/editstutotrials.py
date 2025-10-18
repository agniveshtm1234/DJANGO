"""def edit(request,pk):
    instance_edited = animeinfo.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        summary = request.POST.get('summary')
        Big3 = request.POST.get('Big3')
        instance_edited.title=title
        instance_edited.year=year
        instance_edited.summary=summary
        instance_edited.Big3=Big3
        instance_edited.save()
    frm = animeform(instance=instance_edited)
    return render(request,'create.html',{"frm":frm})"""

#you can use this much line of code , or you can just create another,
#forms object 
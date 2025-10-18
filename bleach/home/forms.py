from django.forms import ModelForm
from django import forms
from .models import animeinfo
class animeform(ModelForm):    #using this method rather than html 
    class Meta:
        model=animeinfo
        fields='__all__' 
        widgets = {'Big3':forms.RadioSelect()}
        
        """since we need all fields from models inside our forms we are specifying __all__ dunder method , otherwise specifiy the 
           needed fields inside a list eg: if there are 5 fields and you only want 3 of them
           declare it as fields = ['field1','field2','field3']"""
        
        """There are many more methods in forms.py , you can add widgets,
        exceptions,help_texts"""

        """when frm.save() is triggered , it creates an object of anime info 
          like this 'animeobj=animeinfo(title=title,year=year,summary=summary,Big3=Big3)'
         ,inside this file,then  it executes INSERT function inside the database."""
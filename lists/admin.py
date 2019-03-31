from django.contrib import admin

# Register your models here.
from .import models
#fields in models are title,text,date,image,level,t_ype
    

class listadmin(admin.ModelAdmin):
    fields=['title','text','date','image','level','t_ype']#fields which are to be visible
    search_fields=['title']#field which is used for searching 
    list_filter=['title','date']#fields which is use for filtering
    list_display=['title','text','image','date','level','t_ype']#order of displaying field
    list_editable =['text',]#fields which are editable


admin.site.register(models.List,listadmin)




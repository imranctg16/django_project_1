from django.contrib import admin
from .models import Catagory,page,UserProfile


class CategoryAdmin(admin.ModelAdmin):          # this is for to simplify urls
    prepopulated_fields = {'slug':('name',)}

class pageadmin(admin.ModelAdmin):
    list_display = ['__str__','catagory','title']
    class Meta:
        model= page


admin.site.register(page,pageadmin)
admin.site.register(Catagory,CategoryAdmin)
admin.site.register(UserProfile)


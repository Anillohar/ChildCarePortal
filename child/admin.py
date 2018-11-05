from django.contrib import admin

from .models import childinfo,typecci,cci,lostchild

from .models import Post,Comment,Question

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(childinfo)
admin.site.register(typecci)
admin.site.register(cci)
admin.site.register(lostchild)
# Register your models here.

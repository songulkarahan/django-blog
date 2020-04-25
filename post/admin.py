from django.contrib import admin
from .models import Post
#.models bu dizindeki modellere Post'u import et demek
#from post.models import Post aynı şey

class PostAdmin(admin.ModelAdmin):

    list_display = ['title','publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title','content']
    class Meta:
        model = Post


admin.site.register(Post,PostAdmin)

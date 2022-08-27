from django.contrib import admin
from .models import post, category, profile, Comment, SubscribedUsers

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author',  'status','category', 'publish', 'approved')
	prepopulated_fields = {"slug": ("title",)}
	list_filter = ('status', 'created', 'author','category', 'tags')
	search_fields = ('title', 'body','tags','author','approved=False')
	raw_id_fields = ('author',)
	publish_hierarchy = 'publish'
	ordering = ('status', 'publish')



class CommentAdmin(admin.ModelAdmin):
	list_display  = ('CommentPost','author', 'body', 'email', 'parent',  'date_added', 'active')
    


admin.site.register(post, PostAdmin)
admin.site.register(category)
admin.site.register(profile)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SubscribedUsers)

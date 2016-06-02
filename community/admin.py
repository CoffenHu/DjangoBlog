from django.contrib import admin
from community.models import Post, Comment, Reaction
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_time'
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = False
    actions = ['make_publish', ]

    # 修改页面的显示
    #exclude = ('topic', 'views', 'attachment')
    #fields = (('title', 'body'), )
    fieldsets = (
        (None, {
            'fields': ('title', 'body',)
        }),
        ('Advanced Options', {
            #'classes': ('collapse', ),
            'fields': ('author', 'collected_by', 'views')
        }),
    )

    def make_publish(self, request, queryset):
        rows_updated = queryset.update(is_published=True)
        message_bit = '{}条信息被发布'.format(rows_updated)
        self.message_user(request, message_bit)
    make_publish.short_description = 'Make Publish'
admin.site.register(Post, PostAdmin)


admin.site.register(Comment)
admin.site.register(Reaction)

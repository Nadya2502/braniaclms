from django.contrib import admin
from django.utils.html import format_html
from mainapp.models import News, Lesson, Course, CoursesTeacher


admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(CoursesTeacher)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title','slug', 'deleted',)
    list_filter = ('deleted',)
    search_fields = ('title', 'intro', 'body',)
    ordering = ('pk',)
    list_per_page = 2
    actions = ('mark_as_delete',)

    def slug(self, obj):
        return format_html(
            '<a href="{}" target "_blank">{}</a>',
            obj.title.lower().replace(' ', '-'),
            obj.title
        )
    slug.short_description = 'Слаг'

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'




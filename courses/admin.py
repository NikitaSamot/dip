from django.contrib import admin

from courses.models import Course, Subject, Module, Text, File, Image, Video


# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'created')
    list_filter = ('created', 'subject')
    search_fields = ('title', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated']
    list_filter = ['owner']
    search_fields = ['title', 'owner__username']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated']
    list_filter = ['owner']
    search_fields = ['title', 'owner__username']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated']
    list_filter = ['owner']
    search_fields = ['title', 'owner__username']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated']
    list_filter = ['owner']
    search_fields = ['title', 'owner__username']
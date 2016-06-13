from django.contrib import admin

from publication.models import Speaker, Subject

class speakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')

admin.site.register(Speaker, speakerAdmin)

class subjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'topic', 'message')

admin.site.register(Subject, subjectAdmin)

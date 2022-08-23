# from pages.models import Team
from pages.models import Contect, Service, Team, Appointment
from django.contrib import admin
from django.utils.html import format_html


class ServiceAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.ser_image.url))

    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'title', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)


# Register your models here.
admin.site.register(Service, ServiceAdmin)


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.team_image.url))

    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'name', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


# Register your models here.
admin.site.register(Team, TeamAdmin)


class ContectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'message')
    list_filter = ('message',)


# Register your models here.
admin.site.register(Contect, ContectAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'message')
    list_filter = ('message',)


# Register your models here.
admin.site.register(Appointment, AppointmentAdmin)

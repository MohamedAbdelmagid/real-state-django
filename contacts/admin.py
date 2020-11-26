from django.contrib import admin

from . models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Custom Contact table in the admin page """

    list_display = ('id', 'name', 'listing', 'email', 'contact_date', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing', 'phone')
    list_editable = ('phone',)
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
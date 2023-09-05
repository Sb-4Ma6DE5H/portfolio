from django.contrib import admin
from .models import Portfolio,CheckUpImage
from .models import Contact,Knowledge

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(CheckUpImage)
class CheckUpImageAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'timestamp')  # Define which fields are displayed in the list view
    # list_filter = ('timestamp',)  # Add filters for the list view
    # search_fields = ('name', 'email', 'message')  # Add a search bar for searching by name, email, or message
    # readonly_fields = ('timestamp',)  # Make the timestamp field read-only
    pass

admin.site.register(Contact, ContactAdmin)



@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    pass
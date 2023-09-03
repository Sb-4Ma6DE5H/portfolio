from django.contrib import admin
from .models import Portfolio,CheckUpImage

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(CheckUpImage)
class CheckUpImageAdmin(admin.ModelAdmin):
    pass

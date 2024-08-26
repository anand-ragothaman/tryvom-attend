from django.contrib import admin

from app.models.category_models import Category

# Define an admin class for the Category model


class CategoryAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('category',  'created_at', 'updated_at')
    # Fields to search within the admin
    search_fields = ['category']


# Register the Category model and its admin class with the admin site
admin.site.register(Category, CategoryAdmin)

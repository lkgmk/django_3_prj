from django.contrib import admin
from .models import NameDetails, Vehicle, Car, \
    Album, Songs, Author, Book

# Register your models here.
admin.site.site_header = "Custom Admin Project"
admin.site.site_title = "Django Admin"


class NameDetailsAdmin(admin.ModelAdmin):
    # Display data according to below columns
    # list_display = ('id', 'person_name', 'country_name', 'full_desc')
    list_display = ('id', 'person_name', 'country_name', 'full_desc')

    # click on fields
    list_display_links = ('country_name', 'full_desc')

    # list editable
    list_editable = ('person_name',)

    # filter by
    list_filter = ('person_name', 'country_name',)

    # search by
    # search_fields = ('person_name', 'country_name', 'price__gte')
    search_fields = ('person_name__startswith', 'country_name',)

    # exclude input form field
    # exclude = ('id', 'person_name',)

    # input form fields
    # fields = ('country_name', 'person_name')
    fields = (('person_name', 'country_name'),)

    # def full_desc(self, obj):
    #     return f'{obj.person_name}  {obj.country_name}'

    @admin.display(description="New Title")
    def full_desc(self, obj):
        return f'{obj.person_name}  {obj.country_name}'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    list_filter = ('title', 'authors__name')
    search_fields = ('authors__desc',)


admin.site.register(NameDetails, NameDetailsAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

admin.site.register([Vehicle, Car, Album, Songs])
# admin.site.register(Vehicle)
# admin.site.register(Car)

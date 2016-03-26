from django.contrib import admin
import nested_admin

from .models import Event, PaidEvent, Item, PaidItem, ItemChoice

class ItemChoiceInline(nested_admin.NestedStackedInline):
    model = ItemChoice
    extra = 0

class ItemInline(nested_admin.NestedStackedInline):
    model = Item
    inlines = [ItemChoiceInline]
    extra = 0

class PaidItemInline(nested_admin.NestedStackedInline):
    model = PaidItem
    inlines = [ItemChoiceInline]
    extra = 0

class EventAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'slug', 'start', 'end', 'status')
    fields = list_display
    inlines = [ItemInline]
    prepopulated_fields = {"slug": ("name",)}

class PaidEventAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'slug', 'start', 'end', 'status', 'fee', 'fees_due')
    fields = list_display
    inlines = [ItemInline, PaidItemInline]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Event, EventAdmin)
admin.site.register(PaidEvent, PaidEventAdmin)

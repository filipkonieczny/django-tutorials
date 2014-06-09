from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # manner of dispalying content
    list_display = ('question', 'pub_date', 'was_published_recently')

    # sort by pub date
    list_filter = ['pub_date']

    # search capability
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
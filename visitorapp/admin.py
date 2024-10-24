from django.contrib import admin
from .models import User, Visits

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'role')
    search_fields = ('firstName', 'lastName', 'email')
    list_filter = ('role',)


@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    list_display = ('user', 'visit_date', 'check_out_date', 'accepted', 'purpose_of_visit')
    list_filter = ('accepted', 'purpose_of_visit')
    search_fields = ('user__email', 'purpose_of_visit')

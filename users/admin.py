''' User admin classes '''
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from django.contrib.auth.models import User


# This is a simple registration
# admin.site.register(Profile)


# This is a more complex registration
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ''' Profile admin '''
    # When display all profiles in the list,
    # display all the next fields:
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # when click on the following attributes, it will
    # redirect to the current user profile
    list_display_links = ('pk', 'user', 'phone_number')
    # the next attributes could be edited in the list line
    list_editable = ('website', 'picture')
    # we can search by the next fields
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    # we will be able to filter by the next attributes
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

    # In the view of the current profile we will see
    fieldsets = (
        ('Profile', {
            'fields' : (('user', 'picture'),)
            }
        ),
        (
            'Extra info', {
                'fields' : (
                    ('website', 'phone_number'),
                    ('biography')
                )
            }
        ),
        ('Metadata', {
            'fields' : (('created', 'modified'),)
            }
        )
    )

    # Uneditable fields (mandatory for created)
    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    ''' Profile in-line admin for users.'''
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    ''' Add profile admin to base user admin. '''
    inlines = (ProfileInline,)
    # override the list display
    list_display = ('username', 'email', 'first_name', 'last_name'
                    , 'is_active', 'is_staff')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
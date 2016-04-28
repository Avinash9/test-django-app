from django.contrib import admin

# Register your models here.

from polls.models import Logs,LogUser

class PollsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Logs, PollsAdmin)


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(LogUser, UserAdmin)
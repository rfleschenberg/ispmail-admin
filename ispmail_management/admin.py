from django.contrib import admin

from ispmail_management.models import (VirtualAliases, VirtualDomains,
                                       VirtualUsers)

admin.site.register(VirtualAliases)
admin.site.register(VirtualDomains)
admin.site.register(VirtualUsers)

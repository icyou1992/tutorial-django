from django.contrib import admin

from reactdjango.models.moim import Moim

admin.site.unregister(Moim)
admin.site.register(Moim)
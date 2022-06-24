from django.contrib import admin

from django.contrib import admin

from example_app.models import Example


class ExampleAdmin(admin.ModelAdmin):
    fields = ('image',)


admin.site.register(Example, ExampleAdmin)

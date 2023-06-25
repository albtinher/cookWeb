from django.contrib import admin

# Register your models here.
import cookweb.models

admin.site.register(cookweb.models.ConfiguracionCookie)
admin.site.register(cookweb.models.URL)
admin.site.register(cookweb.models.CategoriaCookie)


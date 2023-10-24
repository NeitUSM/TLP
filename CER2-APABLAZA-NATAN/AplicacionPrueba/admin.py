from django.contrib import admin
from .models import Entidad
from .models import Comunicado

# Register your models here.

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'logo')
    list_display_links = ('nombre',)

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'entidad' ,'detalle_corto', 'tipo', 'visible', 'publicado_por')
    list_display_links = ('titulo',)
    readonly_fields = ('publicado_por', 'modificado_por','entidad',)
    
    def save_model(self, request, obj, form, change):
        usuario = request.user
        entidadFiltro = Entidad.objects.filter(administracion=usuario).first()
        obj.entidad = entidadFiltro
        if not obj.publicado_por:
            obj.publicado_por = usuario
        obj.modificado_por = usuario
        super(ComunicadoAdmin, self).save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super(ComunicadoAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(publicado_por=request.user)
        return qs

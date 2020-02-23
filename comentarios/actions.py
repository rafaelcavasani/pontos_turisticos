

def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)

def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)

aprova_comentarios.short_description = 'Aprovar comentários'
reprova_comentarios.short_description = 'Repprovar comentários'
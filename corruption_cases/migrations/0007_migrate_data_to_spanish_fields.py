from django.db import migrations


def migrate_data_to_spanish_fields(apps, schema_editor):
    """
    Migrate data from old English field names to new Spanish field names
    """
    CorruptionCase = apps.get_model('corruption_cases', 'CorruptionCase')
    
    # Get all cases
    cases = CorruptionCase.objects.all()
    
    for case in cases:
        # Migrate basic fields
        if hasattr(case, 'title') and case.title:
            case.titulo = case.title
        if hasattr(case, 'short_description') and case.short_description:
            case.descripcion_corta = case.short_description
        if hasattr(case, 'full_description') and case.full_description:
            case.descripcion_completa = case.full_description
        if hasattr(case, 'date') and case.date:
            case.fecha = case.date
        if hasattr(case, 'amount') and case.amount:
            case.importe = case.amount
        if hasattr(case, 'main_image') and case.main_image:
            case.imagen_principal = case.main_image
        if hasattr(case, 'political_party') and case.political_party:
            case.partido_politico = case.political_party
        if hasattr(case, 'institution') and case.institution:
            case.institucion = case.institution
        if hasattr(case, 'corruption_type') and case.corruption_type:
            case.tipo_corrupcion = case.corruption_type
        if hasattr(case, 'tags') and case.tags:
            case.etiquetas.set(case.tags.all())
        if hasattr(case, 'publication_type') and case.publication_type:
            case.tipo_publicacion = case.publication_type
        if hasattr(case, 'author_name') and case.author_name:
            case.nombre_autor = case.author_name
        if hasattr(case, 'external_url') and case.external_url:
            case.url_externa = case.external_url
        if hasattr(case, 'is_annual_amount') and case.is_annual_amount is not None:
            case.es_importe_anual = case.is_annual_amount
        if hasattr(case, 'start_date') and case.start_date:
            case.fecha_inicio = case.start_date
        if hasattr(case, 'sources') and case.sources:
            case.fuentes = case.sources
        if hasattr(case, 'is_featured') and case.is_featured is not None:
            case.es_destacado = case.is_featured
            
        case.save()


def reverse_migrate_data(apps, schema_editor):
    """
    Reverse migration - copy data back to English fields
    """
    CorruptionCase = apps.get_model('corruption_cases', 'CorruptionCase')
    
    cases = CorruptionCase.objects.all()
    
    for case in cases:
        # Reverse migrate basic fields
        if hasattr(case, 'titulo') and case.titulo and case.titulo != "Sin título":
            case.title = case.titulo
        if hasattr(case, 'descripcion_corta') and case.descripcion_corta and case.descripcion_corta != "Sin descripción":
            case.short_description = case.descripcion_corta
        if hasattr(case, 'descripcion_completa') and case.descripcion_completa and case.descripcion_completa != "Sin descripción completa":
            case.full_description = case.descripcion_completa
        if hasattr(case, 'fecha') and case.fecha and case.fecha != "2024-01-01":
            case.date = case.fecha
        if hasattr(case, 'importe') and case.importe and case.importe != 0.00:
            case.amount = case.importe
        if hasattr(case, 'imagen_principal') and case.imagen_principal:
            case.main_image = case.imagen_principal
        if hasattr(case, 'partido_politico') and case.partido_politico:
            case.political_party = case.partido_politico
        if hasattr(case, 'institucion') and case.institucion:
            case.institution = case.institucion
        if hasattr(case, 'tipo_corrupcion') and case.tipo_corrupcion:
            case.corruption_type = case.tipo_corrupcion
        if hasattr(case, 'etiquetas') and case.etiquetas.exists():
            case.tags.set(case.etiquetas.all())
        if hasattr(case, 'tipo_publicacion') and case.tipo_publicacion:
            case.publication_type = case.tipo_publicacion
        if hasattr(case, 'nombre_autor') and case.nombre_autor:
            case.author_name = case.nombre_autor
        if hasattr(case, 'url_externa') and case.url_externa:
            case.external_url = case.url_externa
        if hasattr(case, 'es_importe_anual') and case.es_importe_anual is not None:
            case.is_annual_amount = case.es_importe_anual
        if hasattr(case, 'fecha_inicio') and case.fecha_inicio:
            case.start_date = case.fecha_inicio
        if hasattr(case, 'fuentes') and case.fuentes and case.fuentes != "Sin fuentes":
            case.sources = case.fuentes
        if hasattr(case, 'es_destacado') and case.es_destacado is not None:
            case.is_featured = case.es_destacado
            
        case.save()


class Migration(migrations.Migration):

    dependencies = [
        ('corruption_cases', '0006_remove_video_url_field'),
    ]

    operations = [
        migrations.RunPython(
            migrate_data_to_spanish_fields,
            reverse_migrate_data,
        ),
    ]

from django.db import migrations, models

def migrate_data_to_spanish_fields_direct(apps, schema_editor):
    """
    Migrate data from old English column names to new Spanish field names
    by accessing the database columns directly
    """
    from django.db import connection
    
    with connection.cursor() as cursor:
        # Get all records with old column data
        cursor.execute("""
            SELECT id, title, short_description, full_description, date, amount, 
                   main_image, author_name, publication_type, video_url, external_url,
                   is_annual_amount, start_date, sources, is_featured, created_at, updated_at
            FROM corruption_cases_corruptioncase
        """)
        
        rows = cursor.fetchall()
        
        for row in rows:
            case_id, title, short_description, full_description, date, amount, \
            main_image, author_name, publication_type, video_url, external_url, \
            is_annual_amount, start_date, sources, is_featured, created_at, updated_at = row
            
            # Update the Spanish fields with data from old columns
            update_fields = []
            update_values = []
            
            if title and title != "Sin título":
                update_fields.append("titulo = %s")
                update_values.append(title)
                
            if short_description and short_description != "Sin descripción":
                update_fields.append("descripcion_corta = %s")
                update_values.append(short_description)
                
            if full_description and full_description != "Sin descripción completa":
                update_fields.append("descripcion_completa = %s")
                update_values.append(full_description)
                
            if date and str(date) != "2024-01-01":
                update_fields.append("fecha = %s")
                update_values.append(date)
                
            if amount is not None and amount != 0.00:
                update_fields.append("importe = %s")
                update_values.append(amount)
                
            if main_image:
                update_fields.append("imagen_principal = %s")
                update_values.append(main_image)
                
            if author_name:
                update_fields.append("nombre_autor = %s")
                update_values.append(author_name)
                
            if publication_type:
                update_fields.append("tipo_publicacion = %s")
                update_values.append(publication_type)
                
            # Handle URL fields - prioritize external_url over video_url
            if external_url:
                update_fields.append("url_externa = %s")
                update_values.append(external_url)
            elif video_url:
                update_fields.append("url_externa = %s")
                update_values.append(video_url)
                
            if is_annual_amount is not None:
                update_fields.append("es_importe_anual = %s")
                update_values.append(is_annual_amount)
                
            if start_date:
                update_fields.append("fecha_inicio = %s")
                update_values.append(start_date)
                
            if sources and sources != "Sin fuentes":
                update_fields.append("fuentes = %s")
                update_values.append(sources)
                
            if is_featured is not None:
                update_fields.append("es_destacado = %s")
                update_values.append(is_featured)
                
            if created_at:
                update_fields.append("fecha_creacion = %s")
                update_values.append(created_at)
                
            if updated_at:
                update_fields.append("fecha_actualizacion = %s")
                update_values.append(updated_at)
            
            # Only update if there are fields to update
            if update_fields:
                update_values.append(case_id)
                sql = f"""
                    UPDATE corruption_cases_corruptioncase 
                    SET {', '.join(update_fields)}
                    WHERE id = %s
                """
                cursor.execute(sql, update_values)


def reverse_migrate_data(apps, schema_editor):
    """
    Reverse migration - copy data back to English columns
    """
    from django.db import connection
    
    with connection.cursor() as cursor:
        # Get all records with Spanish field data
        cursor.execute("""
            SELECT id, titulo, descripcion_corta, descripcion_completa, fecha, importe, 
                   imagen_principal, nombre_autor, tipo_publicacion, url_externa,
                   es_importe_anual, fecha_inicio, fuentes, es_destacado, fecha_creacion, fecha_actualizacion
            FROM corruption_cases_corruptioncase
        """)
        
        rows = cursor.fetchall()
        
        for row in rows:
            case_id, titulo, descripcion_corta, descripcion_completa, fecha, importe, \
            imagen_principal, nombre_autor, tipo_publicacion, url_externa, \
            es_importe_anual, fecha_inicio, fuentes, es_destacado, fecha_creacion, fecha_actualizacion = row
            
            # Update the English columns with data from Spanish fields
            update_fields = []
            update_values = []
            
            if titulo and titulo != "Sin título":
                update_fields.append("title = %s")
                update_values.append(titulo)
                
            if descripcion_corta and descripcion_corta != "Sin descripción":
                update_fields.append("short_description = %s")
                update_values.append(descripcion_corta)
                
            if descripcion_completa and descripcion_completa != "Sin descripción completa":
                update_fields.append("full_description = %s")
                update_values.append(descripcion_completa)
                
            if fecha and str(fecha) != "2024-01-01":
                update_fields.append("date = %s")
                update_values.append(fecha)
                
            if importe is not None and importe != 0.00:
                update_fields.append("amount = %s")
                update_values.append(importe)
                
            if imagen_principal:
                update_fields.append("main_image = %s")
                update_values.append(imagen_principal)
                
            if nombre_autor:
                update_fields.append("author_name = %s")
                update_values.append(nombre_autor)
                
            if tipo_publicacion:
                update_fields.append("publication_type = %s")
                update_values.append(tipo_publicacion)
                
            if url_externa:
                update_fields.append("external_url = %s")
                update_values.append(url_externa)
                
            if es_importe_anual is not None:
                update_fields.append("is_annual_amount = %s")
                update_values.append(es_importe_anual)
                
            if fecha_inicio:
                update_fields.append("start_date = %s")
                update_values.append(fecha_inicio)
                
            if fuentes and fuentes != "Sin fuentes":
                update_fields.append("sources = %s")
                update_values.append(fuentes)
                
            if es_destacado is not None:
                update_fields.append("is_featured = %s")
                update_values.append(es_destacado)
                
            if fecha_creacion:
                update_fields.append("created_at = %s")
                update_values.append(fecha_creacion)
                
            if fecha_actualizacion:
                update_fields.append("updated_at = %s")
                update_values.append(fecha_actualizacion)
            
            # Only update if there are fields to update
            if update_fields:
                update_values.append(case_id)
                sql = f"""
                    UPDATE corruption_cases_corruptioncase 
                    SET {', '.join(update_fields)}
                    WHERE id = %s
                """
                cursor.execute(sql, update_values)


class Migration(migrations.Migration):

    dependencies = [
        ('corruption_cases', '0007_migrate_data_to_spanish_fields'),
    ]

    operations = [
        migrations.RunPython(
            migrate_data_to_spanish_fields_direct,
            reverse_migrate_data,
        ),
    ]

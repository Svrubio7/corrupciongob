"""
Management command to create development data
Only for use in development mode
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from corruption_cases.models import (
    CorruptionCase, PoliticalParty, Institution, Country, CorruptionType, Region
)
from datetime import date
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Creates development data with 3 casos and 3 articles'

    def handle(self, *args, **kwargs):
        # Only allow in development/debug mode
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR('This command can only be run in DEBUG mode'))
            return

        # Create or get required related objects
        party1, _ = PoliticalParty.objects.get_or_create(
            name='Partido Ejemplo 1',
            defaults={'short_name': 'PE1', 'color': '#FF0000'}
        )
        party2, _ = PoliticalParty.objects.get_or_create(
            name='Partido Ejemplo 2',
            defaults={'short_name': 'PE2', 'color': '#0000FF'}
        )
        
        institution1, _ = Institution.objects.get_or_create(
            name='Ayuntamiento de Ejemplo',
            defaults={'institution_type': 'municipal', 'region': 'Madrid'}
        )
        institution2, _ = Institution.objects.get_or_create(
            name='Gobierno de Ejemplo',
            defaults={'institution_type': 'central', 'region': 'Nacional'}
        )
        
        country1, _ = Country.objects.get_or_create(
            name='España',
            defaults={'code': 'ESP'}
        )
        
        corruption_type1, _ = CorruptionType.objects.get_or_create(
            name='Malversación',
            defaults={'description': 'Uso indebido de fondos públicos'}
        )
        corruption_type2, _ = CorruptionType.objects.get_or_create(
            name='Cohecho',
            defaults={'description': 'Soborno a funcionarios públicos'}
        )
        
        region1, _ = Region.objects.get_or_create(
            name='Madrid',
            defaults={'autonomous_community': 'Comunidad de Madrid'}
        )

        # Create 3 casos (cases)
        casos = [
            {
                'title': 'Caso Dev 1: Malversación de Fondos Municipales',
                'short_description': 'Investigación sobre el uso indebido de 2.5 millones de euros del presupuesto municipal.',
                'full_description': '''Este es un caso de desarrollo para pruebas.

# Resumen del Caso
Se detectó una malversación de fondos públicos en el ayuntamiento entre 2020 y 2023.

## Detalles
- Importe total: 2.5 millones de euros
- Duración: 4 años
- Afectados: Ciudadanos del municipio

Los fondos fueron destinados a empresas fantasma controladas por funcionarios municipales.''',
                'date': date(2023, 6, 15),
                'amount': Decimal('2500000.00'),
                'political_party': party1,
                'institution': institution1,
                'corruption_type': corruption_type1,
                'country': country1,
                'region': region1,
                'publication_type': 'case',
                'is_featured': True,
                'amount_2020': Decimal('500000.00'),
                'amount_2021': Decimal('750000.00'),
                'amount_2022': Decimal('800000.00'),
                'amount_2023': Decimal('450000.00'),
            },
            {
                'title': 'Caso Dev 2: Contratos Fraudulentos en Obras Públicas',
                'short_description': 'Adjudicación irregular de contratos de obras públicas por valor de 5 millones.',
                'full_description': '''Caso de desarrollo sobre contratos fraudulentos.

# Contexto
Entre 2019 y 2022 se adjudicaron contratos de forma irregular.

## Investigación
Las empresas beneficiarias tenían vínculos con cargos políticos.

Se han iniciado diligencias judiciales.''',
                'date': date(2022, 3, 20),
                'amount': Decimal('5000000.00'),
                'political_party': party2,
                'institution': institution2,
                'corruption_type': corruption_type2,
                'country': country1,
                'region': region1,
                'publication_type': 'case',
                'is_featured': True,
                'amount_2019': Decimal('1200000.00'),
                'amount_2020': Decimal('1500000.00'),
                'amount_2021': Decimal('1300000.00'),
                'amount_2022': Decimal('1000000.00'),
            },
            {
                'title': 'Caso Dev 3: Despilfarro en Gastos de Representación',
                'short_description': 'Uso excesivo e injustificado de fondos públicos para gastos de representación.',
                'full_description': '''Caso de desarrollo sobre gastos injustificados.

# Descripción
Altos cargos han gastado cantidades desproporcionadas en viajes y eventos.

## Montos
El gasto ascendió a 1.2 millones entre 2021 y 2024.

## Estado
En investigación por el tribunal de cuentas.''',
                'date': date(2024, 1, 10),
                'amount': Decimal('1200000.00'),
                'political_party': party1,
                'institution': institution2,
                'corruption_type': corruption_type1,
                'country': country1,
                'region': region1,
                'publication_type': 'case',
                'is_featured': False,
                'amount_2021': Decimal('300000.00'),
                'amount_2022': Decimal('350000.00'),
                'amount_2023': Decimal('400000.00'),
                'amount_2024': Decimal('150000.00'),
            }
        ]

        for caso_data in casos:
            caso, created = CorruptionCase.objects.get_or_create(
                title=caso_data['title'],
                defaults={k: v for k, v in caso_data.items() if k != 'title'}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created caso: {caso.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Caso already exists: {caso.title}'))

        # Create 3 articles (publications)
        articles = [
            {
                'title': 'Artículo Dev 1: Análisis del Gasto Público en 2023',
                'short_description': 'Un análisis detallado de cómo se distribuyó el presupuesto público durante 2023.',
                'full_description': '''Este es un artículo de desarrollo para pruebas.

# Introducción
Análisis del gasto público del año 2023.

## Principales Hallazgos
- El gasto social aumentó un 5%
- Las inversiones en infraestructura disminuyeron
- Se detectaron varias áreas de mejora

## Conclusiones
Es necesario mejorar la transparencia en la gestión pública.''',
                'date': date(2024, 1, 15),
                'amount': None,
                'publication_type': 'article',
                'author_name': 'Equipo de Análisis DEGU',
                'is_featured': True,
            },
            {
                'title': 'Artículo Dev 2: La Importancia de la Transparencia Gubernamental',
                'short_description': 'Opinión sobre por qué la transparencia es fundamental en la gestión pública.',
                'full_description': '''Artículo de opinión sobre transparencia.

# La Transparencia como Pilar
La transparencia gubernamental es esencial para la democracia.

## Beneficios
- Mayor confianza ciudadana
- Reducción de la corrupción
- Mejor uso de recursos públicos

## Recomendaciones
Implementar sistemas de datos abiertos y auditorías regulares.''',
                'date': date(2023, 11, 5),
                'amount': None,
                'publication_type': 'opinion',
                'author_name': 'María García Rodríguez',
                'is_featured': True,
            },
            {
                'title': 'Artículo Dev 3: Informe sobre Contratación Pública 2023',
                'short_description': 'Informe detallado sobre los procesos de contratación pública durante el año 2023.',
                'full_description': '''Informe sobre contratación pública.

# Resumen Ejecutivo
Análisis de los procesos de contratación del sector público.

## Datos Principales
- Se adjudicaron 15,000 contratos
- Valor total: 50,000 millones de euros
- 85% mediante procedimiento abierto

## Áreas de Mejora
- Digitalización de procesos
- Mayor competencia
- Reducción de plazos''',
                'date': date(2024, 2, 20),
                'amount': None,
                'publication_type': 'report',
                'author_name': 'Departamento de Investigación',
                'is_featured': False,
            }
        ]

        for article_data in articles:
            article, created = CorruptionCase.objects.get_or_create(
                title=article_data['title'],
                defaults={k: v for k, v in article_data.items() if k != 'title'}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created article: {article.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Article already exists: {article.title}'))

        self.stdout.write(self.style.SUCCESS('Development data creation complete!'))
        self.stdout.write(self.style.SUCCESS('Created/verified 3 casos and 3 articles'))


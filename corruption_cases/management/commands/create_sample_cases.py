from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from decimal import Decimal
from corruption_cases.models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, CorruptionCase
)

class Command(BaseCommand):
    help = 'Create sample corruption cases for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample corruption cases...')
        
        # Get existing objects
        psoe = PoliticalParty.objects.get(short_name='PSOE')
        pp = PoliticalParty.objects.get(short_name='PP')
        vox = PoliticalParty.objects.get(short_name='VOX')
        
        madrid_ayuntamiento = Institution.objects.get(name='Ayuntamiento de Madrid')
        barcelona_ayuntamiento = Institution.objects.get(name='Ayuntamiento de Barcelona')
        ministerio_transportes = Institution.objects.get(name='Ministerio de Transportes')
        
        malversacion = CorruptionType.objects.get(name='Malversación de fondos')
        cohecho = CorruptionType.objects.get(name='Cohecho')
        fraude = CorruptionType.objects.get(name='Fraude')
        
        madrid = Region.objects.get(name='Madrid')
        barcelona = Region.objects.get(name='Barcelona')
        
        # Sample corruption cases
        cases = [
            {
                'title': 'Caso Gürtel - Red de corrupción del PP',
                'short_description': 'Red de corrupción que afectó a múltiples administraciones del PP',
                'full_description': 'El caso Gürtel es una trama de corrupción que afectó principalmente al Partido Popular. La red se dedicaba a la concesión irregular de contratos públicos a cambio de comisiones ilegales. El caso se extendió por múltiples comunidades autónomas y municipios.',
                'date': date(2009, 2, 1),
                'amount': Decimal('120000000.00'),
                'political_party': pp,
                'institution': madrid_ayuntamiento,
                'corruption_type': malversacion,
                'region': madrid,
                'is_featured': True,
            },
            {
                'title': 'Caso Púnica - Corrupción en Madrid',
                'short_description': 'Trama de corrupción en el Ayuntamiento de Madrid',
                'full_description': 'El caso Púnica es una trama de corrupción que afectó al Ayuntamiento de Madrid durante la alcaldía de Ana Botella. Se investigaron presuntas irregularidades en contratos públicos y financiación ilegal del PP.',
                'date': date(2014, 10, 15),
                'amount': Decimal('25000000.00'),
                'political_party': pp,
                'institution': madrid_ayuntamiento,
                'corruption_type': cohecho,
                'region': madrid,
                'is_featured': True,
            },
            {
                'title': 'Caso 3% - Corrupción en Cataluña',
                'short_description': 'Comisiones ilegales en contratos de la Generalitat',
                'full_description': 'El caso 3% es una trama de corrupción que afectó a la Generalitat de Catalunya. Se investigó la exigencia de comisiones del 3% sobre contratos públicos para financiar Convergència Democràtica de Catalunya.',
                'date': date(2012, 3, 20),
                'amount': Decimal('45000000.00'),
                'political_party': None,  # CDC (no longer exists)
                'institution': Institution.objects.get(name='Generalitat de Catalunya'),
                'corruption_type': fraude,
                'region': barcelona,
                'is_featured': False,
            },
            {
                'title': 'Caso ERE - Fraude en Andalucía',
                'short_description': 'Fraude en expedientes de regulación de empleo',
                'full_description': 'El caso ERE es una trama de fraude que afectó a la Junta de Andalucía. Se investigó el desvío de fondos destinados a expedientes de regulación de empleo (ERE) para otros fines.',
                'date': date(2010, 5, 10),
                'amount': Decimal('680000000.00'),
                'political_party': psoe,
                'institution': Institution.objects.get(name='Junta de Andalucía'),
                'corruption_type': malversacion,
                'region': Region.objects.get(name='Sevilla'),
                'is_featured': True,
            },
            {
                'title': 'Caso Lezo - Corrupción en Madrid',
                'short_description': 'Trama de corrupción en el Ayuntamiento de Madrid',
                'full_description': 'El caso Lezo es una trama de corrupción que afectó al Ayuntamiento de Madrid. Se investigaron presuntas irregularidades en contratos de limpieza y mantenimiento.',
                'date': date(2013, 7, 8),
                'amount': Decimal('15000000.00'),
                'political_party': pp,
                'institution': madrid_ayuntamiento,
                'corruption_type': cohecho,
                'region': madrid,
                'is_featured': False,
            },
        ]
        
        for case_data in cases:
            case, created = CorruptionCase.objects.get_or_create(
                title=case_data['title'],
                defaults=case_data
            )
            if created:
                self.stdout.write(f'Created case: {case.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample corruption cases!')
        ) 
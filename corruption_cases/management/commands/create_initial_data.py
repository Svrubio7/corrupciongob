from django.core.management.base import BaseCommand
from corruption_cases.models import PoliticalParty, Institution, CorruptionType, Region, Tag

class Command(BaseCommand):
    help = 'Create initial data for the corruption portal'

    def handle(self, *args, **options):
        self.stdout.write('Creating initial data...')
        
        # Create political parties
        parties = [
            {'name': 'Partido Socialista Obrero Español', 'short_name': 'PSOE', 'color': '#FF0000'},
            {'name': 'Partido Popular', 'short_name': 'PP', 'color': '#0066CC'},
            {'name': 'Vox', 'short_name': 'VOX', 'color': '#5D8C3E'},
            {'name': 'Unidas Podemos', 'short_name': 'UP', 'color': '#8B4513'},
            {'name': 'Ciudadanos', 'short_name': 'Cs', 'color': '#FF6600'},
            {'name': 'Esquerra Republicana de Catalunya', 'short_name': 'ERC', 'color': '#FFD700'},
            {'name': 'Partido Nacionalista Vasco', 'short_name': 'PNV', 'color': '#228B22'},
        ]
        
        for party_data in parties:
            party, created = PoliticalParty.objects.get_or_create(
                name=party_data['name'],
                defaults=party_data
            )
            if created:
                self.stdout.write(f'Created political party: {party.name}')
        
        # Create corruption types
        corruption_types = [
            'Malversación de fondos',
            'Cohecho',
            'Tráfico de influencias',
            'Fraude',
            'Prevaricación',
            'Negociación prohibida',
            'Blanqueo de capitales',
            'Cohecho pasivo',
            'Cohecho activo',
            'Peculado',
        ]
        
        for corruption_type in corruption_types:
            obj, created = CorruptionType.objects.get_or_create(name=corruption_type)
            if created:
                self.stdout.write(f'Created corruption type: {corruption_type}')
        
        # Create regions
        regions = [
            {'name': 'Madrid', 'autonomous_community': 'Comunidad de Madrid'},
            {'name': 'Barcelona', 'autonomous_community': 'Cataluña'},
            {'name': 'Valencia', 'autonomous_community': 'Comunidad Valenciana'},
            {'name': 'Sevilla', 'autonomous_community': 'Andalucía'},
            {'name': 'Bilbao', 'autonomous_community': 'País Vasco'},
            {'name': 'Zaragoza', 'autonomous_community': 'Aragón'},
            {'name': 'Málaga', 'autonomous_community': 'Andalucía'},
            {'name': 'Murcia', 'autonomous_community': 'Región de Murcia'},
            {'name': 'Palma de Mallorca', 'autonomous_community': 'Islas Baleares'},
            {'name': 'Las Palmas', 'autonomous_community': 'Canarias'},
        ]
        
        for region_data in regions:
            region, created = Region.objects.get_or_create(
                name=region_data['name'],
                defaults=region_data
            )
            if created:
                self.stdout.write(f'Created region: {region.name}')
        
        # Create institutions
        institutions = [
            {'name': 'Ministerio de Transportes', 'institution_type': 'central'},
            {'name': 'Ministerio de Sanidad', 'institution_type': 'central'},
            {'name': 'Ministerio de Educación', 'institution_type': 'central'},
            {'name': 'Ayuntamiento de Madrid', 'institution_type': 'municipal'},
            {'name': 'Ayuntamiento de Barcelona', 'institution_type': 'municipal'},
            {'name': 'Generalitat de Catalunya', 'institution_type': 'autonomous'},
            {'name': 'Gobierno Vasco', 'institution_type': 'autonomous'},
            {'name': 'Junta de Andalucía', 'institution_type': 'autonomous'},
            {'name': 'Diputación de Barcelona', 'institution_type': 'provincial'},
            {'name': 'Diputación de Madrid', 'institution_type': 'provincial'},
        ]
        
        for institution_data in institutions:
            institution, created = Institution.objects.get_or_create(
                name=institution_data['name'],
                defaults=institution_data
            )
            if created:
                self.stdout.write(f'Created institution: {institution.name}')
        
        # Create some common tags
        tags = [
            'Caso Gürtel',
            'Caso Púnica',
            'Caso Lezo',
            'Caso ERE',
            'Caso 3%',
            'Caso Palau',
            'Caso Noos',
            'Caso Bárcenas',
            'Caso Bankia',
            'Caso Pujol',
        ]
        
        for tag in tags:
            obj, created = Tag.objects.get_or_create(name=tag)
            if created:
                self.stdout.write(f'Created tag: {tag}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created initial data!')
        ) 
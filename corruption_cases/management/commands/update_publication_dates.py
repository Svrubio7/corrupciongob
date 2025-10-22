from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
from corruption_cases.models import CorruptionCase


class Command(BaseCommand):
    help = 'Update publication_date for existing cases to 30/09/2025'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be updated without making changes',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        
        # Set the target date to September 30, 2025
        target_date = datetime(2025, 9, 30, 12, 0, 0)  # 12:00 PM on Sept 30, 2025
        
        # Find cases without publication_date
        cases_without_pub_date = CorruptionCase.objects.filter(publication_date__isnull=True)
        
        if not cases_without_pub_date.exists():
            self.stdout.write(
                self.style.SUCCESS('All cases already have publication_date set.')
            )
            return
        
        self.stdout.write(f'Found {cases_without_pub_date.count()} cases without publication_date')
        self.stdout.write(f'Will set publication_date to: {target_date.strftime("%d/%m/%Y %H:%M")}')
        
        if dry_run:
            self.stdout.write('DRY RUN - No changes will be made')
            for case in cases_without_pub_date:
                self.stdout.write(f'  - {case.title} (created: {case.created_at})')
        else:
            updated_count = 0
            for case in cases_without_pub_date:
                case.publication_date = target_date
                case.save()
                updated_count += 1
                self.stdout.write(f'Updated: {case.title}')
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully updated {updated_count} cases with publication_date = 30/09/2025')
            )

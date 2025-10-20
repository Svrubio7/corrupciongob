# Generated manually

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('corruption_cases', '0006_country_corruptioncase_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corruptioncase',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Importe en euros (obligatorio solo para casos)', max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Importe'),
        ),
    ]
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='predictions_deadline',
            field=models.DateTimeField(
                blank=True, null=True,
                help_text='Predictions automatically close after this date/time (UTC).',
            ),
        ),
        migrations.AddField(
            model_name='tournament',
            name='predictions_locked',
            field=models.BooleanField(
                default=False,
                help_text='Manual override: lock predictions regardless of deadline.',
            ),
        ),
    ]

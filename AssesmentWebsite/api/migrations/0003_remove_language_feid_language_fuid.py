# Generated by Django 4.2.6 on 2023-12-05 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='feid',
        ),
        migrations.AddField(
            model_name='language',
            name='fuid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expertise_id', to='api.demographic'),
        ),
    ]

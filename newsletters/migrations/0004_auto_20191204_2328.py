# Generated by Django 3.0 on 2019-12-04 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0003_auto_20191204_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='frequency',
            field=models.CharField(choices=[('monthly', 'Mensual'), ('daily', 'Diario'), ('weekly', 'Semanal')], default='monthly', max_length=10),
        ),
    ]

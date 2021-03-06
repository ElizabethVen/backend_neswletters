# Generated by Django 3.0 on 2019-12-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.FileField(upload_to='uploads/')),
                ('target', models.IntegerField()),
                ('frequency', models.CharField(choices=[('weekly', 'Semanal'), ('monthly', 'Mensual'), ('daily', 'Diario')], default='monthly', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-17 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_appointment_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/map', verbose_name='Карта проезда')),
                ('phone', models.CharField(max_length=100, verbose_name='Контактный телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-05 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clipboard', '0006_alter_clipboard_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clipboard',
            options={'ordering': ['-created_date']},
        ),
    ]
# Generated by Django 2.0.8 on 2018-09-26 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pki', '0006_add_x509_passphrase_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ca',
            name='passphrase',
        ),
        migrations.RemoveField(
            model_name='cert',
            name='passphrase',
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-19 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0004_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

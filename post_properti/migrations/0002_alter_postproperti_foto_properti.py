# Generated by Django 4.2.7 on 2023-12-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_properti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproperti',
            name='foto_properti',
            field=models.URLField(),
        ),
    ]

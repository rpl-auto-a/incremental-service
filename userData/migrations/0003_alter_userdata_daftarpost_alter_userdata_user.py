# Generated by Django 4.2.7 on 2023-12-03 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_properti', '0002_alter_postproperti_foto_properti'),
        ('userData', '0002_userdata_daftarpost_userdata_postfavorit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='daftarPost',
            field=models.ManyToManyField(blank=True, related_name='daftarPost', to='post_properti.postproperti'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
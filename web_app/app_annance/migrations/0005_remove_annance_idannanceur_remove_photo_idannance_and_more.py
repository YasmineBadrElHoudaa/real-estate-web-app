# Generated by Django 4.1.4 on 2023-02-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_annance', '0004_remove_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annance',
            name='idAnnanceur',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='idAnnance',
        ),
        migrations.AddField(
            model_name='annance',
            name='EmailAnnanceur',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='titreAnnance',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='titreAnnance',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
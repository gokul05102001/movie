# Generated by Django 4.2.1 on 2023-07-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='fhshj', upload_to='gallery'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.1 on 2019-05-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]

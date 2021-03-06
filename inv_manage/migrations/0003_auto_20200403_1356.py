# Generated by Django 3.0.4 on 2020-04-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv_manage', '0002_auto_20200403_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='internal_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='storage_location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

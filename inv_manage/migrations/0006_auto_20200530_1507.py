# Generated by Django 3.0.4 on 2020-05-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv_manage', '0005_sharepass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(default='item_pics/default.png', upload_to='item_pics'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-07-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20190717_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]

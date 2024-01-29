# Generated by Django 5.0.1 on 2024-01-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sizzleslice', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/png;base64,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', max_length=1000),
        ),
    ]

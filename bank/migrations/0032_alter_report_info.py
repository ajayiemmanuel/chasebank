# Generated by Django 4.2.4 on 2023-09-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0031_rename_code_report_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='info',
            field=models.CharField(default='Welcome', max_length=200),
        ),
    ]

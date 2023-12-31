# Generated by Django 4.2.4 on 2023-09-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0016_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avater.png', null=True, upload_to=''),
        ),
    ]

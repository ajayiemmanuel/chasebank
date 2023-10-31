# Generated by Django 4.2.4 on 2023-09-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0024_loan_name_alter_loan_action_alter_loan_active_loans_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='action',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='loan',
            name='amount_to_pay',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_id',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='loan',
            name='next_payment_date',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
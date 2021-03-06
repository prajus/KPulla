# Generated by Django 3.0.5 on 2020-07-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0005_transactions_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debts',
            name='compounding_term',
            field=models.SmallIntegerField(choices=[(1, 'Yearly'), (2, 'Half Yearly'), (3, 'Quarterly'), (4, 'Monthly')]),
        ),
        migrations.AlterField(
            model_name='debts',
            name='deposit_term',
            field=models.SmallIntegerField(choices=[(1, 'Years'), (2, 'Months'), (3, 'Days')]),
        ),
    ]

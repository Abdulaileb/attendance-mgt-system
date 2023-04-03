# Generated by Django 3.1.14 on 2023-03-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20230302_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='1 Silicon Hills', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(choices=[('M', 'Marriage'), ('S', 'Single'), ('D', 'Divorced'), ('W', 'Widowed')], default='S', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='total_hours_worked',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
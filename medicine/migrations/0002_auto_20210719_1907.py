# Generated by Django 3.0 on 2021-07-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='form',
            field=models.CharField(choices=[('Tablet', 'Tablet'), ('Powder', 'Powder'), ('Liquid', 'Liquid'), ('Injection', 'Injection')], max_length=10),
        ),
    ]

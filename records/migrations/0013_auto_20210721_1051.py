# Generated by Django 3.0 on 2021-07-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_auto_20210721_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='infplanoneblock',
            name='visit_no_a',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='infplantwoblock',
            name='visit_no_b',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

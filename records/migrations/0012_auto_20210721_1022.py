# Generated by Django 3.0 on 2021-07-21 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_auto_20210721_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infplanoneblock',
            old_name='comment',
            new_name='comment_a',
        ),
        migrations.RenameField(
            model_name='infplanoneblock',
            old_name='et',
            new_name='et_a',
        ),
        migrations.RenameField(
            model_name='infplanoneblock',
            old_name='left',
            new_name='left_a',
        ),
        migrations.RenameField(
            model_name='infplanoneblock',
            old_name='right',
            new_name='right_a',
        ),
        migrations.RenameField(
            model_name='infplantwoblock',
            old_name='comment',
            new_name='comment_b',
        ),
        migrations.RenameField(
            model_name='infplantwoblock',
            old_name='et',
            new_name='et_b',
        ),
        migrations.RenameField(
            model_name='infplantwoblock',
            old_name='left',
            new_name='left_b',
        ),
        migrations.RenameField(
            model_name='infplantwoblock',
            old_name='right',
            new_name='right_b',
        ),
    ]

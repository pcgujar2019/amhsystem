# Generated by Django 3.0 on 2021-07-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20210720_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g1_age',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g1_comment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g1_sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g2_age',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g2_comment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g2_sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g3_age',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g3_comment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g3_sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g4_age',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g4_comment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g4_sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g5_age',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g5_comment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='gynacopdfirstblock',
            name='g5_sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ancopdfirstblock',
            name='g1',
            field=models.CharField(blank=True, choices=[('PTND', 'Ptnd'), ('FTND', 'Ftnd'), ('LSCS', 'Lscs'), ('IUD', 'Iud'), ('Missed Abortion', 'Missed Abortion')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ancopdfirstblock',
            name='g2',
            field=models.CharField(blank=True, choices=[('PTND', 'Ptnd'), ('FTND', 'Ftnd'), ('LSCS', 'Lscs'), ('IUD', 'Iud'), ('Missed Abortion', 'Missed Abortion')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ancopdfirstblock',
            name='g3',
            field=models.CharField(blank=True, choices=[('PTND', 'Ptnd'), ('FTND', 'Ftnd'), ('LSCS', 'Lscs'), ('IUD', 'Iud'), ('Missed Abortion', 'Missed Abortion')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ancopdfirstblock',
            name='g4',
            field=models.CharField(blank=True, choices=[('PTND', 'Ptnd'), ('FTND', 'Ftnd'), ('LSCS', 'Lscs'), ('IUD', 'Iud'), ('Missed Abortion', 'Missed Abortion')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ancopdfirstblock',
            name='g5',
            field=models.CharField(blank=True, choices=[('PTND', 'Ptnd'), ('FTND', 'Ftnd'), ('LSCS', 'Lscs'), ('IUD', 'Iud'), ('Missed Abortion', 'Missed Abortion')], max_length=20),
        ),
    ]

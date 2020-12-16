# Generated by Django 3.1.4 on 2020-12-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userinfo_usertoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'machinetype',
            },
        ),
        migrations.DeleteModel(
            name='Tttest',
        ),
        migrations.RenameField(
            model_name='thing',
            old_name='coordinate_x',
            new_name='position_x',
        ),
        migrations.RenameField(
            model_name='thing',
            old_name='coordinate_y',
            new_name='position_y',
        ),
        migrations.AlterField(
            model_name='house',
            name='status_code',
            field=models.IntegerField(choices=[(1, 'working'), (2, 'standby'), (3, 'malfunction')]),
        ),
        migrations.AlterField(
            model_name='thing',
            name='status_code',
            field=models.IntegerField(choices=[(1, 'working'), (2, 'standby'), (3, 'malfunction')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]

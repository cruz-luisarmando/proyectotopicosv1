# Generated by Django 2.2.6 on 2019-11-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutoriallac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tutorial_lac', models.CharField(max_length=50)),
                ('descripcion_tutorial_lac', models.TextField()),
            ],
        ),
    ]

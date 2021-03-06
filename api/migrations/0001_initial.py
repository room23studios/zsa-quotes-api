# Generated by Django 2.0.3 on 2018-03-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(unique=True)),
                ('date', models.DateTimeField()),
                ('annotation', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
    ]

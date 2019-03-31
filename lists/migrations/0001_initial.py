# Generated by Django 2.1.5 on 2019-03-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('level', models.CharField(max_length=25)),
                ('t_ype', models.CharField(max_length=25)),
                ('instructor', models.CharField(max_length=25)),
            ],
        ),
    ]
# Generated by Django 2.2.24 on 2021-10-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=25)),
                ('ename', models.CharField(max_length=30)),
                ('eemail', models.EmailField(max_length=254)),
                ('eaddress', models.TextField()),
            ],
        ),
    ]

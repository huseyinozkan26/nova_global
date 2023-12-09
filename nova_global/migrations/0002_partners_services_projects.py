# Generated by Django 4.2.8 on 2023-12-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova_global', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=444)),
                ('desc', models.TextField()),
                ('partner_logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=455)),
                ('desc', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('images', models.ManyToManyField(related_name='Services', to='nova_global.images')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=444)),
                ('desc', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('images', models.ManyToManyField(related_name='Projects', to='nova_global.images')),
                ('partner', models.ManyToManyField(related_name='Projects', to='nova_global.partners')),
            ],
        ),
    ]
# Generated by Django 3.1 on 2020-08-13 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('description', models.TextField()),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.location')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

# Generated by Django 3.0 on 2019-12-18 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('OS', models.CharField(max_length=20)),
                ('CPU', models.CharField(max_length=20)),
                ('GPU', models.CharField(max_length=20)),
                ('cam', models.CharField(max_length=20)),
                ('mic', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=8000)),
                ('example', models.CharField(max_length=8000)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cost', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ZtrUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=1)),
                ('nickname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('salt', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('user_devices', models.ManyToManyField(to='base_app.Devices')),
                ('user_products', models.ManyToManyField(to='base_app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='UserPref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_speed', models.IntegerField()),
                ('user_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base_app.ZtrUser')),
            ],
        ),
    ]
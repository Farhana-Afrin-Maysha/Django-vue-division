# Generated by Django 3.0.4 on 2020-03-20 05:22

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
                ('name', models.CharField(max_length=100)),
                ('bn_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('bn_name', models.CharField(max_length=25)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('bn_name', models.CharField(max_length=25)),
                ('lat', models.CharField(max_length=15, null=True)),
                ('lon', models.CharField(max_length=15, null=True)),
                ('url', models.CharField(max_length=50)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Probad.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Chondokotha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Probad.District')),
            ],
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-20 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Probad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chondokotha',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Probad.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chondokotha',
            name='district',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Probad.District'),
        ),
    ]

# Generated by Django 3.2.16 on 2022-10-30 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brigada',
            options={'ordering': ['brigada_name'], 'verbose_name': 'Бригада', 'verbose_name_plural': 'Бригады'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['city_name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'ordering': ['object_name'], 'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
        migrations.AddField(
            model_name='object',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='objects', to='objects.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='brigada',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brigadas', to='objects.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='object',
            name='brigada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='objects', to='objects.brigada', verbose_name='Бригада'),
        ),
    ]

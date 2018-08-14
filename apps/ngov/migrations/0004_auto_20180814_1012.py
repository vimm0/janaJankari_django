# Generated by Django 2.1 on 2018-08-14 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngov', '0003_auto_20180814_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='location_en',
            field=models.CharField(max_length=254, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='department',
            name='location_ne',
            field=models.CharField(max_length=254, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='department',
            name='name_en',
            field=models.CharField(max_length=254, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='department',
            name='name_ne',
            field=models.CharField(max_length=254, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='office',
            name='department_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='office',
            name='department_ne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='office',
            name='ministry_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Ministry', verbose_name='Ministry'),
        ),
        migrations.AddField(
            model_name='office',
            name='ministry_ne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Ministry', verbose_name='Ministry'),
        ),
        migrations.AddField(
            model_name='office',
            name='name_en',
            field=models.CharField(max_length=254, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='office',
            name='name_ne',
            field=models.CharField(max_length=254, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='office',
            name='website_en',
            field=models.URLField(null=True, verbose_name='website'),
        ),
        migrations.AddField(
            model_name='office',
            name='website_ne',
            field=models.URLField(null=True, verbose_name='website'),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-29 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('goal', models.IntegerField()),
                ('activity_level', models.IntegerField()),
                ('time_commitment', models.IntegerField()),
                ('calorie_target', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('fats', models.IntegerField()),
                ('program', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('savol', models.CharField(max_length=100)),
                ('javoblar', models.CharField(max_length=100)),
            ],
        ),
    ]

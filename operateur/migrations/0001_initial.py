# Generated by Django 3.2.20 on 2024-02-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('id_operateur', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
    ]
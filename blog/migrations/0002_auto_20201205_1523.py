# Generated by Django 3.0.5 on 2020-12-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
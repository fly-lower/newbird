# Generated by Django 2.2.1 on 2019-09-12 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_auto_20190911_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=None)),
                ('gender', models.CharField(max_length=8)),
                ('teacher_person', models.ManyToManyField(to='homeapp.Person')),
            ],
        ),
    ]
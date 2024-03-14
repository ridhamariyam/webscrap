# Generated by Django 5.0.3 on 2024-03-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('protocol', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('uptime', models.CharField(max_length=50)),
            ],
        ),
    ]
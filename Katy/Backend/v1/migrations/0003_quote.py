# Generated by Django 3.0.8 on 2023-01-24 06:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_auto_20230124_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('create_id', models.IntegerField()),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('update_id', models.IntegerField(blank=True, null=True)),
                ('is_open', models.BooleanField(default=True)),
                ('type', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
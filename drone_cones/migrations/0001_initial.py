# Generated by Django 4.1.7 on 2023-11-10 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('lastName', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('cart', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('flavor', models.CharField(max_length=100)),
                ('stockAvailable', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('items', models.JSONField()),
                ('drone', models.IntegerField()),
                ('deliverySuccessful', models.BooleanField()),
                ('timeOrdered', models.DateField()),
                ('timeDelivered', models.DateField()),
                ('timeToDeliver', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_cones.account')),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('droneName', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('scoops', models.IntegerField()),
                ('isActive', models.BooleanField(default=False)),
                ('dateRegistered', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_cones.account')),
            ],
        ),
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accessLevel', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_cones.account')),
            ],
        ),
    ]

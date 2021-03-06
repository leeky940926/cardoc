# Generated by Django 3.2.9 on 2021-11-23 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableYearType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('yearType', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'year_types',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('brandName', models.CharField(max_length=20)),
                ('brandNameEng', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('imImported', models.BooleanField(default=False)),
                ('brandImageUrl', models.CharField(max_length=500)),
                ('brandUrl', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('gradeName', models.CharField(max_length=20)),
                ('fuelType', models.CharField(max_length=20)),
                ('displacement', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='ModelGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('modelName', models.CharField(max_length=20)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.brand')),
            ],
            options={
                'db_table': 'model_groups',
            },
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('trimName', models.CharField(max_length=20)),
                ('salesCode', models.PositiveIntegerField()),
                ('bodySize', models.CharField(max_length=5)),
                ('bodyStyle', models.CharField(max_length=20)),
                ('transmission', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('priceUnit', models.PositiveIntegerField()),
                ('isRecommended', models.BooleanField(default=False)),
                ('releaseDate', models.DateField(null=True)),
                ('discontinuedDate', models.DateField(null=True)),
                ('carTypeCode', models.PositiveIntegerField()),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.grade')),
            ],
            options={
                'db_table': 'trims',
            },
        ),
        migrations.CreateModel(
            name='TrimUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('trim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.trim')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'trims_users',
            },
        ),
        migrations.AddField(
            model_name='trim',
            name='user',
            field=models.ManyToManyField(through='trims.TrimUser', to='users.User'),
        ),
        migrations.CreateModel(
            name='SubModelGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('submodelGroupYearTypeFrom', models.PositiveIntegerField()),
                ('submodelGroupYearTypeTo', models.PositiveIntegerField()),
                ('submodelGroupName', models.CharField(max_length=20)),
                ('modelGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.modelgroup')),
            ],
            options={
                'db_table': 'submodel_groups',
            },
        ),
        migrations.CreateModel(
            name='SubModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('submodelName', models.CharField(max_length=20)),
                ('submodelNameEng', models.CharField(max_length=20)),
                ('submodelImageUrl', models.CharField(max_length=500)),
                ('submodelGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.submodelgroup')),
                ('yearType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.availableyeartype')),
            ],
            options={
                'db_table': 'submodels',
            },
        ),
        migrations.CreateModel(
            name='RearTire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=20)),
                ('multiValues', models.CharField(max_length=20)),
                ('trim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.trim')),
            ],
            options={
                'db_table': 'rear_tires',
            },
        ),
        migrations.AddField(
            model_name='grade',
            name='submodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.submodel'),
        ),
        migrations.CreateModel(
            name='FrontTire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=20)),
                ('multiValues', models.CharField(max_length=20)),
                ('trim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trims.trim')),
            ],
            options={
                'db_table': 'front_tires',
            },
        ),
    ]

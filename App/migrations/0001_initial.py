# Generated by Django 4.0.1 on 2022-01-30 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Number', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meal_Name', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=255)),
                ('Description', models.TextField()),
                ('Image', models.FileField(default='Image/default.jpg', upload_to='Images')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Number', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Date', models.DateField()),
                ('NumberofPeople', models.CharField(choices=[('Below 10People', 'Below 10People'), ('10 People', '10 People'), ('20 People', '20 People'), ('50 People', '50 People'), ('100 People', '100 People'), ('Above 100People', 'Above 100People')], max_length=255)),
                ('Description', models.TextField()),
                ('Meal_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.meals')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Number', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Date', models.DateField()),
                ('DeliveringAddress', models.TextField()),
                ('Plates', models.IntegerField()),
                ('Description', models.TextField()),
                ('Meal_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.meals')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(choices=[('Drinks', 'Drinks'), ('Food', 'Food'), ('Sandwich', 'Sandwich'), ('Snacks', 'Snacks')], max_length=255)),
                ('Description', models.TextField()),
                ('Image', models.FileField(default='Image/default.jpg', upload_to='Images')),
                ('Meal_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.meals')),
            ],
        ),
        migrations.CreateModel(
            name='AllItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Price', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Image', models.FileField(default='Image/default.jpg', upload_to='Images')),
                ('Category_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
                ('Meal_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.meals')),
            ],
        ),
    ]

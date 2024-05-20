# Generated by Django 5.0.6 on 2024-05-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('course', models.CharField(choices=[('Cetificate in Health Science', 'Cetificate in Health Science'), ('Certificate in Applied Technology', 'Certificate in Applied Technology'), ('Bachelor of Information Technology', 'Bachelor of Information Technology'), ('Bachelors in Business Technology', 'Bachelors in Business Technology'), ('Master of Public Health', 'Master of Public Health')], max_length=34)),
                ('entryscheme', models.CharField(choices=[('A-Level certificate', 'A-Level certificate'), ('Adult/Mature Learning', 'Adult/Mature Learning'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Bachelors', 'Bachelors')], max_length=21)),
                ('intake', models.CharField(choices=[('January Intake', 'January Intake'), ('May Intake', 'May Intake'), ('August Intake', 'August Intake')], max_length=14)),
                ('sponsorship', models.CharField(choices=[('Private', 'Private'), ('Government', 'Government'), ('Bursary', 'Bursary')], max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('date_of_birth', models.DateField()),
                ('residence', models.CharField(max_length=255)),
            ],
        ),
    ]
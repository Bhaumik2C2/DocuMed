# Generated by Django 5.0.3 on 2024-03-11 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_remove_doctoruser_password_and_more'),
        ('patients', '0007_alter_documents_author_alter_medication_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctoruser'),
        ),
        migrations.CreateModel(
            name='SharedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctoruser')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.documents')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patientuser')),
            ],
        ),
    ]

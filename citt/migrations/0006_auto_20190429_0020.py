# Generated by Django 2.2 on 2019-04-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citt', '0005_auto_20190429_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='estado_evento',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Cerrado', 'Cerrado')], max_length=20, null=True),
        ),
    ]

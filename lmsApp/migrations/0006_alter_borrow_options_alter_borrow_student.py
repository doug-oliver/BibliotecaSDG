# Generated by Django 4.0.3 on 2023-07-18 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lmsApp', '0005_borrow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrow',
            options={'verbose_name_plural': 'Transações de Impréstimos'},
        ),
        migrations.AlterField(
            model_name='borrow',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to=settings.AUTH_USER_MODEL),
        ),
    ]

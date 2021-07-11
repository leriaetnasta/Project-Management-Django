# Generated by Django 3.2.3 on 2021-07-06 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_employe', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_responsable', models.BooleanField(default=False)),
                ('titre', models.CharField(choices=[('Mr', 'Mr'), ('Mme', 'Mme')], default='Mr', max_length=4, null=True)),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autre', 'Autre')], default='Homme', max_length=8)),
                ('ce', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('role', models.CharField(choices=[('COMPTABLE', 'Comptable'), ('DIRECTEUR', 'Directeur'), ('SECRETAIRE', 'Secretaire'), ("RESPONSABLE D'ACHAT", "Responsable d'achat"), ('COMMERCIAL', 'Commercial'), ('CHEF DE SERVISE', 'Chef de service'), ('RESPONSABLE RH', 'Responsable RH'), ('TECHNICIEN', 'Technicien'), ('INGENIEUR', 'Ingenieur')], default=0, max_length=100)),
                ('adresse', models.TextField()),
                ('ville', models.CharField(max_length=100)),
                ('telephone', models.CharField(default='+212600000000', help_text='Entrer un numero de telephone E.G 2126XXXXXXXX', max_length=20)),
                ('cin', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('employe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.employe')),
            ],
            bases=('accounts.employe',),
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('employe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.employe')),
            ],
            bases=('accounts.employe',),
        ),
    ]
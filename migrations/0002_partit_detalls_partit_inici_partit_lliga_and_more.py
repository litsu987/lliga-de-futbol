# Generated by Django 4.2 on 2024-02-29 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lliga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partit',
            name='detalls',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partit',
            name='inici',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partit',
            name='lliga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lliga.lliga'),
        ),
        migrations.AlterUniqueTogether(
            name='partit',
            unique_together={('local', 'visitant', 'lliga')},
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temps', models.TimeField()),
                ('tipus', models.CharField(choices=[('GOL', 'Gol'), ('AUTOGOL', 'Autogol'), ('FALTA', 'Falta'), ('PENALTY', 'Penalty'), ('MANS', 'Mans'), ('CESSIO', 'Cessio'), ('FORA_DE_JOC', 'Fora De Joc'), ('ASSISTENCIA', 'Assistencia'), ('TARGETA_GROGA', 'Targeta Groga'), ('TARGETA_VERMELLA', 'Targeta Vermella')], max_length=30)),
                ('detalls', models.TextField(blank=True, null=True)),
                ('equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lliga.equip')),
                ('jugador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_fets', to='lliga.jugador')),
                ('jugador2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_rebuts', to='lliga.jugador')),
                ('partit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lliga.partit')),
            ],
        ),
        migrations.RemoveField(
            model_name='partit',
            name='data',
        ),
        migrations.RemoveField(
            model_name='partit',
            name='resultat_local',
        ),
        migrations.RemoveField(
            model_name='partit',
            name='resultat_visitant',
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-22 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionPrueba', '0003_alter_comunicado_detalle_alter_entidad_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Publicación'),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modificados', to='AplicacionPrueba.usuario'),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='publicado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicados', to='AplicacionPrueba.usuario'),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='tipo',
            field=models.CharField(choices=[('S', 'Suspensión de Actividades'), ('C', 'Suspensión de Clases'), ('I', 'Información')], max_length=25),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_imagem_alter_servico_icone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('recurso', models.CharField(max_length=100, verbose_name='Recurso')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Camadas'), ('lni-laptop-phone', 'Responsivo'), ('lni-cog', 'Engrenagem')], max_length=25, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Design'), ('lni-users', 'Usuarios'), ('lni-rocket', 'Foguete'), ('lni-mobile', 'Mobile'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Grafico')], max_length=12, verbose_name='Icone'),
        ),
    ]
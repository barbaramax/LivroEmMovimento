from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='aclivroemmovimento@gmail.com', help_text='E-mail usado no botão de e-mail da aba de contatos.', max_length=254, verbose_name='E-mail de contato')),
                ('whatsapp', models.CharField(default='(21) 98097-4799', help_text='Número do WhatsApp com DDD. Pode ser digitado com máscara (ex.: (21) 98097-4799). O DDI 55 é adicionado automaticamente.', max_length=32, verbose_name='WhatsApp')),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Configuração de contato',
                'verbose_name_plural': 'Configurações de contato',
            },
        ),
    ]
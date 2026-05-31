from django.db import migrations


SINGLETON_ID = 1
DEFAULT_EMAIL = "aclivroemmovimento@gmail.com"
DEFAULT_WHATSAPP = "(21) 98097-4799"


def seed_default(apps, schema_editor):
    ContactSettings = apps.get_model("contato", "ContactSettings")
    ContactSettings.objects.update_or_create(
        pk=SINGLETON_ID,
        defaults={"email": DEFAULT_EMAIL, "whatsapp": DEFAULT_WHATSAPP},
    )


def remove_default(apps, schema_editor):
    ContactSettings = apps.get_model("contato", "ContactSettings")
    ContactSettings.objects.filter(pk=SINGLETON_ID).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("contato", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_default, remove_default),
    ]

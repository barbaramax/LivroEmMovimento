from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from .models import ContactSettings
from .services import (
    build_mailto_url,
    build_whatsapp_url,
    sanitize_phone,
    to_whatsapp_number,
)


class ServicesTests(TestCase):
    def test_sanitize_phone_remove_nao_digitos(self):
        self.assertEqual(sanitize_phone("(21) 98097-4799"), "21980974799")
        self.assertEqual(sanitize_phone("+55 (21) 98097-4799"), "5521980974799")
        self.assertEqual(sanitize_phone(""), "")
        self.assertEqual(sanitize_phone(None), "")

    def test_to_whatsapp_number_adiciona_ddi(self):
        self.assertEqual(to_whatsapp_number("(21) 98097-4799"), "5521980974799")

    def test_to_whatsapp_number_mantem_ddi_existente(self):
        self.assertEqual(to_whatsapp_number("+55 21 98097-4799"), "5521980974799")

    def test_build_whatsapp_url_basico(self):
        self.assertEqual(
            build_whatsapp_url("(21) 98097-4799"),
            "https://wa.me/5521980974799",
        )

    def test_build_whatsapp_url_com_mensagem(self):
        url = build_whatsapp_url("(21) 98097-4799", message="Olá!")
        self.assertTrue(url.startswith("https://wa.me/5521980974799?text="))

    def test_build_mailto_url_basico(self):
        self.assertEqual(
            build_mailto_url("foo@bar.com"),
            "mailto:foo@bar.com",
        )

    def test_build_mailto_url_com_assunto(self):
        url = build_mailto_url("foo@bar.com", subject="Oi")
        self.assertEqual(url, "mailto:foo@bar.com?subject=Oi")


class ContactSettingsModelTests(TestCase):
    def test_load_cria_registro_padrao(self):
        obj = ContactSettings.load()
        self.assertEqual(obj.pk, ContactSettings.SINGLETON_ID)
        self.assertEqual(obj.email, "aclivroemmovimento@gmail.com")
        self.assertEqual(obj.whatsapp, "(21) 98097-4799")

    def test_singleton_save_forca_pk(self):
        ContactSettings.load()
        novo = ContactSettings(email="x@x.com", whatsapp="(21) 98097-4799")
        novo.save()
        self.assertEqual(ContactSettings.objects.count(), 1)

    def test_delete_nao_remove_registro(self):
        obj = ContactSettings.load()
        obj.delete()
        self.assertTrue(ContactSettings.objects.filter(pk=obj.pk).exists())

    def test_get_mailto_url(self):
        obj = ContactSettings.load()
        self.assertEqual(
            obj.get_mailto_url(),
            "mailto:aclivroemmovimento@gmail.com",
        )

    def test_get_whatsapp_url(self):
        obj = ContactSettings.load()
        self.assertEqual(
            obj.get_whatsapp_url(),
            "https://wa.me/5521980974799",
        )

    def test_clean_rejeita_telefone_invalido(self):
        obj = ContactSettings.load()
        obj.whatsapp = "123"
        with self.assertRaises(ValidationError):
            obj.full_clean()


class ContatoViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        ContactSettings.load()  # garante o singleton

    def test_email_redirect(self):
        resp = self.client.get(reverse("contato:email"))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp["Location"], "mailto:aclivroemmovimento@gmail.com")

    def test_whatsapp_redirect(self):
        resp = self.client.get(reverse("contato:whatsapp"))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp["Location"], "https://wa.me/5521980974799")

    def test_contact_info_json(self):
        resp = self.client.get(reverse("contato:info"))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["email"], "aclivroemmovimento@gmail.com")
        self.assertEqual(data["whatsapp_sanitized"], "5521980974799")
        self.assertEqual(data["mailto_url"], "mailto:aclivroemmovimento@gmail.com")
        self.assertEqual(data["whatsapp_url"], "https://wa.me/5521980974799")

    def test_redirects_refletem_admin(self):
        obj = ContactSettings.load()
        obj.email = "novo@exemplo.com"
        obj.whatsapp = "(11) 99999-0000"
        obj.save()

        resp = self.client.get(reverse("contato:email"))
        self.assertEqual(resp["Location"], "mailto:novo@exemplo.com")

        resp = self.client.get(reverse("contato:whatsapp"))
        self.assertEqual(resp["Location"], "https://wa.me/5511999990000")

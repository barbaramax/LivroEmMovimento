from django.core.exceptions import ValidationError
from django.db import models

from .services import (
    build_mailto_url,
    build_whatsapp_url,
    sanitize_phone,
    to_whatsapp_number,
)


class ContactSettings(models.Model):

    SINGLETON_ID = 1

    email = models.EmailField(
        "E-mail de contato",
        default="aclivroemmovimento@gmail.com",
        help_text="E-mail usado no botão de e-mail da aba de contatos.",
    )
    whatsapp = models.CharField(
        "WhatsApp",
        max_length=32,
        default="(21) 98097-4799",
        help_text=(
            "Número do WhatsApp com DDD. Pode ser digitado com máscara "
            "(ex.: (21) 98097-4799). O DDI 55 é adicionado automaticamente."
        ),
    )
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuração de contato"
        verbose_name_plural = "Configurações de contato"

    def __str__(self):
        return "Configurações de contato"

    def save(self, *args, **kwargs):
        self.pk = self.SINGLETON_ID
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return

    @classmethod
    def load(cls) -> "ContactSettings":
        obj, _ = cls.objects.get_or_create(pk=cls.SINGLETON_ID)
        return obj

    def clean(self):
        super().clean()
        digits = sanitize_phone(self.whatsapp)
        if not digits or len(digits) < 10 or len(digits) > 13:
            raise ValidationError(
                {"whatsapp": "Informe um número válido com DDD (ex.: (21) 98097-4799)."}
            )

    @property
    def whatsapp_sanitized(self) -> str:
        return to_whatsapp_number(self.whatsapp)

    def get_mailto_url(self, subject: str = "", body: str = "") -> str:
        return build_mailto_url(self.email, subject=subject, body=body)

    def get_whatsapp_url(self, message: str = "") -> str:
        return build_whatsapp_url(self.whatsapp, message=message)

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from .models import ContactSettings


@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):
    list_display = ("email", "whatsapp", "atualizado_em")
    readonly_fields = ("atualizado_em", "preview_mailto", "preview_whatsapp")
    fieldsets = (
        ("Dados de contato", {"fields": ("email", "whatsapp")}),
        (
            "Pré-visualização dos links",
            {
                "fields": ("preview_mailto", "preview_whatsapp"),
                "description": (
                    "Links gerados automaticamente a partir dos dados acima. "
                    "Use-os para conferir antes de salvar."
                ),
            },
        ),
        ("Auditoria", {"fields": ("atualizado_em",)}),
    )

    def has_add_permission(self, request):
        return not ContactSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = ContactSettings.objects.first()
        if obj is not None:
            url = reverse(
                "admin:%s_%s_change"
                % (self.model._meta.app_label, self.model._meta.model_name),
                args=[obj.pk],
            )
            return HttpResponseRedirect(url)
        return super().changelist_view(request, extra_context)

    @admin.display(description="Link de e-mail (mailto:)")
    def preview_mailto(self, obj):
        if not obj or not obj.pk:
            return "—"
        url = obj.get_mailto_url()
        return format_html('<a href="{0}">{0}</a>', url)

    @admin.display(description="Link do WhatsApp (wa.me)")
    def preview_whatsapp(self, obj):
        if not obj or not obj.pk:
            return "—"
        url = obj.get_whatsapp_url()
        return format_html('<a href="{0}" target="_blank">{0}</a>', url)

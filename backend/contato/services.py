import re
from urllib.parse import quote


DEFAULT_COUNTRY_CODE = "55"


def sanitize_phone(raw: str) -> str:
    if not raw:
        return ""
    return re.sub(r"\D+", "", raw)


def to_whatsapp_number(raw: str, country_code: str = DEFAULT_COUNTRY_CODE) -> str:
    digits = sanitize_phone(raw)
    if not digits:
        return ""

    if digits.startswith(country_code):
        return digits

    return f"{country_code}{digits}"


def build_whatsapp_url(raw: str, message: str = "") -> str:
    number = to_whatsapp_number(raw)
    if not number:
        return ""

    url = f"https://wa.me/{number}"
    if message:
        url = f"{url}?text={quote(message)}"
    return url


def build_mailto_url(email: str, subject: str = "", body: str = "") -> str:
    if not email:
        return ""

    url = f"mailto:{email}"
    params = []
    if subject:
        params.append(f"subject={quote(subject)}")
    if body:
        params.append(f"body={quote(body)}")
    if params:
        url = f"{url}?{'&'.join(params)}"
    return url

#!/usr/bin/env python3
"""Telefon maketinin uygulama metinlerini uygulamanın kendi çevirilerinden çeker.

Maketteki her yazı ("Kayıtlarda ara", "Hesap / Şifre", "QR ile içe aktar"…)
uygulamanın strings.xml dosyalarından gelir; site kendi çevirisini uydurmaz.
Böylece maket, uygulamanın o dildeki hâlini gösterir ve uygulamada bir metin
değişince tek komutla buraya da yansır:

    python3 telefon_metin.py ../vault      # uygulama deposunun yolu

Çıktı: telefon_metin.json (16 dil). build.py her sayfaya yalnız o sayfanın
dilini gömer.
"""
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ORDER = ["en", "tr", "es", "hi", "ar", "zh", "fr", "bn", "pt", "ru", "ur", "id", "de", "ja", "pcm", "vi"]

KEYS = [
    "home_search_hint",
    "type_login", "type_everyday", "type_card", "type_note",
    "note_kind_general", "note_kind_script", "note_kind_key",
    "note_kind_fingerprint", "note_kind_recovery", "note_kind_config",
    "field_full_name", "field_username", "field_password", "field_url",
    "field_phone", "field_email", "field_address", "field_cardholder",
    "field_card_number", "field_expiry", "field_cvv", "field_iban", "field_notes",
    "detail_show_fingerprint", "detail_fingerprint_len",
    "detail_quick_title", "detail_quick_off", "detail_quick_on",
    "detail_dates", "detail_usage_title", "detail_usage_empty",
    "home_import_qr", "home_import_text",
    "qr_status_aim", "qr_status_received", "qr_status_done", "qr_cancel",
    "qr_camera_analysis",
    "paste_title_qr", "paste_qr_ready", "paste_label_backup_password",
    "paste_btn_import", "paste_btn_importing", "paste_btn_cancel",
    "bt_title", "bt_connecting", "bt_connected", "bt_typing_progress",
    "bt_done_summary", "bt_close", "bt_layout_tr", "bt_layout_us",
    "bt_duration_seconds",
]
PLURALS = ["vm_import_added"]


def android_text(raw):
    """Android kaynak kaçışlarını çöz: \\' \\" \\n \\t \\@ \\? ve çevreleyen tırnak."""
    s = raw.strip()
    if len(s) >= 2 and s[0] == s[-1] == '"':
        s = s[1:-1]
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            n = s[i + 1]
            # \uXXXX: Arapça ve Urduca'daki yön yalıtıcıları (U+2068/2069) böyle yazılı.
            if n == "u" and re.fullmatch(r"[0-9a-fA-F]{4}", s[i + 2:i + 6]):
                out.append(chr(int(s[i + 2:i + 6], 16)))
                i += 6
                continue
            out.append({"n": "\n", "t": "\t"}.get(n, n))
            i += 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def inner_text(el):
    """<string> içeriği; <xliff:g> gibi iç öğeler varsa metinleri birleştirilir."""
    return "".join(el.itertext())


def load(res_dir):
    root = ET.parse(res_dir / "strings.xml").getroot()
    strings, plurals = {}, {}
    for el in root:
        name = el.get("name")
        if el.tag == "string":
            strings[name] = android_text(inner_text(el))
        elif el.tag == "plurals":
            plurals[name] = {it.get("quantity"): android_text(inner_text(it)) for it in el}
    return strings, plurals


def arac_metinleri(aktar_html):
    """aktar.html'in kendi arayüz metinleri (yalnız tr ve en var).

    Dizüstü maketi aracın gerçek yazılarını göstersin diye. Şablonlu
    metinler (`Kare ${i}/${n}`) Android biçimine (%1$d) çevrilir.
    """
    s = aktar_html.read_text(encoding="utf-8")
    out = {}
    for dil in ("tr", "en"):
        bas = re.search(rf"\n\s*{dil}\s*:\s*\{{", s)
        if not bas:
            sys.exit(f"aktar.html içinde {dil} sözlüğü bulunamadı")
        blok = s[bas.end():bas.end() + 20000]
        t = {}
        for k in ("h1", "btnQr", "uyariQr", "lblBaslik", "lblTur", "turNot", "lblNoteKind", "nkAnahtar",
                  "lblParola", "lblYol", "yolQr"):
            m = re.search(rf"\b{k}:\s*\"((?:[^\"\\]|\\.)*)\"", blok)
            if not m:
                sys.exit(f"aktar.html {dil}.{k} yok")
            t[k] = m.group(1).replace('\\"', '"')
        m = re.search(r"kareCok:\s*\(i, n, sn\)\s*=>\s*`([^`]*)`", blok)
        if not m:
            sys.exit(f"aktar.html {dil}.kareCok yok")
        t["kareCok"] = m.group(1).replace("${i}", "%1$d").replace("${n}", "%2$d").replace("${sn}", "%3$d")
        out[dil] = t
    return out


def main():
    app = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../vault")
    res = app / "app/src/main/res"
    base_s, base_p = load(res / "values")
    data = {}
    for code in ORDER:
        d = res / ("values" if code == "en" else f"values-{code}")
        s, p = load(d)
        t = {}
        for k in KEYS:
            if k not in base_s:
                sys.exit(f"anahtar uygulamada yok: {k}")
            t[k] = s.get(k, base_s[k])     # çevrilmemişse uygulama da İngilizce gösterir
        for k in PLURALS:
            forms = p.get(k) or base_p[k]
            t[k] = {q: forms[q] for q in ("one", "other") if q in forms} or base_p[k]
        data[code] = t
    data["_arac"] = arac_metinleri(app / "tools/aktar.html")
    out = pathlib.Path(__file__).parent / "telefon_metin.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(ORDER)} dil × {len(KEYS) + len(PLURALS)} metin")


if __name__ == "__main__":
    main()

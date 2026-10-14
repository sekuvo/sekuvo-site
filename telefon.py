"""Telefon maketinin sayfaya gömülen verisi.

Üç kaynak birleşir:
  app   — uygulamanın kendi metinleri (telefon_metin.json; telefon_metin.py
          uygulama deposundan çeker). Site bunları çevirmez, olduğu gibi alır.
  demo  — maketteki kasanın içeriği: kayıt başlıkları, etiket adları, örnek
          ad ve adres kalıbı. DEĞERLER burada değil: parolalar, anahtarlar,
          kart numaraları her sayfa açılışında tarayıcıda rastgele üretilir
          (js/telefon.js). E-postalar example.com'dur (RFC 2606).
  site  — maketin çevresindeki site metinleri (model seçici, ölçek notu).

Çevirisi olmayan dil İngilizce demo içeriğine düşer; uygulama metinleri ise
her dilde uygulamanın kendisinden gelir.
"""
import json
import pathlib

_KOK = pathlib.Path(__file__).parent
APP = json.loads((_KOK / "telefon_metin.json").read_text(encoding="utf-8"))

DEMO = {}

DEMO["en"] = dict(
    adlar=["Alex Morgan", "Sam Taylor", "Jordan Lee", "Casey Brooks", "Riley Chen"],
    etiket_finans="finance", etiket_kisisel="personal", etiket_is="work",
    baslik_aws="AWS · CLI key",
    baslik_banka="Northwind Bank",
    baslik_deploy="Deploy key (ed25519)",
    baslik_wifi="Home Wi-Fi",
    baslik_google="Google account",
    baslik_kimlik="ID & address",
    baslik_mc="Mastercard · online",
    baslik_env="prod.env · API keys",
    baslik_visa="Visa · everyday",
    baslik_kodlar="Backup codes · Google",
    alan_erisim="Access key ID",
    alan_gizli="Secret access key",
    alan_parmak="fingerprint",
    alan_ssid="Network name (SSID)",
    ssid="HomeNet_5G",
    banka_uygulama="Northwind mobile",
    adres="%1$d Example Street, Springfield",
    bt_cihaz="MacBook Pro",
    yeni_baslik="Server SSH (staging)",
)

DEMO["tr"] = dict(
    adlar=["Deniz Yılmaz", "Ece Demir", "Can Aydın", "Elif Kaya", "Mert Çelik", "Zeynep Şahin"],
    etiket_finans="finans", etiket_kisisel="kişisel", etiket_is="iş",
    baslik_aws="AWS · CLI anahtarı",
    baslik_banka="Northwind Bank",
    baslik_deploy="Deploy anahtarı (ed25519)",
    baslik_wifi="Ev Wi-Fi",
    baslik_google="Google hesabı",
    baslik_kimlik="Kimlik ve adres",
    baslik_mc="Mastercard · online",
    baslik_env="prod.env · API anahtarları",
    baslik_visa="Visa · günlük",
    baslik_kodlar="Yedek kodlar · Google",
    alan_erisim="Erişim anahtarı (Access key ID)",
    alan_gizli="Gizli anahtar (Secret access key)",
    alan_parmak="parmak izi",
    alan_ssid="Ağ adı (SSID)",
    ssid="EvAgi_5G",
    banka_uygulama="Northwind mobil",
    adres="Demo Sok. No: %1$d, Kadıköy / İstanbul",
    bt_cihaz="MacBook Pro",
    yeni_baslik="Sunucu SSH (staging)",
)

SITE = {}
SITE["en"] = dict(secici_etiket="Phone model", olcu="1:1 scale · %1$s × %2$s mm")
SITE["tr"] = dict(secici_etiket="Telefon modeli", olcu="1:1 ölçek · %1$s × %2$s mm")

# Roboto: Android'in sistem yazı tipi — maketteki uygulama onunla çizilir.
FONT_URL = ("https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600"
            "&family=Roboto+Mono:wght@400&display=swap")


def veri(code, yon):
    """Sayfaya <script type="application/json" id="telefon-veri"> olarak gömülür."""
    blob = {
        "lang": code, "dir": yon,
        "app": APP[code],
        "demo": {**DEMO["en"], **DEMO.get(code, {})},
        "site": {**SITE["en"], **SITE.get(code, {})},
        # aktar.html yalnız tr ve en konuşur; maket de aracın gerçek hâlini gösterir.
        "arac": APP["_arac"]["tr" if code == "tr" else "en"],
    }
    return json.dumps(blob, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

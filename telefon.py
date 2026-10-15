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
SITE["en"] = dict(secici_etiket="Phone model", olcu="1:1 scale · %1$s × %2$s mm", kopyalandi='%1$s copied · clipboard clears in 45 s, or when you return to the app', ios_kopyalandi='%1$s copied · this iPhone only, cleared in 45 s')
SITE["tr"] = dict(secici_etiket="Telefon modeli", olcu="1:1 ölçek · %1$s × %2$s mm", kopyalandi='%1$s kopyalandı · pano 45 sn sonra ya da uygulamaya dönünce temizlenir', ios_kopyalandi="%1$s kopyalandı · yalnız bu iPhone'da, 45 sn sonra silinir")
SITE["de"] = dict(secici_etiket="Telefonmodell", olcu="Maßstab 1:1 · %1$s × %2$s mm", kopyalandi='%1$s kopiert · Zwischenablage wird nach 45 s oder bei Rückkehr zur App geleert', ios_kopyalandi='%1$s kopiert · nur auf diesem iPhone, nach 45 s gelöscht')
SITE["es"] = dict(secici_etiket="Modelo de teléfono", olcu="Escala 1:1 · %1$s × %2$s mm", kopyalandi='%1$s copiado · el portapapeles se vacía en 45 s o al volver a la app', ios_kopyalandi='%1$s copiado · solo en este iPhone, se borra en 45 s')
SITE["fr"] = dict(secici_etiket="Modèle de téléphone", olcu="Échelle 1:1 · %1$s × %2$s mm", kopyalandi="%1$s copié · le presse-papiers s'efface après 45 s ou au retour dans l'app", ios_kopyalandi='%1$s copié · sur cet iPhone seulement, effacé après 45 s')
SITE["pt"] = dict(secici_etiket="Modelo do telefone", olcu="Escala 1:1 · %1$s × %2$s mm", kopyalandi='%1$s copiado · a área de transferência limpa em 45 s ou ao voltar ao app', ios_kopyalandi='%1$s copiado · só neste iPhone, apagado em 45 s')
SITE["ru"] = dict(secici_etiket="Модель телефона", olcu="Масштаб 1:1 · %1$s × %2$s мм", kopyalandi='%1$s скопировано · буфер очистится через 45 с или при возврате в приложение', ios_kopyalandi='%1$s скопировано · только на этом iPhone, удалится через 45 с')
SITE["id"] = dict(secici_etiket="Model ponsel", olcu="Skala 1:1 · %1$s × %2$s mm", kopyalandi='%1$s disalin · papan klip dibersihkan dalam 45 dtk atau saat kembali ke aplikasi', ios_kopyalandi='%1$s disalin · hanya di iPhone ini, dihapus dalam 45 dtk')
SITE["vi"] = dict(secici_etiket="Mẫu điện thoại", olcu="Tỉ lệ 1:1 · %1$s × %2$s mm", kopyalandi='Đã sao chép %1$s · bảng tạm xóa sau 45 giây hoặc khi quay lại ứng dụng', ios_kopyalandi='Đã sao chép %1$s · chỉ trên iPhone này, xóa sau 45 giây')
SITE["zh"] = dict(secici_etiket="手机型号", olcu="1:1 比例 · %1$s × %2$s mm", kopyalandi='已复制%1$s · 剪贴板将在 45 秒后或返回应用时清空', ios_kopyalandi='已复制%1$s · 仅限此 iPhone，45 秒后清除')
SITE["ja"] = dict(secici_etiket="機種", olcu="原寸 1:1 · %1$s × %2$s mm", kopyalandi='%1$s をコピー · クリップボードは 45 秒後またはアプリに戻ると消去', ios_kopyalandi='%1$s をコピー · この iPhone 内のみ、45 秒後に消去')
SITE["pcm"] = dict(secici_etiket="Phone model", olcu="1:1 scale · %1$s × %2$s mm", kopyalandi='%1$s don copy · clipboard go clear after 45 s, or when you come back to di app', ios_kopyalandi='%1$s don copy · only for dis iPhone, e go clear after 45 s')
SITE["hi"] = dict(secici_etiket="फ़ोन मॉडल", olcu="1:1 पैमाना · %1$s × %2$s mm", kopyalandi='%1$s कॉपी हुआ · क्लिपबोर्ड 45 सेकंड में या ऐप पर लौटने पर साफ़ होगा', ios_kopyalandi='%1$s कॉपी हुआ · केवल इस iPhone पर, 45 सेकंड में मिट जाएगा')
SITE["bn"] = dict(secici_etiket="ফোনের মডেল", olcu="১:১ মাপ · %1$s × %2$s mm", kopyalandi='%1$s কপি হয়েছে · ক্লিপবোর্ড ৪৫ সেকেন্ডে বা অ্যাপে ফিরলে মুছে যাবে', ios_kopyalandi='%1$s কপি হয়েছে · শুধু এই iPhone-এ, ৪৫ সেকেন্ডে মুছে যাবে')
# Sağdan sola dillerde sayılar ve "mm" FSI…PDI (⁨ ⁩) ile yalıtılır: "149,6 × 71,7"
# sırası ve "1:1" bozulmaz (uygulamanın ar/ur metinlerindeki kuralın aynısı).
SITE["ar"] = dict(secici_etiket="طراز الهاتف", olcu="مقياس ⁨‎1:1⁩ · ⁨%1$s × %2$s mm⁩", kopyalandi='تم نسخ %1$s · تُمسح الحافظة بعد \u200e45\u200e ث أو عند العودة إلى التطبيق', ios_kopyalandi='تم نسخ %1$s · على هذا الـ iPhone فقط، يُمسح بعد \u200e45\u200e ث')
SITE["ur"] = dict(secici_etiket="فون کا ماڈل", olcu="پیمانہ ⁨‎1:1⁩ · ⁨%1$s × %2$s mm⁩", kopyalandi='%1$s کاپی ہو گیا · کلپ بورڈ \u200e45\u200e سیکنڈ میں یا ایپ پر واپسی پر صاف ہو جائے گا', ios_kopyalandi='%1$s کاپی ہو گیا · صرف اس iPhone پر، \u200e45\u200e سیکنڈ میں مٹ جائے گا')

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

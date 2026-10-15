"""Aktarım: anasayfa kartı ve /transfer/ sayfasının metinleri.

TASLAK (2026-10-14): metinler kullanıcıyla birlikte gözden geçirilecek;
şimdilik yalnız en ve tr var, diğer diller İngilizceye düşer. Bu yüzden
16 dil çevrilmeden yayına çıkmaz.

aktar.html'in sürümü, boyutu ve SHA-256'sı TEK yerde: aşağıdaki sabitler.
build.py, uygulama deposu yanındaysa (../vault/tools/aktar.html) özeti
oradaki dosyayla karşılaştırır ve tutmazsa uyarır; SEKUVO_YAYIN=1 ile durur —
sitede yazan değerle indirilen dosyanın ayrışması, tam da doğrulamanın
yakalaması gereken şeydir.
"""
from kaynak import GITHUB

AKTAR_SURUM = "v1.0.0"
AKTAR_SHA256 = "85ee1729fda96072b36303074f21a170d5361c0577a920ef631bd6884d5b653d"
AKTAR_BOYUT = 53833  # bayt
AKTAR_INDIR = f"{GITHUB}/releases/download/{AKTAR_SURUM}/aktar.html"
AKTAR_SURUM_SAYFASI = f"{GITHUB}/releases/tag/{AKTAR_SURUM}"

T = {}

T["en"] = dict(
    # anasayfa: kahraman telefonu
    tel_alt="Sekuvo on a phone: the entry list, an entry's details and typing a password to a computer over Bluetooth. Every value shown is generated randomly in this page.",
    tel_not="Every password, key and card number on this screen is generated at random in this page — none of it is real, and none of it leaves your browser.",
    # anasayfa: aktarım kartı
    nav="Transfer",
    eyebrow="From computer to phone",
    h2="Long secrets aren't typed by hand.<br>Move them by QR.",
    kicker="SSH keys, .env files, recovery codes… aktar.html encrypts the secret on your computer and Sekuvo reads it with the camera. No server, no account, no clipboard in between — only light travelling from a screen to a lens.",
    steps=[
        ("Download and verify",
         "aktar.html is a single HTML file. Download it, compare its SHA-256 with the value below, and open it from your own disk."),
        ("Encrypt on the computer",
         "Paste the secret and choose a transfer password. Encryption runs inside the browser, on your machine; the envelope is drawn on screen as QR codes."),
        ("Scan with the phone",
         "In Sekuvo: ➕ → Import via QR. Scan the frames, enter the same password, and the entry lands in your vault."),
    ],
    dl_btn="Download aktar.html",
    dl_meta="{surum} · {boyut} · one file, runs from your own disk",
    sha_label="SHA-256",
    verify_sum="How do I verify it?",
    verify_p="Run the command for your system in a terminal; the output must match the value above exactly. The same value is published in the GitHub release notes. You can also keep it in Sekuvo as a Tool anchor (the fingerprint button on the home screen) and compare against your phone the next time you download.",
    dl_note="A download, not a web page: the address bar shows file://. sekuvo.com never asks you for a secret.",
    arac_dili="aktar.html currently speaks English and Turkish.",
    more="Every way to transfer, in detail",
    sahne_alt="aktar.html on a laptop shows the encrypted envelope as cycling QR frames; Sekuvo on the phone scans them, asks for the transfer password and adds the entry.",
    kb="KB",
    # /transfer/ sayfası
    p_title="Computer to phone transfer — Sekuvo",
    p_desc="How to move SSH keys, .env files and recovery codes from a computer into Sekuvo without a network: aktar.html and QR, the encrypted envelope, import from text.",
    p_eyebrow="Transfer",
    p_h1="From computer to phone,<br>with no network <em>in between.</em>",
    p_lede="Sekuvo has no internet permission, so a secret reaches your phone only along a path you show it. This page walks through those paths: the easiest is aktar.html and QR, the most cautious is an envelope you build in your own terminal.",
    why_eyebrow="Why QR",
    why_h2="Three doors stay shut.",
    why=[
        ("Typing by hand breaks things",
         "One wrong character in a 64-character API key and the key is dead. Typing a long private key into a phone is, in practice, impossible."),
        ("The clipboard leaks",
         "Whatever you copy can be read by the app that is open at that moment, and cloud clipboards carry it to other devices. That is why Sekuvo never uses it as a path."),
        ("There is no network",
         "The app has no INTERNET permission, so file sync, e-mail or a server are not options. Light travelling from a screen to a camera crosses no network at all."),
    ],
    how_eyebrow="Step by step",
    how_h2="With aktar.html",
    how=[
        ("Download", "Get aktar.html with the button above or from the release page. It is one file; nothing to install."),
        ("Verify", "Compute its SHA-256 and compare it with the published value. If they differ, do not open the file."),
        ("Open", "Double-click it. The address bar shows file://, not a website, and the page never connects to the internet."),
        ("Fill in and encrypt", "Write a title, pick a type (Account, Everyday, Card or Secure note), paste the secret or pick a .pem / .env file. Choose a backup password and press Encrypt and show the QR."),
        ("Scan on the phone", "Sekuvo → ➕ → Import via QR. Large envelopes are split into several frames that cycle on screen; the phone collects them in any order. Enter the same password and the entry is added."),
    ],
    wiz_eyebrow="Don't even type the password",
    wiz_h2="The transfer wizard",
    wiz_p="The ⇄ button on the home screen opens the transfer wizard. The phone generates a single-use password of letters and digits — immune to keyboard-layout differences — and, acting as a Bluetooth keyboard, types it into both password fields of aktar.html at once. Press Encrypt and show the QR on the computer and Scan QR in the wizard: the password is already on the phone, so you never type it.",
    other_eyebrow="Other paths",
    other_h2="When you'd rather not use aktar.html",
    other=[
        ("Envelope → QR page",
         "Don't want the browser to encrypt anything? Build the envelope in your own terminal with a thirty-line script; this page only turns ciphertext into QR frames.",
         "aktar"),
        ("Import from text",
         "Any way you can carry the envelope as text works: ➕ → Import from text, paste, enter the password.",
         ""),
        ("Command line: vault-clip.py",
         "Does the same from the clipboard or a file, and draws the QR right in the terminal.",
         "clip"),
        ("Build your own envelope",
         "The envelope is an open format, not something only Sekuvo can make. The recipe is in the repository.",
         "zarf"),
    ],
    other_link_aktar="Open the Envelope → QR page",
    other_link_clip="See the code on GitHub",
    other_link_zarf="Read the recipe",
    env_eyebrow="What the QR carries",
    env_h2="An envelope, never the secret.",
    env_p="Whoever photographs the QR gets only this. The transfer password becomes a key through 310,000 rounds of PBKDF2, which makes every guess slow; without the password the data field is noise.",
    faq_eyebrow="Questions",
    faq_h2="Frequently asked",
    faq=[
        ("Does my secret go to the internet?",
         "No. aktar.html encrypts with the browser's WebCrypto on your machine and draws the QR on your screen. Sekuvo has no internet permission; the camera image is decoded inside the app."),
        ("Why a downloaded file instead of a web page?",
         "A web page that asks for secrets looks exactly like a phishing page. And a page on a server can change on every visit; the digest of a file you downloaded is fixed and checkable."),
        ("What about large files?",
         "The entry limit is 256 KB. Large envelopes are split into several QR frames that cycle; the phone collects them in any order and shows which frames are still missing."),
        ("Which languages does aktar.html speak?",
         "English and Turkish for now."),
        ("And from phone to computer?",
         "The other direction is Bluetooth: your phone types into the computer like a keyboard, with nothing installed on the computer."),
    ],
    back="← Back to sekuvo.com",
)

T["tr"] = dict(
    tel_alt="Sekuvo bir telefonda: kayıt listesi, kayıt ayrıntısı ve bir şifrenin Bluetooth ile bilgisayara yazılması. Gösterilen bütün değerler bu sayfada rastgele üretilir.",
    tel_not="Bu ekrandaki her parola, anahtar ve kart numarası bu sayfada rastgele üretilir — hiçbiri gerçek değil ve hiçbiri tarayıcından çıkmaz.",
    nav="Aktarım",
    eyebrow="Bilgisayardan telefona",
    h2="Uzun sırlar elle yazılmaz.<br>QR ile aktar.",
    kicker="SSH anahtarı, .env dosyası, kurtarma kodları… Bilgisayarındaki sırrı aktar.html şifreler, Sekuvo kamerayla okur. Arada sunucu, hesap ya da pano yok; yalnız ekrandan kameraya giden ışık var.",
    steps=[
        ("İndir ve doğrula",
         "aktar.html tek bir HTML dosyasıdır. İndir, SHA-256 özetini aşağıdaki değerle karşılaştır ve kendi diskinden aç."),
        ("Bilgisayarda şifrele",
         "Sırrını yapıştır, bir aktarım parolası belirle. Şifreleme tarayıcının içinde, senin makinende yapılır; zarf ekrana QR olarak çizilir."),
        ("Telefonla oku",
         "Sekuvo'da ➕ → QR ile içe aktar. Kareleri okut, aynı parolayı gir; kayıt kasana eklenir."),
    ],
    dl_btn="aktar.html'i indir",
    dl_meta="{surum} · {boyut} · tek dosya, kendi diskinden çalışır",
    sha_label="SHA-256",
    verify_sum="Nasıl doğrularım?",
    verify_p="Sistemine uygun komutu terminalde çalıştır; çıkan değer yukarıdakiyle birebir aynı olmalı. Aynı değer GitHub sürüm notunda da yayımlanır. İstersen Sekuvo'da Araç çıpası olarak sakla (ana ekrandaki parmak izi düğmesi); bir sonraki indirmede telefonundaki değerle karşılaştırırsın.",
    dl_note="Bu bir web sayfası değil, indirilen bir dosya: adres çubuğunda file:// görünür. sekuvo.com senden asla bir sır istemez.",
    arac_dili="aktar.html şimdilik Türkçe ve İngilizce.",
    more="Aktarımın bütün yolları ve ayrıntılar",
    sahne_alt="Dizüstü bilgisayarda aktar.html şifreli zarfı dönen QR kareleri olarak gösteriyor; telefondaki Sekuvo kareleri okuyor, aktarım parolasını istiyor ve kaydı ekliyor.",
    kb="KB",
    p_title="Bilgisayardan telefona aktarım — Sekuvo",
    p_desc="SSH anahtarlarını, .env dosyalarını ve kurtarma kodlarını bilgisayardan Sekuvo'ya ağsız aktarmanın yolları: aktar.html ve QR, şifreli zarf, metinden içe aktarma.",
    p_eyebrow="Aktarım",
    p_h1="Bilgisayardan telefona,<br>arada <em>ağ olmadan.</em>",
    p_lede="Sekuvo'nun internet izni yok; telefonuna bir sır ancak senin gösterdiğin yoldan girer. Bu sayfa o yolları anlatıyor: en kolayı aktar.html ve QR, en temkinlisi kendi terminalinde kurduğun zarf.",
    why_eyebrow="Neden QR",
    why_h2="Üç kapı kapalı kalır.",
    why=[
        ("Elle yazmak bozar",
         "64 karakterlik bir API anahtarında tek bir yanlış harf, anahtarı geçersiz kılar. Uzun bir özel anahtarı telefona elle yazmak pratikte imkânsızdır."),
        ("Pano sızdırır",
         "Kopyaladığın değeri o an açık olan uygulama okuyabilir; bulut panoları onu başka cihazlara taşır. Sekuvo bu yüzden panoyu yol olarak kullanmaz."),
        ("Ağ yok",
         "Uygulamanın INTERNET izni yok; dosya eşitleme, e-posta ya da sunucu bu yüzden seçenek değil. Ekrandan kameraya giden ışık ise hiçbir ağdan geçmez."),
    ],
    how_eyebrow="Adım adım",
    how_h2="aktar.html ile",
    how=[
        ("İndir", "aktar.html'i yukarıdaki düğmeden ya da sürüm sayfasından al. Tek bir dosyadır; kurulacak bir şey yok."),
        ("Doğrula", "SHA-256 özetini hesapla ve yayımlanan değerle karşılaştır. Tutmuyorsa dosyayı açma."),
        ("Aç", "Çift tıkla. Adres çubuğunda bir site değil file:// görünür; sayfa internete hiç bağlanmaz."),
        ("Doldur ve şifrele", "Başlığı yaz, türü seç (Hesap, Gündelik, Kart ya da Güvenli Not), sırrı yapıştır ya da bir .pem / .env dosyası seç. Bir yedek parolası belirle ve Şifrele ve QR göster'e bas."),
        ("Telefonda oku", "Sekuvo → ➕ → QR ile içe aktar. Büyük zarflar ekranda dönen birkaç kareye bölünür; telefon onları sırasız toplar. Aynı parolayı gir, kayıt eklenir."),
    ],
    wiz_eyebrow="Parolayı bile yazma",
    wiz_h2="Aktarım sihirbazı",
    wiz_p="Ana ekrandaki ⇄ düğmesi aktarım sihirbazını açar. Telefon harf ve rakamdan oluşan, tek aktarımlık bir parola üretir — klavye düzeni farkından etkilenmez — ve Bluetooth klavye olarak onu aktar.html'deki iki parola alanına birden yazar. Bilgisayarda Şifrele ve QR göster'e, sihirbazda QR okut'a bas: parola zaten telefonda olduğu için hiçbir şey yazmazsın.",
    other_eyebrow="Diğer yollar",
    other_h2="aktar.html'i kullanmak istemezsen",
    other=[
        ("Zarf → QR sayfası",
         "Şifrelemeyi tarayıcıya bile bırakmak istemiyor musun? Zarfı kendi terminalinde otuz satırlık bir betikle kur; bu sayfa yalnız şifreli metni QR karelerine çevirir.",
         "aktar"),
        ("Metinden içe aktar",
         "Zarfı metin olarak taşıyabildiğin her yol çalışır: ➕ → Metinden içe aktar, yapıştır, parolayı gir.",
         ""),
        ("Komut satırı: vault-clip.py",
         "Aynı işi panodan ya da bir dosyadan yapar, QR'ı doğrudan terminale çizer.",
         "clip"),
        ("Kendi zarfını üret",
         "Zarf yalnız Sekuvo'nun üretebildiği bir şey değil, açık bir biçimdir. Tarifi depoda.",
         "zarf"),
    ],
    other_link_aktar="Zarf → QR sayfasını aç",
    other_link_clip="Kodu GitHub'da gör",
    other_link_zarf="Tarifi oku",
    env_eyebrow="QR ne taşır",
    env_h2="Bir zarf; sırrın kendisi asla.",
    env_p="QR'ın fotoğrafını çeken yalnız bunu görür. Aktarım parolası 310.000 turluk PBKDF2 ile anahtara dönüşür, bu da her tahmini yavaşlatır; parola olmadan veri alanı yalnız gürültüdür.",
    faq_eyebrow="Sorular",
    faq_h2="Sık sorulanlar",
    faq=[
        ("Sırrım internete gidiyor mu?",
         "Hayır. aktar.html şifrelemeyi tarayıcının WebCrypto'suyla, kendi makinende yapar ve QR'ı ekranına çizer. Sekuvo'nun internet izni yoktur; kamera görüntüsü uygulamanın içinde çözülür."),
        ("Neden web sayfası değil de indirilen bir dosya?",
         "Sır isteyen bir web sayfası tam da bir kimlik avı sayfası gibi görünür. Ayrıca sunucudaki bir sayfa her açılışta değişebilir; indirdiğin dosyanın özeti ise sabittir ve doğrulanabilir."),
        ("Büyük dosyalar ne olacak?",
         "Kayıt sınırı 256 KB. Büyük zarflar birden çok QR karesine bölünür; kareler döner, telefon onları sırasız toplar ve eksik kareleri gösterir."),
        ("aktar.html hangi dillerde?",
         "Şimdilik Türkçe ve İngilizce."),
        ("Telefondan bilgisayara?",
         "Ters yön Bluetooth'tur: telefonun bilgisayara klavye gibi yazar, bilgisayara hiçbir şey kurulmaz."),
    ],
    back="← sekuvo.com'a dön",
)


def t(code):
    """Çevirisi olmayan dil İngilizceye düşer (TASLAK — yayından önce 16 dil)."""
    return {**T["en"], **T.get(code, {})}


def boyut_metni(code):
    kb = round(AKTAR_BOYUT / 1024)
    return f"{kb} {t(code)['kb']}"


ZARF_ORNEK = """{
  "app": "vault",
  "version": 1,
  "kdf": {
    "algo": "PBKDF2WithHmacSHA256",
    "iterations": 310000,
    "salt": "…16 bytes, base64…"
  },
  "cipher": "AES-256-GCM",
  "data": "…12-byte IV + ciphertext + 16-byte tag, base64…"
}"""

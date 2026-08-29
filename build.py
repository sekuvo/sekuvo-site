#!/usr/bin/env python3
"""Builds sekuvo.com from one source of truth.

Every language page comes from the same template, so a copy change lands in
all five at once instead of drifting between hand-edited files. Run:

    python3 build.py

Output: index.html (en) and tr/, es/, hi/, ar/ index files.
"""
import pathlib

from guide import G, SHOTS, CAPTIONS

SITE = "https://sekuvo.com"
GITHUB = "https://github.com/afgover/Vault"

# Scripts that Bricolage Grotesque does not cover get an IBM Plex face that
# does; the mono face stays the same everywhere because it only ever renders
# code, which is Latin in every language.
FONTS = {
    "latin": ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..800"
              "&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap",
              '"Bricolage Grotesque", Georgia, serif', '"IBM Plex Sans", "Segoe UI", system-ui, sans-serif'),
    "devanagari": ("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Devanagari:wght@400;500;600;700"
                   "&family=IBM+Plex+Mono:wght@400;500&display=swap",
                   '"IBM Plex Sans Devanagari", system-ui, sans-serif',
                   '"IBM Plex Sans Devanagari", system-ui, sans-serif'),
    "arabic": ("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700"
               "&family=IBM+Plex+Mono:wght@400;500&display=swap",
               '"IBM Plex Sans Arabic", system-ui, sans-serif',
               '"IBM Plex Sans Arabic", system-ui, sans-serif'),
    "cjk-sc": ("https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700"
               "&family=IBM+Plex+Mono:wght@400;500&display=swap",
               '"Noto Sans SC", system-ui, sans-serif',
               '"Noto Sans SC", system-ui, sans-serif'),
    "bengali": ("https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;500;600;700"
                "&family=IBM+Plex+Mono:wght@400;500&display=swap",
                '"Noto Sans Bengali", system-ui, sans-serif',
                '"Noto Sans Bengali", system-ui, sans-serif'),
    # IBM Plex Sans ships a Cyrillic subset, so no separate script family is
    # needed here — unlike Bricolage Grotesque, which is Latin-only.
    "cyrillic": ("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700"
                 "&family=IBM+Plex+Mono:wght@400;500&display=swap",
                 '"IBM Plex Sans", system-ui, sans-serif',
                 '"IBM Plex Sans", system-ui, sans-serif'),
}

CHAIN_LATIN = ('Master password ─<b>PBKDF2 · 310,000 rounds</b>─▶ KEK ─<b>AES-GCM wrap</b>─▶ '
               'dataKey ─▶ <b>AES-256-GCM</b> on every entry')

L = {}

L["en"] = dict(
    lang="en", dir="ltr", script="latin", path="", name="English",
    title="Sekuvo — Your Secure Vault",
    desc="Sekuvo — your secure vault. A fully offline password vault for Android: no internet permission, AES-256, open source (GPLv3).",
    nav=("Security", "Channels", "Download", "Privacy"),
    eyebrow="Offline password vault for Android",
    h1="Your secrets<br>never <em>leave.</em>",
    lede="Sekuvo is your secure vault: passwords, cards and notes, encrypted on your phone with a key only your master password can derive. It has no server, no account, no sync — and no way to phone home.",
    btn_src="Source on GitHub", btn_priv="Privacy policy",
    cta_note="Google Play listing is in preparation. Sekuvo is free and GPLv3 — the code is the proof.",
    proof_cap="AndroidManifest.xml — every permission it has",
    proof_alt="The app manifest requests camera, biometrics and Bluetooth, and a search for the INTERNET permission returns no matches.",
    proof_no="(no matches — the permission does not exist)",
    sec_eyebrow="Security model",
    sec_h2="Encryption you can audit, not believe.",
    sec_kicker="Every sensitive field is sealed with AES-256-GCM. The key never touches a server because there is no server; it is derived on your phone, from your master password, every time you unlock.",
    chain=CHAIN_LATIN,
    cells=[("Locks when the screen sleeps",
            "The key is wiped from memory the moment the screen goes dark — folding a foldable counts. One unlock serves the app, the keyboard and autofill together."),
           ("Backups that outlive the phone",
            "One encrypted <span class=\"mono-note\">.vaultbak</span> file, stored wherever you choose. File + backup password restores everything on any device — the recovery path is tested end to end."),
           ("No recovery backdoor",
            "Forget the master password and the data is gone. That is the design: a door only you can open has no spare key under the mat.")],
    ch_eyebrow="Clipboard-free by design",
    ch_h2="Three ways out, all under your finger.",
    ch_kicker="The clipboard is where secrets go to be stolen. Sekuvo types values straight to their destination instead.",
    lanes=[("Autofill", "Android autofill service",
            "Sign-in and card forms offer your entries directly. While locked, the system gets nothing — unlock first, then choose."),
           ("Keyboard", "Sekuvo Keyboard",
            "Switch to it in any app and type a stored secret into the field — searchable, recents on top, no copy step."),
           ("Bluetooth", "Types into your computer",
            "Your phone becomes a Bluetooth keyboard and types the secret at the computer's cursor. Nothing is installed on the computer.")],
    dl_eyebrow="Get Sekuvo", dl_h2="Free, open source, GPLv3.",
    dl_app_h="Android app",
    dl_app_p="The Google Play listing is in preparation. Until then you can build from source — the repository README covers it in two commands.",
    dl_tools_h="Computer-side tools",
    dl_tools_p="The computer-side tool is a single HTML file — <code>aktar.html</code> — and it is a download, not a web page: it runs entirely on your machine, and this site never asks you for a secret.",
    dl_tools_note="github.com → Releases · verify the published SHA-256",
    dl_app_link="Read the guide →",
    dl_tools_link="How to get aktar.html and use it →",
    contact="Contact",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>your secure vault.</em>",
)

L["tr"] = dict(
    lang="tr", dir="ltr", script="latin", path="tr/", name="Türkçe",
    title="Sekuvo — Güvenli Kasan",
    desc="Sekuvo — güvenli kasan. Android için tamamen çevrimdışı parola kasası: internet izni yok, AES-256, açık kaynak (GPLv3).",
    nav=("Güvenlik", "Kanallar", "İndir", "Gizlilik"),
    eyebrow="Android için çevrimdışı parola kasası",
    h1="Sırların<br>asla <em>çıkmaz.</em>",
    lede="Sekuvo senin güvenli kasan: parolalar, kartlar ve notlar, yalnız ana parolandan türeyen bir anahtarla telefonunda şifrelenir. Sunucusu yok, hesabı yok, eşitlemesi yok — ve eve haber verme yolu yok.",
    btn_src="GitHub'da kaynak kodu", btn_priv="Gizlilik politikası",
    cta_note="Google Play kaydı hazırlanıyor. Sekuvo ücretsiz ve GPLv3 — kanıt kodun kendisi.",
    proof_cap="AndroidManifest.xml — sahip olduğu bütün izinler",
    proof_alt="Uygulama manifesti kamera, biyometri ve Bluetooth istiyor; INTERNET izni araması hiçbir sonuç vermiyor.",
    proof_no="(eşleşme yok — böyle bir izin hiç yok)",
    sec_eyebrow="Güvenlik modeli",
    sec_h2="İnanılacak değil, denetlenecek şifreleme.",
    sec_kicker="Her hassas alan AES-256-GCM ile mühürlenir. Anahtar hiçbir sunucuya uğramaz, çünkü sunucu yoktur; her kilit açışında telefonunda, ana parolandan türetilir.",
    chain=('Ana parola ─<b>PBKDF2 · 310.000 tur</b>─▶ KEK ─<b>AES-GCM sarma</b>─▶ '
           'dataKey ─▶ her kayıtta <b>AES-256-GCM</b>'),
    cells=[("Ekran uyuyunca kilitlenir",
            "Ekran karardığı anda anahtar bellekten silinir — katlanabilir cihazı katlamak da sayılır. Tek kilit açma; uygulama, klavye ve otomatik doldurma için birlikte geçerlidir."),
           ("Telefondan uzun ömürlü yedek",
            "İstediğin yere koyduğun tek bir şifreli <span class=\"mono-note\">.vaultbak</span> dosyası. Dosya artı yedek parolası her cihazda her şeyi geri getirir — kurtarma yolu uçtan uca sınandı."),
           ("Kurtarma arka kapısı yok",
            "Ana parolanı unutursan veri gider. Tasarım bu: yalnız senin açabildiğin bir kapının paspas altında yedek anahtarı olmaz.")],
    ch_eyebrow="Tasarımı gereği panosuz",
    ch_h2="Üç çıkış yolu, üçü de parmağının altında.",
    ch_kicker="Pano, sırların çalınmaya gittiği yerdir. Sekuvo değerleri onun yerine doğrudan hedefine yazar.",
    lanes=[("Otomatik doldurma", "Android otomatik doldurma servisi",
            "Giriş ve kart formları kayıtlarını doğrudan sunar. Kilitliyken sisteme hiçbir şey gitmez — önce kilidi aç, sonra seç."),
           ("Klavye", "Sekuvo Klavyesi",
            "Herhangi bir uygulamada klavyeye geç, kayıtlı sırrı doğrudan alana yaz — aranabilir, son kullanılanlar üstte, kopyalama adımı yok."),
           ("Bluetooth", "Bilgisayarına yazar",
            "Telefonun Bluetooth klavyeye dönüşür ve sırrı bilgisayardaki imlecin olduğu yere yazar. Bilgisayara hiçbir şey kurulmaz.")],
    dl_eyebrow="Sekuvo'yu edin", dl_h2="Ücretsiz, açık kaynak, GPLv3.",
    dl_app_h="Android uygulaması",
    dl_app_p="Google Play kaydı hazırlanıyor. O zamana kadar kaynaktan derleyebilirsin — depodaki README iki komutla anlatıyor.",
    dl_tools_h="Bilgisayar tarafı araçlar",
    dl_tools_p="Bilgisayar tarafındaki araç tek bir HTML dosyasıdır — <code>aktar.html</code> — ve web sayfası değil, indirilen bir dosyadır: tamamen kendi makinende çalışır ve bu site senden asla bir sır istemez.",
    dl_tools_note="github.com → Releases · yayınlanan SHA-256'yı doğrula",
    dl_app_link="Kılavuzu oku →",
    dl_tools_link="aktar.html'i nasıl alır, nasıl kullanırsın →",
    contact="İletişim",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>güvenli kasan.</em>",
)

L["es"] = dict(
    lang="es", dir="ltr", script="latin", path="es/", name="Español",
    title="Sekuvo — Tu bóveda segura",
    desc="Sekuvo — tu bóveda segura. Una bóveda de contraseñas totalmente sin conexión para Android: sin permiso de internet, AES-256, código abierto (GPLv3).",
    nav=("Seguridad", "Canales", "Descargar", "Privacidad"),
    eyebrow="Bóveda de contraseñas sin conexión para Android",
    h1="Tus secretos<br>nunca <em>salen.</em>",
    lede="Sekuvo es tu bóveda segura: contraseñas, tarjetas y notas, cifradas en tu teléfono con una clave que solo tu contraseña maestra puede derivar. Sin servidor, sin cuenta, sin sincronización — y sin forma de llamar a casa.",
    btn_src="Código en GitHub", btn_priv="Política de privacidad",
    cta_note="La ficha de Google Play está en preparación. Sekuvo es gratis y GPLv3 — el código es la prueba.",
    proof_cap="AndroidManifest.xml — todos los permisos que tiene",
    proof_alt="El manifiesto pide cámara, biometría y Bluetooth, y la búsqueda del permiso INTERNET no devuelve coincidencias.",
    proof_no="(sin coincidencias — ese permiso no existe)",
    sec_eyebrow="Modelo de seguridad",
    sec_h2="Cifrado que puedes auditar, no creer.",
    sec_kicker="Cada campo sensible se sella con AES-256-GCM. La clave nunca toca un servidor porque no hay servidor; se deriva en tu teléfono, desde tu contraseña maestra, cada vez que desbloqueas.",
    chain=('Contraseña maestra ─<b>PBKDF2 · 310.000 rondas</b>─▶ KEK ─<b>envoltura AES-GCM</b>─▶ '
           'dataKey ─▶ <b>AES-256-GCM</b> en cada entrada'),
    cells=[("Se bloquea cuando la pantalla se apaga",
            "La clave se borra de la memoria en cuanto la pantalla se apaga — plegar un plegable también cuenta. Un solo desbloqueo sirve para la app, el teclado y el autocompletado."),
           ("Copias que sobreviven al teléfono",
            "Un único archivo cifrado <span class=\"mono-note\">.vaultbak</span> guardado donde tú elijas. El archivo más su contraseña restauran todo en cualquier dispositivo — la vía de recuperación está probada de extremo a extremo."),
           ("Sin puerta trasera de recuperación",
            "Si olvidas la contraseña maestra, los datos se pierden. Es el diseño: una puerta que solo tú abres no guarda una llave bajo el felpudo.")],
    ch_eyebrow="Sin portapapeles por diseño",
    ch_h2="Tres salidas, todas bajo tu dedo.",
    ch_kicker="El portapapeles es donde los secretos acaban robados. Sekuvo escribe los valores directamente en su destino.",
    lanes=[("Autocompletado", "Servicio de autocompletado de Android",
            "Los formularios de inicio de sesión y de tarjeta ofrecen tus entradas directamente. Bloqueado, el sistema no recibe nada — desbloquea primero, luego elige."),
           ("Teclado", "Teclado Sekuvo",
            "Cámbialo en cualquier app y escribe un secreto guardado en el campo — con búsqueda, los recientes arriba y sin paso de copiado."),
           ("Bluetooth", "Escribe en tu ordenador",
            "Tu teléfono se convierte en un teclado Bluetooth y escribe el secreto donde está el cursor. En el ordenador no se instala nada.")],
    dl_eyebrow="Consigue Sekuvo", dl_h2="Gratis, código abierto, GPLv3.",
    dl_app_h="Aplicación Android",
    dl_app_p="La ficha de Google Play está en preparación. Hasta entonces puedes compilar desde el código — el README del repositorio lo explica en dos comandos.",
    dl_tools_h="Herramientas de escritorio",
    dl_tools_p="La herramienta de escritorio es un único archivo HTML — <code>aktar.html</code> — y es una descarga, no una página web: funciona por completo en tu máquina, y este sitio nunca te pide un secreto.",
    dl_tools_note="github.com → Releases · verifica el SHA-256 publicado",
    dl_app_link="Lee la guía →",
    dl_tools_link="Cómo conseguir aktar.html y usarlo →",
    contact="Contacto",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>tu bóveda segura.</em>",
)

L["hi"] = dict(
    lang="hi", dir="ltr", script="devanagari", path="hi/", name="हिन्दी",
    title="Sekuvo — आपकी सुरक्षित तिजोरी",
    desc="Sekuvo — आपकी सुरक्षित तिजोरी। Android के लिए पूरी तरह ऑफ़लाइन पासवर्ड तिजोरी: इंटरनेट अनुमति नहीं, AES-256, ओपन सोर्स (GPLv3)।",
    nav=("सुरक्षा", "रास्ते", "डाउनलोड", "निजता"),
    eyebrow="Android के लिए ऑफ़लाइन पासवर्ड तिजोरी",
    h1="आपके राज़<br>कभी <em>बाहर नहीं जाते।</em>",
    lede="Sekuvo आपकी सुरक्षित तिजोरी है: पासवर्ड, कार्ड और नोट्स — आपके फ़ोन पर उस कुंजी से एन्क्रिप्टेड जो सिर्फ़ आपका मास्टर पासवर्ड बना सकता है। कोई सर्वर नहीं, कोई खाता नहीं, कोई सिंक नहीं — और कहीं ख़बर भेजने का कोई रास्ता नहीं।",
    btn_src="GitHub पर सोर्स", btn_priv="निजता नीति",
    cta_note="Google Play लिस्टिंग तैयार की जा रही है। Sekuvo मुफ़्त और GPLv3 है — कोड ही प्रमाण है।",
    proof_cap="AndroidManifest.xml — इसकी सारी अनुमतियाँ",
    proof_alt="मैनिफ़ेस्ट कैमरा, बायोमेट्रिक्स और ब्लूटूथ माँगता है, और INTERNET अनुमति की खोज पर कोई मिलान नहीं मिलता।",
    proof_no="(कोई मिलान नहीं — यह अनुमति मौजूद ही नहीं है)",
    sec_eyebrow="सुरक्षा मॉडल",
    sec_h2="ऐसा एन्क्रिप्शन जिसे मानना नहीं, जाँचना है।",
    sec_kicker="हर संवेदनशील फ़ील्ड AES-256-GCM से सील होता है। कुंजी किसी सर्वर तक नहीं पहुँचती, क्योंकि सर्वर है ही नहीं; वह हर बार अनलॉक पर आपके फ़ोन में आपके मास्टर पासवर्ड से बनती है।",
    chain=('मास्टर पासवर्ड ─<b>PBKDF2 · 310,000 राउंड</b>─▶ KEK ─<b>AES-GCM रैप</b>─▶ '
           'dataKey ─▶ हर एंट्री पर <b>AES-256-GCM</b>'),
    cells=[("स्क्रीन बुझते ही लॉक",
            "स्क्रीन बंद होते ही कुंजी मेमोरी से मिट जाती है — फ़ोल्डेबल को मोड़ना भी गिना जाता है। एक बार अनलॉक ऐप, कीबोर्ड और ऑटोफ़िल तीनों के लिए काम करता है।"),
           ("फ़ोन से ज़्यादा टिकने वाला बैकअप",
            "एक एन्क्रिप्टेड <span class=\"mono-note\">.vaultbak</span> फ़ाइल, जहाँ चाहें रखें। फ़ाइल और बैकअप पासवर्ड मिलकर किसी भी डिवाइस पर सब कुछ लौटा देते हैं — यह रास्ता पूरी तरह जाँचा जा चुका है।"),
           ("कोई रिकवरी बैकडोर नहीं",
            "मास्टर पासवर्ड भूले तो डेटा गया। यही डिज़ाइन है: जिस दरवाज़े को सिर्फ़ आप खोलते हैं, उसकी दूसरी चाबी चौखट के नीचे नहीं रखी होती।")],
    ch_eyebrow="डिज़ाइन से ही क्लिपबोर्ड-मुक्त",
    ch_h2="बाहर निकलने के तीन रास्ते, तीनों उँगली के नीचे।",
    ch_kicker="क्लिपबोर्ड वही जगह है जहाँ राज़ चोरी होते हैं। Sekuvo मान सीधे उनकी मंज़िल पर लिखता है।",
    lanes=[("ऑटोफ़िल", "Android ऑटोफ़िल सेवा",
            "साइन-इन और कार्ड फ़ॉर्म सीधे आपकी एंट्री दिखाते हैं। लॉक रहते सिस्टम को कुछ नहीं मिलता — पहले अनलॉक, फिर चुनाव।"),
           ("कीबोर्ड", "Sekuvo कीबोर्ड",
            "किसी भी ऐप में इस पर स्विच करें और सहेजा हुआ राज़ सीधे फ़ील्ड में लिखें — खोज के साथ, हाल के ऊपर, कॉपी का कदम नहीं।"),
           ("ब्लूटूथ", "आपके कंप्यूटर में टाइप करता है",
            "आपका फ़ोन ब्लूटूथ कीबोर्ड बन जाता है और राज़ को कर्सर की जगह पर टाइप करता है। कंप्यूटर पर कुछ भी इंस्टॉल नहीं होता।")],
    dl_eyebrow="Sekuvo पाएँ", dl_h2="मुफ़्त, ओपन सोर्स, GPLv3।",
    dl_app_h="Android ऐप",
    dl_app_p="Google Play लिस्टिंग तैयार की जा रही है। तब तक आप सोर्स से बना सकते हैं — रिपॉज़िटरी का README दो कमांड में बताता है।",
    dl_tools_h="कंप्यूटर-साइड टूल",
    dl_tools_p="कंप्यूटर-साइड टूल एक ही HTML फ़ाइल है — <code>aktar.html</code> — और यह वेब पेज नहीं, डाउनलोड है: यह पूरी तरह आपकी मशीन पर चलता है, और यह साइट कभी कोई राज़ नहीं माँगती।",
    dl_tools_note="github.com → Releases · प्रकाशित SHA-256 जाँचें",
    dl_app_link="गाइड पढ़ें →",
    dl_tools_link="aktar.html कैसे लें और कैसे इस्तेमाल करें →",
    contact="संपर्क",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>आपकी सुरक्षित तिजोरी।</em>",
)

L["ar"] = dict(
    lang="ar", dir="rtl", script="arabic", path="ar/", name="العربية",
    title="Sekuvo — خزنتك الآمنة",
    desc="Sekuvo — خزنتك الآمنة. خزنة كلمات مرور تعمل دون اتصال بالكامل على أندرويد: بلا إذن إنترنت، AES-256، مفتوحة المصدر (GPLv3).",
    nav=("الأمان", "القنوات", "التنزيل", "الخصوصية"),
    eyebrow="خزنة كلمات مرور دون اتصال لأندرويد",
    h1="أسرارك<br>لا <em>تغادر أبدًا.</em>",
    lede="Sekuvo هي خزنتك الآمنة: كلمات المرور والبطاقات والملاحظات، مشفَّرة على هاتفك بمفتاح لا تشتقّه إلا كلمة مرورك الرئيسية. لا خادم، ولا حساب، ولا مزامنة — ولا سبيل للاتصال بأي جهة.",
    btn_src="المصدر على GitHub", btn_priv="سياسة الخصوصية",
    cta_note="صفحة Google Play قيد الإعداد. Sekuvo مجاني وبرخصة GPLv3 — والشيفرة هي الدليل.",
    proof_cap="AndroidManifest.xml — كل الأذونات التي يطلبها",
    proof_alt="يطلب الملف الكاميرا والقياسات الحيوية والبلوتوث، والبحث عن إذن الإنترنت لا يعطي أي نتيجة.",
    proof_no="(لا نتائج — هذا الإذن غير موجود أصلًا)",
    sec_eyebrow="نموذج الأمان",
    sec_h2="تشفير تدقّقه، لا تصدّقه.",
    sec_kicker="كل حقل حسّاس مختوم بـ AES-256-GCM. المفتاح لا يمرّ بأي خادم لأنه لا يوجد خادم؛ يُشتقّ على هاتفك من كلمة مرورك الرئيسية في كل مرة تفتح فيها القفل.",
    chain=CHAIN_LATIN,
    cells=[("يُقفل عند انطفاء الشاشة",
            "يُمحى المفتاح من الذاكرة لحظة انطفاء الشاشة — وطيّ الهاتف القابل للطي يُحتسب كذلك. فتحة واحدة تخدم التطبيق ولوحة المفاتيح والملء التلقائي معًا."),
           ("نسخ احتياطية تبقى بعد الهاتف",
            "ملف <span class=\"mono-note\">.vaultbak</span> مشفَّر واحد تحفظه حيث تشاء. الملف مع كلمة مرور النسخة يستعيدان كل شيء على أي جهاز — ومسار الاستعادة مُجرَّب من طرف إلى طرف."),
           ("لا باب خلفي للاستعادة",
            "إن نسيت كلمة المرور الرئيسية ضاعت البيانات. هذا هو التصميم: باب لا يفتحه سواك لا يخبّئ مفتاحًا احتياطيًا تحت السجادة.")],
    ch_eyebrow="بلا حافظة بحكم التصميم",
    ch_h2="ثلاثة مخارج، كلها تحت إصبعك.",
    ch_kicker="الحافظة هي المكان الذي تُسرق فيه الأسرار. لذلك يكتب Sekuvo القيم مباشرة في وجهتها.",
    lanes=[("الملء التلقائي", "خدمة الملء التلقائي في أندرويد",
            "تعرض نماذج تسجيل الدخول والبطاقات مدخلاتك مباشرة. وأثناء القفل لا يحصل النظام على شيء — افتح القفل أولًا ثم اختر."),
           ("لوحة المفاتيح", "لوحة مفاتيح Sekuvo",
            "بدّل إليها في أي تطبيق واكتب سرًّا محفوظًا في الحقل — مع البحث، والأحدث في الأعلى، ودون خطوة نسخ."),
           ("بلوتوث", "يكتب في حاسوبك",
            "يتحول هاتفك إلى لوحة مفاتيح بلوتوث ويكتب السر عند مؤشر الحاسوب. ولا يُثبَّت شيء على الحاسوب.")],
    dl_eyebrow="احصل على Sekuvo", dl_h2="مجاني، مفتوح المصدر، GPLv3.",
    dl_app_h="تطبيق أندرويد",
    dl_app_p="صفحة Google Play قيد الإعداد. وحتى ذلك الحين يمكنك البناء من المصدر — ملف README في المستودع يشرح ذلك بأمرين.",
    dl_tools_h="أدوات الحاسوب",
    dl_tools_p="أداة الحاسوب ملف HTML واحد — <code>aktar.html</code> — وهي ملف يُنزَّل لا صفحة ويب: تعمل بالكامل على جهازك، وهذا الموقع لا يطلب منك سرًّا أبدًا.",
    dl_tools_note="github.com → Releases · تحقّق من بصمة SHA-256 المنشورة",
    dl_app_link="اقرأ الدليل ←",
    dl_tools_link="كيف تحصل على aktar.html وكيف تستخدمه ←",
    contact="اتصل بنا",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>خزنتك الآمنة.</em>",
)

L["zh"] = dict(
    lang="zh", dir="ltr", script="cjk-sc", path="zh/", name="简体中文",
    title="Sekuvo — 你的安全密码库",
    desc="Sekuvo — 你的安全密码库。一款完全离线的 Android 密码库：无互联网权限，AES-256 加密，开源（GPLv3）。",
    nav=("安全", "通道", "下载", "隐私"),
    eyebrow="Android 离线密码库",
    h1="你的秘密<br>从不<em>外泄。</em>",
    lede="Sekuvo 是你的安全密码库：密码、银行卡和笔记，在你的手机上用只有主密码才能派生的密钥加密。没有服务器，没有账户，没有同步 — 也没有向外发送数据的途径。",
    btn_src="GitHub 上的源代码", btn_priv="隐私政策",
    cta_note="Google Play 页面正在准备中。Sekuvo 免费且遵循 GPLv3 — 代码本身就是证明。",
    proof_cap="AndroidManifest.xml — 它拥有的全部权限",
    proof_alt="应用清单请求了相机、生物识别和蓝牙权限，搜索 INTERNET 权限没有任何匹配结果。",
    proof_no="（没有匹配 — 这项权限根本不存在）",
    sec_eyebrow="安全模型",
    sec_h2="可审计，而非只能信任的加密。",
    sec_kicker="每个敏感字段都用 AES-256-GCM 封装。密钥永远不会接触服务器，因为根本没有服务器；每次解锁时都会在你的手机上，从主密码重新派生。",
    chain=('主密码 ─<b>PBKDF2 · 310,000 轮</b>─▶ KEK ─<b>AES-GCM 封装</b>─▶ '
           'dataKey ─▶ 每条记录 <b>AES-256-GCM</b>'),
    cells=[("屏幕熄灭即锁定",
            "屏幕一变暗，密钥就立即从内存中清除 — 折叠屏合上也算。一次解锁同时服务于应用、键盘和自动填充。"),
           ("比手机寿命更长的备份",
            "一个加密的 <span class=\"mono-note\">.vaultbak</span> 文件，存放在你选择的任何地方。文件加上备份密码可在任何设备上恢复一切 — 这条恢复路径经过端到端测试。"),
           ("没有恢复后门",
            "忘记主密码，数据就永远消失。这正是设计初衷：只有你能打开的门，不会在门垫下面藏一把备用钥匙。")],
    ch_eyebrow="设计上就不经过剪贴板",
    ch_h2="三条出路，都在你的指尖。",
    ch_kicker="剪贴板正是秘密被窃取的地方。Sekuvo 把值直接写入目标位置。",
    lanes=[("自动填充", "Android 自动填充服务",
            "登录和银行卡表单直接提供你的条目。密码库锁定时，系统什么也得不到 — 先解锁，再选择。"),
           ("键盘", "Sekuvo 键盘",
            "在任意应用中切换到它，把已保存的密文直接输入到字段中 — 可搜索，最近使用的排在最前，无需复制这一步。"),
           ("蓝牙", "输入到你的电脑",
            "你的手机变成一个蓝牙键盘，把密文输入到电脑光标所在的位置。电脑上不会安装任何东西。")],
    dl_eyebrow="获取 Sekuvo", dl_h2="免费、开源、GPLv3。",
    dl_app_h="Android 应用",
    dl_app_p="Google Play 页面正在准备中。在此之前你可以从源码构建 — 仓库的 README 用两条命令说明了方法。",
    dl_tools_h="电脑端工具",
    dl_tools_p="电脑端工具是一个单独的 HTML 文件 — <code>aktar.html</code> — 它是一个下载文件，而不是网页：完全在你自己的电脑上运行，本网站绝不会向你索要密文。",
    dl_tools_note="github.com → Releases · 核对发布的 SHA-256",
    dl_app_link="阅读指南 →",
    dl_tools_link="如何获取并使用 aktar.html →",
    contact="联系方式",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>你的安全密码库。</em>",
)

L["fr"] = dict(
    lang="fr", dir="ltr", script="latin", path="fr/", name="Français",
    title="Sekuvo — Votre coffre sécurisé",
    desc="Sekuvo — votre coffre sécurisé. Un coffre de mots de passe entièrement hors ligne pour Android : sans permission internet, AES-256, open source (GPLv3).",
    nav=("Sécurité", "Canaux", "Télécharger", "Confidentialité"),
    eyebrow="Coffre de mots de passe hors ligne pour Android",
    h1="Tes secrets<br>ne <em>sortent</em> jamais.",
    lede="Sekuvo est ton coffre sécurisé : mots de passe, cartes et notes, chiffrés sur ton téléphone avec une clé que seul ton mot de passe principal peut dériver. Pas de serveur, pas de compte, pas de synchronisation — et aucun moyen d'appeler la maison.",
    btn_src="Code source sur GitHub", btn_priv="Politique de confidentialité",
    cta_note="La fiche Google Play est en préparation. Sekuvo est gratuit et sous GPLv3 — le code en est la preuve.",
    proof_cap="AndroidManifest.xml — toutes les permissions qu'elle possède",
    proof_alt="Le manifeste de l'application demande la caméra, la biométrie et le Bluetooth, et une recherche de la permission INTERNET ne renvoie aucun résultat.",
    proof_no="(aucun résultat — cette permission n'existe pas)",
    sec_eyebrow="Modèle de sécurité",
    sec_h2="Un chiffrement à auditer, pas à croire sur parole.",
    sec_kicker="Chaque champ sensible est scellé avec AES-256-GCM. La clé ne touche jamais un serveur, car il n'y en a pas ; elle est dérivée sur ton téléphone, à partir de ton mot de passe principal, à chaque déverrouillage.",
    chain=('Mot de passe principal ─<b>PBKDF2 · 310 000 tours</b>─▶ KEK ─<b>enveloppement AES-GCM</b>─▶ '
           'dataKey ─▶ <b>AES-256-GCM</b> sur chaque entrée'),
    cells=[("Se verrouille quand l'écran s'éteint",
            "La clé est effacée de la mémoire dès que l'écran s'assombrit — replier un pliable compte aussi. Un seul déverrouillage sert à la fois l'application, le clavier et la saisie automatique."),
           ("Des sauvegardes qui survivent au téléphone",
            "Un unique fichier chiffré <span class=\"mono-note\">.vaultbak</span>, stocké où tu veux. Le fichier plus le mot de passe de sauvegarde restaurent tout sur n'importe quel appareil — le chemin de récupération est testé de bout en bout."),
           ("Aucune porte dérobée de récupération",
            "Oublie le mot de passe principal et les données disparaissent. C'est le principe même : une porte que toi seul peux ouvrir n'a pas de double planqué sous le paillasson.")],
    ch_eyebrow="Sans presse-papiers, par conception",
    ch_h2="Trois sorties, toutes sous ton doigt.",
    ch_kicker="Le presse-papiers est l'endroit où les secrets se font voler. Sekuvo écrit les valeurs directement à leur destination.",
    lanes=[("Saisie automatique", "Service de saisie automatique Android",
            "Les formulaires de connexion et de carte proposent directement tes entrées. Verrouillé, le système ne reçoit rien — déverrouille d'abord, puis choisis."),
           ("Clavier", "Clavier Sekuvo",
            "Bascule dessus dans n'importe quelle application et saisis un secret enregistré dans le champ — avec recherche, éléments récents en haut, sans étape de copie."),
           ("Bluetooth", "Écrit sur ton ordinateur",
            "Ton téléphone devient un clavier Bluetooth et saisit le secret à l'emplacement du curseur de l'ordinateur. Rien n'est installé sur l'ordinateur.")],
    dl_eyebrow="Obtenir Sekuvo", dl_h2="Gratuit, open source, GPLv3.",
    dl_app_h="Application Android",
    dl_app_p="La fiche Google Play est en préparation. En attendant, tu peux compiler depuis les sources — le README du dépôt l'explique en deux commandes.",
    dl_tools_h="Outils côté ordinateur",
    dl_tools_p="L'outil côté ordinateur est un simple fichier HTML — <code>aktar.html</code> — et c'est un téléchargement, pas une page web : il fonctionne entièrement sur ta machine, et ce site ne te demande jamais de secret.",
    dl_tools_note="github.com → Releases · vérifie le SHA-256 publié",
    dl_app_link="Lire le guide →",
    dl_tools_link="Comment obtenir et utiliser aktar.html →",
    contact="Contact",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>ton coffre sécurisé.</em>",
)

L["bn"] = dict(
    lang="bn", dir="ltr", script="bengali", path="bn/", name="বাংলা",
    title="Sekuvo — আপনার নিরাপদ ভল্ট",
    desc="Sekuvo — আপনার নিরাপদ ভল্ট। Android-এর জন্য সম্পূর্ণ অফলাইন পাসওয়ার্ড ভল্ট: ইন্টারনেট অনুমতি নেই, AES-256, ওপেন সোর্স (GPLv3)।",
    nav=("নিরাপত্তা", "চ্যানেল", "ডাউনলোড", "গোপনীয়তা"),
    eyebrow="Android-এর জন্য অফলাইন পাসওয়ার্ড ভল্ট",
    h1="আপনার গোপন তথ্য<br>কখনো <em>বেরোয় না।</em>",
    lede="Sekuvo আপনার নিরাপদ ভল্ট: পাসওয়ার্ড, কার্ড ও নোট, আপনার ফোনে এমন একটি কী দিয়ে এনক্রিপ্ট করা যা শুধু আপনার মূল পাসওয়ার্ড থেকেই তৈরি করা যায়। কোনো সার্ভার নেই, অ্যাকাউন্ট নেই, সিঙ্ক নেই — এবং বাইরে কিছু পাঠানোর কোনো উপায় নেই।",
    btn_src="GitHub-এ সোর্স কোড", btn_priv="গোপনীয়তা নীতি",
    cta_note="Google Play লিস্টিং প্রস্তুত হচ্ছে। Sekuvo বিনামূল্যে এবং GPLv3-এর অধীনে — কোডটাই তার প্রমাণ।",
    proof_cap="AndroidManifest.xml — এর সব অনুমতি",
    proof_alt="অ্যাপের ম্যানিফেস্ট ক্যামেরা, বায়োমেট্রিক্স ও ব্লুটুথ চায়, এবং INTERNET অনুমতি খুঁজে কোনো মিল পাওয়া যায়নি।",
    proof_no="(কোনো মিল নেই — এই অনুমতিটি আসলে নেই)",
    sec_eyebrow="নিরাপত্তা মডেল",
    sec_h2="বিশ্বাস নয়, যাচাই করা যায় এমন এনক্রিপশন।",
    sec_kicker="প্রতিটি স্পর্শকাতর ফিল্ড AES-256-GCM দিয়ে সিল করা। কী কখনো কোনো সার্ভারে যায় না, কারণ কোনো সার্ভারই নেই; প্রতিবার আনলক করার সময় এটি আপনার ফোনে, আপনার মূল পাসওয়ার্ড থেকে তৈরি হয়।",
    chain=('মূল পাসওয়ার্ড ─<b>PBKDF2 · ৩,১০,০০০ রাউন্ড</b>─▶ KEK ─<b>AES-GCM র‍্যাপ</b>─▶ '
           'dataKey ─▶ প্রতিটি এন্ট্রিতে <b>AES-256-GCM</b>'),
    cells=[("স্ক্রিন বন্ধ হলেই লক",
            "স্ক্রিন অন্ধকার হওয়ার মুহূর্তেই কী মেমোরি থেকে মুছে যায় — ফোল্ডেবল ফোন ভাঁজ করাও এর মধ্যে পড়ে। একবার আনলক করলেই তা অ্যাপ, কীবোর্ড এবং অটোফিল একসাথে ব্যবহার করে।"),
           ("ফোনের চেয়ে বেশিদিন টিকে থাকা ব্যাকআপ",
            "একটি এনক্রিপ্টেড <span class=\"mono-note\">.vaultbak</span> ফাইল, আপনার পছন্দের যেকোনো জায়গায় রাখা যায়। ফাইল এবং ব্যাকআপ পাসওয়ার্ড দিয়ে যেকোনো ডিভাইসে সবকিছু ফিরে আসে — পুনরুদ্ধারের পথটি সম্পূর্ণভাবে পরীক্ষিত।"),
           ("পুনরুদ্ধারের কোনো ব্যাকডোর নেই",
            "মূল পাসওয়ার্ড ভুলে গেলে তথ্য চিরতরে হারিয়ে যায়। এটাই নকশা: যে দরজা শুধু আপনিই খুলতে পারেন, তার নিচে কোনো বাড়তি চাবি লুকানো থাকে না।")],
    ch_eyebrow="নকশা অনুযায়ীই ক্লিপবোর্ড-মুক্ত",
    ch_h2="তিনটি পথ, সবই আপনার আঙুলের নিচে।",
    ch_kicker="ক্লিপবোর্ড হলো সেই জায়গা যেখান থেকে গোপন তথ্য চুরি হয়। Sekuvo মানগুলো সরাসরি তাদের গন্তব্যে লেখে।",
    lanes=[("অটোফিল", "Android অটোফিল সার্ভিস",
            "সাইন-ইন ও কার্ড ফর্মে সরাসরি আপনার এন্ট্রি দেখানো হয়। লক থাকা অবস্থায় সিস্টেম কিছুই পায় না — আগে আনলক করুন, তারপর বেছে নিন।"),
           ("কীবোর্ড", "Sekuvo কীবোর্ড",
            "যেকোনো অ্যাপে এটিতে স্যুইচ করে সংরক্ষিত তথ্য সরাসরি ফিল্ডে টাইপ করুন — খোঁজা যায়, সাম্প্রতিকগুলো উপরে, কপি করার প্রয়োজন নেই।"),
           ("ব্লুটুথ", "আপনার কম্পিউটারে টাইপ করে",
            "আপনার ফোন একটি ব্লুটুথ কীবোর্ডে পরিণত হয় এবং কম্পিউটারের কার্সারে গোপন তথ্য টাইপ করে। কম্পিউটারে কিছুই ইনস্টল হয় না।")],
    dl_eyebrow="Sekuvo নিন", dl_h2="বিনামূল্যে, ওপেন সোর্স, GPLv3।",
    dl_app_h="Android অ্যাপ",
    dl_app_p="Google Play লিস্টিং প্রস্তুত হচ্ছে। ততক্ষণ আপনি সোর্স থেকে বিল্ড করতে পারেন — রিপোজিটরির README দুটি কমান্ডে তা ব্যাখ্যা করে।",
    dl_tools_h="কম্পিউটার-সাইড টুল",
    dl_tools_p="কম্পিউটার-সাইড টুলটি একটি একক HTML ফাইল — <code>aktar.html</code> — এবং এটি একটি ডাউনলোড, ওয়েব পেজ নয়: এটি সম্পূর্ণভাবে আপনার মেশিনে চলে, এবং এই সাইট আপনার কাছে কখনো গোপন তথ্য চায় না।",
    dl_tools_note="github.com → Releases · প্রকাশিত SHA-256 যাচাই করুন",
    dl_app_link="গাইড পড়ুন →",
    dl_tools_link="aktar.html কীভাবে পাবেন এবং ব্যবহার করবেন →",
    contact="যোগাযোগ",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>আপনার নিরাপদ ভল্ট।</em>",
)

L["pt"] = dict(
    lang="pt", dir="ltr", script="latin", path="pt/", name="Português",
    title="Sekuvo — Seu cofre seguro",
    desc="Sekuvo — seu cofre seguro. Um cofre de senhas totalmente offline para Android: sem permissão de internet, AES-256, código aberto (GPLv3).",
    nav=("Segurança", "Canais", "Baixar", "Privacidade"),
    eyebrow="Cofre de senhas offline para Android",
    h1="Seus segredos<br>nunca <em>saem.</em>",
    lede="O Sekuvo é o seu cofre seguro: senhas, cartões e notas, criptografados no seu telefone com uma chave que só a sua senha principal consegue derivar. Sem servidor, sem conta, sem sincronização — e nenhuma forma de avisar alguém.",
    btn_src="Código-fonte no GitHub", btn_priv="Política de privacidade",
    cta_note="A ficha da Google Play está em preparação. O Sekuvo é gratuito e GPLv3 — o código é a prova.",
    proof_cap="AndroidManifest.xml — todas as permissões que ele tem",
    proof_alt="O manifesto do aplicativo pede câmera, biometria e Bluetooth, e uma busca pela permissão INTERNET não retorna nenhum resultado.",
    proof_no="(nenhum resultado — essa permissão não existe)",
    sec_eyebrow="Modelo de segurança",
    sec_h2="Criptografia para auditar, não para acreditar.",
    sec_kicker="Todo campo sensível é selado com AES-256-GCM. A chave nunca toca um servidor porque não existe servidor; ela é derivada no seu telefone, a partir da sua senha principal, toda vez que você desbloqueia.",
    chain=('Senha principal ─<b>PBKDF2 · 310.000 rodadas</b>─▶ KEK ─<b>envelopamento AES-GCM</b>─▶ '
           'dataKey ─▶ <b>AES-256-GCM</b> em cada item'),
    cells=[("Bloqueia quando a tela apaga",
            "A chave é apagada da memória no instante em que a tela escurece — fechar um dobrável também conta. Um único desbloqueio serve o aplicativo, o teclado e o preenchimento automático juntos."),
           ("Backups que sobrevivem ao telefone",
            "Um único arquivo criptografado <span class=\"mono-note\">.vaultbak</span>, guardado onde você escolher. Arquivo mais senha de backup restauram tudo em qualquer dispositivo — o caminho de recuperação é testado de ponta a ponta."),
           ("Sem porta dos fundos de recuperação",
            "Esqueça a senha principal e os dados se vão. É assim por design: uma porta que só você pode abrir não tem uma chave reserva debaixo do tapete.")],
    ch_eyebrow="Sem área de transferência por design",
    ch_h2="Três saídas, todas na ponta do seu dedo.",
    ch_kicker="A área de transferência é onde segredos são roubados. O Sekuvo digita os valores direto no destino.",
    lanes=[("Preenchimento automático", "Serviço de preenchimento automático do Android",
            "Formulários de login e de cartão oferecem seus itens diretamente. Enquanto bloqueado, o sistema não recebe nada — desbloqueie primeiro, depois escolha."),
           ("Teclado", "Teclado Sekuvo",
            "Mude para ele em qualquer aplicativo e digite um segredo salvo direto no campo — pesquisável, recentes no topo, sem etapa de cópia."),
           ("Bluetooth", "Digita no seu computador",
            "Seu telefone vira um teclado Bluetooth e digita o segredo no cursor do computador. Nada é instalado no computador.")],
    dl_eyebrow="Obter o Sekuvo", dl_h2="Gratuito, código aberto, GPLv3.",
    dl_app_h="Aplicativo Android",
    dl_app_p="A ficha da Google Play está em preparação. Até lá, você pode compilar a partir do código-fonte — o README do repositório explica em dois comandos.",
    dl_tools_h="Ferramentas do lado do computador",
    dl_tools_p="A ferramenta do lado do computador é um único arquivo HTML — <code>aktar.html</code> — e é um download, não uma página web: ela roda inteiramente na sua máquina, e este site nunca pede um segredo a você.",
    dl_tools_note="github.com → Releases · confira o SHA-256 publicado",
    dl_app_link="Leia o guia →",
    dl_tools_link="Como obter e usar o aktar.html →",
    contact="Contato",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>seu cofre seguro.</em>",
)

L["ru"] = dict(
    lang="ru", dir="ltr", script="cyrillic", path="ru/", name="Русский",
    title="Sekuvo — Ваше защищённое хранилище",
    desc="Sekuvo — ваше защищённое хранилище. Полностью офлайн-менеджер паролей для Android: без разрешения на интернет, AES-256, открытый код (GPLv3).",
    nav=("Безопасность", "Каналы", "Скачать", "Конфиденциальность"),
    eyebrow="Офлайн-хранилище паролей для Android",
    h1="Ваши секреты<br>никогда не <em>покидают телефон.</em>",
    lede="Sekuvo — ваше защищённое хранилище: пароли, карты и заметки, зашифрованные на телефоне ключом, который может получить только ваш основной пароль. Без сервера, без аккаунта, без синхронизации — и без способа кому-либо сообщить.",
    btn_src="Исходный код на GitHub", btn_priv="Политика конфиденциальности",
    cta_note="Страница в Google Play готовится. Sekuvo бесплатен и распространяется под GPLv3 — код тому доказательство.",
    proof_cap="AndroidManifest.xml — все разрешения, которые у него есть",
    proof_alt="Манифест приложения запрашивает камеру, биометрию и Bluetooth, а поиск разрешения INTERNET не даёт ни одного результата.",
    proof_no="(нет результатов — этого разрешения не существует)",
    sec_eyebrow="Модель безопасности",
    sec_h2="Шифрование, которое можно проверить, а не принять на веру.",
    sec_kicker="Каждое чувствительное поле запечатано AES-256-GCM. Ключ никогда не касается сервера, потому что сервера нет; он вычисляется на вашем телефоне из основного пароля при каждой разблокировке.",
    chain=('Основной пароль ─<b>PBKDF2 · 310 000 раундов</b>─▶ KEK ─<b>обёртка AES-GCM</b>─▶ '
           'dataKey ─▶ <b>AES-256-GCM</b> для каждой записи'),
    cells=[("Блокируется, когда гаснет экран",
            "Ключ стирается из памяти в момент, когда экран гаснет — складывание складного телефона тоже считается. Одна разблокировка обслуживает приложение, клавиатуру и автозаполнение одновременно."),
           ("Резервные копии переживают телефон",
            "Один зашифрованный файл <span class=\"mono-note\">.vaultbak</span>, хранящийся там, где вы решите. Файл плюс пароль резервной копии восстанавливают всё на любом устройстве — путь восстановления протестирован от начала до конца."),
           ("Нет чёрного хода для восстановления",
            "Забудьте основной пароль — и данные исчезнут. Так и задумано: дверь, которую можете открыть только вы, не имеет запасного ключа под ковриком.")],
    ch_eyebrow="Без буфера обмена по замыслу",
    ch_h2="Три канала — все у вас под рукой.",
    ch_kicker="Буфер обмена — это место, откуда крадут секреты. Sekuvo вводит значения прямо в место назначения.",
    lanes=[("Автозаполнение", "Служба автозаполнения Android",
            "Формы входа и карты сами предлагают ваши записи. Пока хранилище заблокировано, система не получает ничего — сначала разблокируйте, затем выбирайте."),
           ("Клавиатура", "Клавиатура Sekuvo",
            "Переключитесь на неё в любом приложении и введите сохранённый секрет прямо в поле — с поиском, недавними записями сверху, без шага копирования."),
           ("Bluetooth", "Вводит на вашем компьютере",
            "Телефон становится Bluetooth-клавиатурой и вводит секрет в позицию курсора на компьютере. На компьютер ничего не устанавливается.")],
    dl_eyebrow="Получить Sekuvo", dl_h2="Бесплатно, открытый код, GPLv3.",
    dl_app_h="Приложение для Android",
    dl_app_p="Страница в Google Play готовится. А пока можно собрать из исходного кода — README репозитория объясняет это в двух командах.",
    dl_tools_h="Инструменты на стороне компьютера",
    dl_tools_p="Инструмент для компьютера — это один HTML-файл, <code>aktar.html</code>, и это скачиваемый файл, а не веб-страница: он полностью работает на вашей машине, и этот сайт никогда не спросит у вас секрет.",
    dl_tools_note="github.com → Releases · проверьте опубликованный SHA-256",
    dl_app_link="Читать руководство →",
    dl_tools_link="Как получить и использовать aktar.html →",
    contact="Контакты",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>ваше защищённое хранилище.</em>",
)

ORDER = ["en", "tr", "es", "hi", "ar", "zh", "fr", "bn", "pt", "ru"]

STYLE = """
  html { color-scheme: light dark; }
  :root {
    --ground: #16130f;
    --surface: #201c16;
    --line: #35302699;
    --ink: #ede6da;
    --muted: #9c927f;
    --brass: #c9a34c;
    --brass-ink: #16130f;
    --ok: #7fa86b;
  }
  @media (prefers-color-scheme: light) {
    :root:not([data-theme="dark"]) {
      --ground: #f1eee8;
      --surface: #faf8f4;
      --line: #d8d2c455;
      --ink: #221d15;
      --muted: #6f6753;
      --brass: #8a6d2a;
      --brass-ink: #f8f4ec;
      --ok: #4f7a3d;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--ground);
    color: var(--ink);
    font-family: __BODY__;
    font-size: 17px;
    line-height: 1.65;
  }
  .wrap { max-width: 62rem; margin: 0 auto; padding: 0 1.5rem; }

  h1, h2, h3 { font-family: __DISPLAY__; line-height: 1.14; text-wrap: balance; margin: 0; }
  .eyebrow {
    font-family: "IBM Plex Mono", monospace;
    font-size: .78rem; letter-spacing: .18em; text-transform: uppercase;
    color: var(--brass);
  }
  a { color: var(--brass); text-decoration-thickness: 1px; text-underline-offset: 3px; }
  a:focus-visible, .btn:focus-visible { outline: 2px solid var(--brass); outline-offset: 3px; }

  header { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; padding: 1.6rem 0 0; flex-wrap: wrap; }
  .brand { font-family: __DISPLAY__; font-weight: 700; font-size: 1.25rem; }
  nav { display: flex; gap: 1.4rem; font-size: .92rem; flex-wrap: wrap; }
  nav a { color: var(--muted); text-decoration: none; }
  nav a:hover { color: var(--brass); }

  .langs { display: flex; gap: .75rem; font-size: .82rem; flex-wrap: wrap; padding: .9rem 0 0; }
  .langs a { color: var(--muted); text-decoration: none; }
  .langs a:hover { color: var(--brass); }
  .langs .here { color: var(--brass); font-weight: 600; }

  .hero { padding: 4.5rem 0; display: grid; grid-template-columns: 1.15fr .85fr; gap: 3.5rem; align-items: center; }
  .hero h1 { font-size: clamp(2.5rem, 5.8vw, 4.2rem); font-weight: 640; }
  .hero h1 em { font-style: normal; color: var(--brass); }
  .hero .lede { color: var(--muted); max-width: 34rem; margin: 1.4rem 0 2.2rem; }
  .cta { display: flex; gap: .9rem; flex-wrap: wrap; }
  .btn { display: inline-block; padding: .7rem 1.25rem; border-radius: 4px; font-weight: 600; font-size: .95rem; text-decoration: none; border: 1px solid var(--brass); }
  .btn.solid { background: var(--brass); color: var(--brass-ink); }
  .btn.ghost { color: var(--brass); }
  .cta-note { font-size: .82rem; color: var(--muted); margin-top: .8rem; }

  .proof {
    background: var(--surface); border: 1px solid var(--line); border-radius: 6px;
    font-family: "IBM Plex Mono", monospace; font-size: .8rem; line-height: 1.75;
    padding: 1.3rem 1.4rem; overflow-x: auto;
  }
  .proof .cap { font-size: .72rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); display: block; margin-bottom: .8rem; }
  .proof .p  { color: var(--ink); white-space: pre; }
  .proof .c  { color: var(--muted); white-space: pre; }
  .proof .no { color: var(--ok); white-space: pre; font-weight: 500; }

  section { padding: 3.6rem 0; border-top: 1px solid var(--line); }
  section h2 { font-size: 1.9rem; font-weight: 600; margin-bottom: .4rem; }
  .kicker { color: var(--muted); max-width: 40rem; margin: 0 0 2.4rem; }

  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.2rem 2.6rem; margin-top: 2.4rem; }
  .cell h3 { font-size: 1.06rem; font-weight: 600; margin-bottom: .45rem; }
  .cell p { margin: 0; font-size: .93rem; color: var(--muted); }

  .chain {
    font-family: "IBM Plex Mono", monospace; font-size: .82rem; color: var(--muted);
    background: var(--surface); border: 1px solid var(--line); border-radius: 6px;
    padding: 1.1rem 1.4rem; overflow-x: auto; white-space: pre; line-height: 1.9;
  }
  .chain b { color: var(--brass); font-weight: 500; }

  .lanes { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 6px; overflow: hidden; }
  .lane { background: var(--surface); padding: 1.5rem 1.4rem; }
  .lane .n { font-family: "IBM Plex Mono", monospace; font-size: .72rem; color: var(--brass); letter-spacing: .12em; text-transform: uppercase; }
  .lane h3 { font-size: 1rem; margin: .5rem 0 .4rem; }
  .lane p { margin: 0; font-size: .88rem; color: var(--muted); }

  .dl { display: flex; gap: 2.6rem; align-items: flex-start; flex-wrap: wrap; margin-top: 1.6rem; }
  .dl > div { flex: 1 1 18rem; }
  .dl h3 { font-size: 1.05rem; margin-bottom: .4rem; }
  .dl p { color: var(--muted); font-size: .93rem; margin: 0 0 .5rem; }
  .mono-note { font-family: "IBM Plex Mono", monospace; font-size: .8rem; color: var(--muted); }

  footer { border-top: 1px solid var(--line); padding: 2.2rem 0 3rem; font-size: .85rem; color: var(--muted); display: flex; justify-content: space-between; gap: 1.5rem; flex-wrap: wrap; }
  footer a { color: var(--muted); }
  footer a:hover { color: var(--brass); }
  footer em { font-style: normal; color: var(--brass); }

  @media (prefers-reduced-motion: no-preference) {
    .hero > * { animation: rise .7s cubic-bezier(.2,.6,.2,1) both; }
    .hero > *:nth-child(2) { animation-delay: .12s; }
    @keyframes rise { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }
  }

  @media (max-width: 780px) {
    .hero { grid-template-columns: 1fr; padding-top: 3rem; gap: 2.4rem; }
    .grid, .lanes { grid-template-columns: 1fr; }
  }
"""

PAGE = """<!DOCTYPE html>
<html lang="{lang}" dir="{dir}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="/favicon.png" sizes="32x32">
<link rel="icon" href="/img/icon-512.png" sizes="512x512">
<link rel="apple-touch-icon" href="/img/icon-180.png">
{alternates}
<link rel="stylesheet" href="{font_url}">
<style>{style}</style>
</head>
<body>
<div class="wrap">
  <header>
    <span class="brand">Sekuvo</span>
    <nav>
      <a href="#security">{nav0}</a>
      <a href="#channels">{nav1}</a>
      <a href="#download">{nav2}</a>
      <a href="{guide_url}">{guide_label}</a>
      <a href="{privacy_url}">{nav3}</a>
    </nav>
  </header>
  <div class="langs">{langs}</div>

  <div class="hero">
    <div>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      <div class="cta">
        <a class="btn solid" href="{github}">{btn_src}</a>
        <a class="btn ghost" href="{privacy_url}">{btn_priv}</a>
      </div>
      <p class="cta-note">{cta_note}</p>
    </div>

    <div class="proof" dir="ltr" role="img" aria-label="{proof_alt}">
      <span class="cap">{proof_cap}</span>
<span class="p">&lt;uses-permission android:name="…USE_BIOMETRIC" /&gt;
&lt;uses-permission android:name="…CAMERA" /&gt;
&lt;uses-permission android:name="…VIBRATE" /&gt;
&lt;uses-permission android:name="…BLUETOOTH_CONNECT" /&gt;</span>

<span class="c">$ grep INTERNET AndroidManifest.xml</span>
<span class="no">{proof_no}</span>
    </div>
  </div>

  <section id="security">
    <span class="eyebrow">{sec_eyebrow}</span>
    <h2>{sec_h2}</h2>
    <p class="kicker">{sec_kicker}</p>
    <div class="chain" dir="ltr">{chain}</div>
    <div class="grid">{cells}</div>
  </section>

  <section id="channels">
    <span class="eyebrow">{ch_eyebrow}</span>
    <h2>{ch_h2}</h2>
    <p class="kicker">{ch_kicker}</p>
    <div class="lanes">{lanes}</div>
  </section>

  <section id="download">
    <span class="eyebrow">{dl_eyebrow}</span>
    <h2>{dl_h2}</h2>
    <div class="dl">
      <div>
        <h3>{dl_app_h}</h3>
        <p>{dl_app_p}</p>
        <p><a href="{guide_url}#start">{dl_app_link}</a></p>
      </div>
      <div>
        <h3>{dl_tools_h}</h3>
        <p>{dl_tools_p}</p>
        <p class="mono-note" dir="ltr">{dl_tools_note}</p>
        <p><a href="{guide_url}#transfer">{dl_tools_link}</a></p>
      </div>
    </div>
  </section>

  <footer>
    <span>{footer}</span>
    <span dir="ltr">
      <a href="{github}">GitHub</a> ·
      <a href="mailto:contact@sekuvo.com">{contact}</a> ·
      <a href="{privacy_url}">{nav3}</a> ·
      <a href="https://www.gnu.org/licenses/gpl-3.0.html">GPLv3</a>
    </span>
  </footer>
</div>
</body>
</html>
"""


def build():
    root = pathlib.Path(__file__).parent
    for code in ORDER:
        t = L[code]
        font_url, display, body = FONTS[t["script"]]
        style = STYLE.replace("__DISPLAY__", display).replace("__BODY__", body)

        alternates = "\n".join(
            f'<link rel="alternate" hreflang="{L[c]["lang"]}" href="{SITE}/{L[c]["path"]}">'
            for c in ORDER
        ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/">'

        langs = " ·\n    ".join(
            f'<a class="here" href="{SITE}/{L[c]["path"]}" lang="{L[c]["lang"]}">{L[c]["name"]}</a>'
            if c == code else
            f'<a href="{SITE}/{L[c]["path"]}" lang="{L[c]["lang"]}">{L[c]["name"]}</a>'
            for c in ORDER
        )

        cells = "".join(
            f'<div class="cell"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["cells"]
        )
        lanes = "".join(
            f'<div class="lane"><div class="n">{n}</div><h3>{h}</h3><p>{p}</p></div>'
            for n, h, p in t["lanes"]
        )

        html = PAGE.format(
            lang=t["lang"], dir=t["dir"], desc=t["desc"], title=t["title"],
            alternates=alternates, font_url=font_url, style=style, langs=langs,
            site=SITE, github=GITHUB,
            privacy_url=f"{SITE}/{t['path']}privacy/",
            guide_url=f"{SITE}/{t['path']}guide/",
            guide_label=G[code]["nav_label"],
            nav0=t["nav"][0], nav1=t["nav"][1], nav2=t["nav"][2], nav3=t["nav"][3],
            eyebrow=t["eyebrow"], h1=t["h1"], lede=t["lede"],
            btn_src=t["btn_src"], btn_priv=t["btn_priv"], cta_note=t["cta_note"],
            proof_alt=t["proof_alt"], proof_cap=t["proof_cap"], proof_no=t["proof_no"],
            sec_eyebrow=t["sec_eyebrow"], sec_h2=t["sec_h2"], sec_kicker=t["sec_kicker"],
            chain=t["chain"], cells=cells,
            ch_eyebrow=t["ch_eyebrow"], ch_h2=t["ch_h2"], ch_kicker=t["ch_kicker"],
            lanes=lanes,
            dl_eyebrow=t["dl_eyebrow"], dl_h2=t["dl_h2"],
            dl_app_h=t["dl_app_h"], dl_app_p=t["dl_app_p"],
            dl_tools_h=t["dl_tools_h"], dl_tools_p=t["dl_tools_p"],
            dl_tools_note=t["dl_tools_note"],
            dl_app_link=t["dl_app_link"], dl_tools_link=t["dl_tools_link"],
            contact=t["contact"], footer=t["footer"],
        )

        out = root / t["path"] / "index.html" if t["path"] else root / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"{out.relative_to(root)}  ({len(html):,} bytes)")


# ─────────────────────────────────────────────────────────────────────────────
# Privacy policy, one page per language.
#
# English is the binding version and the translations say so: a policy is a
# legal statement, and a translated nuance that drifts from the original would
# be the version a reader relies on. Naming one authoritative text keeps the
# translations useful without making them load-bearing.
# ─────────────────────────────────────────────────────────────────────────────

EFFECTIVE = "2026-08-25"

P = {}

P["en"] = dict(
    title="Sekuvo — Privacy Policy",
    desc="Sekuvo privacy policy: no data collected, no data shared, no internet permission.",
    h1="Privacy Policy",
    meta=f"App: <strong>Sekuvo</strong> (com.sekuvo.app) · Developer: Ahmet Govercile · Effective date: {EFFECTIVE}",
    back="← Back to sekuvo.com",
    authoritative=None,
    sections=[
        ("Summary",
         "<p><strong>Sekuvo does not collect, transmit, or share any data.</strong> It is an offline password vault. The app does not request the Internet permission, so it is technically incapable of sending your data anywhere.</p>"),
        ("Data storage",
         "<p>Everything you store in Sekuvo (titles, usernames, passwords, notes, usage history) stays on your device, encrypted with a key derived from your master password. Nothing is uploaded, synced, or backed up to any server by the app.</p>"),
        ("Data collection and sharing",
         "<ul><li>No personal data is collected.</li><li>No data is shared with third parties.</li><li>No analytics, advertising, or tracking libraries are included.</li><li>No account is required to use the app.</li></ul>"),
        ("Permissions",
         "<ul><li><strong>Camera</strong> — used only to scan QR codes you choose to scan, for importing your own data. Frames are processed on the device and never leave it.</li><li><strong>Biometrics</strong> — used only to unlock the vault on your device, through the Android biometric system. Sekuvo never sees or stores your fingerprint or face data.</li><li><strong>Bluetooth</strong> — used only when you explicitly ask Sekuvo to type a password to a nearby computer as a Bluetooth keyboard. Only the characters you choose to send are transmitted, directly to the device you paired.</li></ul>"),
        ("Backups and transfers",
         "<p>Backups and transfers happen only when you start them, produce an encrypted file or QR codes protected by a password you set, and are saved or displayed only where you direct them. The app never sends them anywhere on its own.</p>"),
        ("Children",
         "<p>Sekuvo does not collect data from anyone, including children.</p>"),
        ("Changes",
         "<p>If this policy ever changes, the new version will be published at this address with an updated effective date.</p>"),
        ("Contact",
         '<p>Questions: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["tr"] = dict(
    title="Sekuvo — Gizlilik Politikası",
    desc="Sekuvo gizlilik politikası: veri toplanmaz, veri paylaşılmaz, internet izni yoktur.",
    h1="Gizlilik Politikası",
    meta=f"Uygulama: <strong>Sekuvo</strong> (com.sekuvo.app) · Geliştirici: Ahmet Govercile · Yürürlük tarihi: {EFFECTIVE}",
    back="← sekuvo.com'a dön",
    authoritative="Bu metin İngilizce aslından çevrilmiştir. Bir uyuşmazlık hâlinde <a href=\"https://sekuvo.com/privacy/\">İngilizce sürüm</a> geçerlidir.",
    sections=[
        ("Özet",
         "<p><strong>Sekuvo hiçbir veri toplamaz, iletmez ve paylaşmaz.</strong> Çevrimdışı bir parola kasasıdır. Uygulama İnternet izni istemez; dolayısıyla verinizi bir yere göndermesi teknik olarak mümkün değildir.</p>"),
        ("Verinin saklanması",
         "<p>Sekuvo'ya kaydettiğiniz her şey (başlıklar, kullanıcı adları, parolalar, notlar, kullanım geçmişi) cihazınızda kalır ve ana parolanızdan türetilen bir anahtarla şifrelenir. Uygulama hiçbir veriyi bir sunucuya yüklemez, eşitlemez veya yedeklemez.</p>"),
        ("Veri toplama ve paylaşma",
         "<ul><li>Hiçbir kişisel veri toplanmaz.</li><li>Üçüncü taraflarla hiçbir veri paylaşılmaz.</li><li>Analitik, reklam veya izleme kütüphanesi içermez.</li><li>Kullanmak için hesap gerekmez.</li></ul>"),
        ("İzinler",
         "<ul><li><strong>Kamera</strong> — yalnızca sizin taramayı seçtiğiniz QR kodlarını okumak için, kendi verinizi içe aktarırken kullanılır. Görüntüler cihazda işlenir, cihazdan çıkmaz.</li><li><strong>Biyometri</strong> — yalnızca kasayı cihazınızda açmak için, Android'in biyometri sistemi üzerinden kullanılır. Sekuvo parmak izinizi veya yüz verinizi hiçbir zaman görmez ve saklamaz.</li><li><strong>Bluetooth</strong> — yalnızca siz açıkça istediğinizde, bir parolayı yakındaki bir bilgisayara Bluetooth klavye gibi yazmak için kullanılır. Yalnızca göndermeyi seçtiğiniz karakterler, doğrudan eşleştirdiğiniz cihaza iletilir.</li></ul>"),
        ("Yedekler ve aktarımlar",
         "<p>Yedekleme ve aktarma yalnızca siz başlattığınızda gerçekleşir; belirlediğiniz bir parolayla korunan şifreli bir dosya ya da QR kodları üretir ve yalnızca sizin gösterdiğiniz yere kaydedilir veya görüntülenir. Uygulama bunları kendiliğinden hiçbir yere göndermez.</p>"),
        ("Çocuklar",
         "<p>Sekuvo, çocuklar dahil hiç kimseden veri toplamaz.</p>"),
        ("Değişiklikler",
         "<p>Bu politika değişirse, yeni sürüm güncellenmiş yürürlük tarihiyle bu adreste yayınlanır.</p>"),
        ("İletişim",
         '<p>Sorular için: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["es"] = dict(
    title="Sekuvo — Política de Privacidad",
    desc="Política de privacidad de Sekuvo: no se recopilan datos, no se comparten datos, sin permiso de internet.",
    h1="Política de Privacidad",
    meta=f"Aplicación: <strong>Sekuvo</strong> (com.sekuvo.app) · Desarrollador: Ahmet Govercile · Fecha de entrada en vigor: {EFFECTIVE}",
    back="← Volver a sekuvo.com",
    authoritative="Este texto es una traducción del original en inglés. En caso de discrepancia, prevalece la <a href=\"https://sekuvo.com/privacy/\">versión en inglés</a>.",
    sections=[
        ("Resumen",
         "<p><strong>Sekuvo no recopila, transmite ni comparte ningún dato.</strong> Es una bóveda de contraseñas sin conexión. La aplicación no solicita el permiso de Internet, por lo que es técnicamente incapaz de enviar tus datos a ninguna parte.</p>"),
        ("Almacenamiento de datos",
         "<p>Todo lo que guardas en Sekuvo (títulos, usuarios, contraseñas, notas, historial de uso) permanece en tu dispositivo, cifrado con una clave derivada de tu contraseña maestra. La aplicación no sube, sincroniza ni respalda nada en ningún servidor.</p>"),
        ("Recopilación y uso compartido de datos",
         "<ul><li>No se recopilan datos personales.</li><li>No se comparten datos con terceros.</li><li>No incluye bibliotecas de analítica, publicidad ni rastreo.</li><li>No se necesita una cuenta para usar la aplicación.</li></ul>"),
        ("Permisos",
         "<ul><li><strong>Cámara</strong> — se usa únicamente para leer los códigos QR que tú decides escanear, al importar tus propios datos. Las imágenes se procesan en el dispositivo y nunca salen de él.</li><li><strong>Biometría</strong> — se usa únicamente para desbloquear la bóveda en tu dispositivo, a través del sistema biométrico de Android. Sekuvo nunca ve ni almacena tu huella o tu rostro.</li><li><strong>Bluetooth</strong> — se usa únicamente cuando pides expresamente que Sekuvo escriba una contraseña en un ordenador cercano como teclado Bluetooth. Solo se transmiten los caracteres que eliges enviar, directamente al dispositivo emparejado.</li></ul>"),
        ("Copias de seguridad y transferencias",
         "<p>Las copias y transferencias ocurren solo cuando tú las inicias, generan un archivo cifrado o códigos QR protegidos por una contraseña que tú defines, y se guardan o muestran solo donde tú indicas. La aplicación nunca los envía a ningún sitio por su cuenta.</p>"),
        ("Menores",
         "<p>Sekuvo no recopila datos de nadie, incluidos los menores.</p>"),
        ("Cambios",
         "<p>Si esta política cambia, la nueva versión se publicará en esta dirección con una fecha de entrada en vigor actualizada.</p>"),
        ("Contacto",
         '<p>Consultas: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["hi"] = dict(
    title="Sekuvo — निजता नीति",
    desc="Sekuvo निजता नीति: कोई डेटा एकत्र नहीं, कोई डेटा साझा नहीं, इंटरनेट अनुमति नहीं।",
    h1="निजता नीति",
    meta=f"ऐप: <strong>Sekuvo</strong> (com.sekuvo.app) · डेवलपर: Ahmet Govercile · प्रभावी तिथि: {EFFECTIVE}",
    back="← sekuvo.com पर वापस",
    authoritative="यह पाठ अंग्रेज़ी मूल का अनुवाद है। मतभेद की स्थिति में <a href=\"https://sekuvo.com/privacy/\">अंग्रेज़ी संस्करण</a> मान्य होगा।",
    sections=[
        ("सारांश",
         "<p><strong>Sekuvo कोई डेटा एकत्र, प्रेषित या साझा नहीं करता।</strong> यह एक ऑफ़लाइन पासवर्ड तिजोरी है। ऐप इंटरनेट अनुमति माँगता ही नहीं, इसलिए आपका डेटा कहीं भेजना तकनीकी रूप से असंभव है।</p>"),
        ("डेटा का भंडारण",
         "<p>आप Sekuvo में जो कुछ रखते हैं (शीर्षक, उपयोगकर्ता नाम, पासवर्ड, नोट्स, उपयोग इतिहास) वह आपके डिवाइस पर ही रहता है, आपके मास्टर पासवर्ड से बनी कुंजी से एन्क्रिप्टेड। ऐप कुछ भी किसी सर्वर पर अपलोड, सिंक या बैकअप नहीं करता।</p>"),
        ("डेटा संग्रह और साझाकरण",
         "<ul><li>कोई व्यक्तिगत डेटा एकत्र नहीं किया जाता।</li><li>किसी तीसरे पक्ष के साथ कोई डेटा साझा नहीं किया जाता।</li><li>कोई एनालिटिक्स, विज्ञापन या ट्रैकिंग लाइब्रेरी शामिल नहीं है।</li><li>ऐप इस्तेमाल करने के लिए खाता ज़रूरी नहीं।</li></ul>"),
        ("अनुमतियाँ",
         "<ul><li><strong>कैमरा</strong> — केवल उन QR कोड को पढ़ने के लिए जिन्हें आप स्कैन करना चुनते हैं, अपना डेटा आयात करते समय। फ़्रेम डिवाइस पर ही संसाधित होते हैं और कभी बाहर नहीं जाते।</li><li><strong>बायोमेट्रिक्स</strong> — केवल आपके डिवाइस पर तिजोरी खोलने के लिए, Android की बायोमेट्रिक प्रणाली के ज़रिए। Sekuvo आपकी उँगली या चेहरे का डेटा न कभी देखता है, न संग्रहीत करता है।</li><li><strong>ब्लूटूथ</strong> — केवल तब, जब आप स्पष्ट रूप से कहें कि Sekuvo पास के कंप्यूटर में ब्लूटूथ कीबोर्ड बनकर पासवर्ड टाइप करे। केवल वही अक्षर भेजे जाते हैं जो आप चुनते हैं, सीधे उस जोड़े गए डिवाइस को।</li></ul>"),
        ("बैकअप और स्थानांतरण",
         "<p>बैकअप और स्थानांतरण तभी होते हैं जब आप उन्हें शुरू करते हैं; वे आपके तय किए पासवर्ड से सुरक्षित एन्क्रिप्टेड फ़ाइल या QR कोड बनाते हैं, और केवल वहीं सहेजे या दिखाए जाते हैं जहाँ आप कहते हैं। ऐप उन्हें अपने आप कहीं नहीं भेजता।</p>"),
        ("बच्चे",
         "<p>Sekuvo किसी से भी डेटा एकत्र नहीं करता, बच्चों से भी नहीं।</p>"),
        ("बदलाव",
         "<p>यदि यह नीति कभी बदलती है, तो नया संस्करण अद्यतन प्रभावी तिथि के साथ इसी पते पर प्रकाशित किया जाएगा।</p>"),
        ("संपर्क",
         '<p>प्रश्न: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["ar"] = dict(
    title="Sekuvo — سياسة الخصوصية",
    desc="سياسة خصوصية Sekuvo: لا جمع للبيانات، ولا مشاركة لها، ولا إذن إنترنت.",
    h1="سياسة الخصوصية",
    meta=f"التطبيق: <strong>Sekuvo</strong> (com.sekuvo.app) · المطوّر: Ahmet Govercile · تاريخ السريان: {EFFECTIVE}",
    back="← العودة إلى sekuvo.com",
    authoritative="هذا النص ترجمة عن الأصل الإنجليزي. وعند الاختلاف تُعتمد <a href=\"https://sekuvo.com/privacy/\">النسخة الإنجليزية</a>.",
    sections=[
        ("الملخّص",
         "<p><strong>لا يجمع Sekuvo أي بيانات ولا ينقلها ولا يشاركها.</strong> فهو خزنة كلمات مرور تعمل دون اتصال. ولا يطلب التطبيق إذن الإنترنت، لذا يستحيل عليه تقنيًا إرسال بياناتك إلى أي جهة.</p>"),
        ("تخزين البيانات",
         "<p>كل ما تحفظه في Sekuvo (العناوين وأسماء المستخدمين وكلمات المرور والملاحظات وسجل الاستخدام) يبقى على جهازك، مشفَّرًا بمفتاح مشتقّ من كلمة مرورك الرئيسية. ولا يرفع التطبيق شيئًا ولا يزامنه ولا ينسخه إلى أي خادم.</p>"),
        ("جمع البيانات ومشاركتها",
         "<ul><li>لا تُجمع أي بيانات شخصية.</li><li>لا تُشارك أي بيانات مع أطراف أخرى.</li><li>لا يتضمن التطبيق مكتبات تحليلات أو إعلانات أو تتبّع.</li><li>لا يلزم إنشاء حساب لاستخدامه.</li></ul>"),
        ("الأذونات",
         "<ul><li><strong>الكاميرا</strong> — تُستخدم فقط لقراءة رموز QR التي تختار مسحها عند استيراد بياناتك. وتُعالَج الصور على الجهاز ولا تغادره أبدًا.</li><li><strong>القياسات الحيوية</strong> — تُستخدم فقط لفتح الخزنة على جهازك عبر نظام أندرويد الحيوي. ولا يرى Sekuvo بصمتك أو وجهك ولا يخزّنهما إطلاقًا.</li><li><strong>البلوتوث</strong> — يُستخدم فقط حين تطلب صراحةً أن يكتب Sekuvo كلمة مرور في حاسوب قريب بوصفه لوحة مفاتيح بلوتوث. ولا تُرسَل إلا الأحرف التي تختارها، مباشرةً إلى الجهاز المقترن.</li></ul>"),
        ("النسخ الاحتياطية والنقل",
         "<p>لا تحدث النسخ ولا عمليات النقل إلا حين تبدأها أنت، وتنتج ملفًا مشفَّرًا أو رموز QR محمية بكلمة مرور تحدّدها، ولا تُحفَظ أو تُعرَض إلا حيث توجّهها. ولا يرسلها التطبيق إلى أي مكان من تلقاء نفسه.</p>"),
        ("الأطفال",
         "<p>لا يجمع Sekuvo بيانات من أي شخص، بمن فيهم الأطفال.</p>"),
        ("التغييرات",
         "<p>إذا تغيّرت هذه السياسة يومًا، ستُنشر النسخة الجديدة على هذا العنوان مع تاريخ سريان محدَّث.</p>"),
        ("التواصل",
         '<p>للاستفسارات: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["zh"] = dict(
    title="Sekuvo — 隐私政策",
    desc="Sekuvo 隐私政策：不收集数据，不共享数据，无互联网权限。",
    h1="隐私政策",
    meta=f"应用：<strong>Sekuvo</strong> (com.sekuvo.app) · 开发者：Ahmet Govercile · 生效日期：{EFFECTIVE}",
    back="← 返回 sekuvo.com",
    authoritative="本文本译自英文原文。如有差异，以<a href=\"https://sekuvo.com/privacy/\">英文版本</a>为准。",
    sections=[
        ("概要",
         "<p><strong>Sekuvo 不收集、不传输、也不共享任何数据。</strong>它是一款离线密码库。应用不请求互联网权限，因此在技术上无法将你的数据发送到任何地方。</p>"),
        ("数据存储",
         "<p>你在 Sekuvo 中保存的一切（标题、用户名、密码、笔记、使用记录）都留在你的设备上，并用由主密码派生的密钥加密。应用不会将任何内容上传、同步或备份到任何服务器。</p>"),
        ("数据收集与共享",
         "<ul><li>不收集任何个人数据。</li><li>不与第三方共享任何数据。</li><li>不包含任何数据分析、广告或跟踪库。</li><li>使用本应用无需创建账户。</li></ul>"),
        ("权限说明",
         "<ul><li><strong>相机</strong> — 仅用于扫描你选择扫描的二维码，以导入你自己的数据。图像处理在设备本地完成，绝不会离开设备。</li><li><strong>生物识别</strong> — 仅通过 Android 生物识别系统用于在你的设备上解锁密码库。Sekuvo 绝不会查看或存储你的指纹或面部数据。</li><li><strong>蓝牙</strong> — 仅在你明确要求 Sekuvo 以蓝牙键盘的方式向附近电脑输入密码时使用。只会发送你选择的字符，且直接发送给你配对过的设备。</li></ul>"),
        ("备份与传输",
         "<p>备份和传输仅在你主动发起时才会发生，会生成一个由你设置的密码保护的加密文件或二维码，并只保存或显示在你指定的位置。应用绝不会自行将其发送到任何地方。</p>"),
        ("儿童",
         "<p>Sekuvo 不收集任何人（包括儿童）的数据。</p>"),
        ("变更",
         "<p>如果本政策发生变更，新版本将发布在此地址，并附有更新后的生效日期。</p>"),
        ("联系方式",
         '<p>如有疑问，请联系：<a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["fr"] = dict(
    title="Sekuvo — Politique de confidentialité",
    desc="Politique de confidentialité de Sekuvo : aucune donnée collectée, aucune donnée partagée, aucune permission internet.",
    h1="Politique de confidentialité",
    meta=f"Application : <strong>Sekuvo</strong> (com.sekuvo.app) · Développeur : Ahmet Govercile · Date d'entrée en vigueur : {EFFECTIVE}",
    back="← Retour à sekuvo.com",
    authoritative="Ce texte est une traduction de l'original en anglais. En cas de divergence, la <a href=\"https://sekuvo.com/privacy/\">version anglaise</a> prévaut.",
    sections=[
        ("Résumé",
         "<p><strong>Sekuvo ne collecte, ne transmet ni ne partage aucune donnée.</strong> C'est un coffre de mots de passe hors ligne. L'application ne demande pas la permission Internet, elle est donc techniquement incapable d'envoyer tes données où que ce soit.</p>"),
        ("Stockage des données",
         "<p>Tout ce que tu enregistres dans Sekuvo (titres, identifiants, mots de passe, notes, historique d'utilisation) reste sur ton appareil, chiffré avec une clé dérivée de ton mot de passe principal. Rien n'est téléversé, synchronisé ni sauvegardé sur un serveur par l'application.</p>"),
        ("Collecte et partage des données",
         "<ul><li>Aucune donnée personnelle n'est collectée.</li><li>Aucune donnée n'est partagée avec des tiers.</li><li>Aucune bibliothèque d'analyse, de publicité ou de suivi n'est incluse.</li><li>Aucun compte n'est requis pour utiliser l'application.</li></ul>"),
        ("Permissions",
         "<ul><li><strong>Caméra</strong> — utilisée uniquement pour scanner les codes QR que tu choisis de scanner, afin d'importer tes propres données. Les images sont traitées sur l'appareil et ne le quittent jamais.</li><li><strong>Biométrie</strong> — utilisée uniquement pour déverrouiller le coffre sur ton appareil, via le système biométrique d'Android. Sekuvo ne voit ni ne stocke jamais ton empreinte ou ton visage.</li><li><strong>Bluetooth</strong> — utilisé uniquement quand tu demandes explicitement à Sekuvo de saisir un mot de passe sur un ordinateur à proximité, en tant que clavier Bluetooth. Seuls les caractères que tu choisis d'envoyer sont transmis, directement à l'appareil que tu as appairé.</li></ul>"),
        ("Sauvegardes et transferts",
         "<p>Les sauvegardes et transferts n'ont lieu que lorsque tu les déclenches, produisent un fichier chiffré ou des codes QR protégés par un mot de passe que tu définis, et ne sont enregistrés ou affichés que là où tu les diriges. L'application ne les envoie jamais nulle part de sa propre initiative.</p>"),
        ("Enfants",
         "<p>Sekuvo ne collecte de données de personne, y compris des enfants.</p>"),
        ("Modifications",
         "<p>Si cette politique venait à changer, la nouvelle version serait publiée à cette adresse avec une date d'entrée en vigueur mise à jour.</p>"),
        ("Contact",
         '<p>Questions : <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["bn"] = dict(
    title="Sekuvo — গোপনীয়তা নীতি",
    desc="Sekuvo গোপনীয়তা নীতি: কোনো তথ্য সংগ্রহ করা হয় না, কোনো তথ্য শেয়ার করা হয় না, ইন্টারনেট অনুমতি নেই।",
    h1="গোপনীয়তা নীতি",
    meta=f"অ্যাপ: <strong>Sekuvo</strong> (com.sekuvo.app) · ডেভেলপার: Ahmet Govercile · কার্যকর তারিখ: {EFFECTIVE}",
    back="← sekuvo.com-এ ফিরে যান",
    authoritative="এই লেখাটি ইংরেজি মূল থেকে অনুবাদ করা হয়েছে। কোনো পার্থক্য থাকলে <a href=\"https://sekuvo.com/privacy/\">ইংরেজি সংস্করণ</a> কার্যকর থাকবে।",
    sections=[
        ("সারসংক্ষেপ",
         "<p><strong>Sekuvo কোনো তথ্য সংগ্রহ, প্রেরণ বা শেয়ার করে না।</strong> এটি একটি অফলাইন পাসওয়ার্ড ভল্ট। অ্যাপটি ইন্টারনেট অনুমতি চায় না, তাই কারিগরিভাবে এটি আপনার তথ্য কোথাও পাঠাতে অক্ষম।</p>"),
        ("তথ্য সংরক্ষণ",
         "<p>Sekuvo-তে আপনি যা সংরক্ষণ করেন (শিরোনাম, ইউজারনেম, পাসওয়ার্ড, নোট, ব্যবহারের ইতিহাস) সবকিছু আপনার ডিভাইসেই থাকে, আপনার মূল পাসওয়ার্ড থেকে তৈরি একটি কী দিয়ে এনক্রিপ্ট করা। অ্যাপটি কোনো তথ্য কোনো সার্ভারে আপলোড, সিঙ্ক বা ব্যাকআপ করে না।</p>"),
        ("তথ্য সংগ্রহ ও শেয়ারিং",
         "<ul><li>কোনো ব্যক্তিগত তথ্য সংগ্রহ করা হয় না।</li><li>তৃতীয় পক্ষের সাথে কোনো তথ্য শেয়ার করা হয় না।</li><li>কোনো অ্যানালিটিক্স, বিজ্ঞাপন বা ট্র্যাকিং লাইব্রেরি নেই।</li><li>ব্যবহারের জন্য কোনো অ্যাকাউন্ট প্রয়োজন নেই।</li></ul>"),
        ("অনুমতি",
         "<ul><li><strong>ক্যামেরা</strong> — শুধু আপনার স্ক্যান করা QR কোড পড়তে, নিজের তথ্য ইম্পোর্ট করার জন্য ব্যবহৃত হয়। ছবি ডিভাইসেই প্রক্রিয়া করা হয়, কখনো বাইরে যায় না।</li><li><strong>বায়োমেট্রিক্স</strong> — শুধু আপনার ডিভাইসে, Android-এর বায়োমেট্রিক সিস্টেমের মাধ্যমে ভল্ট আনলক করতে ব্যবহৃত হয়। Sekuvo কখনো আপনার ফিঙ্গারপ্রিন্ট বা মুখের তথ্য দেখে না বা সংরক্ষণ করে না।</li><li><strong>ব্লুটুথ</strong> — শুধু আপনি স্পষ্টভাবে Sekuvo-কে কাছের কোনো কম্পিউটারে ব্লুটুথ কীবোর্ড হিসেবে পাসওয়ার্ড টাইপ করতে বললে ব্যবহৃত হয়। শুধু আপনার পাঠানোর জন্য বেছে নেওয়া অক্ষরগুলো, সরাসরি আপনার জোড়া লাগানো ডিভাইসে পাঠানো হয়।</li></ul>"),
        ("ব্যাকআপ ও ট্রান্সফার",
         "<p>ব্যাকআপ ও ট্রান্সফার শুধু আপনি শুরু করলেই ঘটে, আপনার নির্ধারিত পাসওয়ার্ড দিয়ে সুরক্ষিত একটি এনক্রিপ্টেড ফাইল বা QR কোড তৈরি করে, এবং শুধু আপনার নির্দেশিত জায়গায় সংরক্ষিত বা দেখানো হয়। অ্যাপটি নিজে থেকে এগুলো কোথাও পাঠায় না।</p>"),
        ("শিশু",
         "<p>Sekuvo শিশুসহ কারও কাছ থেকেই কোনো তথ্য সংগ্রহ করে না।</p>"),
        ("পরিবর্তন",
         "<p>এই নীতি কখনো পরিবর্তিত হলে, নতুন সংস্করণটি হালনাগাদ কার্যকর তারিখসহ এই ঠিকানায় প্রকাশিত হবে।</p>"),
        ("যোগাযোগ",
         '<p>প্রশ্নের জন্য: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["pt"] = dict(
    title="Sekuvo — Política de Privacidade",
    desc="Política de privacidade do Sekuvo: nenhum dado é coletado, nenhum dado é compartilhado, sem permissão de internet.",
    h1="Política de Privacidade",
    meta=f"Aplicativo: <strong>Sekuvo</strong> (com.sekuvo.app) · Desenvolvedor: Ahmet Govercile · Data de vigência: {EFFECTIVE}",
    back="← Voltar para sekuvo.com",
    authoritative="Este texto é uma tradução do original em inglês. Em caso de divergência, prevalece a <a href=\"https://sekuvo.com/privacy/\">versão em inglês</a>.",
    sections=[
        ("Resumo",
         "<p><strong>O Sekuvo não coleta, transmite nem compartilha nenhum dado.</strong> É um cofre de senhas offline. O aplicativo não pede a permissão de Internet, então é tecnicamente incapaz de enviar seus dados para qualquer lugar.</p>"),
        ("Armazenamento de dados",
         "<p>Tudo o que você salva no Sekuvo (títulos, usuários, senhas, notas, histórico de uso) fica no seu dispositivo, criptografado com uma chave derivada da sua senha principal. Nada é enviado, sincronizado ou salvo em backup em nenhum servidor pelo aplicativo.</p>"),
        ("Coleta e compartilhamento de dados",
         "<ul><li>Nenhum dado pessoal é coletado.</li><li>Nenhum dado é compartilhado com terceiros.</li><li>Nenhuma biblioteca de análise, publicidade ou rastreamento está incluída.</li><li>Nenhuma conta é necessária para usar o aplicativo.</li></ul>"),
        ("Permissões",
         "<ul><li><strong>Câmera</strong> — usada apenas para escanear códigos QR que você escolhe escanear, para importar seus próprios dados. As imagens são processadas no dispositivo e nunca saem dele.</li><li><strong>Biometria</strong> — usada apenas para desbloquear o cofre no seu dispositivo, pelo sistema biométrico do Android. O Sekuvo nunca vê nem armazena sua impressão digital ou dados do rosto.</li><li><strong>Bluetooth</strong> — usado apenas quando você pede explicitamente ao Sekuvo para digitar uma senha em um computador próximo, atuando como teclado Bluetooth. Apenas os caracteres que você escolhe enviar são transmitidos, diretamente ao dispositivo pareado.</li></ul>"),
        ("Backups e transferências",
         "<p>Backups e transferências só acontecem quando você os inicia, produzem um arquivo criptografado ou códigos QR protegidos por uma senha que você define, e são salvos ou exibidos apenas onde você indicar. O aplicativo nunca os envia para lugar nenhum por conta própria.</p>"),
        ("Crianças",
         "<p>O Sekuvo não coleta dados de ninguém, incluindo crianças.</p>"),
        ("Alterações",
         "<p>Se esta política mudar algum dia, a nova versão será publicada neste endereço com uma data de vigência atualizada.</p>"),
        ("Contato",
         '<p>Dúvidas: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

P["ru"] = dict(
    title="Sekuvo — Политика конфиденциальности",
    desc="Политика конфиденциальности Sekuvo: данные не собираются, не передаются и не используются совместно, разрешение на интернет отсутствует.",
    h1="Политика конфиденциальности",
    meta=f"Приложение: <strong>Sekuvo</strong> (com.sekuvo.app) · Разработчик: Ahmet Govercile · Дата вступления в силу: {EFFECTIVE}",
    back="← Назад на sekuvo.com",
    authoritative="Этот текст является переводом английского оригинала. В случае расхождений приоритет имеет <a href=\"https://sekuvo.com/privacy/\">версия на английском языке</a>.",
    sections=[
        ("Краткое содержание",
         "<p><strong>Sekuvo не собирает, не передаёт и не делится никакими данными.</strong> Это офлайн-хранилище паролей. Приложение не запрашивает разрешение на интернет, поэтому технически неспособно отправить ваши данные куда-либо.</p>"),
        ("Хранение данных",
         "<p>Всё, что вы сохраняете в Sekuvo (названия, имена пользователей, пароли, заметки, история использования), остаётся на вашем устройстве, зашифрованное ключом, полученным из вашего основного пароля. Приложение ничего не отправляет, не синхронизирует и не резервирует ни на один сервер.</p>"),
        ("Сбор и передача данных",
         "<ul><li>Персональные данные не собираются.</li><li>Данные не передаются третьим лицам.</li><li>Библиотеки аналитики, рекламы или отслеживания не включены.</li><li>Для использования приложения аккаунт не требуется.</li></ul>"),
        ("Разрешения",
         "<ul><li><strong>Камера</strong> — используется только для сканирования QR-кодов, которые вы решаете сканировать, чтобы импортировать собственные данные. Изображения обрабатываются на устройстве и никогда его не покидают.</li><li><strong>Биометрия</strong> — используется только для разблокировки хранилища на вашем устройстве через биометрическую систему Android. Sekuvo никогда не видит и не хранит ваш отпечаток пальца или данные лица.</li><li><strong>Bluetooth</strong> — используется только когда вы явно просите Sekuvo ввести пароль на ближайшем компьютере, выступая в роли Bluetooth-клавиатуры. Передаются только выбранные вами символы, напрямую сопряжённому устройству.</li></ul>"),
        ("Резервные копии и переносы",
         "<p>Резервное копирование и перенос происходят только когда вы их запускаете, создают зашифрованный файл или QR-коды, защищённые заданным вами паролем, и сохраняются или показываются только там, куда вы укажете. Приложение никогда не отправляет их куда-либо самостоятельно.</p>"),
        ("Дети",
         "<p>Sekuvo не собирает данные ни от кого, включая детей.</p>"),
        ("Изменения",
         "<p>Если эта политика когда-либо изменится, новая версия будет опубликована по этому адресу с обновлённой датой вступления в силу.</p>"),
        ("Контакты",
         '<p>Вопросы: <a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></p>'),
    ],
)

POLICY_PAGE = """<!DOCTYPE html>
<html lang="{lang}" dir="{dir}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="/favicon.png" sizes="32x32">
<link rel="icon" href="/img/icon-512.png" sizes="512x512">
<link rel="apple-touch-icon" href="/img/icon-180.png">
{alternates}
<link rel="stylesheet" href="{font_url}">
<style>{style}
  .prose {{ max-width: 44rem; padding: 3rem 0 4rem; }}
  .prose h1 {{ font-size: clamp(2rem, 4vw, 2.6rem); font-weight: 640; }}
  .prose h2 {{ font-size: 1.2rem; font-weight: 600; margin: 2.4rem 0 .6rem; }}
  .prose p, .prose li {{ color: var(--muted); }}
  .prose ul {{ padding-inline-start: 1.2rem; }}
  .prose li {{ margin-bottom: .5rem; }}
  .prose strong {{ color: var(--ink); }}
  .meta {{ font-family: "IBM Plex Mono", monospace; font-size: .8rem; color: var(--muted); margin-top: .8rem; }}
  .note {{ border: 1px solid var(--line); border-radius: 6px; padding: .9rem 1.1rem; font-size: .88rem; color: var(--muted); margin-top: 1.6rem; }}
  .back {{ display: inline-block; margin-top: 2.6rem; font-size: .9rem; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <span class="brand">Sekuvo</span>
    <nav><a href="{guide_url}">{guide_label}</a> <a href="{home_url}">sekuvo.com</a></nav>
  </header>
  <div class="langs">{langs}</div>

  <div class="prose">
    <h1>{h1}</h1>
    <p class="meta">{meta}</p>
    {note}
    {body}
    <a class="back" href="{home_url}">{back}</a>
  </div>

  <footer>
    <span>© 2026 Ahmet Govercile · Sekuvo</span>
    <span dir="ltr"><a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></span>
  </footer>
</div>
</body>
</html>
"""


def build_policies():
    root = pathlib.Path(__file__).parent
    for code in ORDER:
        t, pol = L[code], P[code]
        font_url, display, body_face = FONTS[t["script"]]
        style = STYLE.replace("__DISPLAY__", display).replace("__BODY__", body_face)

        alternates = "\n".join(
            f'<link rel="alternate" hreflang="{L[c]["lang"]}" href="{SITE}/{L[c]["path"]}privacy/">'
            for c in ORDER
        ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/privacy/">'

        langs = " ·\n    ".join(
            (f'<a class="here" href="{SITE}/{L[c]["path"]}privacy/" lang="{L[c]["lang"]}">{L[c]["name"]}</a>'
             if c == code else
             f'<a href="{SITE}/{L[c]["path"]}privacy/" lang="{L[c]["lang"]}">{L[c]["name"]}</a>')
            for c in ORDER
        )

        note = f'<p class="note">{pol["authoritative"]}</p>' if pol["authoritative"] else ""
        body = "".join(f"<h2>{h}</h2>{b}" for h, b in pol["sections"])

        html = POLICY_PAGE.format(
            lang=t["lang"], dir=t["dir"], desc=pol["desc"], title=pol["title"],
            alternates=alternates, font_url=font_url, style=style, langs=langs,
            home_url=f"{SITE}/{t['path']}", h1=pol["h1"], meta=pol["meta"],
            guide_url=f"{SITE}/{t['path']}guide/", guide_label=G[code]["nav_label"],
            note=note, body=body, back=pol["back"],
        )

        out = root / t["path"] / "privacy" / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"{out.relative_to(root)}  ({len(html):,} bytes)")


# ─────────────────────────────────────────────────────────────────────────────
# Guide pages. Content lives in guide.py; this only renders it.
# ─────────────────────────────────────────────────────────────────────────────

GUIDE_PAGE = """<!DOCTYPE html>
<html lang="{lang}" dir="{dir}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="/favicon.png" sizes="32x32">
<link rel="icon" href="/img/icon-512.png" sizes="512x512">
<link rel="apple-touch-icon" href="/img/icon-180.png">
{alternates}
<link rel="stylesheet" href="{font_url}">
<style>{style}
  .prose {{ max-width: 46rem; padding: 3rem 0 4rem; }}
  .prose h1 {{ font-size: clamp(2rem, 4vw, 2.6rem); font-weight: 640; }}
  .prose h2 {{ font-size: 1.35rem; font-weight: 600; margin: 3rem 0 .7rem; padding-top: 1.6rem; border-top: 1px solid var(--line); }}
  .prose h2:first-of-type {{ border-top: none; padding-top: 0; }}
  .prose h3 {{ font-size: 1.02rem; font-weight: 600; margin: 1.8rem 0 .5rem; color: var(--brass); }}
  .prose p, .prose li {{ color: var(--muted); }}
  .prose ul, .prose ol {{ padding-inline-start: 1.4rem; }}
  .prose li {{ margin-bottom: .55rem; }}
  .prose strong {{ color: var(--ink); }}
  .prose code {{ font-family: "IBM Plex Mono", monospace; font-size: .85em; background: var(--surface); border: 1px solid var(--line); border-radius: 3px; padding: .1em .35em; }}
  .lede-big {{ font-size: 1.05rem; color: var(--muted); margin: 1rem 0 2rem; }}
  .toc {{ background: var(--surface); border: 1px solid var(--line); border-radius: 6px; padding: 1.2rem 1.4rem; margin-bottom: 1rem; }}
  .toc ol {{ margin: 0; padding-inline-start: 1.2rem; columns: 2; column-gap: 2rem; }}
  .toc li {{ margin-bottom: .35rem; font-size: .92rem; }}
  .back {{ display: inline-block; margin-top: 2.6rem; font-size: .9rem; }}
  .shots {{ display: flex; gap: 1.4rem; flex-wrap: wrap; margin: 1.6rem 0 .4rem; }}
  .shots figure {{ margin: 0; flex: 0 1 15rem; }}
  .shots img {{
    width: 100%; height: auto; display: block;
    border: 1px solid var(--line); border-radius: 10px;
    background: var(--surface);
  }}
  .shots figcaption {{ font-size: .82rem; color: var(--muted); margin-top: .6rem; line-height: 1.5; }}
  @media (max-width: 620px) {{ .toc ol {{ columns: 1; }} .shots figure {{ flex: 1 1 100%; }} }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <span class="brand">Sekuvo</span>
    <nav><a href="{privacy_url}">{privacy_label}</a> <a href="{home_url}">sekuvo.com</a></nav>
  </header>
  <div class="langs">{langs}</div>

  <div class="prose">
    <h1>{h1}</h1>
    <p class="lede-big">{lede}</p>
    <nav class="toc"><ol>{toc}</ol></nav>
    {body}
    <a class="back" href="{home_url}">{back}</a>
  </div>

  <footer>
    <span>© 2026 Ahmet Govercile · Sekuvo</span>
    <span dir="ltr"><a href="mailto:contact@sekuvo.com">contact@sekuvo.com</a></span>
  </footer>
</div>
</body>
</html>
"""


def build_guides():
    root = pathlib.Path(__file__).parent
    for code in ORDER:
        t, g = L[code], G[code]
        font_url, display, body_face = FONTS[t["script"]]
        style = STYLE.replace("__DISPLAY__", display).replace("__BODY__", body_face)

        alternates = "\n".join(
            f'<link rel="alternate" hreflang="{L[c]["lang"]}" href="{SITE}/{L[c]["path"]}guide/">'
            for c in ORDER
        ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/guide/">'

        langs = " ·\n    ".join(
            (f'<a class="here" href="{SITE}/{L[c]["path"]}guide/" lang="{L[c]["lang"]}">{L[c]["name"]}</a>'
             if c == code else
             f'<a href="{SITE}/{L[c]["path"]}guide/" lang="{L[c]["lang"]}">{L[c]["name"]}</a>')
            for c in ORDER
        )

        toc = "".join(f'<li><a href="#{sid}">{h2}</a></li>' for sid, h2, _ in g["sections"])
        caps = CAPTIONS[code]

        def figures(sid):
            files = SHOTS.get(sid)
            if not files:
                return ""
            items = "".join(
                f'<figure><img src="{SITE}/img/{f}" alt="{caps[f]}" '
                f'loading="lazy" width="405" height="900">'
                f'<figcaption>{caps[f]}</figcaption></figure>'
                for f in files
            )
            return f'<div class="shots">{items}</div>'

        body = "".join(
            f'<h2 id="{sid}">{h2}</h2>' + "".join(blocks) + figures(sid)
            for sid, h2, blocks in g["sections"]
        )

        html = GUIDE_PAGE.format(
            lang=t["lang"], dir=t["dir"], desc=g["desc"], title=g["title"],
            alternates=alternates, font_url=font_url, style=style, langs=langs,
            home_url=f"{SITE}/{t['path']}",
            privacy_url=f"{SITE}/{t['path']}privacy/", privacy_label=t["nav"][3],
            h1=g["h1"], lede=g["lede"], toc=toc, body=body, back=g["back"],
        )

        out = root / t["path"] / "guide" / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"{out.relative_to(root)}  ({len(html):,} bytes)")


if __name__ == "__main__":
    build()
    build_policies()
    build_guides()

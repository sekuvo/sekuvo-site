#!/usr/bin/env python3
"""Builds sekuvo.com from one source of truth.

Every language page comes from the same template, so a copy change lands in
all five at once instead of drifting between hand-edited files. Run:

    python3 build.py

Output: index.html (en) and tr/, es/, hi/, ar/ index files.
"""
import pathlib

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
    dl_tools_p="The QR transfer tools are downloads, not web pages: they run entirely on your machine, and this site never asks for a secret.",
    dl_tools_note="github.com → Releases · verify the published SHA-256",
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
    dl_tools_p="QR aktarım araçları web sayfası değil, indirilen dosyadır: tamamen kendi makinende çalışır ve bu site senden asla bir sır istemez.",
    dl_tools_note="github.com → Releases · yayınlanan SHA-256'yı doğrula",
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
    dl_tools_p="Las herramientas de transferencia por QR son descargas, no páginas web: funcionan por completo en tu máquina, y este sitio nunca te pide un secreto.",
    dl_tools_note="github.com → Releases · verifica el SHA-256 publicado",
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
    dl_tools_p="QR ट्रांसफ़र टूल वेब पेज नहीं, डाउनलोड हैं: वे पूरी तरह आपकी मशीन पर चलते हैं, और यह साइट कभी कोई राज़ नहीं माँगती।",
    dl_tools_note="github.com → Releases · प्रकाशित SHA-256 जाँचें",
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
    dl_tools_p="أدوات النقل عبر QR ملفات تُنزَّل لا صفحات ويب: تعمل بالكامل على جهازك، وهذا الموقع لا يطلب منك سرًّا أبدًا.",
    dl_tools_note="github.com → Releases · تحقّق من بصمة SHA-256 المنشورة",
    footer="© 2026 Ahmet Govercile · Sekuvo — <em>خزنتك الآمنة.</em>",
)

ORDER = ["en", "tr", "es", "hi", "ar"]

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
      <a href="{site}/privacy/">{nav3}</a>
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
        <a class="btn ghost" href="{site}/privacy/">{btn_priv}</a>
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
      </div>
      <div>
        <h3>{dl_tools_h}</h3>
        <p>{dl_tools_p}</p>
        <p class="mono-note" dir="ltr">{dl_tools_note}</p>
      </div>
    </div>
  </section>

  <footer>
    <span>{footer}</span>
    <span dir="ltr">
      <a href="{github}">GitHub</a> ·
      <a href="{site}/privacy/">{nav3}</a> ·
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
            dl_tools_note=t["dl_tools_note"], footer=t["footer"],
        )

        out = root / t["path"] / "index.html" if t["path"] else root / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"{out.relative_to(root)}  ({len(html):,} bytes)")


if __name__ == "__main__":
    build()

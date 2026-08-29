# -*- coding: utf-8 -*-
"""Aktar içerikleri: ana sayfadaki aktar.html bölümü (AK) ve gömülü
Zarf → QR sayfası (A), 16 dilde.

Gömülü sayfa BİLEREK şifreleme yapmaz: yalnız zaten şifrelenmiş bir zarfı
QR karelerine çevirir. Böylece "bu site senden asla bir sır istemez" sözü
bozulmaz — düz metin sır hiçbir zaman bu siteye girmez. Zarfı kullanıcı
kendi makinesinde, aşağıdaki betikle üretir (docs/kendi-zarfini-uret.md
ile aynı biçim: PBKDF2-HMAC-SHA256 310k + AES-256-GCM).
"""

# Komut blokları dilden bağımsızdır (kod evrenseldir); yorumlar İngilizce.

VERIFY_CMDS = """# macOS / Linux
shasum -a 256 aktar.html

# Windows (PowerShell / cmd)
certutil -hashfile aktar.html SHA256"""

CMD_UNIX = """# macOS / Linux
# generate a password (letters+digits, ~119 bits):
python3 -c "import secrets,string; print(''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(20)))"

pip3 install cryptography
python3 zarf-uret.py "Server SSH" > zarf.json   # paste the secret, then Ctrl-D
pbcopy < zarf.json                              # macOS; Linux: xclip -sel clip < zarf.json"""

CMD_WIN = """# Windows (PowerShell)
# generate a password (letters+digits, ~119 bits):
python -c "import secrets,string; print(''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(20)))"

pip install cryptography
python zarf-uret.py "Server SSH" > zarf.json    # paste the secret, then Ctrl-Z + Enter
Get-Content zarf.json | Set-Clipboard"""

PY_SCRIPT = '''#!/usr/bin/env python3
# zarf-uret.py - reads the secret from stdin, writes a Sekuvo envelope to stdout.
# Usage: python3 zarf-uret.py "Title" > zarf.json   (paste the secret, then Ctrl-D)
# Requires: pip install cryptography
import sys, os, json, time, base64, hashlib, getpass
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

title = sys.argv[1] if len(sys.argv) > 1 else "Transfer"
secret = sys.stdin.read()
password = getpass.getpass("Envelope password (ASCII, generated): ")
assert password.isascii() and len(password) >= 8, "ASCII and at least 8 characters"

now = int(time.time() * 1000)
payload = json.dumps({"entries": [{
    "type": "NOTE", "title": title,
    "createdAt": now, "updatedAt": now, "quick": False,
    "data": {"notes": secret},
}]}, ensure_ascii=False)

salt = os.urandom(16)
key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 310_000, 32)
iv = os.urandom(12)
blob = iv + AESGCM(key).encrypt(iv, payload.encode(), None)
print(json.dumps({
    "app": "vault", "version": 1,
    "kdf": {"algo": "PBKDF2WithHmacSHA256", "iterations": 310_000,
            "salt": base64.b64encode(salt).decode()},
    "cipher": "AES-256-GCM",
    "data": base64.b64encode(blob).decode(),
}))'''

# Sayfanın uygulama JS'i. __TEXTS__ derleme sırasında dil sözlüğüyle değişir.
# Kare biçimi uygulamadaki QrTransfer ile birebir: VLT1|i/n|P·Z|base64,
# parça 1200 karakter, çok karede sürüm 25 sabit, hata düzeltme "L",
# döngü 1200 ms (tools/aktar.html ile aynı değerler).
AKTAR_JS = r"""
"use strict";
const T = __TEXTS__;
const $ = (id) => document.getElementById(id);
function b64(bytes) { let s = ""; for (const b of bytes) s += String.fromCharCode(b); return btoa(s); }

const QR_CHUNK = 1200;
async function frames(envText) {
  const raw = new TextEncoder().encode(envText);
  let flag = "P", bytes = raw;
  if (typeof CompressionStream !== "undefined") {
    try {
      const cs = new CompressionStream("deflate-raw");
      const z = new Uint8Array(await new Response(new Blob([raw]).stream().pipeThrough(cs)).arrayBuffer());
      if (z.length < raw.length) { flag = "Z"; bytes = z; }
    } catch (_) {}
  }
  const data = b64(bytes), parts = [];
  for (let i = 0; i < data.length; i += QR_CHUNK) parts.push(data.slice(i, i + QR_CHUNK));
  const n = parts.length || 1;
  return parts.map((p, i) => "VLT1|" + (i + 1) + "/" + n + "|" + flag + "|" + p);
}

let loop = null;
function show(fr) {
  if (loop) { clearInterval(loop); loop = null; }
  const ver = fr.length > 1 ? 25 : 0;
  const draw = (t) => {
    const q = qrcode(ver, "L"); q.addData(t); q.make();
    $("qr").innerHTML = q.createSvgTag({ cellSize: 5, margin: 3 });
  };
  if (fr.length === 1) { draw(fr[0]); $("info").textContent = T.frame_single; return; }
  let i = 0;
  const step = () => {
    draw(fr[i]);
    $("info").textContent = T.frame_multi
      .replace("%1", i + 1).replace("%2", fr.length)
      .replace("%3", (fr.length * 1.2).toFixed(0));
    i = (i + 1) % fr.length;
  };
  step(); loop = setInterval(step, 1200);
}

function isEnvelope(s) {
  try {
    const o = JSON.parse(s);
    return !!o && o.app === "vault" && !!o.kdf && !!o.cipher && typeof o.data === "string";
  } catch (_) { return false; }
}

$("go").addEventListener("click", async () => {
  $("err").textContent = ""; $("qr").innerHTML = ""; $("info").textContent = "";
  const v = $("env").value.trim();
  if (!v) { $("err").textContent = T.err_empty; return; }
  if (!isEnvelope(v)) { $("err").textContent = T.err_invalid; return; }
  show(await frames(v));
});

// GİZLİLİK: yazım denetimi alan içeriğini buluta gönderebilir — kapat.
for (const el of document.querySelectorAll("textarea")) {
  el.setAttribute("spellcheck", "false");
  el.setAttribute("autocorrect", "off");
  el.setAttribute("autocapitalize", "off");
  el.setAttribute("autocomplete", "off");
}
"""

# ── Ana sayfa: aktar.html bölümü ────────────────────────────────────────────

AK = {}

AK["en"] = dict(
    ak_h="aktar.html: download, verify, use",
    ak_steps=[
        "Open the project's Releases page and download aktar.html.",
        "Check its SHA-256 against the value published next to it — the commands shown here print it.",
        "Open the file from your own disk: the address bar shows file://, not a website.",
        "Paste your content, set a transfer password, and encrypt — the envelope comes out as QR codes or text.",
        "On the phone: Sekuvo → + → Import via QR, scan, and enter the same password.",
    ],
    ak_embed_p="Rather not run any encryption in a browser? Encrypt in your own terminal instead, and use the embedded QR page — it accepts only the encrypted envelope, never a raw secret.",
    ak_embed_link="Open the envelope → QR page",
)

AK["tr"] = dict(
    ak_h="aktar.html: indir, doğrula, kullan",
    ak_steps=[
        "Projenin Releases sayfasını aç ve aktar.html'i indir.",
        "SHA-256'sını yanında yayımlanan değerle karşılaştır — buradaki komutlar onu yazdırır.",
        "Dosyayı kendi diskinden aç: adres çubuğunda bir site değil file:// görünür.",
        "İçeriğini yapıştır, bir aktarım parolası belirle ve şifrele — zarf QR kod ya da metin olarak çıkar.",
        "Telefonda: Sekuvo → + → QR ile aktar, tara ve aynı parolayı gir.",
    ],
    ak_embed_p="Tarayıcıda hiç şifreleme çalıştırmak istemiyor musun? Sırrı kendi terminalinde şifrele ve gömülü QR sayfasını kullan — o sayfa yalnız şifreli zarfı kabul eder, asla çıplak bir sır istemez.",
    ak_embed_link="Zarf → QR sayfasını aç",
)

AK["es"] = dict(
    ak_h="aktar.html: descarga, verifica, usa",
    ak_steps=[
        "Abre la página de Releases del proyecto y descarga aktar.html.",
        "Comprueba su SHA-256 con el valor publicado al lado — los comandos de aquí lo imprimen.",
        "Abre el archivo desde tu propio disco: la barra de direcciones muestra file://, no un sitio web.",
        "Pega tu contenido, define una contraseña de transferencia y cifra — el sobre sale como códigos QR o texto.",
        "En el teléfono: Sekuvo → + → Importar por QR, escanea e introduce la misma contraseña.",
    ],
    ak_embed_p="¿Prefieres no ejecutar ningún cifrado en un navegador? Cifra en tu propia terminal y usa la página QR integrada: solo acepta el sobre cifrado, nunca un secreto en claro.",
    ak_embed_link="Abrir la página sobre → QR",
)

AK["hi"] = dict(
    ak_h="aktar.html: डाउनलोड करें, सत्यापित करें, इस्तेमाल करें",
    ak_steps=[
        "प्रोजेक्ट का Releases पेज खोलें और aktar.html डाउनलोड करें।",
        "इसका SHA-256 पास में प्रकाशित मान से मिलाएँ — यहाँ दिए कमांड उसे प्रिंट करते हैं।",
        "फ़ाइल को अपनी ही डिस्क से खोलें: एड्रेस बार में file:// दिखता है, कोई वेबसाइट नहीं।",
        "अपनी सामग्री चिपकाएँ, एक ट्रांसफ़र पासवर्ड सेट करें और एन्क्रिप्ट करें — लिफ़ाफ़ा QR कोड या टेक्स्ट के रूप में निकलता है।",
        "फ़ोन पर: Sekuvo → + → QR से आयात, स्कैन करें और वही पासवर्ड डालें।",
    ],
    ak_embed_p="ब्राउज़र में कोई एन्क्रिप्शन नहीं चलाना चाहते? अपने ही टर्मिनल में एन्क्रिप्ट करें और एम्बेडेड QR पेज इस्तेमाल करें — वह केवल एन्क्रिप्टेड लिफ़ाफ़ा स्वीकार करता है, कभी कोई खुला रहस्य नहीं।",
    ak_embed_link="लिफ़ाफ़ा → QR पेज खोलें",
)

AK["ar"] = dict(
    ak_h="aktar.html: نزّل، تحقّق، استخدم",
    ak_steps=[
        "افتح صفحة Releases الخاصة بالمشروع ونزّل aktar.html.",
        "قارن بصمته SHA-256 بالقيمة المنشورة بجانبه — الأوامر هنا تطبعها.",
        "افتح الملف من قرصك الخاص: يظهر في شريط العنوان file:// لا موقع ويب.",
        "الصق محتواك، حدّد كلمة مرور للنقل وشفّر — يخرج المظروف كرموز QR أو نصًّا.",
        "على الهاتف: Sekuvo → + → استيراد عبر QR، امسح وأدخل كلمة المرور نفسها.",
    ],
    ak_embed_p="أتفضّل ألّا تشغّل أي تشفير في المتصفح؟ شفّر في طرفيتك الخاصة واستخدم صفحة QR المدمجة — فهي لا تقبل إلا المظروف المشفَّر، ولا تطلب سرًّا مكشوفًا أبدًا.",
    ak_embed_link="افتح صفحة المظروف → QR",
)

AK["zh"] = dict(
    ak_h="获取 aktar.html:下载、校验、使用",
    ak_steps=[
        "打开项目的 Releases 页面并下载 aktar.html。",
        "用旁边公布的值核对其 SHA-256 —— 这里的命令会打印它。",
        "从你自己的磁盘打开文件:地址栏显示 file://,而不是网站。",
        "粘贴内容、设置传输密码并加密 —— 信封以二维码或文本形式输出。",
        "在手机上:Sekuvo → + → 通过二维码导入,扫描并输入相同的密码。",
    ],
    ak_embed_p="完全不想在浏览器里运行加密?在你自己的终端里加密,然后使用内嵌的二维码页面 —— 它只接受加密信封,绝不接受明文秘密。",
    ak_embed_link="打开 信封 → 二维码 页面",
)

AK["fr"] = dict(
    ak_h="aktar.html : télécharge, vérifie, utilise",
    ak_steps=[
        "Ouvre la page Releases du projet et télécharge aktar.html.",
        "Compare son SHA-256 à la valeur publiée à côté — les commandes ci-contre l'affichent.",
        "Ouvre le fichier depuis ton propre disque : la barre d'adresse montre file://, pas un site web.",
        "Colle ton contenu, définis un mot de passe de transfert et chiffre — l'enveloppe sort en codes QR ou en texte.",
        "Sur le téléphone : Sekuvo → + → Importer via QR, scanne et saisis le même mot de passe.",
    ],
    ak_embed_p="Tu préfères ne lancer aucun chiffrement dans un navigateur ? Chiffre dans ton propre terminal et utilise la page QR intégrée — elle n'accepte que l'enveloppe chiffrée, jamais un secret en clair.",
    ak_embed_link="Ouvrir la page enveloppe → QR",
)

AK["bn"] = dict(
    ak_h="aktar.html: ডাউনলোড, যাচাই, ব্যবহার",
    ak_steps=[
        "প্রজেক্টের Releases পৃষ্ঠা খুলুন এবং aktar.html ডাউনলোড করুন।",
        "এর SHA-256 পাশে প্রকাশিত মানের সাথে মিলিয়ে দেখুন — এখানকার কমান্ডগুলো সেটি প্রিন্ট করে।",
        "ফাইলটি নিজের ডিস্ক থেকে খুলুন: অ্যাড্রেস বারে দেখাবে file://, কোনো ওয়েবসাইট নয়।",
        "আপনার বিষয়বস্তু পেস্ট করুন, একটি ট্রান্সফার পাসওয়ার্ড দিন এবং এনক্রিপ্ট করুন — এনভেলপটি QR কোড বা টেক্সট হিসেবে বেরোয়।",
        "ফোনে: Sekuvo → + → QR দিয়ে ইম্পোর্ট করুন, স্ক্যান করুন এবং একই পাসওয়ার্ড দিন।",
    ],
    ak_embed_p="ব্রাউজারে কোনো এনক্রিপশনই চালাতে চান না? নিজের টার্মিনালে এনক্রিপ্ট করুন এবং এমবেডেড QR পৃষ্ঠাটি ব্যবহার করুন — সেটি কেবল এনক্রিপ্টেড এনভেলপ নেয়, কখনো খোলা গোপন তথ্য নয়।",
    ak_embed_link="এনভেলপ → QR পৃষ্ঠা খুলুন",
)

AK["pt"] = dict(
    ak_h="aktar.html: baixe, verifique, use",
    ak_steps=[
        "Abra a página de Releases do projeto e baixe o aktar.html.",
        "Confira o SHA-256 com o valor publicado ao lado — os comandos aqui o imprimem.",
        "Abra o arquivo do seu próprio disco: a barra de endereço mostra file://, não um site.",
        "Cole seu conteúdo, defina uma senha de transferência e criptografe — o envelope sai como códigos QR ou texto.",
        "No telefone: Sekuvo → + → Importar por QR, escaneie e digite a mesma senha.",
    ],
    ak_embed_p="Prefere não executar nenhuma criptografia em um navegador? Criptografe no seu próprio terminal e use a página QR incorporada — ela só aceita o envelope criptografado, nunca um segredo em claro.",
    ak_embed_link="Abrir a página envelope → QR",
)

AK["ru"] = dict(
    ak_h="aktar.html: скачайте, проверьте, используйте",
    ak_steps=[
        "Откройте страницу Releases проекта и скачайте aktar.html.",
        "Сверьте его SHA-256 с опубликованным рядом значением — команды здесь его выводят.",
        "Откройте файл со своего диска: в адресной строке будет file://, а не сайт.",
        "Вставьте содержимое, задайте пароль переноса и зашифруйте — конверт выйдет в виде QR-кодов или текста.",
        "На телефоне: Sekuvo → + → Импорт через QR, отсканируйте и введите тот же пароль.",
    ],
    ak_embed_p="Не хотите запускать шифрование в браузере вообще? Зашифруйте в собственном терминале и используйте встроенную QR-страницу — она принимает только зашифрованный конверт и никогда не просит открытый секрет.",
    ak_embed_link="Открыть страницу конверт → QR",
)

AK["ur"] = dict(
    ak_h="aktar.html: ڈاؤن لوڈ کریں، تصدیق کریں، استعمال کریں",
    ak_steps=[
        "پروجیکٹ کا Releases صفحہ کھولیں اور aktar.html ڈاؤن لوڈ کریں۔",
        "اس کا SHA-256 پاس شائع شدہ قدر سے ملائیں — یہاں دیے گئے کمانڈز اسے پرنٹ کرتے ہیں۔",
        "فائل کو اپنی ہی ڈسک سے کھولیں: ایڈریس بار میں file:// نظر آتا ہے، کوئی ویب سائٹ نہیں۔",
        "اپنا مواد پیسٹ کریں، منتقلی کا پاس ورڈ مقرر کریں اور مرمز کریں — لفافہ QR کوڈز یا متن کی صورت نکلتا ہے۔",
        "فون پر: Sekuvo → + → QR کے ذریعے درآمد کریں، اسکین کریں اور وہی پاس ورڈ درج کریں۔",
    ],
    ak_embed_p="براؤزر میں کوئی خفیہ کاری چلانا ہی نہیں چاہتے؟ اپنے ٹرمینل میں مرمز کریں اور سائٹ کے اندر موجود QR صفحہ استعمال کریں — وہ صرف مرمز شدہ لفافہ قبول کرتا ہے، کبھی کوئی کھلا راز نہیں۔",
    ak_embed_link="لفافہ → QR صفحہ کھولیں",
)

AK["id"] = dict(
    ak_h="aktar.html: unduh, verifikasi, gunakan",
    ak_steps=[
        "Buka halaman Releases proyek dan unduh aktar.html.",
        "Cocokkan SHA-256-nya dengan nilai yang dipublikasikan di sampingnya — perintah di sini mencetaknya.",
        "Buka file dari diskmu sendiri: bilah alamat menampilkan file://, bukan situs web.",
        "Tempel isinya, atur kata sandi transfer, dan enkripsi — amplop keluar sebagai kode QR atau teks.",
        "Di ponsel: Sekuvo → + → Impor lewat QR, pindai, dan masukkan kata sandi yang sama.",
    ],
    ak_embed_p="Tidak mau menjalankan enkripsi apa pun di browser? Enkripsi di terminalmu sendiri dan gunakan halaman QR bawaan situs — halaman itu hanya menerima amplop terenkripsi, tidak pernah rahasia mentah.",
    ak_embed_link="Buka halaman amplop → QR",
)

AK["de"] = dict(
    ak_h="aktar.html: herunterladen, prüfen, verwenden",
    ak_steps=[
        "Öffne die Releases-Seite des Projekts und lade aktar.html herunter.",
        "Vergleiche seinen SHA-256-Wert mit dem daneben veröffentlichten — die Befehle hier geben ihn aus.",
        "Öffne die Datei von deiner eigenen Festplatte: Die Adressleiste zeigt file://, keine Website.",
        "Füge deinen Inhalt ein, lege ein Übertragungspasswort fest und verschlüssele — der Umschlag kommt als QR-Codes oder Text heraus.",
        "Am Telefon: Sekuvo → + → Über QR importieren, scannen und dasselbe Passwort eingeben.",
    ],
    ak_embed_p="Du möchtest gar keine Verschlüsselung im Browser ausführen? Verschlüssele in deinem eigenen Terminal und nutze die eingebettete QR-Seite — sie akzeptiert nur den verschlüsselten Umschlag, niemals ein Klartext-Geheimnis.",
    ak_embed_link="Die Seite Umschlag → QR öffnen",
)

AK["ja"] = dict(
    ak_h="aktar.html:ダウンロード、検証、使用",
    ak_steps=[
        "プロジェクトのReleasesページを開き、aktar.htmlをダウンロードします。",
        "SHA-256を横に公開されている値と照合します — ここのコマンドがそれを表示します。",
        "ファイルを自分のディスクから開きます:アドレスバーにはウェブサイトではなくfile://が表示されます。",
        "内容を貼り付け、転送パスワードを設定して暗号化します — 封筒はQRコードまたはテキストとして出力されます。",
        "端末で:Sekuvo → + → QRでインポート、スキャンして同じパスワードを入力します。",
    ],
    ak_embed_p="ブラウザで暗号化を一切実行したくない場合は、自分のターミナルで暗号化し、サイト内蔵のQRページを使ってください — そのページは暗号化された封筒のみを受け付け、生の秘密情報を求めることは決してありません。",
    ak_embed_link="封筒 → QR ページを開く",
)

AK["pcm"] = dict(
    ak_h="aktar.html: download am, verify am, use am",
    ak_steps=[
        "Open the project Releases page and download aktar.html.",
        "Check im SHA-256 with the value wey dem publish beside am — the commands here dey print am.",
        "Open the file from your own disk: the address bar go show file://, no be website.",
        "Paste your content, set transfer password, and encrypt — the envelope go come out as QR codes or text.",
        "For the phone: Sekuvo → + → Import through QR, scan am, and enter the same password.",
    ],
    ak_embed_p="You no wan run any encryption for browser at all? Encrypt for your own terminal and use the QR page wey dey inside the site — e dey accept only the encrypted envelope, never raw secret.",
    ak_embed_link="Open the envelope → QR page",
)

AK["vi"] = dict(
    ak_h="aktar.html: tải xuống, kiểm chứng, sử dụng",
    ak_steps=[
        "Mở trang Releases của dự án và tải aktar.html xuống.",
        "Đối chiếu SHA-256 của nó với giá trị được công bố kế bên — các lệnh ở đây in ra giá trị đó.",
        "Mở tệp từ chính ổ đĩa của bạn: thanh địa chỉ hiển thị file://, không phải một trang web.",
        "Dán nội dung, đặt mật khẩu chuyển giao và mã hóa — phong bì xuất ra dưới dạng mã QR hoặc văn bản.",
        "Trên điện thoại: Sekuvo → + → Nhập qua QR, quét và nhập cùng mật khẩu.",
    ],
    ak_embed_p="Không muốn chạy bất kỳ mã hóa nào trong trình duyệt? Hãy mã hóa trong terminal của chính bạn và dùng trang QR nhúng sẵn — trang đó chỉ nhận phong bì đã mã hóa, không bao giờ nhận bí mật thô.",
    ak_embed_link="Mở trang phong bì → QR",
)

# ── Gömülü Zarf → QR sayfası ────────────────────────────────────────────────

A = {}

A["en"] = dict(
    title="Sekuvo — Envelope → QR",
    desc="Turn an already-encrypted Sekuvo envelope into QR frames. Nothing is encrypted on this page and no secret is ever asked for.",
    h1="Envelope → QR",
    lede="This page turns an already-encrypted Sekuvo envelope into QR frames your phone can scan. It performs no encryption and never asks for a secret: you produce the envelope on your own machine, and only ciphertext is pasted here.",
    warn="The most conservative path is still the downloaded aktar.html, opened from your own disk. This page exists for the case where you encrypt in your own terminal and only need the QR display.",
    make_h="1 · Produce the envelope on your own machine",
    make_p="The script below builds exactly the envelope the app opens (PBKDF2-HMAC-SHA256 · 310,000 rounds + AES-256-GCM). Save it as zarf-uret.py and read it before running it — it is about thirty lines. Generate the password instead of inventing one; the first command does that.",
    make_note="Paste the secret into the script's input rather than typing it on the command line — that way it never lands in your shell history.",
    paste_h="2 · Paste the envelope",
    paste_label='Encrypted envelope — the JSON the script printed, starting with {"app": "vault"…',
    btn="Show the QR",
    err_empty="The field is empty — paste the envelope the script printed.",
    err_invalid="This is not an encrypted Sekuvo envelope. Only ciphertext belongs here — never paste a raw secret into any web page.",
    frame_single="Single frame — scan it with Sekuvo → + → Import via QR.",
    frame_multi="Frame %1 / %2 — the frames repeat in a loop (~%3 s per cycle); hold the phone steady until the app reports completion.",
    phone_h="3 · On the phone",
    phone_p="Sekuvo → + → Import via QR → scan the frames → enter the same password → Add to existing.",
)

A["tr"] = dict(
    title="Sekuvo — Zarf → QR",
    desc="Zaten şifrelenmiş bir Sekuvo zarfını QR karelerine çevir. Bu sayfada hiçbir şey şifrelenmez ve asla bir sır istenmez.",
    h1="Zarf → QR",
    lede="Bu sayfa, zaten şifrelenmiş bir Sekuvo zarfını telefonun okuyabileceği QR karelerine çevirir. Şifreleme yapmaz ve asla bir sır istemez: zarfı kendi makinende üretirsin, buraya yalnız şifreli metin yapıştırılır.",
    warn="En temkinli yol hâlâ indirilen ve kendi diskinden açılan aktar.html'dir. Bu sayfa, şifrelemeyi kendi terminalinde yapıp yalnız QR gösterimine ihtiyaç duyduğun durum için var.",
    make_h="1 · Zarfı kendi makinende üret",
    make_p="Aşağıdaki betik, uygulamanın açtığı zarfın birebir aynısını kurar (PBKDF2-HMAC-SHA256 · 310.000 tur + AES-256-GCM). zarf-uret.py adıyla kaydet ve çalıştırmadan önce oku — otuz satır kadar. Parolayı uydurma, üret; ilk komut bunun için.",
    make_note="Sırrı komut satırına yazma, betiğin girdisine yapıştır — böylece kabuk geçmişine düşmez.",
    paste_h="2 · Zarfı yapıştır",
    paste_label='Şifreli zarf — betiğin yazdırdığı, {"app": "vault"… ile başlayan JSON',
    btn="QR'ı göster",
    err_empty="Alan boş — betiğin yazdırdığı zarfı yapıştır.",
    err_invalid="Bu, şifrelenmiş bir Sekuvo zarfı değil. Buraya yalnız şifreli metin girer — çıplak bir sırrı hiçbir web sayfasına yapıştırma.",
    frame_single="Tek kare — Sekuvo → + → QR ile aktar deyip okut.",
    frame_multi="Kare %1 / %2 — kareler döngüyle tekrar eder (tur ~%3 sn); uygulama tamamlandı diyene kadar telefonu sabit tut.",
    phone_h="3 · Telefonda",
    phone_p="Sekuvo → + → QR ile aktar → kareleri okut → aynı parolayı gir → Mevcuta ekle.",
)

A["es"] = dict(
    title="Sekuvo — Sobre → QR",
    desc="Convierte un sobre Sekuvo ya cifrado en cuadros QR. En esta página no se cifra nada y nunca se pide un secreto.",
    h1="Sobre → QR",
    lede="Esta página convierte un sobre Sekuvo ya cifrado en cuadros QR que tu teléfono puede escanear. No realiza ningún cifrado y nunca pide un secreto: el sobre lo produces en tu propia máquina, y aquí solo se pega texto cifrado.",
    warn="El camino más conservador sigue siendo el aktar.html descargado y abierto desde tu propio disco. Esta página existe para el caso en que cifras en tu propia terminal y solo necesitas la visualización QR.",
    make_h="1 · Produce el sobre en tu propia máquina",
    make_p="El script de abajo construye exactamente el sobre que la aplicación abre (PBKDF2-HMAC-SHA256 · 310.000 rondas + AES-256-GCM). Guárdalo como zarf-uret.py y léelo antes de ejecutarlo — son unas treinta líneas. Genera la contraseña en vez de inventarla; el primer comando lo hace.",
    make_note="Pega el secreto en la entrada del script en lugar de escribirlo en la línea de comandos — así nunca queda en el historial de tu shell.",
    paste_h="2 · Pega el sobre",
    paste_label='Sobre cifrado — el JSON que imprimió el script, que empieza con {"app": "vault"…',
    btn="Mostrar el QR",
    err_empty="El campo está vacío — pega el sobre que imprimió el script.",
    err_invalid="Esto no es un sobre Sekuvo cifrado. Aquí solo entra texto cifrado — nunca pegues un secreto en claro en ninguna página web.",
    frame_single="Un solo cuadro — escanéalo con Sekuvo → + → Importar por QR.",
    frame_multi="Cuadro %1 / %2 — los cuadros se repiten en bucle (~%3 s por vuelta); mantén el teléfono firme hasta que la aplicación indique que terminó.",
    phone_h="3 · En el teléfono",
    phone_p="Sekuvo → + → Importar por QR → escanea los cuadros → introduce la misma contraseña → Añadir a lo existente.",
)

A["hi"] = dict(
    title="Sekuvo — लिफ़ाफ़ा → QR",
    desc="पहले से एन्क्रिप्टेड Sekuvo लिफ़ाफ़े को QR फ़्रेम में बदलें। इस पेज पर कुछ भी एन्क्रिप्ट नहीं होता और कभी कोई रहस्य नहीं माँगा जाता।",
    h1="लिफ़ाफ़ा → QR",
    lede="यह पेज पहले से एन्क्रिप्टेड Sekuvo लिफ़ाफ़े को ऐसे QR फ़्रेम में बदलता है जिन्हें आपका फ़ोन स्कैन कर सके। यह कोई एन्क्रिप्शन नहीं करता और कभी कोई रहस्य नहीं माँगता: लिफ़ाफ़ा आप अपनी ही मशीन पर बनाते हैं, और यहाँ केवल एन्क्रिप्टेड टेक्स्ट चिपकाया जाता है।",
    warn="सबसे सतर्क रास्ता अब भी डाउनलोड किया हुआ aktar.html है, जिसे अपनी ही डिस्क से खोला जाए। यह पेज उस स्थिति के लिए है जब आप अपने टर्मिनल में एन्क्रिप्ट करते हैं और आपको केवल QR प्रदर्शन चाहिए।",
    make_h="1 · लिफ़ाफ़ा अपनी ही मशीन पर बनाएँ",
    make_p="नीचे दी स्क्रिप्ट ठीक वही लिफ़ाफ़ा बनाती है जिसे ऐप खोलता है (PBKDF2-HMAC-SHA256 · 310,000 राउंड + AES-256-GCM)। इसे zarf-uret.py नाम से सहेजें और चलाने से पहले पढ़ें — यह लगभग तीस पंक्तियाँ है। पासवर्ड गढ़ने के बजाय जनरेट करें; पहला कमांड यही करता है।",
    make_note="रहस्य को कमांड लाइन पर टाइप करने के बजाय स्क्रिप्ट के इनपुट में चिपकाएँ — इस तरह वह कभी आपके शेल इतिहास में नहीं जाता।",
    paste_h="2 · लिफ़ाफ़ा चिपकाएँ",
    paste_label='एन्क्रिप्टेड लिफ़ाफ़ा — स्क्रिप्ट द्वारा प्रिंट किया JSON, जो {"app": "vault"… से शुरू होता है',
    btn="QR दिखाएँ",
    err_empty="फ़ील्ड खाली है — स्क्रिप्ट द्वारा प्रिंट किया लिफ़ाफ़ा चिपकाएँ।",
    err_invalid="यह कोई एन्क्रिप्टेड Sekuvo लिफ़ाफ़ा नहीं है। यहाँ केवल एन्क्रिप्टेड टेक्स्ट आता है — कोई खुला रहस्य किसी भी वेब पेज पर कभी न चिपकाएँ।",
    frame_single="एक ही फ़्रेम — इसे Sekuvo → + → QR से आयात से स्कैन करें।",
    frame_multi="फ़्रेम %1 / %2 — फ़्रेम लूप में दोहराते हैं (~%3 सेकंड प्रति चक्र); ऐप के पूर्ण बताने तक फ़ोन स्थिर रखें।",
    phone_h="3 · फ़ोन पर",
    phone_p="Sekuvo → + → QR से आयात → फ़्रेम स्कैन करें → वही पासवर्ड डालें → मौजूदा में जोड़ें।",
)

A["ar"] = dict(
    title="Sekuvo — مظروف → QR",
    desc="حوّل مظروف Sekuvo مشفَّرًا سلفًا إلى إطارات QR. لا يُشفَّر شيء في هذه الصفحة ولا يُطلب سرّ أبدًا.",
    h1="مظروف → QR",
    lede="تحوّل هذه الصفحة مظروف Sekuvo المشفَّر سلفًا إلى إطارات QR يستطيع هاتفك مسحها. لا تجري أي تشفير ولا تطلب سرًّا أبدًا: تنتج المظروف على جهازك الخاص، ولا يُلصق هنا إلا نص مشفَّر.",
    warn="الطريق الأكثر تحفظًا يبقى aktar.html المنزَّل والمفتوح من قرصك الخاص. هذه الصفحة موجودة للحالة التي تشفّر فيها في طرفيتك ولا تحتاج إلا إلى عرض QR.",
    make_h="1 · أنتج المظروف على جهازك الخاص",
    make_p="يبني السكربت أدناه المظروف نفسه الذي يفتحه التطبيق (PBKDF2-HMAC-SHA256 · 310٬000 دورة + AES-256-GCM). احفظه باسم zarf-uret.py واقرأه قبل تشغيله — نحو ثلاثين سطرًا. ولّد كلمة المرور بدل اختلاقها؛ الأمر الأول يفعل ذلك.",
    make_note="الصق السرّ في مدخل السكربت بدل كتابته في سطر الأوامر — هكذا لا يستقر أبدًا في سجل الصدفة.",
    paste_h="2 · الصق المظروف",
    paste_label='المظروف المشفَّر — ملف JSON الذي طبعه السكربت، ويبدأ بـ {"app": "vault"…',
    btn="اعرض QR",
    err_empty="الحقل فارغ — الصق المظروف الذي طبعه السكربت.",
    err_invalid="هذا ليس مظروف Sekuvo مشفَّرًا. لا يدخل هنا إلا نص مشفَّر — لا تلصق سرًّا مكشوفًا في أي صفحة ويب أبدًا.",
    frame_single="إطار واحد — امسحه عبر Sekuvo → + → استيراد عبر QR.",
    frame_multi="الإطار %1 / %2 — تتكرر الإطارات في حلقة (~%3 ث للدورة)؛ ثبّت الهاتف حتى يعلن التطبيق الاكتمال.",
    phone_h="3 · على الهاتف",
    phone_p="Sekuvo → + → استيراد عبر QR → امسح الإطارات → أدخل كلمة المرور نفسها → الإضافة إلى الموجود.",
)

A["zh"] = dict(
    title="Sekuvo — 信封 → 二维码",
    desc="把已加密的 Sekuvo 信封转换为二维码帧。本页不进行任何加密,也绝不索要秘密。",
    h1="信封 → 二维码",
    lede="本页把已加密的 Sekuvo 信封转换为手机可以扫描的二维码帧。它不做任何加密,也绝不索要秘密:信封在你自己的机器上生成,这里只粘贴密文。",
    warn="最稳妥的方式仍是下载 aktar.html 并从自己的磁盘打开。本页针对的情形是:你在自己的终端里完成加密,只需要二维码展示。",
    make_h="1 · 在你自己的机器上生成信封",
    make_p="下面的脚本构建的信封与应用打开的完全一致(PBKDF2-HMAC-SHA256 · 310,000 轮 + AES-256-GCM)。将它保存为 zarf-uret.py,运行前先读一遍 —— 大约三十行。密码请生成而不要自己编;第一条命令就是做这件事的。",
    make_note="把秘密粘贴到脚本的输入里,而不要写在命令行上 —— 这样它永远不会留在 shell 历史记录中。",
    paste_h="2 · 粘贴信封",
    paste_label='加密信封 —— 脚本打印的 JSON,以 {"app": "vault"… 开头',
    btn="显示二维码",
    err_empty="输入框是空的 —— 请粘贴脚本打印的信封。",
    err_invalid="这不是加密的 Sekuvo 信封。这里只接受密文 —— 永远不要把明文秘密粘贴到任何网页。",
    frame_single="单帧 —— 用 Sekuvo → + → 通过二维码导入 扫描它。",
    frame_multi="第 %1 / %2 帧 —— 各帧循环播放(每轮约 %3 秒);请稳住手机,直到应用提示完成。",
    phone_h="3 · 在手机上",
    phone_p="Sekuvo → + → 通过二维码导入 → 扫描各帧 → 输入相同的密码 → 添加到现有条目。",
)

A["fr"] = dict(
    title="Sekuvo — Enveloppe → QR",
    desc="Transforme une enveloppe Sekuvo déjà chiffrée en cadres QR. Rien n'est chiffré sur cette page et aucun secret n'est jamais demandé.",
    h1="Enveloppe → QR",
    lede="Cette page transforme une enveloppe Sekuvo déjà chiffrée en cadres QR que ton téléphone peut scanner. Elle n'effectue aucun chiffrement et ne demande jamais de secret : tu produis l'enveloppe sur ta propre machine, et seul du texte chiffré est collé ici.",
    warn="Le chemin le plus prudent reste l'aktar.html téléchargé, ouvert depuis ton propre disque. Cette page existe pour le cas où tu chiffres dans ton propre terminal et n'as besoin que de l'affichage QR.",
    make_h="1 · Produis l'enveloppe sur ta propre machine",
    make_p="Le script ci-dessous construit exactement l'enveloppe que l'application ouvre (PBKDF2-HMAC-SHA256 · 310 000 tours + AES-256-GCM). Enregistre-le sous zarf-uret.py et lis-le avant de l'exécuter — une trentaine de lignes. Génère le mot de passe au lieu de l'inventer ; la première commande s'en charge.",
    make_note="Colle le secret dans l'entrée du script plutôt que de le taper sur la ligne de commande — il n'atterrira ainsi jamais dans l'historique de ton shell.",
    paste_h="2 · Colle l'enveloppe",
    paste_label='Enveloppe chiffrée — le JSON imprimé par le script, qui commence par {"app": "vault"…',
    btn="Afficher le QR",
    err_empty="Le champ est vide — colle l'enveloppe imprimée par le script.",
    err_invalid="Ceci n'est pas une enveloppe Sekuvo chiffrée. Seul du texte chiffré a sa place ici — ne colle jamais un secret en clair dans une page web.",
    frame_single="Un seul cadre — scanne-le avec Sekuvo → + → Importer via QR.",
    frame_multi="Cadre %1 / %2 — les cadres défilent en boucle (~%3 s par tour) ; garde le téléphone stable jusqu'à ce que l'application annonce la fin.",
    phone_h="3 · Sur le téléphone",
    phone_p="Sekuvo → + → Importer via QR → scanne les cadres → saisis le même mot de passe → Ajouter à l'existant.",
)

A["bn"] = dict(
    title="Sekuvo — এনভেলপ → QR",
    desc="আগে থেকে এনক্রিপ্ট করা Sekuvo এনভেলপকে QR ফ্রেমে রূপান্তর করুন। এই পৃষ্ঠায় কিছুই এনক্রিপ্ট হয় না এবং কখনো গোপন তথ্য চাওয়া হয় না।",
    h1="এনভেলপ → QR",
    lede="এই পৃষ্ঠা আগে থেকে এনক্রিপ্ট করা একটি Sekuvo এনভেলপকে এমন QR ফ্রেমে রূপান্তর করে যা আপনার ফোন স্ক্যান করতে পারে। এটি কোনো এনক্রিপশন করে না এবং কখনো গোপন তথ্য চায় না: এনভেলপটি আপনি নিজের মেশিনে তৈরি করেন, এখানে কেবল এনক্রিপ্টেড টেক্সটই পেস্ট হয়।",
    warn="সবচেয়ে সাবধানী পথ এখনো ডাউনলোড করা aktar.html, যা নিজের ডিস্ক থেকে খোলা হয়। এই পৃষ্ঠাটি সেই পরিস্থিতির জন্য যখন আপনি নিজের টার্মিনালে এনক্রিপ্ট করেন এবং কেবল QR প্রদর্শন দরকার।",
    make_h="1 · এনভেলপটি নিজের মেশিনে তৈরি করুন",
    make_p="নিচের স্ক্রিপ্টটি ঠিক সেই এনভেলপই বানায় যা অ্যাপ খোলে (PBKDF2-HMAC-SHA256 · ৩,১০,০০০ রাউন্ড + AES-256-GCM)। এটিকে zarf-uret.py নামে সংরক্ষণ করুন এবং চালানোর আগে পড়ুন — প্রায় ত্রিশ লাইন। পাসওয়ার্ড বানিয়ে না নিয়ে জেনারেট করুন; প্রথম কমান্ডটি সেটিই করে।",
    make_note="গোপন তথ্যটি কমান্ড লাইনে টাইপ না করে স্ক্রিপ্টের ইনপুটে পেস্ট করুন — তাহলে সেটি কখনো আপনার শেল ইতিহাসে থাকবে না।",
    paste_h="2 · এনভেলপ পেস্ট করুন",
    paste_label='এনক্রিপ্টেড এনভেলপ — স্ক্রিপ্টের প্রিন্ট করা JSON, যা {"app": "vault"… দিয়ে শুরু',
    btn="QR দেখান",
    err_empty="ঘরটি খালি — স্ক্রিপ্টের প্রিন্ট করা এনভেলপটি পেস্ট করুন।",
    err_invalid="এটি কোনো এনক্রিপ্টেড Sekuvo এনভেলপ নয়। এখানে কেবল এনক্রিপ্টেড টেক্সটই চলে — খোলা গোপন তথ্য কখনো কোনো ওয়েব পৃষ্ঠায় পেস্ট করবেন না।",
    frame_single="একটিই ফ্রেম — Sekuvo → + → QR দিয়ে ইম্পোর্ট করুন দিয়ে স্ক্যান করুন।",
    frame_multi="ফ্রেম %1 / %2 — ফ্রেমগুলো লুপে ঘোরে (প্রতি চক্রে ~%3 সেকেন্ড); অ্যাপ সম্পন্ন না বলা পর্যন্ত ফোন স্থির রাখুন।",
    phone_h="3 · ফোনে",
    phone_p="Sekuvo → + → QR দিয়ে ইম্পোর্ট করুন → ফ্রেমগুলো স্ক্যান করুন → একই পাসওয়ার্ড দিন → বিদ্যমানে যোগ করুন।",
)

A["pt"] = dict(
    title="Sekuvo — Envelope → QR",
    desc="Converta um envelope Sekuvo já criptografado em quadros QR. Nada é criptografado nesta página e nenhum segredo é jamais pedido.",
    h1="Envelope → QR",
    lede="Esta página converte um envelope Sekuvo já criptografado em quadros QR que seu telefone pode escanear. Ela não realiza nenhuma criptografia e nunca pede um segredo: você produz o envelope na sua própria máquina, e aqui só se cola texto criptografado.",
    warn="O caminho mais conservador continua sendo o aktar.html baixado, aberto do seu próprio disco. Esta página existe para o caso em que você criptografa no seu próprio terminal e só precisa da exibição QR.",
    make_h="1 · Produza o envelope na sua própria máquina",
    make_p="O script abaixo constrói exatamente o envelope que o aplicativo abre (PBKDF2-HMAC-SHA256 · 310.000 rodadas + AES-256-GCM). Salve-o como zarf-uret.py e leia-o antes de executar — são cerca de trinta linhas. Gere a senha em vez de inventá-la; o primeiro comando faz isso.",
    make_note="Cole o segredo na entrada do script em vez de digitá-lo na linha de comando — assim ele nunca fica no histórico do seu shell.",
    paste_h="2 · Cole o envelope",
    paste_label='Envelope criptografado — o JSON que o script imprimiu, começando com {"app": "vault"…',
    btn="Mostrar o QR",
    err_empty="O campo está vazio — cole o envelope que o script imprimiu.",
    err_invalid="Isto não é um envelope Sekuvo criptografado. Aqui só entra texto criptografado — nunca cole um segredo em claro em nenhuma página web.",
    frame_single="Quadro único — escaneie com Sekuvo → + → Importar por QR.",
    frame_multi="Quadro %1 / %2 — os quadros se repetem em loop (~%3 s por volta); mantenha o telefone firme até o aplicativo indicar a conclusão.",
    phone_h="3 · No telefone",
    phone_p="Sekuvo → + → Importar por QR → escaneie os quadros → digite a mesma senha → Adicionar aos existentes.",
)

A["ru"] = dict(
    title="Sekuvo — Конверт → QR",
    desc="Превратите уже зашифрованный конверт Sekuvo в QR-кадры. На этой странице ничего не шифруется, и секрет никогда не запрашивается.",
    h1="Конверт → QR",
    lede="Эта страница превращает уже зашифрованный конверт Sekuvo в QR-кадры, которые может отсканировать телефон. Она не выполняет шифрование и никогда не просит секрет: конверт вы создаёте на собственной машине, сюда вставляется только шифротекст.",
    warn="Самый осторожный путь — по-прежнему скачанный aktar.html, открытый с собственного диска. Эта страница существует для случая, когда вы шифруете в своём терминале и вам нужен только показ QR.",
    make_h="1 · Создайте конверт на своей машине",
    make_p="Скрипт ниже собирает ровно тот конверт, который открывает приложение (PBKDF2-HMAC-SHA256 · 310 000 раундов + AES-256-GCM). Сохраните его как zarf-uret.py и прочитайте перед запуском — около тридцати строк. Пароль сгенерируйте, а не придумывайте; это делает первая команда.",
    make_note="Вставляйте секрет во ввод скрипта, а не печатайте его в командной строке — так он никогда не попадёт в историю shell.",
    paste_h="2 · Вставьте конверт",
    paste_label='Зашифрованный конверт — JSON, который вывел скрипт, начинается с {"app": "vault"…',
    btn="Показать QR",
    err_empty="Поле пустое — вставьте конверт, который вывел скрипт.",
    err_invalid="Это не зашифрованный конверт Sekuvo. Сюда попадает только шифротекст — никогда не вставляйте открытый секрет ни в одну веб-страницу.",
    frame_single="Один кадр — отсканируйте его через Sekuvo → + → Импорт через QR.",
    frame_multi="Кадр %1 / %2 — кадры повторяются по кругу (~%3 с на цикл); держите телефон неподвижно, пока приложение не сообщит о завершении.",
    phone_h="3 · На телефоне",
    phone_p="Sekuvo → + → Импорт через QR → отсканируйте кадры → введите тот же пароль → Добавить к существующим.",
)

A["ur"] = dict(
    title="Sekuvo — لفافہ → QR",
    desc="پہلے سے مرمز شدہ Sekuvo لفافے کو QR فریمز میں بدلیں۔ اس صفحے پر کچھ مرمز نہیں ہوتا اور کبھی کوئی راز نہیں مانگا جاتا۔",
    h1="لفافہ → QR",
    lede="یہ صفحہ پہلے سے مرمز شدہ Sekuvo لفافے کو ایسے QR فریمز میں بدلتا ہے جنہیں آپ کا فون اسکین کر سکے۔ یہ کوئی خفیہ کاری نہیں کرتا اور کبھی راز نہیں مانگتا: لفافہ آپ اپنی ہی مشین پر بناتے ہیں، اور یہاں صرف مرمز شدہ متن پیسٹ ہوتا ہے۔",
    warn="سب سے محتاط راستہ اب بھی ڈاؤن لوڈ کیا ہوا aktar.html ہے، جو اپنی ڈسک سے کھولا جائے۔ یہ صفحہ اس صورت کے لیے ہے جب آپ اپنے ٹرمینل میں مرمز کریں اور آپ کو صرف QR دکھانے کی ضرورت ہو۔",
    make_h="1 · لفافہ اپنی ہی مشین پر بنائیں",
    make_p="نیچے دیا اسکرپٹ بالکل وہی لفافہ بناتا ہے جو ایپ کھولتی ہے (PBKDF2-HMAC-SHA256 · 310,000 راؤنڈز + AES-256-GCM)۔ اسے zarf-uret.py کے نام سے محفوظ کریں اور چلانے سے پہلے پڑھیں — تقریباً تیس سطریں۔ پاس ورڈ خود گھڑنے کے بجائے جنریٹ کریں؛ پہلا کمانڈ یہی کرتا ہے۔",
    make_note="راز کو کمانڈ لائن پر ٹائپ کرنے کے بجائے اسکرپٹ کے ان پٹ میں پیسٹ کریں — یوں وہ کبھی آپ کی شیل ہسٹری میں نہیں جاتا۔",
    paste_h="2 · لفافہ پیسٹ کریں",
    paste_label='مرمز شدہ لفافہ — اسکرپٹ کا پرنٹ کردہ JSON، جو {"app": "vault"… سے شروع ہوتا ہے',
    btn="QR دکھائیں",
    err_empty="خانہ خالی ہے — اسکرپٹ کا پرنٹ کردہ لفافہ پیسٹ کریں۔",
    err_invalid="یہ کوئی مرمز شدہ Sekuvo لفافہ نہیں۔ یہاں صرف مرمز شدہ متن آتا ہے — کھلا راز کبھی کسی ویب صفحے پر پیسٹ نہ کریں۔",
    frame_single="ایک ہی فریم — اسے Sekuvo → + → QR کے ذریعے درآمد کریں سے اسکین کریں۔",
    frame_multi="فریم %1 / %2 — فریم لوپ میں دہراتے ہیں (~%3 سیکنڈ فی چکر)؛ ایپ کے مکمل بتانے تک فون کو ساکن رکھیں۔",
    phone_h="3 · فون پر",
    phone_p="Sekuvo → + → QR کے ذریعے درآمد کریں → فریم اسکین کریں → وہی پاس ورڈ درج کریں → موجودہ میں شامل کریں۔",
)

A["id"] = dict(
    title="Sekuvo — Amplop → QR",
    desc="Ubah amplop Sekuvo yang sudah terenkripsi menjadi bingkai QR. Tidak ada yang dienkripsi di halaman ini dan rahasia tidak pernah diminta.",
    h1="Amplop → QR",
    lede="Halaman ini mengubah amplop Sekuvo yang sudah terenkripsi menjadi bingkai QR yang bisa dipindai ponselmu. Halaman ini tidak melakukan enkripsi dan tidak pernah meminta rahasia: amplop kamu buat di mesinmu sendiri, dan di sini hanya teks terenkripsi yang ditempel.",
    warn="Jalur paling hati-hati tetaplah aktar.html yang diunduh, dibuka dari diskmu sendiri. Halaman ini ada untuk kasus ketika kamu mengenkripsi di terminalmu sendiri dan hanya butuh tampilan QR.",
    make_h="1 · Buat amplop di mesinmu sendiri",
    make_p="Skrip di bawah membangun persis amplop yang dibuka aplikasi (PBKDF2-HMAC-SHA256 · 310.000 putaran + AES-256-GCM). Simpan sebagai zarf-uret.py dan baca sebelum menjalankannya — sekitar tiga puluh baris. Buat kata sandi dengan generator, jangan dikarang; perintah pertama melakukannya.",
    make_note="Tempel rahasia ke input skrip alih-alih mengetiknya di baris perintah — dengan begitu ia tidak pernah masuk riwayat shell-mu.",
    paste_h="2 · Tempel amplop",
    paste_label='Amplop terenkripsi — JSON yang dicetak skrip, dimulai dengan {"app": "vault"…',
    btn="Tampilkan QR",
    err_empty="Kolom kosong — tempel amplop yang dicetak skrip.",
    err_invalid="Ini bukan amplop Sekuvo terenkripsi. Hanya teks terenkripsi yang boleh di sini — jangan pernah menempel rahasia mentah ke halaman web mana pun.",
    frame_single="Satu bingkai — pindai dengan Sekuvo → + → Impor lewat QR.",
    frame_multi="Bingkai %1 / %2 — bingkai berulang dalam lingkaran (~%3 dtk per putaran); tahan ponsel tetap stabil sampai aplikasi melaporkan selesai.",
    phone_h="3 · Di ponsel",
    phone_p="Sekuvo → + → Impor lewat QR → pindai bingkai → masukkan kata sandi yang sama → Tambahkan ke yang sudah ada.",
)

A["de"] = dict(
    title="Sekuvo — Umschlag → QR",
    desc="Verwandle einen bereits verschlüsselten Sekuvo-Umschlag in QR-Bilder. Auf dieser Seite wird nichts verschlüsselt, und ein Geheimnis wird nie abgefragt.",
    h1="Umschlag → QR",
    lede="Diese Seite verwandelt einen bereits verschlüsselten Sekuvo-Umschlag in QR-Bilder, die dein Telefon scannen kann. Sie führt keine Verschlüsselung durch und fragt nie nach einem Geheimnis: Den Umschlag erzeugst du auf deinem eigenen Rechner, hier wird nur Chiffretext eingefügt.",
    warn="Der vorsichtigste Weg bleibt das heruntergeladene aktar.html, geöffnet von deiner eigenen Festplatte. Diese Seite existiert für den Fall, dass du in deinem eigenen Terminal verschlüsselst und nur die QR-Anzeige brauchst.",
    make_h="1 · Erzeuge den Umschlag auf deinem eigenen Rechner",
    make_p="Das Skript unten baut genau den Umschlag, den die App öffnet (PBKDF2-HMAC-SHA256 · 310.000 Runden + AES-256-GCM). Speichere es als zarf-uret.py und lies es vor dem Ausführen — etwa dreißig Zeilen. Generiere das Passwort, statt es dir auszudenken; der erste Befehl erledigt das.",
    make_note="Füge das Geheimnis in die Eingabe des Skripts ein, statt es auf der Kommandozeile zu tippen — so landet es nie in deinem Shell-Verlauf.",
    paste_h="2 · Füge den Umschlag ein",
    paste_label='Verschlüsselter Umschlag — das vom Skript ausgegebene JSON, beginnend mit {"app": "vault"…',
    btn="QR anzeigen",
    err_empty="Das Feld ist leer — füge den vom Skript ausgegebenen Umschlag ein.",
    err_invalid="Dies ist kein verschlüsselter Sekuvo-Umschlag. Hierher gehört nur Chiffretext — füge niemals ein Klartext-Geheimnis in irgendeine Webseite ein.",
    frame_single="Ein einzelnes Bild — scanne es mit Sekuvo → + → Über QR importieren.",
    frame_multi="Bild %1 / %2 — die Bilder wiederholen sich in einer Schleife (~%3 s pro Durchlauf); halte das Telefon ruhig, bis die App den Abschluss meldet.",
    phone_h="3 · Am Telefon",
    phone_p="Sekuvo → + → Über QR importieren → Bilder scannen → dasselbe Passwort eingeben → Zum Bestehenden hinzufügen.",
)

A["ja"] = dict(
    title="Sekuvo — 封筒 → QR",
    desc="すでに暗号化されたSekuvoの封筒をQRフレームに変換します。このページでは何も暗号化されず、秘密情報を求められることもありません。",
    h1="封筒 → QR",
    lede="このページは、すでに暗号化されたSekuvoの封筒を、端末でスキャンできるQRフレームに変換します。暗号化は一切行わず、秘密情報を求めることもありません:封筒は自分のマシンで作成し、ここには暗号文だけを貼り付けます。",
    warn="最も慎重な方法は、今でもダウンロードしたaktar.htmlを自分のディスクから開くことです。このページは、自分のターミナルで暗号化を済ませ、QR表示だけが必要な場合のためにあります。",
    make_h="1 · 封筒を自分のマシンで作成する",
    make_p="下のスクリプトは、アプリが開く封筒とまったく同じもの(PBKDF2-HMAC-SHA256 · 310,000回 + AES-256-GCM)を作成します。zarf-uret.pyという名前で保存し、実行前に読んでください — 約30行です。パスワードは自分で考えず生成してください;最初のコマンドがそれを行います。",
    make_note="秘密情報はコマンドラインに打ち込まず、スクリプトの入力に貼り付けてください — そうすればシェル履歴に残ることはありません。",
    paste_h="2 · 封筒を貼り付ける",
    paste_label='暗号化された封筒 — スクリプトが出力したJSONで、{"app": "vault"…で始まります',
    btn="QRを表示",
    err_empty="入力欄が空です — スクリプトが出力した封筒を貼り付けてください。",
    err_invalid="これは暗号化されたSekuvoの封筒ではありません。ここには暗号文だけが入ります — 生の秘密情報をウェブページに貼り付けることは決してしないでください。",
    frame_single="1フレームのみ — Sekuvo → + → QRでインポート でスキャンしてください。",
    frame_multi="フレーム %1 / %2 — フレームはループで繰り返されます(1周 約%3秒);アプリが完了を報告するまで端末を安定させてください。",
    phone_h="3 · 端末で",
    phone_p="Sekuvo → + → QRでインポート → フレームをスキャン → 同じパスワードを入力 → 既存のものに追加。",
)

A["pcm"] = dict(
    title="Sekuvo — Envelope → QR",
    desc="Turn Sekuvo envelope wey don already encrypt into QR frames. Nothing dey encrypt for dis page and secret no dey ever asked.",
    h1="Envelope → QR",
    lede="Dis page dey turn Sekuvo envelope wey don already encrypt into QR frames wey your phone fit scan. E no dey do any encryption and e no dey ever ask for secret: you go produce the envelope for your own machine, and na only ciphertext dey paste here.",
    warn="The most careful path still be the downloaded aktar.html, wey you open from your own disk. Dis page dey exist for when you encrypt for your own terminal and na only the QR display you need.",
    make_h="1 · Produce the envelope for your own machine",
    make_p="The script below dey build exactly the envelope wey the app dey open (PBKDF2-HMAC-SHA256 · 310,000 rounds + AES-256-GCM). Save am as zarf-uret.py and read am before you run am — na like thirty lines. Generate the password, no invent am; the first command dey do dat.",
    make_note="Paste the secret inside the script input instead of typing am for command line — dat way e no go ever land inside your shell history.",
    paste_h="2 · Paste the envelope",
    paste_label='Encrypted envelope — the JSON wey the script print, wey dey start with {"app": "vault"…',
    btn="Show the QR",
    err_empty="The field empty — paste the envelope wey the script print.",
    err_invalid="Dis one no be encrypted Sekuvo envelope. Na only ciphertext dey belong here — never paste raw secret inside any web page.",
    frame_single="One frame — scan am with Sekuvo → + → Import through QR.",
    frame_multi="Frame %1 / %2 — the frames dey repeat for loop (~%3 s per cycle); hold the phone steady until the app talk say e don finish.",
    phone_h="3 · For the phone",
    phone_p="Sekuvo → + → Import through QR → scan the frames → enter the same password → Add to wetin dey there.",
)

A["vi"] = dict(
    title="Sekuvo — Phong bì → QR",
    desc="Chuyển một phong bì Sekuvo đã mã hóa sẵn thành các khung QR. Không có gì được mã hóa trên trang này và bí mật không bao giờ bị hỏi đến.",
    h1="Phong bì → QR",
    lede="Trang này chuyển một phong bì Sekuvo đã mã hóa sẵn thành các khung QR mà điện thoại của bạn có thể quét. Nó không thực hiện mã hóa và không bao giờ hỏi bí mật: bạn tạo phong bì trên máy của chính mình, và ở đây chỉ dán văn bản đã mã hóa.",
    warn="Con đường thận trọng nhất vẫn là aktar.html được tải xuống, mở từ chính ổ đĩa của bạn. Trang này tồn tại cho trường hợp bạn mã hóa trong terminal của mình và chỉ cần phần hiển thị QR.",
    make_h="1 · Tạo phong bì trên máy của chính bạn",
    make_p="Đoạn mã dưới đây tạo ra chính xác phong bì mà ứng dụng mở (PBKDF2-HMAC-SHA256 · 310.000 vòng + AES-256-GCM). Lưu nó thành zarf-uret.py và đọc trước khi chạy — khoảng ba mươi dòng. Hãy tạo mật khẩu bằng máy thay vì tự nghĩ; lệnh đầu tiên làm việc đó.",
    make_note="Dán bí mật vào đầu vào của đoạn mã thay vì gõ nó trên dòng lệnh — như vậy nó không bao giờ nằm lại trong lịch sử shell của bạn.",
    paste_h="2 · Dán phong bì",
    paste_label='Phong bì mã hóa — JSON mà đoạn mã in ra, bắt đầu bằng {"app": "vault"…',
    btn="Hiện QR",
    err_empty="Ô đang trống — hãy dán phong bì mà đoạn mã đã in ra.",
    err_invalid="Đây không phải một phong bì Sekuvo đã mã hóa. Ở đây chỉ có chỗ cho văn bản mã hóa — đừng bao giờ dán bí mật thô vào bất kỳ trang web nào.",
    frame_single="Một khung duy nhất — quét nó bằng Sekuvo → + → Nhập qua QR.",
    frame_multi="Khung %1 / %2 — các khung lặp lại theo vòng (~%3 giây mỗi vòng); giữ điện thoại ổn định cho đến khi ứng dụng báo hoàn tất.",
    phone_h="3 · Trên điện thoại",
    phone_p="Sekuvo → + → Nhập qua QR → quét các khung → nhập cùng mật khẩu → Thêm vào các mục hiện có.",
)

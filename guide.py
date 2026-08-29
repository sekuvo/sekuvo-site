#!/usr/bin/env python3
"""Guide content for sekuvo.com, one page per language.

Kept apart from build.py because it is prose, not layout: the guide changes
whenever the app's flows change, and mixing it into the page machinery would
make both harder to read. build.py imports G and renders it.
"""

G = {}

# ─────────────────────────────── English ────────────────────────────────────
G["en"] = dict(
    nav_label="Guide",
    title="Sekuvo — Guide",
    desc="How to use Sekuvo: first run, autofill, the keyboard, typing to a computer over Bluetooth, backups and transfers.",
    h1="Guide",
    lede="Everything Sekuvo does, in the order you are likely to need it. Nothing here requires an account or an internet connection.",
    back="← Back to sekuvo.com",
    sections=[
        ("start", "First run", [
            "<p>On first launch you set a <strong>master password</strong>. Every secret you store is encrypted with a key derived from it, so it is the one thing Sekuvo cannot help you recover — write it somewhere safe before you go further.</p>",
            "<p>Already have a backup from another phone? Tap <strong>“I have a backup — restore it”</strong> on the welcome screen. You still set a master password for this device first, then the file picker opens by itself and your entries come back.</p>",
            "<p>If your phone has a fingerprint or face sensor, Sekuvo offers to use it right after setup. That is a convenience layer only: the master password always works, and it is the one that survives a factory reset.</p>",
        ]),
        ("entries", "What you can store", [
            "<p>Four entry types cover most of what people keep in a vault:</p>",
            "<ul><li><strong>Account / Password</strong> — username, password, site or app.</li><li><strong>Everyday</strong> — name, phone, email, address. The things forms ask for constantly.</li><li><strong>Card</strong> — card number, expiry, CVV, IBAN.</li><li><strong>Secure note</strong> — free text, with subtypes for scripts, keys, recovery codes and config files.</li></ul>",
            "<p>Account and Everyday entries also take <strong>custom fields</strong>: any “name + value” pair you like. Custom fields are encrypted exactly like the built-in ones and appear everywhere the others do.</p>",
        ]),
        ("channels", "Using a secret without the clipboard", [
            "<p>The clipboard is readable by other apps and is where secrets get stolen. Sekuvo gives you three ways to deliver a value straight to its destination instead. You can still copy — the clipboard is cleared automatically after 45 seconds — but the three channels below are the reason the app exists.</p>",
        ]),
        ("autofill", "Autofill (inside your phone)", [
            "<p>Sekuvo can act as Android's autofill service, so sign-in and card forms offer your entries directly.</p>",
            "<p><strong>Turning it on:</strong> Sekuvo → Settings → <em>Enable autofill</em> → pick Sekuvo from the system list. The list has different names by device: on Samsung and Android 14+ it is <em>Passwords, passkeys &amp; autofill → Preferred service</em>; on stock Android it is <em>Autofill service</em>.</p>",
            "<p>After that, tapping a username, password or card field in any app shows your matching entries above the keyboard. If the vault is locked you get an unlock step first — while locked, the system is handed nothing at all.</p>",
        ]),
        ("keyboard", "Sekuvo Keyboard (inside your phone)", [
            "<p>The keyboard add-on types stored values into any field, in any app, without a copy step.</p>",
            "<p><strong>Turning it on:</strong> Sekuvo → Settings → <em>Enable the keyboard</em> → switch it on in the system list, then pick “Sekuvo Keyboard” from the keyboard switcher whenever you need it.</p>",
            "<p>Recently used entries sit on top and 🔍 searches titles, usernames and addresses (Turkish letters match their ASCII equivalents, so “sifre” finds “şifre”). While the vault is locked the keyboard shows only entries you marked for quick access — see below.</p>",
        ]),
        ("bluetooth", "Typing into a computer over Bluetooth", [
            "<p>Your phone can act as a Bluetooth keyboard and type a secret at your computer's cursor. Nothing is installed on the computer, it works on Windows, macOS and Linux, and the value never touches the clipboard or a network. Requires Android 9 or newer.</p>",
            "<h3>Step by step</h3>",
            "<ol><li>In Sekuvo, open the entry and tap the 💻 icon next to the field you want typed. <strong>Keep this screen open</strong> — your phone only announces itself as a keyboard while it is.</li><li>On the computer, add the phone as a new Bluetooth device: <em>Settings → Bluetooth &amp; devices → Add device → Bluetooth</em> on Windows, or <em>System Settings → Bluetooth</em> on macOS.</li><li>Confirm the pairing code on both sides.</li><li>Back on the phone, pick your computer from the list and wait for “Connected”.</li><li>Choose <strong>the computer's</strong> keyboard layout — not the phone's. The computer interprets the key codes, so a wrong layout silently turns characters like @ \" ? into different ones.</li><li>Click into the field on the computer where the value should go.</li><li>Tap <strong>Type</strong> on the phone. After a three-second countdown — which exists so you can click into that field — the value is typed key by key.</li></ol>",
            "<h3>Connected, but nothing is typed</h3>",
            "<p>Almost always the same cause: the computer paired with your phone <em>as a phone</em> at some earlier point, so it never enabled the keyboard (HID) service for it. The connection succeeds and the keystrokes go nowhere.</p>",
            "<ol><li>Remove the pairing on the computer (<em>Remove device</em>).</li><li>Remove it on the phone too (<em>Forget</em> in Bluetooth settings). Both sides matter.</li><li>Open the 💻 screen in Sekuvo and leave it open.</li><li>Pair again, starting from the computer.</li><li>To confirm on Windows: <em>Device Manager → Human Interface Devices</em> should now list a Bluetooth HID device.</li></ol>",
            "<p>On macOS, the first connection may open the <strong>Keyboard Setup Assistant</strong>, which asks you to press a key beside the shift key. Until that window is dismissed, macOS processes nothing — this is the usual “connected but silent” cause on a Mac.</p>",
            "<h3>Speed, and checking it</h3>",
            "<p>Keys are sent one at a time, so a long secret takes real time — the dialog shows an estimate. Three speeds are offered, and the safe one is the default on purpose. Before raising it, use <strong>⏱ Speed test</strong>: it types ten identical space-separated blocks and reports measured characters per second. If even one block differs, that speed is not safe on this computer — drop one step.</p>",
            "<p>The speed test doubles as a diagnostic: nothing typed at all means pairing, garbled characters mean the layout, a cut-off run means the speed.</p>",
            "<p>While typing you get a progress bar and a <strong>Stop</strong> button. If the send queue stalls, Sekuvo retries with backoff and, if it still fails, <em>stops and tells you</em> at which character — a secret is never silently half-typed.</p>",
        ]),
        ("lock", "How locking works", [
            "<p>The vault locks the moment the screen it is on goes dark — including folding a foldable shut. At that instant the key is wiped from memory; entry titles may still be listed, but nothing can be decrypted.</p>",
            "<p>Leaving the app while the screen stays on does <em>not</em> lock it. That is deliberate: the app, the keyboard and autofill share one session, so switching to your browser to paste a password would otherwise lock you out mid-task.</p>",
        ]),
        ("quick", "Quick access — a deliberate trade", [
            "<p>Entries you explicitly mark as “use on the keyboard without a password” are stored a second time, encrypted with a separate device key, so the keyboard can read them <em>while the vault is locked</em>.</p>",
            "<p>The trade is stated plainly: those entries are protected by your phone's screen lock, not by your master password. Keep passwords out of it. The mark is off by default; the single exception is new <strong>Everyday</strong> entries, which start marked because names and phone numbers are what you want at hand — you can switch any of them off.</p>",
        ]),
        ("backup", "Backups and restoring", [
            "<p>System backup (Google backup, device transfer) is deliberately disabled, so there is exactly one way your vault leaves the phone and it is a way you chose: <strong>Settings → Create encrypted backup</strong>.</p>",
            "<p>You pick a <em>backup password</em> — make it different from your master password, because the backup password is the one that gets typed on computers. The result is a single <code>.vaultbak</code> file you save wherever you like: Drive, an SD card, a USB stick.</p>",
            "<p>The file is device-independent: its own salt and key-derivation parameters live in its header. File plus backup password restores everything on any phone, even after a factory reset. Restore from <strong>Settings → Restore from backup</strong>, or from the welcome screen on a fresh install.</p>",
            "<p>Restoring offers <em>add to existing</em> or <em>replace all</em>. Both are checked before anything is written — a wrong password fails at the authentication step, and nothing is deleted until the new data is verified.</p>",
        ]),
        ("transfer", "Bringing secrets from a computer", [
            "<p>Typing a long key into a phone by hand is where mistakes happen. Sekuvo takes them across as an encrypted envelope instead, in two forms: text you paste, or QR codes you scan.</p>",
            "<p><strong>On the phone:</strong> the ➕ button offers <em>Import via QR</em> and <em>Import from text</em>. QR import opens the camera; frames are decoded on the device, and multi-frame transfers show progress as they are collected.</p>",
            "<h3>The computer-side tool</h3>",
            "<p>The tool that builds those envelopes is a single HTML file, and it is deliberately <strong>a download, not a website</strong>. sekuvo.com never asks you for a secret; a page that did would be exactly what a phishing site looks like.</p>",
            "<ol><li>Open the project on GitHub and go to <strong>Releases</strong>.</li><li>Download <code>aktar.html</code> from the latest release.</li><li>Check its SHA-256 against the value published beside it: <code>shasum -a 256 aktar.html</code> on macOS or Linux, <code>certutil -hashfile aktar.html SHA256</code> on Windows.</li><li>Open the file by double-clicking it. It runs from your disk — the address bar shows <code>file://</code>, not a website.</li><li>Paste your text, set a transfer password, and it produces the envelope as text or as QR codes.</li><li>On the phone, scan or paste, enter the same password, and choose add or replace.</li></ol>",
            "<p>All of the encryption happens inside your browser, on your machine. There is also <code>vault-clip.py</code> for the command line, which does the same from the clipboard or a file and can render the QR codes in a terminal.</p>",
            "<h3>If you would rather not use the tool</h3>",
            "<p>The envelope is an open format, not something only Sekuvo can make: PBKDF2-HMAC-SHA256 over 310,000 rounds, AES-256-GCM, wrapped in a small JSON object. You can build it yourself from about thirty lines you have read, and paste the result into <em>Import from text</em> \u2014 the app has no way to tell which tool produced it, and does not care.</p>",
            "<p>The recipe is in the repository: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (written in Turkish).</p>",
        ]),
        ("log", "Usage log", [
            "<p>Sekuvo records which field of which entry went where and when: to the clipboard, to a computer over Bluetooth (with the target device's name), or typed into an app from the keyboard. When a computer is compromised, this answers “what went there, what do I need to change”.</p>",
            "<p>The log is encrypted with the same key as your entries and <strong>values are never written to it</strong> — only the type of event, the field name and the destination. Deleting an entry deletes its log, and you can clear the whole thing from Settings.</p>",
        ]),
        ("generator", "Password generator", [
            "<p>Reachable from the 🎲 icon on the home screen, or beside the password field while editing an entry. It uses a cryptographic random source, produces 8–64 characters, lets you choose character classes, can drop look-alike characters, and shows the resulting entropy in bits.</p>",
        ]),
    ],
)

# ─────────────────────────────── Türkçe ─────────────────────────────────────
G["tr"] = dict(
    nav_label="Kılavuz",
    title="Sekuvo — Kılavuz",
    desc="Sekuvo nasıl kullanılır: ilk açılış, otomatik doldurma, klavye, Bluetooth ile bilgisayara yazma, yedekleme ve aktarım.",
    h1="Kılavuz",
    lede="Sekuvo'nun yaptığı her şey, muhtemelen ihtiyaç duyacağın sırayla. Buradaki hiçbir şey hesap ya da internet bağlantısı gerektirmez.",
    back="← sekuvo.com'a dön",
    sections=[
        ("start", "İlk açılış", [
            "<p>İlk açılışta bir <strong>ana parola</strong> belirlersin. Kaydettiğin her sır ondan türetilen bir anahtarla şifrelenir; yani Sekuvo'nun senin için kurtaramayacağı tek şey odur — devam etmeden önce güvenli bir yere yaz.</p>",
            "<p>Başka bir telefondan yedeğin var mı? Karşılama ekranındaki <strong>“Yedeğim var — geri yükle”</strong> bağlantısına dokun. Önce bu cihaz için yine bir ana parola belirlersin, hemen ardından dosya seçici kendiliğinden açılır ve kayıtların geri gelir.</p>",
            "<p>Telefonunda parmak izi ya da yüz tanıma varsa Sekuvo kurulumdan hemen sonra bunu kullanmayı teklif eder. Bu yalnızca bir kolaylık katmanıdır: ana parola her zaman çalışır ve cihaz sıfırlansa bile ayakta kalan odur.</p>",
        ]),
        ("entries", "Neleri saklayabilirsin", [
            "<p>Dört kayıt türü, bir kasada tutulanların çoğunu karşılar:</p>",
            "<ul><li><strong>Hesap / Şifre</strong> — kullanıcı adı, şifre, site ya da uygulama.</li><li><strong>Gündelik</strong> — ad soyad, telefon, e-posta, adres. Formların sürekli istediği şeyler.</li><li><strong>Kart</strong> — kart numarası, son kullanma, CVV, IBAN.</li><li><strong>Güvenli not</strong> — serbest metin; betik, anahtar, kurtarma kodu ve yapılandırma dosyası alt türleriyle.</li></ul>",
            "<p>Hesap ve Gündelik kayıtları ayrıca <strong>ek alan</strong> kabul eder: istediğin kadar “alan adı + değer” çifti. Ek alanlar da yerleşik alanlarla birebir aynı şekilde şifrelenir ve onların göründüğü her yerde görünür.</p>",
        ]),
        ("channels", "Sırrı panoya uğratmadan kullanmak", [
            "<p>Pano başka uygulamalarca okunabilir ve sırların çalındığı yerdir. Sekuvo bunun yerine değeri doğrudan hedefine ulaştıran üç yol sunar. Kopyalamayı da kullanabilirsin — pano 45 saniye sonra otomatik temizlenir — ama uygulamanın var olma sebebi aşağıdaki üç kanaldır.</p>",
        ]),
        ("autofill", "Otomatik doldurma (telefonun içinde)", [
            "<p>Sekuvo, Android'in otomatik doldurma servisi olarak çalışabilir; böylece giriş ve kart formları kayıtlarını doğrudan sunar.</p>",
            "<p><strong>Açmak için:</strong> Sekuvo → Ayarlar → <em>Otomatik doldurmayı etkinleştir</em> → açılan sistem listesinden Sekuvo'yu seç. Listenin adı cihaza göre değişir: Samsung ve Android 14+ cihazlarda <em>Şifreler, parolalar ve otomatik doldurma → Tercih edilen servis</em>, saf Android'de <em>Otomatik doldurma servisi</em>.</p>",
            "<p>Sonrasında herhangi bir uygulamada kullanıcı adı, şifre ya da kart alanına dokunduğunda eşleşen kayıtların klavyenin üstünde çıkar. Kasa kilitliyse önce kilit açma adımı gelir — kilitliyken sisteme hiçbir değer verilmez.</p>",
        ]),
        ("keyboard", "Sekuvo Klavyesi (telefonun içinde)", [
            "<p>Klavye eklentisi, kayıtlı değerleri herhangi bir uygulamada herhangi bir alana kopyalama adımı olmadan yazar.</p>",
            "<p><strong>Açmak için:</strong> Sekuvo → Ayarlar → <em>Klavyeyi etkinleştir</em> → sistem listesinden aç, sonra ihtiyaç duyduğunda klavye değiştiriciden “Sekuvo Klavyesi”ni seç.</p>",
            "<p>Son kullandığın kayıtlar en üstte durur; 🔍 ile başlık, kullanıcı adı ve adres üzerinde arama yapılır (Türkçe harfler ASCII karşılıklarıyla eşleşir, “sifre” yazınca “şifre” bulunur). Kasa kilitliyken klavye yalnızca hızlı erişim işaretli kayıtları gösterir — aşağıya bak.</p>",
        ]),
        ("bluetooth", "Bluetooth ile bilgisayara yazma", [
            "<p>Telefonun Bluetooth klavye gibi davranıp bir sırrı bilgisayarındaki imlecin olduğu yere yazabilir. Bilgisayara hiçbir şey kurulmaz; Windows, macOS ve Linux'ta çalışır; değer ne panodan ne ağdan geçer. Android 9 ve üzeri gerekir.</p>",
            "<h3>Adım adım</h3>",
            "<ol><li>Sekuvo'da kaydı aç ve yazdırmak istediğin alanın yanındaki 💻 simgesine dokun. <strong>Bu ekranı açık tut</strong> — telefon kendini yalnızca bu ekran açıkken klavye olarak duyurur.</li><li>Bilgisayarda telefonu <em>yeni bir Bluetooth cihazı</em> olarak ekle: Windows'ta <em>Ayarlar → Bluetooth ve cihazlar → Cihaz ekle → Bluetooth</em>, macOS'ta <em>Sistem Ayarları → Bluetooth</em>.</li><li>Eşleşme kodunu iki tarafta da onayla.</li><li>Telefona dön, listeden bilgisayarını seç ve “Bağlı” yazmasını bekle.</li><li><strong>Bilgisayarın</strong> klavye düzenini seç — telefonunkini değil. Tuş kodlarını bilgisayar yorumlar; yanlış düzende @ \" ? gibi karakterler sessizce başkasına dönüşür.</li><li>Bilgisayarda, değerin gideceği kutuya tıkla.</li><li>Telefonda <strong>Yaz</strong>'a bas. Üç saniyelik geri sayımdan sonra — ki o üç saniye tam da o kutuya tıklayabilmen için vardır — değer tuş tuş yazılır.</li></ol>",
            "<h3>Bağlı görünüyor ama hiçbir şey yazmıyor</h3>",
            "<p>Neredeyse her zaman aynı sebep: bilgisayar telefonunu daha önce bir noktada <em>telefon olarak</em> eşleştirmiş, dolayısıyla onun için klavye (HID) servisini hiç açmamış. Bağlantı kurulur, tuşlar gider, hiçbir yere varmaz.</p>",
            "<ol><li>Bilgisayarda eşleşmeyi kaldır (<em>Cihazı kaldır</em>).</li><li>Telefonda da kaldır (Bluetooth ayarlarında <em>Eşleştirmeyi unut</em>). İki taraf da önemli.</li><li>Sekuvo'daki 💻 ekranını aç ve açık bırak.</li><li>Eşleştirmeyi <strong>bilgisayardan başlatarak</strong> yeniden yap.</li><li>Windows'ta doğrulaması: <em>Aygıt Yöneticisi → İnsan Arabirim Aygıtları</em> altında artık bir Bluetooth HID aygıtı görünmeli.</li></ol>",
            "<p>macOS'ta ilk bağlantıda <strong>Klavye Kurulum Yardımcısı</strong> açılabilir ve shift tuşunun yanındaki tuşa basmanı ister. O pencere kapanana kadar macOS hiçbir tuşu işlemez — Mac'te “bağlı ama sessiz” durumunun olağan sebebi budur.</p>",
            "<h3>Hız ve hızın denetlenmesi</h3>",
            "<p>Tuşlar tek tek gönderilir, dolayısıyla uzun bir sır gerçekten zaman alır — diyalog tahmini süreyi gösterir. Üç hız sunulur ve güvenli olanın varsayılan olması bilinçlidir. Hızı artırmadan önce <strong>⏱ Hız testi</strong>'ni kullan: boşlukla ayrılmış on özdeş blok yazar ve ölçülen karakter/sn'yi bildirir. Bloklardan biri bile farklıysa o hız bu bilgisayarda güvenli değildir — bir alt kademeye in.</p>",
            "<p>Hız testi aynı zamanda teşhis aracıdır: hiç yazmıyorsa sorun eşleştirmede, karakterler bozuksa düzende, yazma yarıda kesiliyorsa hızdadır.</p>",
            "<p>Yazma sırasında ilerleme çubuğu ve <strong>Durdur</strong> düğmesi vardır. Gönderim kuyruğu tıkanırsa Sekuvo geri çekilerek tekrar dener; yine olmazsa <em>durur ve kaçıncı karakterde durduğunu söyler</em> — bir sır asla sessizce yarım yazılmaz.</p>",
        ]),
        ("lock", "Kilit nasıl çalışır", [
            "<p>Kasa, üzerinde bulunduğu ekran karardığı anda kilitlenir — katlanabilir bir cihazı kapatmak da buna dahildir. O anda anahtar bellekten silinir; kayıt başlıkları hâlâ listelenebilir ama hiçbir şey çözülemez.</p>",
            "<p>Ekran açıkken uygulamadan çıkmak kilitlemez. Bu bilinçlidir: uygulama, klavye ve otomatik doldurma aynı oturumu paylaşır; aksi hâlde bir şifreyi yapıştırmak için tarayıcıya geçmen işin ortasında seni dışarıda bırakırdı.</p>",
        ]),
        ("quick", "Hızlı erişim — bilinçli bir takas", [
            "<p>“Klavyede parolasız kullan” diye işaretlediğin kayıtlar ikinci kez, ayrı bir cihaz anahtarıyla şifrelenip saklanır; böylece klavye onları <em>kasa kilitliyken</em> okuyabilir.</p>",
            "<p>Takas açıkça yazılıdır: o kayıtları koruyan şey ana parolan değil, telefonunun ekran kilidi olur. Şifreleri buraya koyma. İşaret varsayılan olarak kapalıdır; tek istisna yeni <strong>Gündelik</strong> kayıtlarıdır — ad ve telefon numarası zaten el altında olsun istenen şeylerdir, ama istediğini tek tek kapatabilirsin.</p>",
        ]),
        ("backup", "Yedekleme ve geri yükleme", [
            "<p>Sistem yedeklemesi (Google yedekleme, cihaz aktarımı) bilinçli olarak kapalıdır; böylece kasanın telefondan çıkma yolu tektir ve senin seçtiğin yoldur: <strong>Ayarlar → Şifreli yedek oluştur</strong>.</p>",
            "<p>Bir <em>yedek parolası</em> belirlersin — ana parolandan farklı olsun, çünkü bilgisayarlarda yazılan parola yedek parolasıdır. Sonuç, istediğin yere kaydedeceğin tek bir <code>.vaultbak</code> dosyasıdır: Drive, SD kart, USB bellek.</p>",
            "<p>Dosya cihazdan bağımsızdır: kendi tuzu ve anahtar türetme parametreleri başlığında durur. Dosya artı yedek parolası, cihaz sıfırlanmış olsa bile her telefonda her şeyi geri getirir. Geri yükleme <strong>Ayarlar → Yedekten geri yükle</strong>'den, temiz kurulumda ise karşılama ekranından yapılır.</p>",
            "<p>Geri yükleme <em>mevcuta ekle</em> ya da <em>tümünü değiştir</em> sunar. İkisi de hiçbir şey yazılmadan önce denetlenir — yanlış parola doğrulama aşamasında düşer ve yeni veri doğrulanmadan hiçbir şey silinmez.</p>",
        ]),
        ("transfer", "Bilgisayardan sır getirmek", [
            "<p>Uzun bir anahtarı telefona elle yazmak, hataların çıktığı yerdir. Sekuvo bunun yerine sırları şifreli bir zarf hâlinde taşır; iki biçimde: yapıştırdığın metin ya da taradığın QR kodları.</p>",
            "<p><strong>Telefonda:</strong> ➕ düğmesi <em>QR ile içe aktar</em> ve <em>Metinden içe aktar</em> seçeneklerini sunar. QR içe aktarma kamerayı açar; kareler cihazda çözülür ve çok kareli aktarımlarda toplanma ilerlemesi gösterilir.</p>",
            "<h3>Bilgisayar tarafındaki araç</h3>",
            "<p>Bu zarfları üreten araç tek bir HTML dosyasıdır ve bilinçli olarak <strong>bir web sayfası değil, indirilen bir dosyadır</strong>. sekuvo.com senden asla bir sır istemez; isteyen bir sayfa, tam olarak bir kimlik avı sitesinin göründüğü gibi görünürdü.</p>",
            "<ol><li>Projeyi GitHub'da aç ve <strong>Releases</strong> bölümüne git.</li><li>Son sürümden <code>aktar.html</code> dosyasını indir.</li><li>Yanında yayınlanan SHA-256 özetiyle karşılaştır: macOS ve Linux'ta <code>shasum -a 256 aktar.html</code>, Windows'ta <code>certutil -hashfile aktar.html SHA256</code>.</li><li>Dosyayı çift tıklayarak aç. Kendi diskinden çalışır — adres çubuğunda bir site değil <code>file://</code> yazar.</li><li>Metnini yapıştır, bir aktarım parolası belirle; araç zarfı metin ya da QR kodları olarak üretir.</li><li>Telefonda tara ya da yapıştır, aynı parolayı gir, ekle ya da değiştir'i seç.</li></ol>",
            "<p>Şifrelemenin tamamı kendi makinende, tarayıcının içinde olur. Komut satırı için ayrıca <code>vault-clip.py</code> vardır; aynı işi panodan ya da bir dosyadan yapar ve QR kodlarını terminalde çizebilir.</p>",
            "<h3>Aracı hiç kullanmak istemiyorsan</h3>",
            "<p>Zarf, yalnız Sekuvo'nun üretebildiği bir şey değil, açık bir biçimdir: 310.000 turluk PBKDF2-HMAC-SHA256, AES-256-GCM, küçük bir JSON'un içinde. Onu kendi okuduğun otuz satırla da üretebilir, sonucu <em>Metinden içe aktar</em>'a yapıştırabilirsin \u2014 uygulamanın hangi araçla üretildiğini anlamasının yolu yok, umursamıyor da.</p>",
            "<p>Tarifi depoda: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a>.</p>",
        ]),
        ("log", "Kullanım günlüğü", [
            "<p>Sekuvo, hangi kaydın hangi alanının ne zaman nereye gittiğini tutar: panoya, Bluetooth ile bilgisayara (hedef cihazın adıyla) ya da klavyeden hangi uygulamaya. Bir bilgisayar ele geçtiğinde “oraya ne gitti, neyi değiştirmem gerek” sorusunun cevabı budur.</p>",
            "<p>Günlük, kayıtlarınla aynı anahtarla şifrelidir ve <strong>değerlerin kendisi hiçbir koşulda yazılmaz</strong> — yalnızca olayın türü, alan adı ve hedef. Bir kaydı silmek günlüğünü de siler; tamamını Ayarlar'dan temizleyebilirsin.</p>",
        ]),
        ("generator", "Şifre üretici", [
            "<p>Ana ekrandaki 🎲 simgesinden ya da kayıt düzenlerken şifre alanının yanından açılır. Kriptografik rastgelelik kullanır, 8–64 karakter üretir, karakter sınıflarını seçtirir, birbirine benzeyen karakterleri eleyebilir ve sonucun entropisini bit olarak gösterir.</p>",
        ]),
    ],
)

# ─────────────────────────────── Español ────────────────────────────────────
G["es"] = dict(
    nav_label="Guía",
    title="Sekuvo — Guía",
    desc="Cómo usar Sekuvo: primer inicio, autocompletado, teclado, escribir en un ordenador por Bluetooth, copias y transferencias.",
    h1="Guía",
    lede="Todo lo que hace Sekuvo, en el orden en que probablemente lo necesites. Nada de esto requiere una cuenta ni conexión a internet.",
    back="← Volver a sekuvo.com",
    sections=[
        ("start", "Primer inicio", [
            "<p>Al abrir la aplicación por primera vez defines una <strong>contraseña maestra</strong>. Todo lo que guardes se cifra con una clave derivada de ella, así que es lo único que Sekuvo no puede recuperar por ti — anótala en un lugar seguro antes de seguir.</p>",
            "<p>¿Ya tienes una copia de otro teléfono? Toca <strong>«Tengo una copia — restaurarla»</strong> en la pantalla de bienvenida. Primero defines igualmente una contraseña maestra para este dispositivo y, justo después, se abre el selector de archivos y tus entradas vuelven.</p>",
            "<p>Si tu teléfono tiene huella o reconocimiento facial, Sekuvo te ofrece usarlo tras la configuración. Es solo una capa de comodidad: la contraseña maestra siempre funciona y es la que sobrevive a un restablecimiento de fábrica.</p>",
        ]),
        ("entries", "Qué puedes guardar", [
            "<p>Cuatro tipos de entrada cubren casi todo lo que se guarda en una bóveda:</p>",
            "<ul><li><strong>Cuenta / Contraseña</strong> — usuario, contraseña, sitio o aplicación.</li><li><strong>Cotidiano</strong> — nombre, teléfono, correo, dirección. Lo que los formularios piden todo el tiempo.</li><li><strong>Tarjeta</strong> — número, caducidad, CVV, IBAN.</li><li><strong>Nota segura</strong> — texto libre, con subtipos para scripts, claves, códigos de recuperación y archivos de configuración.</li></ul>",
            "<p>Las entradas de Cuenta y Cotidiano admiten además <strong>campos personalizados</strong>: cualquier par «nombre + valor». Se cifran igual que los campos integrados y aparecen en los mismos sitios.</p>",
        ]),
        ("channels", "Usar un secreto sin el portapapeles", [
            "<p>El portapapeles puede leerlo otras aplicaciones y es donde se roban los secretos. Sekuvo te da tres formas de llevar el valor directamente a su destino. También puedes copiar — el portapapeles se limpia solo a los 45 segundos — pero los tres canales siguientes son la razón de ser de la aplicación.</p>",
        ]),
        ("autofill", "Autocompletado (dentro del teléfono)", [
            "<p>Sekuvo puede actuar como servicio de autocompletado de Android, de modo que los formularios de inicio de sesión y de tarjeta ofrezcan tus entradas directamente.</p>",
            "<p><strong>Para activarlo:</strong> Sekuvo → Ajustes → <em>Activar autocompletado</em> → elige Sekuvo en la lista del sistema. Esa lista cambia de nombre según el dispositivo: en Samsung y Android 14+ es <em>Contraseñas, claves de acceso y autocompletado → Servicio preferido</em>; en Android puro, <em>Servicio de autocompletado</em>.</p>",
            "<p>Después, al tocar un campo de usuario, contraseña o tarjeta en cualquier aplicación verás tus entradas coincidentes sobre el teclado. Si la bóveda está bloqueada, primero aparece el desbloqueo — mientras está bloqueada, el sistema no recibe absolutamente nada.</p>",
        ]),
        ("keyboard", "Teclado Sekuvo (dentro del teléfono)", [
            "<p>El complemento de teclado escribe los valores guardados en cualquier campo, en cualquier aplicación, sin paso de copiado.</p>",
            "<p><strong>Para activarlo:</strong> Sekuvo → Ajustes → <em>Activar el teclado</em> → actívalo en la lista del sistema y luego elige «Teclado Sekuvo» en el selector de teclados cuando lo necesites.</p>",
            "<p>Las entradas recientes quedan arriba y 🔍 busca en títulos, usuarios y direcciones. Con la bóveda bloqueada, el teclado muestra solo las entradas marcadas para acceso rápido — más abajo.</p>",
        ]),
        ("bluetooth", "Escribir en un ordenador por Bluetooth", [
            "<p>Tu teléfono puede actuar como teclado Bluetooth y escribir un secreto donde esté el cursor del ordenador. No se instala nada en el ordenador, funciona en Windows, macOS y Linux, y el valor no pasa por el portapapeles ni por la red. Requiere Android 9 o posterior.</p>",
            "<h3>Paso a paso</h3>",
            "<ol><li>En Sekuvo, abre la entrada y toca el icono 💻 junto al campo que quieres escribir. <strong>Deja esta pantalla abierta</strong>: el teléfono solo se anuncia como teclado mientras lo está.</li><li>En el ordenador, añade el teléfono como dispositivo Bluetooth nuevo: <em>Configuración → Bluetooth y dispositivos → Agregar dispositivo → Bluetooth</em> en Windows, o <em>Ajustes del Sistema → Bluetooth</em> en macOS.</li><li>Confirma el código de emparejamiento en ambos lados.</li><li>Vuelve al teléfono, elige tu ordenador de la lista y espera a que diga «Conectado».</li><li>Elige la distribución de teclado <strong>del ordenador</strong>, no la del teléfono. El ordenador interpreta los códigos de tecla, así que una distribución equivocada convierte en silencio caracteres como @ \" ? en otros.</li><li>Haz clic en el campo del ordenador donde debe ir el valor.</li><li>Toca <strong>Escribir</strong> en el teléfono. Tras una cuenta atrás de tres segundos — que existe para que puedas hacer ese clic — el valor se escribe tecla a tecla.</li></ol>",
            "<h3>Dice «conectado», pero no escribe nada</h3>",
            "<p>Casi siempre por lo mismo: el ordenador emparejó tu teléfono <em>como teléfono</em> en algún momento anterior, así que nunca habilitó para él el servicio de teclado (HID). La conexión se establece, las pulsaciones salen y no llegan a ninguna parte.</p>",
            "<ol><li>Quita el emparejamiento en el ordenador (<em>Quitar dispositivo</em>).</li><li>Quítalo también en el teléfono (<em>Olvidar</em> en los ajustes de Bluetooth). Importan los dos lados.</li><li>Abre la pantalla 💻 en Sekuvo y déjala abierta.</li><li>Vuelve a emparejar, empezando <strong>desde el ordenador</strong>.</li><li>Para comprobarlo en Windows: en <em>Administrador de dispositivos → Dispositivos de interfaz de usuario (HID)</em> debe aparecer ahora un dispositivo HID Bluetooth.</li></ol>",
            "<p>En macOS, la primera conexión puede abrir el <strong>Asistente de Configuración del Teclado</strong>, que pide pulsar una tecla junto a la de mayúsculas. Hasta cerrar esa ventana, macOS no procesa nada — es la causa habitual del «conectado pero mudo» en un Mac.</p>",
            "<h3>Velocidad y cómo comprobarla</h3>",
            "<p>Las teclas se envían una a una, así que un secreto largo tarda de verdad — el diálogo muestra una estimación. Hay tres velocidades y que la segura sea la predeterminada es intencionado. Antes de subirla, usa la <strong>⏱ Prueba de velocidad</strong>: escribe diez bloques idénticos separados por espacios e informa de los caracteres por segundo medidos. Si un solo bloque difiere, esa velocidad no es segura en ese ordenador — baja un escalón.</p>",
            "<p>La prueba sirve además como diagnóstico: si no escribe nada, el problema es el emparejamiento; si los caracteres salen mal, la distribución; si se corta, la velocidad.</p>",
            "<p>Durante la escritura hay una barra de progreso y un botón <strong>Detener</strong>. Si la cola de envío se atasca, Sekuvo reintenta con espera creciente y, si aun así falla, <em>se detiene y te dice</em> en qué carácter — un secreto nunca queda escrito a medias en silencio.</p>",
        ]),
        ("lock", "Cómo funciona el bloqueo", [
            "<p>La bóveda se bloquea en cuanto se apaga la pantalla en la que está — incluido plegar un móvil plegable. En ese instante la clave se borra de la memoria; los títulos pueden seguir listados, pero nada puede descifrarse.</p>",
            "<p>Salir de la aplicación con la pantalla encendida <em>no</em> la bloquea. Es deliberado: la aplicación, el teclado y el autocompletado comparten una sesión; de lo contrario, cambiar al navegador para pegar una contraseña te dejaría fuera a mitad de la tarea.</p>",
        ]),
        ("quick", "Acceso rápido — un intercambio consciente", [
            "<p>Las entradas que marcas como «usar en el teclado sin contraseña» se guardan una segunda vez, cifradas con una clave de dispositivo aparte, para que el teclado pueda leerlas <em>con la bóveda bloqueada</em>.</p>",
            "<p>El intercambio se dice sin rodeos: esas entradas quedan protegidas por el bloqueo de pantalla del teléfono, no por tu contraseña maestra. No pongas contraseñas ahí. La marca está desactivada por defecto; la única excepción son las entradas <strong>Cotidiano</strong> nuevas, que empiezan marcadas porque nombres y teléfonos son justo lo que quieres a mano — puedes desactivarlas una a una.</p>",
        ]),
        ("backup", "Copias de seguridad y restauración", [
            "<p>La copia del sistema (copia de Google, transferencia de dispositivo) está desactivada a propósito, así que hay exactamente una forma de que tu bóveda salga del teléfono y es la que tú eliges: <strong>Ajustes → Crear copia cifrada</strong>.</p>",
            "<p>Defines una <em>contraseña de copia</em> — que sea distinta de la maestra, porque la de copia es la que se acaba escribiendo en ordenadores. El resultado es un único archivo <code>.vaultbak</code> que guardas donde quieras: Drive, una tarjeta SD, un USB.</p>",
            "<p>El archivo es independiente del dispositivo: su propia sal y sus parámetros de derivación viven en su cabecera. Archivo más contraseña de copia restauran todo en cualquier teléfono, incluso tras un restablecimiento de fábrica. Restaura desde <strong>Ajustes → Restaurar desde copia</strong>, o desde la pantalla de bienvenida en una instalación nueva.</p>",
            "<p>Al restaurar puedes <em>añadir a lo existente</em> o <em>reemplazar todo</em>. Ambas se verifican antes de escribir nada — una contraseña incorrecta falla en la autenticación y no se borra nada hasta que los datos nuevos están comprobados.</p>",
        ]),
        ("transfer", "Traer secretos desde un ordenador", [
            "<p>Teclear a mano una clave larga en el teléfono es donde aparecen los errores. Sekuvo los pasa como un sobre cifrado, en dos formas: texto que pegas o códigos QR que escaneas.</p>",
            "<p><strong>En el teléfono:</strong> el botón ➕ ofrece <em>Importar por QR</em> e <em>Importar desde texto</em>. La importación por QR abre la cámara; los fotogramas se decodifican en el dispositivo y las transferencias de varios códigos muestran el progreso.</p>",
            "<h3>La herramienta del ordenador</h3>",
            "<p>La herramienta que crea esos sobres es un único archivo HTML y es, a propósito, <strong>una descarga, no un sitio web</strong>. sekuvo.com nunca te pide un secreto; una página que lo hiciera se parecería exactamente a un sitio de phishing.</p>",
            "<ol><li>Abre el proyecto en GitHub y ve a <strong>Releases</strong>.</li><li>Descarga <code>aktar.html</code> de la última versión.</li><li>Comprueba su SHA-256 con el valor publicado al lado: <code>shasum -a 256 aktar.html</code> en macOS o Linux, <code>certutil -hashfile aktar.html SHA256</code> en Windows.</li><li>Abre el archivo con doble clic. Se ejecuta desde tu disco — la barra de direcciones muestra <code>file://</code>, no un sitio web.</li><li>Pega tu texto, define una contraseña de transferencia y la herramienta produce el sobre como texto o como códigos QR.</li><li>En el teléfono, escanea o pega, introduce la misma contraseña y elige añadir o reemplazar.</li></ol>",
            "<p>Todo el cifrado ocurre dentro de tu navegador, en tu máquina. También existe <code>vault-clip.py</code> para la línea de comandos, que hace lo mismo desde el portapapeles o un archivo y puede dibujar los QR en la terminal.</p>",
            "<h3>Si prefieres no usar la herramienta</h3>",
            "<p>El sobre es un formato abierto, no algo que solo Sekuvo pueda crear: PBKDF2-HMAC-SHA256 con 310.000 rondas, AES-256-GCM, envuelto en un pequeño objeto JSON. Puedes construirlo tú mismo con unas treinta líneas que hayas leído y pegar el resultado en <em>Importar desde texto</em> \u2014 la aplicación no tiene forma de saber qué herramienta lo produjo, ni le importa.</p>",
            "<p>La receta está en el repositorio: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (escrita en turco).</p>",
        ]),
        ("log", "Registro de uso", [
            "<p>Sekuvo anota qué campo de qué entrada fue a dónde y cuándo: al portapapeles, a un ordenador por Bluetooth (con el nombre del dispositivo) o escrito en una aplicación desde el teclado. Cuando un ordenador se ve comprometido, esto responde a «qué llegó allí y qué tengo que cambiar».</p>",
            "<p>El registro se cifra con la misma clave que tus entradas y <strong>los valores nunca se escriben en él</strong>: solo el tipo de evento, el nombre del campo y el destino. Borrar una entrada borra su registro, y puedes vaciarlo entero desde Ajustes.</p>",
        ]),
        ("generator", "Generador de contraseñas", [
            "<p>Accesible desde el icono 🎲 de la pantalla principal o junto al campo de contraseña al editar una entrada. Usa una fuente criptográfica de aleatoriedad, produce de 8 a 64 caracteres, permite elegir clases de caracteres, puede descartar caracteres que se confunden entre sí y muestra la entropía resultante en bits.</p>",
        ]),
    ],
)

# ─────────────────────────────── हिन्दी ──────────────────────────────────────
G["hi"] = dict(
    nav_label="मार्गदर्शिका",
    title="Sekuvo — मार्गदर्शिका",
    desc="Sekuvo कैसे इस्तेमाल करें: पहली बार खोलना, ऑटोफ़िल, कीबोर्ड, ब्लूटूथ से कंप्यूटर में टाइप करना, बैकअप और स्थानांतरण।",
    h1="मार्गदर्शिका",
    lede="Sekuvo जो कुछ करता है, उसी क्रम में जिस क्रम में आपको ज़रूरत पड़ेगी। इसमें से किसी के लिए खाता या इंटरनेट कनेक्शन नहीं चाहिए।",
    back="← sekuvo.com पर वापस",
    sections=[
        ("start", "पहली बार खोलना", [
            "<p>पहली बार खोलने पर आप एक <strong>मास्टर पासवर्ड</strong> तय करते हैं। आपका हर राज़ उसी से बनी कुंजी से एन्क्रिप्ट होता है — यानी यही एक चीज़ है जिसे Sekuvo आपके लिए वापस नहीं ला सकता। आगे बढ़ने से पहले इसे किसी सुरक्षित जगह लिख लें।</p>",
            "<p>क्या दूसरे फ़ोन का बैकअप है? स्वागत स्क्रीन पर <strong>“मेरे पास बैकअप है — पुनर्स्थापित करें”</strong> पर टैप करें। इस डिवाइस के लिए मास्टर पासवर्ड फिर भी पहले तय होता है, उसके तुरंत बाद फ़ाइल चयनकर्ता अपने आप खुलता है और आपकी एंट्री लौट आती हैं।</p>",
            "<p>अगर आपके फ़ोन में फ़िंगरप्रिंट या फ़ेस सेंसर है, तो सेटअप के बाद Sekuvo उसे इस्तेमाल करने का सुझाव देता है। यह केवल सुविधा की परत है: मास्टर पासवर्ड हमेशा काम करता है और फ़ैक्ट्री रीसेट के बाद भी वही बचता है।</p>",
        ]),
        ("entries", "आप क्या रख सकते हैं", [
            "<p>चार एंट्री प्रकार वह सब कवर करते हैं जो आम तौर पर तिजोरी में रखा जाता है:</p>",
            "<ul><li><strong>खाता / पासवर्ड</strong> — उपयोगकर्ता नाम, पासवर्ड, साइट या ऐप।</li><li><strong>रोज़मर्रा</strong> — नाम, फ़ोन, ईमेल, पता। वही चीज़ें जो फ़ॉर्म बार-बार माँगते हैं।</li><li><strong>कार्ड</strong> — कार्ड नंबर, समाप्ति, CVV, IBAN।</li><li><strong>सुरक्षित नोट</strong> — खुला पाठ; स्क्रिप्ट, कुंजी, रिकवरी कोड और कॉन्फ़िग फ़ाइलों के उप-प्रकारों के साथ।</li></ul>",
            "<p>खाता और रोज़मर्रा एंट्री में <strong>अपने बनाए फ़ील्ड</strong> भी जोड़े जा सकते हैं: जितने चाहें “नाम + मान” जोड़े। ये भी अंतर्निहित फ़ील्ड जितने ही एन्क्रिप्टेड होते हैं और वहीं दिखते हैं जहाँ बाक़ी।</p>",
        ]),
        ("channels", "क्लिपबोर्ड के बिना राज़ इस्तेमाल करना", [
            "<p>क्लिपबोर्ड दूसरे ऐप पढ़ सकते हैं और वहीं राज़ चोरी होते हैं। Sekuvo इसके बजाय मान को सीधे उसकी मंज़िल तक पहुँचाने के तीन रास्ते देता है। कॉपी करना भी उपलब्ध है — क्लिपबोर्ड 45 सेकंड बाद अपने आप साफ़ हो जाता है — पर ऐप के होने की वजह नीचे दिए तीन रास्ते हैं।</p>",
        ]),
        ("autofill", "ऑटोफ़िल (फ़ोन के भीतर)", [
            "<p>Sekuvo, Android की ऑटोफ़िल सेवा बन सकता है, ताकि साइन-इन और कार्ड फ़ॉर्म सीधे आपकी एंट्री दिखाएँ।</p>",
            "<p><strong>चालू करने के लिए:</strong> Sekuvo → सेटिंग्स → <em>ऑटोफ़िल सक्षम करें</em> → सिस्टम सूची में से Sekuvo चुनें। सूची का नाम डिवाइस के अनुसार बदलता है: Samsung और Android 14+ पर <em>पासवर्ड, पासकी और ऑटोफ़िल → पसंदीदा सेवा</em>; शुद्ध Android पर <em>ऑटोफ़िल सेवा</em>।</p>",
            "<p>इसके बाद किसी भी ऐप में उपयोगकर्ता नाम, पासवर्ड या कार्ड फ़ील्ड पर टैप करते ही आपकी मेल खाती एंट्री कीबोर्ड के ऊपर दिखती हैं। तिजोरी लॉक हो तो पहले अनलॉक का चरण आता है — लॉक रहते सिस्टम को कुछ भी नहीं दिया जाता।</p>",
        ]),
        ("keyboard", "Sekuvo कीबोर्ड (फ़ोन के भीतर)", [
            "<p>कीबोर्ड ऐड-ऑन सहेजे गए मानों को किसी भी ऐप के किसी भी फ़ील्ड में, कॉपी किए बिना टाइप करता है।</p>",
            "<p><strong>चालू करने के लिए:</strong> Sekuvo → सेटिंग्स → <em>कीबोर्ड सक्षम करें</em> → सिस्टम सूची में चालू करें, फिर ज़रूरत पड़ने पर कीबोर्ड स्विचर से “Sekuvo कीबोर्ड” चुनें।</p>",
            "<p>हाल में इस्तेमाल की गई एंट्री ऊपर रहती हैं और 🔍 शीर्षक, उपयोगकर्ता नाम व पते में खोजता है। तिजोरी लॉक होने पर कीबोर्ड केवल त्वरित पहुँच के लिए चिह्नित एंट्री दिखाता है — नीचे देखें।</p>",
        ]),
        ("bluetooth", "ब्लूटूथ से कंप्यूटर में टाइप करना", [
            "<p>आपका फ़ोन ब्लूटूथ कीबोर्ड बनकर कंप्यूटर के कर्सर पर राज़ टाइप कर सकता है। कंप्यूटर पर कुछ भी इंस्टॉल नहीं होता; Windows, macOS और Linux पर चलता है; और मान न क्लिपबोर्ड से गुज़रता है, न नेटवर्क से। Android 9 या नया चाहिए।</p>",
            "<h3>चरण दर चरण</h3>",
            "<ol><li>Sekuvo में एंट्री खोलें और जिस फ़ील्ड को टाइप कराना है उसके पास 💻 आइकन दबाएँ। <strong>यह स्क्रीन खुली रखें</strong> — फ़ोन खुद को कीबोर्ड के रूप में तभी घोषित करता है।</li><li>कंप्यूटर पर फ़ोन को <em>नया ब्लूटूथ डिवाइस</em> जोड़ें: Windows में <em>सेटिंग्स → ब्लूटूथ और डिवाइस → डिवाइस जोड़ें → ब्लूटूथ</em>, macOS में <em>सिस्टम सेटिंग्स → ब्लूटूथ</em>।</li><li>दोनों तरफ़ पेयरिंग कोड की पुष्टि करें।</li><li>फ़ोन पर लौटें, सूची से अपना कंप्यूटर चुनें और “कनेक्टेड” आने तक रुकें।</li><li><strong>कंप्यूटर का</strong> कीबोर्ड लेआउट चुनें — फ़ोन का नहीं। की-कोड कंप्यूटर पढ़ता है; ग़लत लेआउट में @ \" ? जैसे अक्षर चुपचाप बदल जाते हैं।</li><li>कंप्यूटर पर उस फ़ील्ड में क्लिक करें जहाँ मान जाना है।</li><li>फ़ोन पर <strong>टाइप करें</strong> दबाएँ। तीन सेकंड की गिनती के बाद — जो उसी क्लिक के लिए है — मान एक-एक कुंजी करके लिखा जाता है।</li></ol>",
            "<h3>कनेक्टेड दिखता है, पर कुछ टाइप नहीं होता</h3>",
            "<p>वजह लगभग हमेशा एक ही: कंप्यूटर ने पहले कभी आपके फ़ोन को <em>फ़ोन की तरह</em> पेयर किया था, इसलिए उसके लिए कीबोर्ड (HID) सेवा कभी चालू ही नहीं हुई। कनेक्शन बन जाता है, कुंजियाँ जाती हैं, कहीं पहुँचती नहीं।</p>",
            "<ol><li>कंप्यूटर पर पेयरिंग हटाएँ (<em>डिवाइस हटाएँ</em>)।</li><li>फ़ोन पर भी हटाएँ (ब्लूटूथ सेटिंग्स में <em>भूल जाएँ</em>)। दोनों तरफ़ ज़रूरी है।</li><li>Sekuvo में 💻 स्क्रीन खोलें और खुली छोड़ें।</li><li><strong>कंप्यूटर से शुरू करते हुए</strong> दोबारा पेयर करें।</li><li>Windows में पुष्टि: <em>डिवाइस मैनेजर → ह्यूमन इंटरफ़ेस डिवाइस</em> में अब एक ब्लूटूथ HID डिवाइस दिखना चाहिए।</li></ol>",
            "<p>macOS में पहली बार जुड़ते समय <strong>Keyboard Setup Assistant</strong> खुल सकता है, जो shift के बगल वाली कुंजी दबाने को कहता है। वह विंडो बंद होने तक macOS कुछ भी संसाधित नहीं करता — Mac पर “कनेक्टेड पर ख़ामोश” की यही आम वजह है।</p>",
            "<h3>गति और उसकी जाँच</h3>",
            "<p>कुंजियाँ एक-एक कर भेजी जाती हैं, इसलिए लंबे राज़ में सचमुच समय लगता है — डायलॉग अनुमान दिखाता है। तीन गतियाँ हैं और सुरक्षित वाली का डिफ़ॉल्ट होना जानबूझकर है। बढ़ाने से पहले <strong>⏱ गति परीक्षण</strong> चलाएँ: यह स्पेस से अलग दस एक जैसे ब्लॉक लिखता है और मापी गई गति बताता है। एक ब्लॉक भी अलग हो तो वह गति इस कंप्यूटर पर सुरक्षित नहीं — एक पायदान नीचे आएँ।</p>",
            "<p>यह परीक्षण निदान भी है: कुछ न लिखे तो पेयरिंग की समस्या, अक्षर बिगड़ें तो लेआउट की, बीच में रुके तो गति की।</p>",
            "<p>लिखते समय प्रगति पट्टी और <strong>रोकें</strong> बटन रहता है। भेजने की क़तार अटके तो Sekuvo रुक-रुककर दोबारा कोशिश करता है और फिर भी न हो तो <em>रुककर बताता है</em> कि किस अक्षर पर रुका — कोई राज़ चुपचाप आधा नहीं लिखा जाता।</p>",
        ]),
        ("lock", "लॉक कैसे काम करता है", [
            "<p>जिस स्क्रीन पर तिजोरी है, वह बुझते ही तिजोरी लॉक हो जाती है — फ़ोल्डेबल को मोड़ना भी इसमें आता है। उसी क्षण कुंजी मेमोरी से मिट जाती है; शीर्षक भले दिखते रहें, कुछ भी डिक्रिप्ट नहीं हो सकता।</p>",
            "<p>स्क्रीन चालू रहते ऐप से बाहर जाना लॉक <em>नहीं</em> करता। यह जानबूझकर है: ऐप, कीबोर्ड और ऑटोफ़िल एक ही सत्र साझा करते हैं; वरना पासवर्ड चिपकाने के लिए ब्राउज़र पर जाना आपको काम के बीच में ही बाहर कर देता।</p>",
        ]),
        ("quick", "त्वरित पहुँच — एक सोचा-समझा सौदा", [
            "<p>जिन एंट्री को आप “बिना पासवर्ड कीबोर्ड पर इस्तेमाल करें” चिह्नित करते हैं, वे दूसरी बार भी सहेजी जाती हैं — एक अलग डिवाइस कुंजी से एन्क्रिप्टेड — ताकि कीबोर्ड उन्हें <em>तिजोरी लॉक रहते</em> पढ़ सके।</p>",
            "<p>सौदा साफ़ लिखा है: उन एंट्री की सुरक्षा आपके मास्टर पासवर्ड से नहीं, फ़ोन के स्क्रीन लॉक से होती है। पासवर्ड इसमें न रखें। यह चिह्न डिफ़ॉल्ट रूप से बंद है; अपवाद केवल नई <strong>रोज़मर्रा</strong> एंट्री हैं, जो चिह्नित शुरू होती हैं क्योंकि नाम और फ़ोन नंबर वही हैं जो हाथ में चाहिए — इन्हें आप एक-एक कर बंद कर सकते हैं।</p>",
        ]),
        ("backup", "बैकअप और पुनर्स्थापना", [
            "<p>सिस्टम बैकअप (Google बैकअप, डिवाइस ट्रांसफ़र) जानबूझकर बंद है, ताकि आपकी तिजोरी के फ़ोन से बाहर जाने का ठीक एक रास्ता हो और वह आपका चुना हुआ हो: <strong>सेटिंग्स → एन्क्रिप्टेड बैकअप बनाएँ</strong>।</p>",
            "<p>आप एक <em>बैकअप पासवर्ड</em> तय करते हैं — इसे मास्टर पासवर्ड से अलग रखें, क्योंकि कंप्यूटरों पर टाइप होने वाला यही होता है। परिणाम एक <code>.vaultbak</code> फ़ाइल है, जिसे जहाँ चाहें रखें: Drive, SD कार्ड, USB।</p>",
            "<p>फ़ाइल डिवाइस से स्वतंत्र है: उसका अपना सॉल्ट और कुंजी-व्युत्पत्ति पैरामीटर उसके हेडर में रहते हैं। फ़ाइल और बैकअप पासवर्ड मिलकर किसी भी फ़ोन पर, फ़ैक्ट्री रीसेट के बाद भी, सब कुछ लौटा देते हैं। पुनर्स्थापना <strong>सेटिंग्स → बैकअप से पुनर्स्थापित करें</strong> से, और नई इंस्टॉल पर स्वागत स्क्रीन से होती है।</p>",
            "<p>पुनर्स्थापना में <em>मौजूदा में जोड़ें</em> या <em>सब बदलें</em> का विकल्प है। दोनों में कुछ भी लिखे जाने से पहले जाँच होती है — ग़लत पासवर्ड प्रमाणीकरण पर ही गिर जाता है, और नया डेटा जाँचे बिना कुछ नहीं मिटाया जाता।</p>",
        ]),
        ("transfer", "कंप्यूटर से राज़ लाना", [
            "<p>लंबी कुंजी को फ़ोन में हाथ से टाइप करना ही वह जगह है जहाँ ग़लतियाँ होती हैं। Sekuvo उन्हें एन्क्रिप्टेड लिफ़ाफ़े के रूप में लाता है, दो रूपों में: पाठ जिसे आप चिपकाते हैं, या QR कोड जिन्हें आप स्कैन करते हैं।</p>",
            "<p><strong>फ़ोन पर:</strong> ➕ बटन <em>QR से आयात</em> और <em>पाठ से आयात</em> देता है। QR आयात कैमरा खोलता है; फ़्रेम डिवाइस पर ही डिकोड होते हैं और कई फ़्रेम वाले स्थानांतरण में प्रगति दिखती है।</p>",
            "<h3>कंप्यूटर वाला टूल</h3>",
            "<p>ये लिफ़ाफ़े बनाने वाला टूल एक अकेली HTML फ़ाइल है और जानबूझकर <strong>एक डाउनलोड है, वेबसाइट नहीं</strong>। sekuvo.com आपसे कभी कोई राज़ नहीं माँगता; जो पेज माँगे, वह ठीक वैसा ही दिखेगा जैसा एक फ़िशिंग साइट दिखती है।</p>",
            "<ol><li>GitHub पर प्रोजेक्ट खोलें और <strong>Releases</strong> पर जाएँ।</li><li>नवीनतम रिलीज़ से <code>aktar.html</code> डाउनलोड करें।</li><li>उसके साथ प्रकाशित SHA-256 से मिलाएँ: macOS/Linux पर <code>shasum -a 256 aktar.html</code>, Windows पर <code>certutil -hashfile aktar.html SHA256</code>।</li><li>फ़ाइल पर डबल-क्लिक करके खोलें। यह आपकी डिस्क से चलती है — पता पट्टी में वेबसाइट नहीं, <code>file://</code> दिखता है।</li><li>अपना पाठ चिपकाएँ, एक ट्रांसफ़र पासवर्ड तय करें; टूल लिफ़ाफ़ा पाठ या QR कोड के रूप में बनाता है।</li><li>फ़ोन पर स्कैन या चिपकाएँ, वही पासवर्ड डालें, और जोड़ें या बदलें चुनें।</li></ol>",
            "<p>सारा एन्क्रिप्शन आपकी मशीन पर, ब्राउज़र के भीतर होता है। कमांड लाइन के लिए <code>vault-clip.py</code> भी है, जो यही काम क्लिपबोर्ड या फ़ाइल से करता है और QR कोड टर्मिनल में बना सकता है।</p>",
            "<h3>अगर आप टूल इस्तेमाल नहीं करना चाहते</h3>",
            "<p>लिफ़ाफ़ा एक खुला प्रारूप है, ऐसा कुछ नहीं जो सिर्फ़ Sekuvo बना सके: 310,000 राउंड का PBKDF2-HMAC-SHA256, AES-256-GCM, एक छोटे JSON में लिपटा हुआ। आप इसे अपनी पढ़ी हुई लगभग तीस पंक्तियों से खुद बना सकते हैं और परिणाम <em>पाठ से आयात करें</em> में चिपका सकते हैं \u2014 ऐप यह जान ही नहीं सकता कि उसे किस टूल ने बनाया, और उसे फ़र्क़ भी नहीं पड़ता।</p>",
            "<p>तरीक़ा रिपॉज़िटरी में है: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (तुर्की में लिखा हुआ)।</p>",
        ]),
        ("log", "उपयोग लॉग", [
            "<p>Sekuvo दर्ज करता है कि किस एंट्री का कौन-सा फ़ील्ड कब कहाँ गया: क्लिपबोर्ड पर, ब्लूटूथ से कंप्यूटर पर (लक्ष्य डिवाइस के नाम के साथ), या कीबोर्ड से किसी ऐप में। कोई कंप्यूटर हाथ से निकल जाए, तो “वहाँ क्या गया था, क्या बदलना है” का जवाब यही है।</p>",
            "<p>लॉग उसी कुंजी से एन्क्रिप्टेड है जिससे आपकी एंट्री, और <strong>मान कभी उसमें नहीं लिखे जाते</strong> — केवल घटना का प्रकार, फ़ील्ड का नाम और गंतव्य। एंट्री मिटाने पर उसका लॉग भी मिटता है, और पूरा लॉग सेटिंग्स से साफ़ किया जा सकता है।</p>",
        ]),
        ("generator", "पासवर्ड जनरेटर", [
            "<p>होम स्क्रीन के 🎲 आइकन से, या एंट्री संपादित करते समय पासवर्ड फ़ील्ड के पास से खुलता है। यह क्रिप्टोग्राफ़िक यादृच्छिकता का उपयोग करता है, 8–64 अक्षर बनाता है, अक्षर-वर्ग चुनने देता है, मिलते-जुलते अक्षर हटा सकता है, और परिणामी एन्ट्रॉपी बिट में दिखाता है।</p>",
        ]),
    ],
)

# ─────────────────────────────── العربية ────────────────────────────────────
G["ar"] = dict(
    nav_label="الدليل",
    title="Sekuvo — الدليل",
    desc="كيف تستخدم Sekuvo: التشغيل الأول، الملء التلقائي، لوحة المفاتيح، الكتابة في الحاسوب عبر البلوتوث، النسخ الاحتياطية والنقل.",
    h1="الدليل",
    lede="كل ما يفعله Sekuvo، بالترتيب الذي ستحتاجه على الأرجح. لا شيء هنا يتطلب حسابًا ولا اتصالًا بالإنترنت.",
    back="← العودة إلى sekuvo.com",
    sections=[
        ("start", "التشغيل الأول", [
            "<p>عند أول تشغيل تحدّد <strong>كلمة مرور رئيسية</strong>. كل سرّ تحفظه يُشفَّر بمفتاح مشتقّ منها، فهي الشيء الوحيد الذي لا يستطيع Sekuvo استعادته نيابةً عنك — اكتبها في مكان آمن قبل المتابعة.</p>",
            "<p>ألديك نسخة احتياطية من هاتف آخر؟ اضغط <strong>«لديّ نسخة احتياطية — استعادتها»</strong> في شاشة الترحيب. ستحدّد كلمة مرور رئيسية لهذا الجهاز أولًا، ثم يفتح منتقي الملفات تلقائيًا وتعود مدخلاتك.</p>",
            "<p>إن كان هاتفك يدعم البصمة أو الوجه، يعرض Sekuvo استخدامها بعد الإعداد مباشرة. وهي طبقة تيسير فقط: كلمة المرور الرئيسية تعمل دائمًا، وهي التي تبقى بعد إعادة ضبط المصنع.</p>",
        ]),
        ("entries", "ماذا يمكنك أن تحفظ", [
            "<p>أربعة أنواع من المدخلات تغطي معظم ما يُحفظ في خزنة:</p>",
            "<ul><li><strong>حساب / كلمة مرور</strong> — اسم المستخدم وكلمة المرور والموقع أو التطبيق.</li><li><strong>يوميّ</strong> — الاسم والهاتف والبريد والعنوان. ما تطلبه النماذج باستمرار.</li><li><strong>بطاقة</strong> — رقم البطاقة وتاريخ الانتهاء وCVV وIBAN.</li><li><strong>ملاحظة آمنة</strong> — نص حر، مع أنواع فرعية للنصوص البرمجية والمفاتيح ورموز الاستعادة وملفات الإعداد.</li></ul>",
            "<p>كما تقبل مدخلات «حساب» و«يوميّ» <strong>حقولًا مخصّصة</strong>: أي زوج «اسم + قيمة» تريده. وتُشفَّر تمامًا كالحقول المدمجة وتظهر في كل موضع تظهر فيه.</p>",
        ]),
        ("channels", "استخدام السرّ دون الحافظة", [
            "<p>الحافظة يمكن أن تقرأها تطبيقات أخرى، وفيها تُسرق الأسرار. لذلك يمنحك Sekuvo ثلاث طرق لإيصال القيمة مباشرة إلى وجهتها. ويظل النسخ متاحًا — تُمحى الحافظة تلقائيًا بعد 45 ثانية — لكن القنوات الثلاث أدناه هي سبب وجود التطبيق.</p>",
        ]),
        ("autofill", "الملء التلقائي (داخل هاتفك)", [
            "<p>يستطيع Sekuvo العمل كخدمة الملء التلقائي في أندرويد، فتعرض نماذج تسجيل الدخول والبطاقات مدخلاتك مباشرة.</p>",
            "<p><strong>لتفعيله:</strong> Sekuvo → الإعدادات → <em>تفعيل الملء التلقائي</em> → اختر Sekuvo من قائمة النظام. واسم القائمة يختلف بحسب الجهاز: في Samsung وأندرويد 14+ هي <em>كلمات المرور ومفاتيح المرور والملء التلقائي ← الخدمة المفضّلة</em>، وفي أندرويد النقي <em>خدمة الملء التلقائي</em>.</p>",
            "<p>بعدها، عند لمس حقل اسم مستخدم أو كلمة مرور أو بطاقة في أي تطبيق تظهر مدخلاتك المطابقة فوق لوحة المفاتيح. وإن كانت الخزنة مقفلة تأتي خطوة فتح القفل أولًا — وأثناء القفل لا يُسلَّم النظام أي شيء إطلاقًا.</p>",
        ]),
        ("keyboard", "لوحة مفاتيح Sekuvo (داخل هاتفك)", [
            "<p>تكتب إضافة لوحة المفاتيح القيم المحفوظة في أي حقل وفي أي تطبيق، دون خطوة نسخ.</p>",
            "<p><strong>لتفعيلها:</strong> Sekuvo → الإعدادات → <em>تفعيل لوحة المفاتيح</em> → فعّلها من قائمة النظام، ثم اخترها من مبدّل لوحات المفاتيح متى احتجت.</p>",
            "<p>تبقى المدخلات الأحدث في الأعلى، ويبحث 🔍 في العناوين وأسماء المستخدمين والمواقع. وأثناء قفل الخزنة لا تعرض لوحة المفاتيح إلا المدخلات المعلَّمة للوصول السريع — انظر أدناه.</p>",
        ]),
        ("bluetooth", "الكتابة في حاسوب عبر البلوتوث", [
            "<p>يستطيع هاتفك أن يعمل لوحةَ مفاتيح بلوتوث ويكتب السرّ عند مؤشر حاسوبك. لا يُثبَّت شيء على الحاسوب، ويعمل على Windows وmacOS وLinux، ولا تمرّ القيمة بالحافظة ولا بالشبكة. يتطلب أندرويد 9 أو أحدث.</p>",
            "<h3>خطوة بخطوة</h3>",
            "<ol><li>في Sekuvo، افتح المدخلة واضغط أيقونة 💻 بجوار الحقل المراد كتابته. <strong>أبقِ هذه الشاشة مفتوحة</strong> — فالهاتف لا يعلن عن نفسه كلوحة مفاتيح إلا وهي مفتوحة.</li><li>على الحاسوب، أضف الهاتف <em>جهاز بلوتوث جديدًا</em>: في Windows <em>الإعدادات ← البلوتوث والأجهزة ← إضافة جهاز ← بلوتوث</em>، وفي macOS <em>إعدادات النظام ← البلوتوث</em>.</li><li>أكّد رمز الاقتران في الطرفين.</li><li>عُد إلى الهاتف، واختر حاسوبك من القائمة وانتظر ظهور «متصل».</li><li>اختر تخطيط لوحة مفاتيح <strong>الحاسوب</strong> لا الهاتف. فالحاسوب هو من يفسّر رموز المفاتيح، والتخطيط الخاطئ يحوّل بصمت محارف مثل @ \" ? إلى غيرها.</li><li>انقر في الحقل على الحاسوب حيث ستذهب القيمة.</li><li>اضغط <strong>اكتب</strong> على الهاتف. وبعد عدّ تنازلي من ثلاث ثوانٍ — وهو موجود لتتمكن من تلك النقرة — تُكتب القيمة مفتاحًا مفتاحًا.</li></ol>",
            "<h3>يقول «متصل» ولا يكتب شيئًا</h3>",
            "<p>السبب واحد في الغالب: اقترن الحاسوب بهاتفك <em>بوصفه هاتفًا</em> في وقت سابق، فلم يفعّل له خدمة لوحة المفاتيح (HID) قط. فينجح الاتصال وتخرج ضغطات المفاتيح ولا تصل إلى شيء.</p>",
            "<ol><li>أزل الاقتران من الحاسوب (<em>إزالة الجهاز</em>).</li><li>أزله من الهاتف أيضًا (<em>نسيان</em> في إعدادات البلوتوث). كلا الطرفين مهم.</li><li>افتح شاشة 💻 في Sekuvo واتركها مفتوحة.</li><li>أعد الاقتران <strong>بدءًا من الحاسوب</strong>.</li><li>للتأكد في Windows: يجب أن يظهر الآن جهاز HID بلوتوث في <em>إدارة الأجهزة ← أجهزة واجهة المستخدم</em>.</li></ol>",
            "<p>وفي macOS قد يفتح أول اتصال <strong>مساعد إعداد لوحة المفاتيح</strong> الذي يطلب ضغط مفتاح بجوار مفتاح Shift. وحتى إغلاق تلك النافذة لا يعالج macOS شيئًا — وهذا هو السبب المعتاد لحالة «متصل لكنه صامت» على الماك.</p>",
            "<h3>السرعة وكيف تتحقق منها</h3>",
            "<p>تُرسل المفاتيح واحدًا واحدًا، لذا يستغرق السرّ الطويل وقتًا فعليًا — ويعرض المربع الحواري تقديرًا. وتُتاح ثلاث سرعات، وكون الآمنة هي الافتراضية أمر مقصود. وقبل رفعها استخدم <strong>⏱ اختبار السرعة</strong>: يكتب عشر كتل متطابقة مفصولة بمسافات ويبلّغ بعدد المحارف في الثانية. وإن اختلفت كتلة واحدة فتلك السرعة غير آمنة على هذا الحاسوب — انزل درجة.</p>",
            "<p>والاختبار وسيلة تشخيص أيضًا: إن لم يُكتب شيء فالمشكلة في الاقتران، وإن تشوّهت المحارف فهي في التخطيط، وإن انقطعت الكتابة فهي في السرعة.</p>",
            "<p>وأثناء الكتابة يظهر شريط تقدّم وزر <strong>إيقاف</strong>. وإن تعطّل طابور الإرسال أعاد Sekuvo المحاولة بتراجع تدريجي، وإن لم ينجح <em>توقّف وأخبرك</em> عند أي محرف توقّف — فلا يُكتب سرّ نصفه بصمت أبدًا.</p>",
        ]),
        ("lock", "كيف يعمل القفل", [
            "<p>تُقفل الخزنة لحظة انطفاء الشاشة التي هي عليها — ويشمل ذلك طيّ الهاتف القابل للطي. وفي تلك اللحظة يُمحى المفتاح من الذاكرة؛ وقد تبقى العناوين معروضة لكن لا شيء يمكن فكّ تشفيره.</p>",
            "<p>أما مغادرة التطبيق والشاشة مضاءة فلا تُقفلها. وهذا مقصود: التطبيق ولوحة المفاتيح والملء التلقائي يتشاركون جلسة واحدة، وإلا لأخرجك الانتقال إلى المتصفح للصق كلمة مرور من عملك في منتصفه.</p>",
        ]),
        ("quick", "الوصول السريع — مقايضة مقصودة", [
            "<p>المدخلات التي تعلّمها صراحةً بـ«استخدامها في لوحة المفاتيح دون كلمة مرور» تُحفظ مرة ثانية، مشفَّرةً بمفتاح جهاز منفصل، لتتمكن لوحة المفاتيح من قراءتها <em>والخزنة مقفلة</em>.</p>",
            "<p>والمقايضة مذكورة بوضوح: تلك المدخلات يحميها قفل شاشة هاتفك لا كلمة مرورك الرئيسية. فلا تضع فيها كلمات المرور. والعلامة مطفأة افتراضيًا؛ والاستثناء الوحيد مدخلات <strong>يوميّ</strong> الجديدة التي تبدأ معلَّمة لأن الأسماء وأرقام الهواتف هي ما تريده في متناول اليد — ويمكنك إطفاء أي منها.</p>",
        ]),
        ("backup", "النسخ الاحتياطي والاستعادة", [
            "<p>نسخ النظام (نسخ Google، نقل الجهاز) معطَّل عمدًا، فيبقى لخروج خزنتك من الهاتف طريق واحد فقط وهو طريق اخترته أنت: <strong>الإعدادات ← إنشاء نسخة مشفَّرة</strong>.</p>",
            "<p>تحدّد <em>كلمة مرور للنسخة</em> — واجعلها مختلفة عن الرئيسية، لأن كلمة مرور النسخة هي التي تُكتب على الحواسيب. والناتج ملف <code>.vaultbak</code> واحد تحفظه حيث تشاء: Drive أو بطاقة SD أو ذاكرة USB.</p>",
            "<p>والملف مستقل عن الجهاز: ملحُه ومعاملات اشتقاق المفتاح في ترويسته. والملف مع كلمة مرور النسخة يستعيدان كل شيء على أي هاتف، حتى بعد إعادة ضبط المصنع. والاستعادة من <strong>الإعدادات ← الاستعادة من نسخة</strong>، أو من شاشة الترحيب في تثبيت جديد.</p>",
            "<p>وتتيح الاستعادة <em>الإضافة إلى الموجود</em> أو <em>استبدال الكل</em>. وكلاهما يُتحقَّق منه قبل كتابة أي شيء — فكلمة المرور الخاطئة تسقط عند التوثيق، ولا يُحذف شيء قبل التأكد من البيانات الجديدة.</p>",
        ]),
        ("transfer", "جلب الأسرار من حاسوب", [
            "<p>كتابة مفتاح طويل يدويًا في الهاتف هي موضع الأخطاء. لذا ينقلها Sekuvo في مظروف مشفَّر، بصورتين: نص تلصقه، أو رموز QR تمسحها.</p>",
            "<p><strong>على الهاتف:</strong> يقدّم زر ➕ خيارَي <em>استيراد عبر QR</em> و<em>استيراد من نص</em>. ويفتح استيراد QR الكاميرا؛ وتُفكّ الإطارات على الجهاز، وتعرض عمليات النقل متعددة الإطارات تقدّمها أثناء التجميع.</p>",
            "<h3>أداة الحاسوب</h3>",
            "<p>الأداة التي تبني تلك المظاريف ملف HTML واحد، وهي عمدًا <strong>ملف يُنزَّل لا موقع ويب</strong>. فموقع sekuvo.com لا يطلب منك سرًّا أبدًا؛ والصفحة التي تطلبه ستبدو تمامًا كما يبدو موقع تصيّد.</p>",
            "<ol><li>افتح المشروع على GitHub وانتقل إلى <strong>Releases</strong>.</li><li>نزّل <code>aktar.html</code> من أحدث إصدار.</li><li>قارن بصمة SHA-256 بالقيمة المنشورة بجانبه: <code>shasum -a 256 aktar.html</code> على macOS أو Linux، و<code>certutil -hashfile aktar.html SHA256</code> على Windows.</li><li>افتح الملف بنقرة مزدوجة. يعمل من قرصك — ويظهر في شريط العنوان <code>file://</code> لا موقع.</li><li>الصق نصّك، وحدّد كلمة مرور للنقل، فتنتج الأداة المظروف نصًّا أو رموز QR.</li><li>على الهاتف، امسح أو الصق، وأدخل كلمة المرور نفسها، ثم اختر الإضافة أو الاستبدال.</li></ol>",
            "<p>ويجري التشفير كله داخل متصفحك على جهازك. وهناك أيضًا <code>vault-clip.py</code> لسطر الأوامر، يؤدي المهمة نفسها من الحافظة أو من ملف، ويستطيع رسم رموز QR في الطرفية.</p>",
            "<h3>إن كنت تفضّل ألّا تستخدم الأداة</h3>",
            "<p>المظروف صيغة مفتوحة، لا شيء لا يصنعه إلا Sekuvo: خوارزمية PBKDF2-HMAC-SHA256 بـ310٬000 دورة، وAES-256-GCM، ملفوفة في كائن JSON صغير. يمكنك بناؤه بنفسك من نحو ثلاثين سطرًا قرأتها، ثم لصق النتيجة في <em>استيراد من نص</em> \u2014 فالتطبيق لا سبيل له إلى معرفة الأداة التي أنتجته، ولا يعنيه ذلك.</p>",
            "<p>الوصفة في المستودع: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (مكتوبة بالتركية).</p>",
        ]),
        ("log", "سجل الاستخدام", [
            "<p>يسجّل Sekuvo أي حقل من أي مدخلة ذهب إلى أين ومتى: إلى الحافظة، أو إلى حاسوب عبر البلوتوث (باسم الجهاز الهدف)، أو كُتب في تطبيق من لوحة المفاتيح. وحين يُخترق حاسوب، يجيب هذا عن سؤال «ما الذي ذهب إليه وما الذي عليّ تغييره».</p>",
            "<p>والسجل مشفَّر بالمفتاح نفسه الذي يشفّر مدخلاتك، و<strong>القيم لا تُكتب فيه أبدًا</strong> — بل نوع الحدث واسم الحقل والوجهة فقط. وحذف مدخلة يحذف سجلّها، ويمكنك مسح السجل كله من الإعدادات.</p>",
        ]),
        ("generator", "مولّد كلمات المرور", [
            "<p>يُفتح من أيقونة 🎲 في الشاشة الرئيسية، أو بجوار حقل كلمة المرور أثناء تحرير مدخلة. يستخدم مصدر عشوائية تعمّيّ، وينتج من 8 إلى 64 محرفًا، ويتيح اختيار فئات المحارف، ويستطيع استبعاد المحارف المتشابهة، ويعرض الإنتروبيا الناتجة بالبتّات.</p>",
        ]),
    ],
)

G["zh"] = dict(
    nav_label="指南",
    title="Sekuvo — 使用指南",
    desc="Sekuvo 使用指南：首次运行、自动填充、键盘、通过蓝牙输入到电脑、备份与传输。",
    h1="使用指南",
    lede="Sekuvo 的所有功能，按你可能需要的顺序排列。这里的一切都不需要账户或互联网连接。",
    back="← 返回 sekuvo.com",
    sections=[
        ("start", "首次运行", [
            "<p>首次启动时，你会设置一个<strong>主密码</strong>。你保存的每一个密文都用由它派生的密钥加密，因此它是唯一 Sekuvo 无法帮你找回的东西 — 在继续之前，请把它记在安全的地方。</p>",
            "<p>已经有另一部手机的备份了吗？在欢迎界面点击<strong>“我有备份 — 恢复它”</strong>。你仍需先为此设备设置一个主密码，之后文件选择器会自动打开，你的条目就会回来。</p>",
            "<p>如果你的手机支持指纹或面部识别，Sekuvo 会在设置完成后立即提示你启用它。这只是一层便利功能：主密码始终有效，也是唯一能在恢复出厂设置后依然有效的凭据。</p>",
        ]),
        ("entries", "可以保存什么", [
            "<p>四种条目类型涵盖了密码库中大部分常见内容：</p>",
            "<ul><li><strong>账号 / 密码</strong> — 用户名、密码、网站或应用。</li><li><strong>日常信息</strong> — 姓名、电话、邮箱、地址。表单最常要求填写的内容。</li><li><strong>银行卡</strong> — 卡号、有效期、CVV、IBAN。</li><li><strong>安全笔记</strong> — 自由文本，还分脚本、密钥、恢复代码和配置文件等子类型。</li></ul>",
            "<p>账号和日常信息条目还支持<strong>自定义字段</strong>：任意“名称 + 值”组合。自定义字段的加密方式与内置字段完全相同，并出现在所有相同的位置。</p>",
        ]),
        ("channels", "不经过剪贴板使用密文", [
            "<p>剪贴板可以被其他应用读取，是密文最容易被窃取的地方。因此 Sekuvo 提供三种方式，把值直接送达目的地。你仍然可以选择复制 — 剪贴板会在 45 秒后自动清空 — 但下面这三条通道才是这款应用存在的意义。</p>",
        ]),
        ("autofill", "自动填充（手机内）", [
            "<p>Sekuvo 可以作为 Android 的自动填充服务，让登录和银行卡表单直接提供你的条目。</p>",
            "<p><strong>开启方法：</strong>Sekuvo → 设置 → <em>启用自动填充</em> → 在系统列表中选择 Sekuvo。该列表在不同设备上名称不同：三星和 Android 14+ 上是<em>密码、通行密钥和自动填充 → 首选服务</em>；原生 Android 上是<em>自动填充服务</em>。</p>",
            "<p>之后，在任意应用中点击用户名、密码或银行卡字段，就会在键盘上方显示你匹配的条目。如果密码库已锁定，会先出现解锁步骤 — 锁定期间系统完全得不到任何数据。</p>",
        ]),
        ("keyboard", "Sekuvo 键盘（手机内）", [
            "<p>键盘附加组件可以把已保存的值直接输入到任意应用的任意字段，无需复制这一步。</p>",
            "<p><strong>开启方法：</strong>Sekuvo → 设置 → <em>启用键盘</em> → 在系统列表中开启，然后在需要时于键盘切换器中选择“Sekuvo 键盘”。</p>",
            "<p>最近使用的条目排在最前，🔍 可搜索标题、用户名和地址。密码库锁定时，键盘只会显示你标记为快速访问的条目 — 见下文。</p>",
        ]),
        ("bluetooth", "通过蓝牙输入到电脑", [
            "<p>你的手机可以充当蓝牙键盘，把密文输入到电脑光标所在的位置。电脑上不会安装任何东西，支持 Windows、macOS 和 Linux，且该值不会经过剪贴板或网络。需要 Android 9 或更高版本。</p>",
            "<h3>操作步骤</h3>",
            "<ol><li>在 Sekuvo 中打开条目，点击想要输入的字段旁的 💻 图标。<strong>保持该屏幕开启</strong> — 只有在此期间手机才会宣告自己是一个键盘。</li><li>在电脑上将手机添加为新的蓝牙设备：Windows 上是<em>设置 → 蓝牙和其他设备 → 添加设备 → 蓝牙</em>，macOS 上是<em>系统设置 → 蓝牙</em>。</li><li>在双方设备上确认配对码。</li><li>回到手机，从列表中选择你的电脑，等待显示“已连接”。</li><li>选择<strong>电脑</strong>的键盘布局 — 而不是手机的。电脑负责解释按键代码，选错布局会把 @ \" ? 等字符悄悄替换成别的字符。</li><li>在电脑上点击目标值应输入到的字段。</li><li>在手机上点击<strong>输入</strong>。经过三秒倒计时（专门留给你完成点击那个字段）后，值会逐个字符地输入。</li></ol>",
            "<h3>显示已连接，但什么都没输入</h3>",
            "<p>几乎总是同一个原因：电脑之前把你的手机<em>当作普通手机</em>配对过，因此从未为它启用键盘（HID）服务。连接看似成功，但按键信号无处可去。</p>",
            "<ol><li>在电脑上移除配对（<em>移除设备</em>）。</li><li>在手机上也移除（蓝牙设置中的<em>取消配对</em>）。两边都要处理。</li><li>在 Sekuvo 中打开 💻 屏幕并保持开启。</li><li><strong>从电脑端开始</strong>重新配对。</li><li>在 Windows 上确认：设备管理器 → 人体学输入设备中此时应出现一个蓝牙 HID 设备。</li></ol>",
            "<p>在 macOS 上，首次连接可能会打开<strong>键盘设置助理</strong>，要求你按下 Shift 键旁边的某个键。在关闭该窗口之前，macOS 不会处理任何输入 — 这是 Mac 上“已连接但无反应”最常见的原因。</p>",
            "<h3>速度，以及如何检查</h3>",
            "<p>按键是逐个发送的，所以较长的密文确实需要时间 — 对话框会显示预计时间。系统提供三档速度，默认选用安全档是刻意的设计。在提高速度之前，请使用<strong>⏱ 速度测试</strong>：它会输入十个以空格分隔的相同字符块，并报告实测的每秒字符数。只要有一块不同，这个速度在这台电脑上就不安全 — 请降低一档。</p>",
            "<p>速度测试同时也是一种诊断手段：完全没有输入说明是配对问题，字符错乱说明是布局问题，中途中断说明是速度问题。</p>",
            "<p>输入过程中会显示进度条和<strong>停止</strong>按钮。如果发送队列卡住，Sekuvo 会以退避策略重试；如果仍然失败，它会<em>停止并告诉你</em>在哪个字符处中断了 — 密文绝不会被悄悄地只输入一半。</p>",
        ]),
        ("lock", "锁定机制", [
            "<p>密码库会在其所在屏幕熄灭的瞬间锁定 — 折叠屏手机合上也算。那一刻密钥会立即从内存中清除；条目标题可能仍会列出，但没有任何内容能被解密。</p>",
            "<p>屏幕保持点亮时离开应用<em>不会</em>锁定密码库。这是刻意的设计：应用、键盘和自动填充共享同一个会话，否则切到浏览器去粘贴一个密码就会让你在任务进行到一半时被锁在外面。</p>",
        ]),
        ("quick", "快速访问 — 一次明确的取舍", [
            "<p>你明确标记为“在键盘中免密码使用”的条目会被再保存一份，用单独的设备密钥加密，这样键盘就能在<em>密码库锁定期间</em>读取它们。</p>",
            "<p>这个取舍说得很清楚：这些条目受手机锁屏保护，而不是你的主密码。请不要把密码放进去。此标记默认关闭；唯一的例外是新建的<strong>日常信息</strong>条目，它们默认开启，因为姓名和电话号码正是你希望随手可用的内容 — 你可以逐条关闭它。</p>",
        ]),
        ("backup", "备份与恢复", [
            "<p>系统备份（如 Google 备份、设备转移）在设计上被禁用，因此你的密码库离开手机只有一条路径，且是你自己选择的：<strong>设置 → 创建加密备份</strong>。</p>",
            "<p>你会设置一个<em>备份密码</em> — 请让它与主密码不同，因为备份密码是会被输入到电脑上的那个密码。生成的结果是一个 <code>.vaultbak</code> 文件，你可以保存在任何地方：网盘、SD 卡、U 盘。</p>",
            "<p>该文件与设备无关：它自己的盐值和密钥派生参数都保存在文件头中。文件加上备份密码，可以在任何手机上恢复一切，即使经过恢复出厂设置也一样。可从<strong>设置 → 从备份恢复</strong>恢复，或在全新安装时从欢迎界面恢复。</p>",
            "<p>恢复时可选择<em>添加到现有</em>或<em>替换全部</em>。两种方式都会在写入任何内容之前完成校验 — 密码错误会在身份验证阶段就失败，且在新数据确认无误之前不会删除任何东西。</p>",
        ]),
        ("transfer", "从电脑带回密文", [
            "<p>在手机上手动输入一长串密钥正是最容易出错的地方。因此 Sekuvo 改用加密信封来传递，有两种形式：你粘贴的文本，或你扫描的二维码。</p>",
            "<p><strong>在手机上：</strong>➕ 按钮提供<em>通过二维码导入</em>和<em>从文本导入</em>两个选项。二维码导入会打开相机；帧的解码在设备本地完成，多帧传输时会显示收集进度。</p>",
            "<h3>电脑端工具</h3>",
            "<p>用来生成这些信封的工具是一个单独的 HTML 文件，而且是刻意设计为<strong>一个下载文件，而不是一个网站</strong>的。sekuvo.com 绝不会向你索要密文；一个这样做的网页看起来会和钓鱼网站一模一样。</p>",
            "<ol><li>在 GitHub 上打开该项目，进入 <strong>Releases</strong>。</li><li>从最新版本中下载 <code>aktar.html</code>。</li><li>核对它的 SHA-256 与旁边公布的值是否一致：macOS 或 Linux 上用 <code>shasum -a 256 aktar.html</code>，Windows 上用 <code>certutil -hashfile aktar.html SHA256</code>。</li><li>双击打开该文件。它从你的硬盘运行 — 地址栏会显示 <code>file://</code>，而不是一个网站。</li><li>粘贴你的文本，设置一个传输密码，工具就会生成文本形式或二维码形式的信封。</li><li>在手机上扫描或粘贴，输入同一个密码，然后选择添加或替换。</li></ol>",
            "<p>全部加密过程都在你的浏览器里、在你自己的电脑上完成。命令行下还有 <code>vault-clip.py</code>，可以对剪贴板或文件做同样的事，并能在终端里绘制二维码。</p>",
            "<h3>如果你不想使用这个工具</h3>",
            "<p>这个信封是一种开放格式，不是只有 Sekuvo 才能生成的东西：PBKDF2-HMAC-SHA256（310,000 轮）、AES-256-GCM，包裹在一个小型 JSON 对象里。你完全可以用你读过的大约三十行代码自己实现它，然后把结果粘贴到<em>从文本导入</em>中 — 应用无从得知也不关心这个信封是用哪个工具生成的。</p>",
            "<p>具体做法在仓库中：<a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a>（以土耳其语撰写）。</p>",
        ]),
        ("log", "使用记录", [
            "<p>Sekuvo 会记录哪个条目的哪个字段在何时发送到了哪里：剪贴板、通过蓝牙发送到某台电脑（含目标设备名称），或从键盘输入到某个应用。当一台电脑被攻破时，这可以回答“泄露了什么、我需要修改什么”这个问题。</p>",
            "<p>该记录使用与你的条目相同的密钥加密，且<strong>值本身从不会被写入其中</strong> — 只记录事件类型、字段名称和目标。删除一个条目会同时删除它的记录，你也可以在设置中清空整个记录。</p>",
        ]),
        ("generator", "密码生成器", [
            "<p>可从主屏幕的 🎲 图标打开，或在编辑条目时从密码字段旁打开。它使用加密安全的随机数来源，可生成 8–64 个字符，允许你选择字符类别，可以去除容易混淆的字符，并以比特数显示生成结果的熵值。</p>",
        ]),
    ],
)


# ─────────────────────────────────────────────────────────────────────────────
# Screenshots. The mapping is the same in every language — only the captions
# are translated — so a new screenshot is added in one place, not five.
#
# Taken on an emulator with invented entries: the app sets FLAG_SECURE, so a
# real device cannot be photographed, and a real vault must never be.
# ─────────────────────────────────────────────────────────────────────────────

G["fr"] = dict(
    nav_label="Guide",
    title="Sekuvo — Guide",
    desc="Comment utiliser Sekuvo : premier lancement, saisie automatique, clavier, saisie sur un ordinateur par Bluetooth, sauvegardes et transferts.",
    h1="Guide",
    lede="Tout ce que fait Sekuvo, dans l'ordre où tu en auras probablement besoin. Rien ici ne nécessite un compte ou une connexion internet.",
    back="← Retour à sekuvo.com",
    sections=[
        ("start", "Premier lancement", [
            "<p>Au premier lancement, tu définis un <strong>mot de passe principal</strong>. Chaque secret que tu enregistres est chiffré avec une clé qui en dérive, c'est donc la seule chose que Sekuvo ne peut pas t'aider à récupérer — écris-le quelque part en lieu sûr avant d'aller plus loin.</p>",
            "<p>Tu as déjà une sauvegarde d'un autre téléphone ? Touche <strong>« J'ai une sauvegarde — la restaurer »</strong> sur l'écran d'accueil. Tu définis quand même d'abord un mot de passe principal pour cet appareil, puis le sélecteur de fichiers s'ouvre tout seul et tes entrées reviennent.</p>",
            "<p>Si ton téléphone dispose d'un capteur d'empreinte ou de reconnaissance faciale, Sekuvo propose de l'utiliser juste après la configuration. Ce n'est qu'une couche de confort : le mot de passe principal fonctionne toujours, et c'est lui qui survit à une réinitialisation d'usine.</p>",
        ]),
        ("entries", "Ce que tu peux enregistrer", [
            "<p>Quatre types d'entrées couvrent la plupart de ce que l'on garde dans un coffre :</p>",
            "<ul><li><strong>Compte / Mot de passe</strong> — identifiant, mot de passe, site ou application.</li><li><strong>Quotidien</strong> — nom, téléphone, e-mail, adresse. Ce que les formulaires demandent sans cesse.</li><li><strong>Carte</strong> — numéro de carte, expiration, CVV, IBAN.</li><li><strong>Note sécurisée</strong> — texte libre, avec des sous-types pour les scripts, clés, codes de récupération et fichiers de configuration.</li></ul>",
            "<p>Les entrées Compte et Quotidien acceptent aussi des <strong>champs personnalisés</strong> : n'importe quelle paire « nom + valeur ». Les champs personnalisés sont chiffrés exactement comme les champs intégrés et apparaissent partout où les autres apparaissent.</p>",
        ]),
        ("channels", "Utiliser un secret sans le presse-papiers", [
            "<p>Le presse-papiers est lisible par d'autres applications et c'est là que les secrets se font voler. Sekuvo t'offre trois façons d'acheminer une valeur directement à sa destination. Tu peux toujours copier — le presse-papiers est effacé automatiquement après 45 secondes — mais les trois canaux ci-dessous sont la raison d'être de l'application.</p>",
        ]),
        ("autofill", "Saisie automatique (dans ton téléphone)", [
            "<p>Sekuvo peut agir comme service de saisie automatique d'Android, afin que les formulaires de connexion et de carte proposent directement tes entrées.</p>",
            "<p><strong>Pour l'activer :</strong> Sekuvo → Paramètres → <em>Activer la saisie automatique</em> → choisis Sekuvo dans la liste système. Cette liste porte des noms différents selon l'appareil : sur Samsung et Android 14+, c'est <em>Mots de passe, clés d'accès et saisie automatique → Service préféré</em> ; sur Android natif, c'est <em>Service de saisie automatique</em>.</p>",
            "<p>Ensuite, toucher un champ d'identifiant, de mot de passe ou de carte dans n'importe quelle application affiche tes entrées correspondantes au-dessus du clavier. Si le coffre est verrouillé, une étape de déverrouillage apparaît d'abord — tant qu'il est verrouillé, le système ne reçoit strictement rien.</p>",
        ]),
        ("keyboard", "Clavier Sekuvo (dans ton téléphone)", [
            "<p>Le module clavier saisit les valeurs enregistrées dans n'importe quel champ, dans n'importe quelle application, sans étape de copie.</p>",
            "<p><strong>Pour l'activer :</strong> Sekuvo → Paramètres → <em>Activer le clavier</em> → active-le dans la liste système, puis choisis « Clavier Sekuvo » dans le sélecteur de clavier quand tu en as besoin.</p>",
            "<p>Les entrées récemment utilisées restent en haut et 🔍 recherche dans les titres, identifiants et adresses. Quand le coffre est verrouillé, le clavier n'affiche que les entrées que tu as marquées pour l'accès rapide — voir ci-dessous.</p>",
        ]),
        ("bluetooth", "Saisir sur un ordinateur par Bluetooth", [
            "<p>Ton téléphone peut agir comme un clavier Bluetooth et saisir un secret à l'emplacement du curseur de ton ordinateur. Rien n'est installé sur l'ordinateur, cela fonctionne sous Windows, macOS et Linux, et la valeur ne touche jamais le presse-papiers ni un réseau. Nécessite Android 9 ou plus récent.</p>",
            "<h3>Étape par étape</h3>",
            "<ol><li>Dans Sekuvo, ouvre l'entrée et touche l'icône 💻 à côté du champ à saisir. <strong>Garde cet écran ouvert</strong> — ton téléphone ne s'annonce comme clavier que pendant ce temps.</li><li>Sur l'ordinateur, ajoute le téléphone comme nouvel appareil Bluetooth : <em>Paramètres → Bluetooth et appareils → Ajouter un appareil → Bluetooth</em> sous Windows, ou <em>Réglages Système → Bluetooth</em> sous macOS.</li><li>Confirme le code d'appairage des deux côtés.</li><li>De retour sur le téléphone, choisis ton ordinateur dans la liste et attends « Connecté ».</li><li>Choisis la disposition de clavier <strong>de l'ordinateur</strong> — pas celle du téléphone. L'ordinateur interprète les codes de touche, donc une mauvaise disposition transforme silencieusement des caractères comme @ \" ? en d'autres.</li><li>Clique dans le champ de l'ordinateur où la valeur doit aller.</li><li>Touche <strong>Saisir</strong> sur le téléphone. Après un compte à rebours de trois secondes — qui existe pour te laisser le temps de cliquer dans ce champ — la valeur est saisie touche par touche.</li></ol>",
            "<h3>Connecté, mais rien ne s'affiche</h3>",
            "<p>Presque toujours la même cause : l'ordinateur a appairé ton téléphone <em>comme un téléphone</em> à un moment antérieur, donc il n'a jamais activé pour lui le service clavier (HID). La connexion réussit et les frappes ne vont nulle part.</p>",
            "<ol><li>Supprime l'appairage sur l'ordinateur (<em>Supprimer l'appareil</em>).</li><li>Supprime-le aussi sur le téléphone (<em>Oublier</em> dans les paramètres Bluetooth). Les deux côtés comptent.</li><li>Ouvre l'écran 💻 dans Sekuvo et laisse-le ouvert.</li><li>Réappaire, en commençant <strong>par l'ordinateur</strong>.</li><li>Pour confirmer sous Windows : le <em>Gestionnaire de périphériques → Périphériques d'interface utilisateur</em> devrait maintenant lister un appareil Bluetooth HID.</li></ol>",
            "<p>Sur macOS, la première connexion peut ouvrir l'<strong>Assistant de configuration du clavier</strong>, qui demande d'appuyer sur une touche à côté de la touche majuscule. Tant que cette fenêtre n'est pas fermée, macOS ne traite rien — c'est la cause habituelle du « connecté mais silencieux » sur un Mac.</p>",
            "<h3>Vitesse, et comment la vérifier</h3>",
            "<p>Les touches sont envoyées une à la fois, donc un secret long prend réellement du temps — la boîte de dialogue affiche une estimation. Trois vitesses sont proposées, et le fait que la sûre soit celle par défaut est volontaire. Avant de l'augmenter, utilise le <strong>⏱ Test de vitesse</strong> : il saisit dix blocs identiques séparés par des espaces et rapporte les caractères par seconde mesurés. Si ne serait-ce qu'un bloc diffère, cette vitesse n'est pas sûre sur cet ordinateur — baisse d'un cran.</p>",
            "<p>Le test de vitesse sert aussi de diagnostic : rien de saisi du tout signifie un problème d'appairage, des caractères déformés signifient la disposition, une saisie coupée signifie la vitesse.</p>",
            "<p>Pendant la saisie, tu as une barre de progression et un bouton <strong>Arrêter</strong>. Si la file d'envoi se bloque, Sekuvo réessaie avec un délai croissant et, si cela échoue encore, <em>s'arrête et te le dit</em> en indiquant à quel caractère — un secret n'est jamais saisi à moitié en silence.</p>",
        ]),
        ("lock", "Fonctionnement du verrouillage", [
            "<p>Le coffre se verrouille dès que l'écran sur lequel il se trouve s'éteint — replier un téléphone pliable compte aussi. À cet instant, la clé est effacée de la mémoire ; les titres des entrées peuvent encore être listés, mais rien ne peut être déchiffré.</p>",
            "<p>Quitter l'application avec l'écran allumé ne la verrouille <em>pas</em>. C'est volontaire : l'application, le clavier et la saisie automatique partagent une seule session, sinon basculer vers ton navigateur pour coller un mot de passe t'enfermerait dehors en pleine tâche.</p>",
        ]),
        ("quick", "Accès rapide — un compromis assumé", [
            "<p>Les entrées que tu marques explicitement comme « utiliser au clavier sans mot de passe » sont enregistrées une seconde fois, chiffrées avec une clé d'appareil distincte, afin que le clavier puisse les lire <em>pendant que le coffre est verrouillé</em>.</p>",
            "<p>Le compromis est énoncé clairement : ces entrées sont protégées par le verrouillage d'écran de ton téléphone, pas par ton mot de passe principal. N'y mets pas de mots de passe. Le marquage est désactivé par défaut ; la seule exception concerne les nouvelles entrées <strong>Quotidien</strong>, qui démarrent marquées parce que les noms et numéros de téléphone sont exactement ce que tu veux avoir sous la main — tu peux désactiver chacune d'elles.</p>",
        ]),
        ("backup", "Sauvegardes et restauration", [
            "<p>La sauvegarde système (sauvegarde Google, transfert d'appareil) est délibérément désactivée, il n'existe donc qu'une seule façon pour ton coffre de quitter le téléphone, et c'est celle que tu choisis : <strong>Paramètres → Créer une sauvegarde chiffrée</strong>.</p>",
            "<p>Tu choisis un <em>mot de passe de sauvegarde</em> — fais-le différent de ton mot de passe principal, car c'est le mot de passe de sauvegarde qui finit par être saisi sur des ordinateurs. Le résultat est un unique fichier <code>.vaultbak</code> que tu enregistres où tu veux : Drive, une carte SD, une clé USB.</p>",
            "<p>Le fichier est indépendant de l'appareil : son propre sel et ses paramètres de dérivation de clé vivent dans son en-tête. Le fichier plus le mot de passe de sauvegarde restaurent tout sur n'importe quel téléphone, même après une réinitialisation d'usine. Restaure depuis <strong>Paramètres → Restaurer depuis une sauvegarde</strong>, ou depuis l'écran d'accueil lors d'une installation neuve.</p>",
            "<p>La restauration propose <em>ajouter à l'existant</em> ou <em>tout remplacer</em>. Les deux sont vérifiées avant que quoi que ce soit ne soit écrit — un mot de passe incorrect échoue dès l'étape d'authentification, et rien n'est supprimé avant que les nouvelles données ne soient confirmées.</p>",
        ]),
        ("transfer", "Ramener des secrets depuis un ordinateur", [
            "<p>Saisir une longue clé à la main sur un téléphone est l'endroit où les erreurs se produisent. Sekuvo les fait plutôt voyager sous forme d'enveloppe chiffrée, sous deux formes : du texte que tu colles, ou des codes QR que tu scannes.</p>",
            "<p><strong>Sur le téléphone :</strong> le bouton ➕ propose <em>Importer via QR</em> et <em>Importer depuis du texte</em>. L'import QR ouvre la caméra ; les images sont décodées sur l'appareil, et les transferts multi-images affichent leur progression pendant la collecte.</p>",
            "<h3>L'outil côté ordinateur</h3>",
            "<p>L'outil qui construit ces enveloppes est un simple fichier HTML, et c'est délibérément <strong>un téléchargement, pas un site web</strong>. sekuvo.com ne te demande jamais de secret ; une page qui le ferait ressemblerait exactement à un site de phishing.</p>",
            "<ol><li>Ouvre le projet sur GitHub et va dans <strong>Releases</strong>.</li><li>Télécharge <code>aktar.html</code> depuis la dernière version.</li><li>Vérifie son SHA-256 par rapport à la valeur publiée à côté : <code>shasum -a 256 aktar.html</code> sous macOS ou Linux, <code>certutil -hashfile aktar.html SHA256</code> sous Windows.</li><li>Ouvre le fichier en double-cliquant dessus. Il s'exécute depuis ton disque — la barre d'adresse affiche <code>file://</code>, pas un site web.</li><li>Colle ton texte, définis un mot de passe de transfert, et l'outil produit l'enveloppe sous forme de texte ou de codes QR.</li><li>Sur le téléphone, scanne ou colle, saisis le même mot de passe, puis choisis d'ajouter ou de remplacer.</li></ol>",
            "<p>Tout le chiffrement se produit dans ton navigateur, sur ta machine. Il existe aussi <code>vault-clip.py</code> pour la ligne de commande, qui fait la même chose depuis le presse-papiers ou un fichier et peut afficher les codes QR dans un terminal.</p>",
            "<h3>Si tu préfères ne pas utiliser l'outil</h3>",
            "<p>L'enveloppe est un format ouvert, pas quelque chose que seul Sekuvo peut créer : PBKDF2-HMAC-SHA256 sur 310 000 tours, AES-256-GCM, enveloppé dans un petit objet JSON. Tu peux le construire toi-même à partir d'une trentaine de lignes que tu as lues, puis coller le résultat dans <em>Importer depuis du texte</em> — l'application n'a aucun moyen de savoir quel outil l'a produit, et cela lui est égal.</p>",
            "<p>La recette est dans le dépôt : <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (rédigée en turc).</p>",
        ]),
        ("log", "Journal d'utilisation", [
            "<p>Sekuvo enregistre quel champ de quelle entrée est allé où et quand : vers le presse-papiers, vers un ordinateur par Bluetooth (avec le nom de l'appareil cible), ou saisi dans une application depuis le clavier. Quand un ordinateur est compromis, cela répond à « qu'est-ce qui y est allé, que dois-je changer ».</p>",
            "<p>Le journal est chiffré avec la même clé que tes entrées et <strong>les valeurs n'y sont jamais écrites</strong> — seulement le type d'événement, le nom du champ et la destination. Supprimer une entrée supprime son journal, et tu peux tout effacer depuis les Paramètres.</p>",
        ]),
        ("generator", "Générateur de mots de passe", [
            "<p>Accessible depuis l'icône 🎲 sur l'écran d'accueil, ou à côté du champ de mot de passe lors de la modification d'une entrée. Il utilise une source d'aléa cryptographique, produit de 8 à 64 caractères, permet de choisir les classes de caractères, peut retirer les caractères ambigus, et affiche l'entropie résultante en bits.</p>",
        ]),
    ],
)

G["bn"] = dict(
    nav_label="গাইড",
    title="Sekuvo — গাইড",
    desc="Sekuvo কীভাবে ব্যবহার করবেন: প্রথম চালু, অটোফিল, কীবোর্ড, ব্লুটুথ দিয়ে কম্পিউটারে টাইপ করা, ব্যাকআপ ও ট্রান্সফার।",
    h1="গাইড",
    lede="Sekuvo যা যা করে, আপনার প্রয়োজন হতে পারে এমন ক্রমে। এখানে কোনোকিছুর জন্যই অ্যাকাউন্ট বা ইন্টারনেট সংযোগ লাগে না।",
    back="← sekuvo.com-এ ফিরে যান",
    sections=[
        ("start", "প্রথম চালু", [
            "<p>প্রথম চালুতে আপনি একটি <strong>মূল পাসওয়ার্ড</strong> সেট করেন। আপনার সংরক্ষিত প্রতিটি গোপন তথ্য এর থেকে তৈরি একটি কী দিয়ে এনক্রিপ্ট করা হয়, তাই এটিই একমাত্র জিনিস যা Sekuvo আপনাকে ফিরে পেতে সাহায্য করতে পারে না — এগিয়ে যাওয়ার আগে এটি নিরাপদ কোথাও লিখে রাখুন।</p>",
            "<p>অন্য ফোনের ব্যাকআপ আছে? স্বাগত স্ক্রিনে <strong>“আমার একটি ব্যাকআপ আছে — এটি পুনরুদ্ধার করুন”</strong> চাপুন। আপনি তখনও এই ডিভাইসের জন্য প্রথমে একটি মূল পাসওয়ার্ড সেট করবেন, তারপর ফাইল বাছাইকারীটি নিজে থেকেই খুলবে এবং আপনার এন্ট্রিগুলো ফিরে আসবে।</p>",
            "<p>আপনার ফোনে ফিঙ্গারপ্রিন্ট বা ফেস সেন্সর থাকলে, সেটআপের ঠিক পরেই Sekuvo এটি ব্যবহারের প্রস্তাব দেয়। এটি শুধু একটি সুবিধার স্তর: মূল পাসওয়ার্ড সবসময় কাজ করে, এবং এটিই ফ্যাক্টরি রিসেটের পরও টিকে থাকে।</p>",
        ]),
        ("entries", "যা সংরক্ষণ করতে পারেন", [
            "<p>চার ধরনের এন্ট্রি একটি ভল্টে সাধারণত যা রাখা হয় তার বেশিরভাগ কভার করে:</p>",
            "<ul><li><strong>অ্যাকাউন্ট / পাসওয়ার্ড</strong> — ইউজারনেম, পাসওয়ার্ড, সাইট বা অ্যাপ।</li><li><strong>দৈনন্দিন</strong> — নাম, ফোন, ইমেইল, ঠিকানা। ফর্মগুলো যা বারবার চায়।</li><li><strong>কার্ড</strong> — কার্ড নম্বর, মেয়াদ শেষ, CVV, IBAN।</li><li><strong>নিরাপদ নোট</strong> — মুক্ত লেখা, স্ক্রিপ্ট, কী, পুনরুদ্ধার কোড ও কনফিগারেশন ফাইলের জন্য উপ-প্রকারসহ।</li></ul>",
            "<p>অ্যাকাউন্ট ও দৈনন্দিন এন্ট্রি <strong>কাস্টম ফিল্ড</strong>ও নেয়: আপনার ইচ্ছেমতো যেকোনো “নাম + মান” জোড়া। কাস্টম ফিল্ডগুলো বিল্ট-ইন ফিল্ডের মতোই এনক্রিপ্ট করা হয় এবং একই সব জায়গায় দেখা যায়।</p>",
        ]),
        ("channels", "ক্লিপবোর্ড ছাড়াই গোপন তথ্য ব্যবহার", [
            "<p>ক্লিপবোর্ড অন্য অ্যাপগুলো পড়তে পারে এবং এখান থেকেই গোপন তথ্য চুরি হয়। তাই Sekuvo একটি মান সরাসরি তার গন্তব্যে পৌঁছে দেওয়ার তিনটি উপায় দেয়। আপনি তবু কপি করতে পারেন — ৪৫ সেকেন্ড পর ক্লিপবোর্ড নিজে থেকেই মুছে যায় — তবে নিচের তিনটি চ্যানেলই এই অ্যাপের থাকার মূল কারণ।</p>",
        ]),
        ("autofill", "অটোফিল (ফোনের ভেতরে)", [
            "<p>Sekuvo Android-এর অটোফিল সার্ভিস হিসেবে কাজ করতে পারে, ফলে সাইন-ইন ও কার্ড ফর্মে সরাসরি আপনার এন্ট্রি দেখা যায়।</p>",
            "<p><strong>চালু করতে:</strong> Sekuvo → সেটিংস → <em>অটোফিল চালু করুন</em> → সিস্টেম তালিকা থেকে Sekuvo বেছে নিন। এই তালিকার নাম ডিভাইসভেদে ভিন্ন: Samsung ও Android 14+-এ <em>পাসওয়ার্ড, পাসকী ও অটোফিল → পছন্দের সার্ভিস</em>; স্টক Android-এ <em>অটোফিল সার্ভিস</em>।</p>",
            "<p>এরপর, যেকোনো অ্যাপে ইউজারনেম, পাসওয়ার্ড বা কার্ড ফিল্ডে চাপলে কীবোর্ডের উপরে আপনার মিলে যাওয়া এন্ট্রিগুলো দেখা যায়। ভল্ট লক থাকলে আগে একটি আনলক ধাপ আসে — লক থাকা অবস্থায় সিস্টেমকে একদমই কিছু দেওয়া হয় না।</p>",
        ]),
        ("keyboard", "Sekuvo কীবোর্ড (ফোনের ভেতরে)", [
            "<p>কীবোর্ড অ্যাড-অনটি যেকোনো অ্যাপের যেকোনো ফিল্ডে সংরক্ষিত মান সরাসরি টাইপ করে, কপি করার কোনো ধাপ ছাড়াই।</p>",
            "<p><strong>চালু করতে:</strong> Sekuvo → সেটিংস → <em>কীবোর্ড চালু করুন</em> → সিস্টেম তালিকায় এটি চালু করুন, তারপর প্রয়োজনে কীবোর্ড সুইচার থেকে “Sekuvo কীবোর্ড” বেছে নিন।</p>",
            "<p>সম্প্রতি ব্যবহৃত এন্ট্রিগুলো উপরে থাকে এবং 🔍 শিরোনাম, ইউজারনেম ও ঠিকানায় খোঁজে। ভল্ট লক থাকলে কীবোর্ডে শুধু দ্রুত-অ্যাক্সেসের জন্য চিহ্নিত এন্ট্রিগুলো দেখা যায় — নিচে দেখুন।</p>",
        ]),
        ("bluetooth", "ব্লুটুথ দিয়ে কম্পিউটারে টাইপ করা", [
            "<p>আপনার ফোন একটি ব্লুটুথ কীবোর্ড হিসেবে কাজ করতে পারে এবং আপনার কম্পিউটারের কার্সারে গোপন তথ্য টাইপ করতে পারে। কম্পিউটারে কিছুই ইনস্টল হয় না, এটি Windows, macOS ও Linux-এ কাজ করে, এবং মানটি কখনো ক্লিপবোর্ড বা নেটওয়ার্ক স্পর্শ করে না। Android 9 বা তার পরের সংস্করণ প্রয়োজন।</p>",
            "<h3>ধাপে ধাপে</h3>",
            "<ol><li>Sekuvo-তে, এন্ট্রিটি খুলুন এবং যে ফিল্ড টাইপ করতে চান তার পাশের 💻 আইকনে চাপুন। <strong>এই স্ক্রিনটি খোলা রাখুন</strong> — ফোনটি শুধু তখনই নিজেকে কীবোর্ড হিসেবে ঘোষণা করে।</li><li>কম্পিউটারে, ফোনটিকে নতুন ব্লুটুথ ডিভাইস হিসেবে যোগ করুন: Windows-এ <em>সেটিংস → ব্লুটুথ ও ডিভাইস → ডিভাইস যোগ করুন → ব্লুটুথ</em>, অথবা macOS-এ <em>সিস্টেম সেটিংস → ব্লুটুথ</em>।</li><li>দুই পাশেই জোড়া লাগানোর কোড নিশ্চিত করুন।</li><li>ফোনে ফিরে এসে তালিকা থেকে আপনার কম্পিউটার বেছে নিন এবং “সংযুক্ত” দেখা পর্যন্ত অপেক্ষা করুন।</li><li><strong>কম্পিউটারের</strong> কীবোর্ড লেআউট বেছে নিন — ফোনেরটি নয়। কম্পিউটার কী-কোড নিজের মতো বুঝে নেয়, তাই ভুল লেআউট নিঃশব্দে @ \" ? এর মতো অক্ষরকে অন্য অক্ষরে বদলে দেয়।</li><li>কম্পিউটারে যে ফিল্ডে মানটি যাওয়া দরকার সেখানে ক্লিক করুন।</li><li>ফোনে <strong>টাইপ করুন</strong> চাপুন। তিন সেকেন্ডের একটি কাউন্টডাউনের পর — যা আপনাকে সেই ফিল্ডে ক্লিক করার সময় দেওয়ার জন্যই আছে — মানটি একটি একটি করে অক্ষর টাইপ হয়।</li></ol>",
            "<h3>সংযুক্ত, কিন্তু কিছুই টাইপ হচ্ছে না</h3>",
            "<p>প্রায় সবসময় একই কারণ: কম্পিউটারটি আগে কোনো এক সময় আপনার ফোনকে <em>সাধারণ ফোন হিসেবে</em> জোড়া লাগিয়েছিল, তাই কখনো এর জন্য কীবোর্ড (HID) সার্ভিস চালু করেনি। সংযোগ সফল হয় কিন্তু কীস্ট্রোকগুলো কোথাও পৌঁছায় না।</p>",
            "<ol><li>কম্পিউটারে জোড়া লাগানো তুলে ফেলুন (<em>ডিভাইস সরান</em>)।</li><li>ফোনেও তুলে ফেলুন (ব্লুটুথ সেটিংসে <em>ভুলে যান</em>)। দুই পাশই গুরুত্বপূর্ণ।</li><li>Sekuvo-তে 💻 স্ক্রিনটি খুলুন এবং খোলা রাখুন।</li><li><strong>কম্পিউটার থেকে শুরু করে</strong> আবার জোড়া লাগান।</li><li>Windows-এ নিশ্চিত করতে: ডিভাইস ম্যানেজার → হিউম্যান ইন্টারফেস ডিভাইসে এখন একটি ব্লুটুথ HID ডিভাইস দেখানো উচিত।</li></ol>",
            "<p>macOS-এ, প্রথম সংযোগে <strong>কীবোর্ড সেটআপ সহায়ক</strong> খুলতে পারে, যা শিফট কী-এর পাশের একটি কী চাপতে বলে। এই উইন্ডোটি বন্ধ না করা পর্যন্ত macOS কিছুই প্রক্রিয়া করে না — Mac-এ “সংযুক্ত কিন্তু নীরব” হওয়ার এটাই সাধারণ কারণ।</p>",
            "<h3>গতি, এবং কীভাবে যাচাই করবেন</h3>",
            "<p>কী একটি একটি করে পাঠানো হয়, তাই লম্বা গোপন তথ্যে সত্যিই সময় লাগে — ডায়ালগে একটি আনুমানিক সময় দেখানো হয়। তিনটি গতি দেওয়া আছে, এবং নিরাপদটি ডিফল্ট হওয়া ইচ্ছাকৃত। গতি বাড়ানোর আগে <strong>⏱ স্পিড টেস্ট</strong> ব্যবহার করুন: এটি স্পেস দিয়ে আলাদা করা দশটি একই রকম ব্লক টাইপ করে এবং প্রতি সেকেন্ডে মাপা অক্ষরসংখ্যা জানায়। একটি ব্লকও ভিন্ন হলে, এই কম্পিউটারে সেই গতিটি নিরাপদ নয় — এক ধাপ নামিয়ে নিন।</p>",
            "<p>স্পিড টেস্ট নির্ণয়ের কাজেও ব্যবহার করা যায়: একদমই কিছু টাইপ না হওয়া মানে জোড়া লাগানোর সমস্যা, অক্ষর এলোমেলো হওয়া মানে লেআউটের সমস্যা, মাঝপথে থেমে যাওয়া মানে গতির সমস্যা।</p>",
            "<p>টাইপ করার সময় একটি প্রগ্রেস বার এবং <strong>থামান</strong> বোতাম দেখা যায়। পাঠানোর সারি আটকে গেলে, Sekuvo ক্রমবর্ধমান বিরতি দিয়ে আবার চেষ্টা করে এবং তাতেও ব্যর্থ হলে, ঠিক কোন অক্ষরে থেমেছে তা <em>বলে দিয়ে থেমে যায়</em> — কোনো গোপন তথ্য নিঃশব্দে অর্ধেক টাইপ হয়ে থাকে না।</p>",
        ]),
        ("lock", "লকিং কীভাবে কাজ করে", [
            "<p>যে স্ক্রিনে আছে সেটি বন্ধ হওয়ার মুহূর্তেই ভল্ট লক হয়ে যায় — ফোল্ডেবল ফোন ভাঁজ করাও এর মধ্যে পড়ে। সেই মুহূর্তে কী মেমোরি থেকে মুছে যায়; এন্ট্রির শিরোনাম হয়তো তখনো তালিকায় থাকে, কিন্তু কিছুই ডিক্রিপ্ট করা যায় না।</p>",
            "<p>স্ক্রিন চালু থাকা অবস্থায় অ্যাপ থেকে বেরিয়ে গেলে এটি লক হয় <em>না</em>। এটি ইচ্ছাকৃত: অ্যাপ, কীবোর্ড ও অটোফিল একটি সেশন শেয়ার করে, নাহলে পাসওয়ার্ড পেস্ট করতে ব্রাউজারে গেলেই কাজের মাঝপথে আপনাকে বাইরে আটকে রাখত।</p>",
        ]),
        ("quick", "দ্রুত অ্যাক্সেস — একটি সচেতন আপস", [
            "<p>আপনি স্পষ্টভাবে যে এন্ট্রিগুলোকে “পাসওয়ার্ড ছাড়াই কীবোর্ডে ব্যবহার করুন” বলে চিহ্নিত করেন, সেগুলো আলাদা একটি ডিভাইস কী দিয়ে এনক্রিপ্ট করে দ্বিতীয়বার সংরক্ষণ করা হয়, যাতে <em>ভল্ট লক থাকা অবস্থায়ও</em> কীবোর্ড সেগুলো পড়তে পারে।</p>",
            "<p>এই আপসটি স্পষ্টভাবে বলা আছে: এই এন্ট্রিগুলো আপনার মূল পাসওয়ার্ড নয়, আপনার ফোনের স্ক্রিন লক দিয়ে সুরক্ষিত। এতে পাসওয়ার্ড রাখবেন না। এই চিহ্নটি ডিফল্টভাবে বন্ধ থাকে; একমাত্র ব্যতিক্রম নতুন <strong>দৈনন্দিন</strong> এন্ট্রি, যেগুলো চিহ্নিত অবস্থায় শুরু হয় কারণ নাম ও ফোন নম্বর ঠিক এমন জিনিস যা আপনি হাতের কাছে চান — আপনি এগুলোর যেকোনোটি বন্ধ করে দিতে পারেন।</p>",
        ]),
        ("backup", "ব্যাকআপ ও পুনরুদ্ধার", [
            "<p>সিস্টেম ব্যাকআপ (Google ব্যাকআপ, ডিভাইস ট্রান্সফার) ইচ্ছাকৃতভাবে বন্ধ, তাই আপনার ভল্ট ফোন ছাড়ার একটাই পথ আছে, এবং সেটি আপনার নিজের বেছে নেওয়া: <strong>সেটিংস → এনক্রিপ্টেড ব্যাকআপ তৈরি করুন</strong>।</p>",
            "<p>আপনি একটি <em>ব্যাকআপ পাসওয়ার্ড</em> বেছে নেন — এটি মূল পাসওয়ার্ড থেকে আলাদা রাখুন, কারণ এই পাসওয়ার্ডটিই কম্পিউটারে টাইপ করা হয়। ফলাফল একটি একক <code>.vaultbak</code> ফাইল, যা আপনি যেকোনো জায়গায় রাখতে পারেন: ড্রাইভ, একটি SD কার্ড, একটি USB স্টিক।</p>",
            "<p>ফাইলটি ডিভাইস-স্বাধীন: এর নিজস্ব সল্ট ও কী-ডেরিভেশন প্যারামিটার এর হেডারে থাকে। ফাইল এবং ব্যাকআপ পাসওয়ার্ড দিয়ে যেকোনো ফোনে, এমনকি ফ্যাক্টরি রিসেটের পরেও, সবকিছু ফিরে আসে। <strong>সেটিংস → ব্যাকআপ থেকে পুনরুদ্ধার করুন</strong> থেকে, অথবা নতুন ইনস্টলে স্বাগত স্ক্রিন থেকে পুনরুদ্ধার করুন।</p>",
            "<p>পুনরুদ্ধারে <em>বিদ্যমানে যোগ করুন</em> বা <em>সব প্রতিস্থাপন করুন</em> বেছে নেওয়া যায়। কিছু লেখার আগেই দুটোই যাচাই করা হয় — ভুল পাসওয়ার্ড যাচাইকরণ ধাপেই ব্যর্থ হয়, এবং নতুন তথ্য নিশ্চিত না হওয়া পর্যন্ত কিছুই মোছা হয় না।</p>",
        ]),
        ("transfer", "কম্পিউটার থেকে গোপন তথ্য আনা", [
            "<p>ফোনে হাতে একটি লম্বা কী টাইপ করাই সবচেয়ে বেশি ভুল হওয়ার জায়গা। তাই Sekuvo এগুলো একটি এনক্রিপ্টেড এনভেলপ হিসেবে পার করে, দুই রূপে: আপনার পেস্ট করা লেখা, অথবা আপনার স্ক্যান করা QR কোড।</p>",
            "<p><strong>ফোনে:</strong> ➕ বোতামে <em>QR দিয়ে ইম্পোর্ট করুন</em> এবং <em>টেক্সট থেকে ইম্পোর্ট করুন</em> অপশন আছে। QR ইম্পোর্ট ক্যামেরা খোলে; ফ্রেমগুলো ডিভাইসেই ডিকোড হয়, এবং একাধিক-ফ্রেমের ট্রান্সফারে সংগ্রহের অগ্রগতি দেখানো হয়।</p>",
            "<h3>কম্পিউটার-সাইড টুল</h3>",
            "<p>যে টুলটি এই এনভেলপগুলো তৈরি করে সেটি একটি একক HTML ফাইল, এবং এটি ইচ্ছাকৃতভাবে <strong>একটি ডাউনলোড, ওয়েবসাইট নয়</strong>। sekuvo.com আপনার কাছে কখনো গোপন তথ্য চায় না; যে পেজ তা চাইবে সেটি ঠিক একটি ফিশিং সাইটের মতোই দেখাবে।</p>",
            "<ol><li>GitHub-এ প্রজেক্টটি খুলুন এবং <strong>Releases</strong>-এ যান।</li><li>সর্বশেষ রিলিজ থেকে <code>aktar.html</code> ডাউনলোড করুন।</li><li>পাশে প্রকাশিত মানের সাথে এর SHA-256 মিলিয়ে দেখুন: macOS বা Linux-এ <code>shasum -a 256 aktar.html</code>, Windows-এ <code>certutil -hashfile aktar.html SHA256</code>।</li><li>ডাবল-ক্লিক করে ফাইলটি খুলুন। এটি আপনার ডিস্ক থেকে চলে — অ্যাড্রেস বারে ওয়েবসাইট নয়, <code>file://</code> দেখা যায়।</li><li>আপনার লেখা পেস্ট করুন, একটি ট্রান্সফার পাসওয়ার্ড সেট করুন, এবং এটি টেক্সট বা QR কোড হিসেবে এনভেলপ তৈরি করে।</li><li>ফোনে, স্ক্যান বা পেস্ট করুন, একই পাসওয়ার্ড দিন, তারপর যোগ করা বা প্রতিস্থাপন করা বেছে নিন।</li></ol>",
            "<p>সব এনক্রিপশন আপনার ব্রাউজারের ভেতরে, আপনার নিজের মেশিনে ঘটে। কমান্ড লাইনের জন্য <code>vault-clip.py</code>ও আছে, যা ক্লিপবোর্ড বা একটি ফাইল থেকে একই কাজ করে এবং টার্মিনালে QR কোড দেখাতে পারে।</p>",
            "<h3>যদি টুলটি ব্যবহার করতে না চান</h3>",
            "<p>এনভেলপটি একটি খোলা ফরম্যাট, শুধু Sekuvo-ই তৈরি করতে পারে এমন কিছু নয়: PBKDF2-HMAC-SHA256 ৩,১০,০০০ রাউন্ডে, AES-256-GCM, একটি ছোট JSON অবজেক্টে মোড়া। আপনি পড়া প্রায় ত্রিশ লাইন কোড দিয়ে নিজেই এটি তৈরি করতে পারেন এবং ফলাফলটি <em>টেক্সট থেকে ইম্পোর্ট করুন</em>-এ পেস্ট করতে পারেন — অ্যাপটি জানার কোনো উপায় নেই কোন টুল দিয়ে এটি তৈরি হয়েছে, এবং এতে কিছু যায়ও আসে না।</p>",
            "<p>রেসিপিটি রিপোজিটরিতে আছে: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (তুর্কি ভাষায় লেখা)।</p>",
        ]),
        ("log", "ব্যবহারের লগ", [
            "<p>Sekuvo রেকর্ড করে কোন এন্ট্রির কোন ফিল্ড কখন কোথায় গেছে: ক্লিপবোর্ডে, ব্লুটুথ দিয়ে কোনো কম্পিউটারে (লক্ষ্য ডিভাইসের নামসহ), অথবা কীবোর্ড থেকে কোনো অ্যাপে টাইপ হয়েছে। কোনো কম্পিউটার আপোস হলে, এটি উত্তর দেয় “সেখানে কী গেছে, আমার কী পরিবর্তন করা দরকার”।</p>",
            "<p>লগটি আপনার এন্ট্রির মতোই একই কী দিয়ে এনক্রিপ্ট করা এবং <strong>মানগুলো কখনো এতে লেখা হয় না</strong> — শুধু ইভেন্টের ধরন, ফিল্ডের নাম এবং গন্তব্য। একটি এন্ট্রি মুছলে তার লগও মুছে যায়, এবং আপনি সেটিংস থেকে পুরো লগ মুছে ফেলতে পারেন।</p>",
        ]),
        ("generator", "পাসওয়ার্ড জেনারেটর", [
            "<p>হোম স্ক্রিনের 🎲 আইকন থেকে, অথবা কোনো এন্ট্রি এডিট করার সময় পাসওয়ার্ড ফিল্ডের পাশ থেকে খোলা যায়। এটি একটি ক্রিপ্টোগ্রাফিক র‍্যান্ডম উৎস ব্যবহার করে, ৮–৬৪ অক্ষর তৈরি করে, অক্ষরের শ্রেণি বেছে নিতে দেয়, একই রকম দেখতে অক্ষর বাদ দিতে পারে, এবং ফলাফলের এনট্রপি বিট আকারে দেখায়।</p>",
        ]),
    ],
)

G["pt"] = dict(
    nav_label="Guia",
    title="Sekuvo — Guia",
    desc="Como usar o Sekuvo: primeira execução, preenchimento automático, o teclado, digitação em um computador via Bluetooth, backups e transferências.",
    h1="Guia",
    lede="Tudo o que o Sekuvo faz, na ordem em que você provavelmente vai precisar. Nada aqui exige conta ou conexão com a internet.",
    back="← Voltar para sekuvo.com",
    sections=[
        ("start", "Primeira execução", [
            "<p>Na primeira abertura, você define uma <strong>senha principal</strong>. Cada segredo que você salva é criptografado com uma chave derivada dela, então é a única coisa que o Sekuvo não pode ajudar você a recuperar — anote-a em um lugar seguro antes de continuar.</p>",
            "<p>Já tem um backup de outro telefone? Toque em <strong>“Tenho um backup — restaurá-lo”</strong> na tela de boas-vindas. Você ainda define primeiro uma senha principal para este dispositivo, e depois o seletor de arquivos abre sozinho e seus itens voltam.</p>",
            "<p>Se o seu telefone tem sensor de impressão digital ou de rosto, o Sekuvo oferece usá-lo logo após a configuração. Isso é apenas uma camada de conveniência: a senha principal sempre funciona, e é ela que sobrevive a uma restauração de fábrica.</p>",
        ]),
        ("entries", "O que você pode salvar", [
            "<p>Quatro tipos de item cobrem a maior parte do que as pessoas guardam em um cofre:</p>",
            "<ul><li><strong>Conta / Senha</strong> — usuário, senha, site ou aplicativo.</li><li><strong>Dia a dia</strong> — nome, telefone, e-mail, endereço. O que os formulários pedem o tempo todo.</li><li><strong>Cartão</strong> — número do cartão, validade, CVV, IBAN.</li><li><strong>Nota segura</strong> — texto livre, com subtipos para scripts, chaves, códigos de recuperação e arquivos de configuração.</li></ul>",
            "<p>Itens de Conta e Dia a dia também aceitam <strong>campos personalizados</strong>: qualquer par “nome + valor” que você quiser. Campos personalizados são criptografados exatamente como os integrados e aparecem em todos os lugares em que os outros aparecem.</p>",
        ]),
        ("channels", "Usando um segredo sem a área de transferência", [
            "<p>A área de transferência pode ser lida por outros aplicativos e é onde segredos são roubados. Por isso o Sekuvo oferece três formas de entregar um valor direto ao destino. Você ainda pode copiar — a área de transferência é limpa automaticamente após 45 segundos — mas os três canais abaixo são o motivo de o aplicativo existir.</p>",
        ]),
        ("autofill", "Preenchimento automático (dentro do telefone)", [
            "<p>O Sekuvo pode atuar como o serviço de preenchimento automático do Android, então formulários de login e de cartão oferecem seus itens diretamente.</p>",
            "<p><strong>Para ativar:</strong> Sekuvo → Configurações → <em>Ativar preenchimento automático</em> → escolha o Sekuvo na lista do sistema. Essa lista tem nomes diferentes por dispositivo: em Samsung e Android 14+ é <em>Senhas, chaves de acesso e preenchimento automático → Serviço preferido</em>; no Android puro é <em>Serviço de preenchimento automático</em>.</p>",
            "<p>Depois disso, tocar em um campo de usuário, senha ou cartão em qualquer aplicativo mostra seus itens correspondentes acima do teclado. Se o cofre estiver bloqueado, aparece primeiro uma etapa de desbloqueio — enquanto bloqueado, o sistema não recebe absolutamente nada.</p>",
        ]),
        ("keyboard", "Teclado Sekuvo (dentro do telefone)", [
            "<p>O complemento de teclado digita valores salvos em qualquer campo, em qualquer aplicativo, sem etapa de cópia.</p>",
            "<p><strong>Para ativar:</strong> Sekuvo → Configurações → <em>Ativar o teclado</em> → ative-o na lista do sistema, depois escolha “Teclado Sekuvo” no seletor de teclado sempre que precisar.</p>",
            "<p>Itens usados recentemente ficam no topo e o 🔍 pesquisa em títulos, usuários e endereços. Com o cofre bloqueado, o teclado mostra apenas itens que você marcou para acesso rápido — veja abaixo.</p>",
        ]),
        ("bluetooth", "Digitando em um computador via Bluetooth", [
            "<p>Seu telefone pode atuar como um teclado Bluetooth e digitar um segredo no cursor do seu computador. Nada é instalado no computador, funciona em Windows, macOS e Linux, e o valor nunca toca a área de transferência ou uma rede. Requer Android 9 ou mais recente.</p>",
            "<h3>Passo a passo</h3>",
            "<ol><li>No Sekuvo, abra o item e toque no ícone 💻 ao lado do campo que você quer digitar. <strong>Mantenha esta tela aberta</strong> — seu telefone só se anuncia como teclado enquanto ela estiver aberta.</li><li>No computador, adicione o telefone como um novo dispositivo Bluetooth: <em>Configurações → Bluetooth e dispositivos → Adicionar dispositivo → Bluetooth</em> no Windows, ou <em>Ajustes do Sistema → Bluetooth</em> no macOS.</li><li>Confirme o código de pareamento nos dois lados.</li><li>De volta ao telefone, escolha seu computador na lista e espere aparecer “Conectado”.</li><li>Escolha o layout de teclado <strong>do computador</strong> — não o do telefone. O computador interpreta os códigos de tecla, então um layout errado transforma silenciosamente caracteres como @ \" ? em outros.</li><li>Clique no campo do computador onde o valor deve ir.</li><li>Toque em <strong>Digitar</strong> no telefone. Após uma contagem regressiva de três segundos — que existe para você conseguir clicar naquele campo — o valor é digitado tecla por tecla.</li></ol>",
            "<h3>Conectado, mas nada é digitado</h3>",
            "<p>Quase sempre a mesma causa: o computador pareou seu telefone <em>como um telefone</em> em algum momento anterior, então nunca ativou o serviço de teclado (HID) para ele. A conexão funciona e as teclas não vão para lugar nenhum.</p>",
            "<ol><li>Remova o pareamento no computador (<em>Remover dispositivo</em>).</li><li>Remova-o no telefone também (<em>Esquecer</em> nas configurações de Bluetooth). Os dois lados importam.</li><li>Abra a tela 💻 no Sekuvo e deixe-a aberta.</li><li>Pareie de novo, começando <strong>pelo computador</strong>.</li><li>Para confirmar no Windows: o <em>Gerenciador de Dispositivos → Dispositivos de Interface Humana</em> deve agora listar um dispositivo Bluetooth HID.</li></ol>",
            "<p>No macOS, a primeira conexão pode abrir o <strong>Assistente de Configuração do Teclado</strong>, que pede para você pressionar uma tecla ao lado da tecla shift. Até essa janela ser fechada, o macOS não processa nada — essa é a causa comum de “conectado mas silencioso” em um Mac.</p>",
            "<h3>Velocidade, e como verificá-la</h3>",
            "<p>As teclas são enviadas uma de cada vez, então um segredo longo realmente demora — a caixa de diálogo mostra uma estimativa. Três velocidades são oferecidas, e a segura ser o padrão é proposital. Antes de aumentar, use o <strong>⏱ Teste de velocidade</strong>: ele digita dez blocos idênticos separados por espaço e informa os caracteres por segundo medidos. Se ao menos um bloco for diferente, essa velocidade não é segura neste computador — baixe um degrau.</p>",
            "<p>O teste de velocidade também serve como diagnóstico: nada digitado significa pareamento, caracteres embaralhados significam o layout, uma execução cortada significa a velocidade.</p>",
            "<p>Durante a digitação você vê uma barra de progresso e um botão <strong>Parar</strong>. Se a fila de envio travar, o Sekuvo tenta de novo com espera crescente e, se ainda assim falhar, <em>para e avisa você</em> em qual caractere — um segredo nunca fica digitado pela metade em silêncio.</p>",
        ]),
        ("lock", "Como funciona o bloqueio", [
            "<p>O cofre bloqueia no instante em que a tela em que está se apaga — inclusive fechar um telefone dobrável. Nesse instante a chave é apagada da memória; os títulos dos itens podem continuar listados, mas nada pode ser descriptografado.</p>",
            "<p>Sair do aplicativo com a tela acesa <em>não</em> o bloqueia. Isso é proposital: o aplicativo, o teclado e o preenchimento automático compartilham uma sessão, senão trocar para o navegador para colar uma senha deixaria você trancado do lado de fora no meio da tarefa.</p>",
        ]),
        ("quick", "Acesso rápido — uma troca deliberada", [
            "<p>Itens que você marca explicitamente como “usar no teclado sem senha” são salvos uma segunda vez, criptografados com uma chave de dispositivo separada, para que o teclado possa lê-los <em>com o cofre bloqueado</em>.</p>",
            "<p>A troca é dita claramente: esses itens são protegidos pelo bloqueio de tela do seu telefone, não pela sua senha principal. Mantenha senhas fora disso. A marcação vem desativada por padrão; a única exceção são novos itens <strong>Dia a dia</strong>, que começam marcados porque nomes e números de telefone são exatamente o que você quer à mão — você pode desativar qualquer um deles.</p>",
        ]),
        ("backup", "Backups e restauração", [
            "<p>O backup do sistema (backup do Google, transferência de dispositivo) é desativado deliberadamente, então existe exatamente uma forma de seu cofre sair do telefone, e é a que você escolhe: <strong>Configurações → Criar backup criptografado</strong>.</p>",
            "<p>Você escolhe uma <em>senha de backup</em> — deixe-a diferente da sua senha principal, porque a senha de backup é a que acaba sendo digitada em computadores. O resultado é um único arquivo <code>.vaultbak</code> que você salva onde quiser: Drive, um cartão SD, um pendrive.</p>",
            "<p>O arquivo é independente do dispositivo: seu próprio sal e parâmetros de derivação de chave vivem no cabeçalho. Arquivo mais senha de backup restauram tudo em qualquer telefone, mesmo após uma restauração de fábrica. Restaure em <strong>Configurações → Restaurar de um backup</strong>, ou pela tela de boas-vindas em uma instalação nova.</p>",
            "<p>Restaurar oferece <em>adicionar aos existentes</em> ou <em>substituir todos</em>. Ambos são verificados antes de qualquer coisa ser escrita — uma senha errada falha na etapa de autenticação, e nada é excluído até os novos dados serem confirmados.</p>",
        ]),
        ("transfer", "Trazendo segredos de um computador", [
            "<p>Digitar uma chave longa à mão em um telefone é onde erros acontecem. O Sekuvo os transporta como um envelope criptografado, de duas formas: texto que você cola, ou códigos QR que você escaneia.</p>",
            "<p><strong>No telefone:</strong> o botão ➕ oferece <em>Importar por QR</em> e <em>Importar de texto</em>. A importação por QR abre a câmera; os quadros são decodificados no dispositivo, e transferências com vários quadros mostram o progresso enquanto são coletados.</p>",
            "<h3>A ferramenta do lado do computador</h3>",
            "<p>A ferramenta que constrói esses envelopes é um único arquivo HTML, e é deliberadamente <strong>um download, não um site</strong>. O sekuvo.com nunca pede um segredo a você; uma página que fizesse isso seria exatamente como um site de phishing.</p>",
            "<ol><li>Abra o projeto no GitHub e vá em <strong>Releases</strong>.</li><li>Baixe o <code>aktar.html</code> da versão mais recente.</li><li>Confira o SHA-256 dele com o valor publicado ao lado: <code>shasum -a 256 aktar.html</code> no macOS ou Linux, <code>certutil -hashfile aktar.html SHA256</code> no Windows.</li><li>Abra o arquivo dando dois cliques nele. Ele roda a partir do seu disco — a barra de endereço mostra <code>file://</code>, não um site.</li><li>Cole seu texto, defina uma senha de transferência, e ele produz o envelope como texto ou como códigos QR.</li><li>No telefone, escaneie ou cole, digite a mesma senha e escolha adicionar ou substituir.</li></ol>",
            "<p>Toda a criptografia acontece dentro do seu navegador, na sua máquina. Também existe o <code>vault-clip.py</code> para a linha de comando, que faz o mesmo a partir da área de transferência ou de um arquivo e pode desenhar os códigos QR em um terminal.</p>",
            "<h3>Se você preferir não usar a ferramenta</h3>",
            "<p>O envelope é um formato aberto, não algo que só o Sekuvo pode criar: PBKDF2-HMAC-SHA256 com 310.000 rodadas, AES-256-GCM, embrulhado em um pequeno objeto JSON. Você pode construí-lo você mesmo com cerca de trinta linhas que já leu, e colar o resultado em <em>Importar de texto</em> — o aplicativo não tem como saber qual ferramenta o produziu, e não se importa.</p>",
            "<p>A receita está no repositório: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (escrita em turco).</p>",
        ]),
        ("log", "Registro de uso", [
            "<p>O Sekuvo registra qual campo de qual item foi para onde e quando: para a área de transferência, para um computador via Bluetooth (com o nome do dispositivo de destino), ou digitado em um aplicativo pelo teclado. Quando um computador é comprometido, isso responde “o que foi parar lá, o que preciso mudar”.</p>",
            "<p>O registro é criptografado com a mesma chave dos seus itens e <strong>os valores nunca são gravados nele</strong> — apenas o tipo de evento, o nome do campo e o destino. Excluir um item exclui seu registro, e você pode limpar tudo pelas Configurações.</p>",
        ]),
        ("generator", "Gerador de senhas", [
            "<p>Acessível pelo ícone 🎲 na tela inicial, ou ao lado do campo de senha ao editar um item. Ele usa uma fonte criptográfica de aleatoriedade, produz de 8 a 64 caracteres, permite escolher classes de caracteres, pode remover caracteres parecidos entre si, e mostra a entropia resultante em bits.</p>",
        ]),
    ],
)

G["ru"] = dict(
    nav_label="Руководство",
    title="Sekuvo — Руководство",
    desc="Как пользоваться Sekuvo: первый запуск, автозаполнение, клавиатура, ввод на компьютере по Bluetooth, резервные копии и переносы.",
    h1="Руководство",
    lede="Всё, что делает Sekuvo, в том порядке, в котором это, скорее всего, понадобится. Ничто здесь не требует аккаунта или подключения к интернету.",
    back="← Назад на sekuvo.com",
    sections=[
        ("start", "Первый запуск", [
            "<p>При первом открытии вы задаёте <strong>основной пароль</strong>. Каждый секрет, который вы сохраняете, шифруется ключом, полученным из него, поэтому это единственное, что Sekuvo не сможет помочь вам восстановить — запишите его в надёжном месте, прежде чем продолжить.</p>",
            "<p>Уже есть резервная копия с другого телефона? Нажмите «У меня есть резервная копия — восстановить её» на экране приветствия. Вы всё равно сначала зададите основной пароль для этого устройства, а затем выбор файла откроется сам, и ваши записи вернутся.</p>",
            "<p>Если ваш телефон имеет сканер отпечатка или лица, Sekuvo предложит использовать его сразу после настройки. Это лишь слой удобства: основной пароль всегда работает, и именно он переживает сброс до заводских настроек.</p>",
        ]),
        ("entries", "Что можно сохранять", [
            "<p>Четыре типа записей покрывают большую часть того, что люди хранят в хранилище:</p>",
            "<ul><li><strong>Аккаунт / Пароль</strong> — имя пользователя, пароль, сайт или приложение.</li><li><strong>Повседневное</strong> — имя, телефон, эл. почта, адрес. То, что постоянно запрашивают формы.</li><li><strong>Карта</strong> — номер карты, срок действия, CVV, IBAN.</li><li><strong>Защищённая заметка</strong> — свободный текст, с подтипами для скриптов, ключей, кодов восстановления и файлов конфигурации.</li></ul>",
            "<p>Записи типа «Аккаунт» и «Повседневное» также принимают <strong>пользовательские поля</strong>: любую пару «название + значение», какую захотите. Пользовательские поля шифруются точно так же, как встроенные, и появляются везде, где появляются остальные.</p>",
        ]),
        ("channels", "Использование секрета без буфера обмена", [
            "<p>Буфер обмена могут читать другие приложения, и именно там крадут секреты. Поэтому Sekuvo предлагает три способа доставить значение прямо в место назначения. Копировать по-прежнему можно — буфер обмена автоматически очищается через 45 секунд, — но три канала ниже — вот причина существования приложения.</p>",
        ]),
        ("autofill", "Автозаполнение (внутри телефона)", [
            "<p>Sekuvo может выступать службой автозаполнения Android, поэтому формы входа и карты сами предлагают ваши записи.</p>",
            "<p><strong>Чтобы включить:</strong> Sekuvo → Настройки → <em>Включить автозаполнение</em> → выберите Sekuvo в системном списке. Этот список называется по-разному в зависимости от устройства: на Samsung и Android 14+ это «Пароли, ключи доступа и автозаполнение → Предпочтительная служба»; на чистом Android — «Служба автозаполнения».</p>",
            "<p>После этого нажатие на поле имени пользователя, пароля или карты в любом приложении покажет соответствующие записи над клавиатурой. Если хранилище заблокировано, сначала появится шаг разблокировки — пока оно заблокировано, системе не передаётся абсолютно ничего.</p>",
        ]),
        ("keyboard", "Клавиатура Sekuvo (внутри телефона)", [
            "<p>Дополнение клавиатуры вводит сохранённые значения в любое поле, в любом приложении, без шага копирования.</p>",
            "<p><strong>Чтобы включить:</strong> Sekuvo → Настройки → <em>Включить клавиатуру</em> → включите её в системном списке, затем выбирайте «Клавиатура Sekuvo» в переключателе клавиатур, когда потребуется.</p>",
            "<p>Недавно использованные записи находятся сверху, а 🔍 ищет по названиям, именам пользователей и адресам. При заблокированном хранилище клавиатура показывает только записи, отмеченные для быстрого доступа — см. ниже.</p>",
        ]),
        ("bluetooth", "Ввод на компьютере по Bluetooth", [
            "<p>Ваш телефон может выступать Bluetooth-клавиатурой и вводить секрет в позицию курсора на компьютере. На компьютер ничего не устанавливается, работает на Windows, macOS и Linux, а значение никогда не касается буфера обмена или сети. Требуется Android 9 или новее.</p>",
            "<h3>Пошагово</h3>",
            "<ol><li>В Sekuvo откройте запись и нажмите значок 💻 рядом с полем, которое нужно ввести. <strong>Держите этот экран открытым</strong> — телефон объявляет себя клавиатурой только пока он открыт.</li><li>На компьютере добавьте телефон как новое устройство Bluetooth: <em>Настройки → Bluetooth и устройства → Добавить устройство → Bluetooth</em> в Windows, или <em>Системные настройки → Bluetooth</em> в macOS.</li><li>Подтвердите код сопряжения с обеих сторон.</li><li>Вернувшись на телефон, выберите свой компьютер из списка и дождитесь надписи «Подключено».</li><li>Выберите раскладку клавиатуры <strong>КОМПЬЮТЕРА</strong> — не телефона. Компьютер сам интерпретирует коды клавиш, поэтому неверная раскладка незаметно превращает такие символы, как @ \" ?, в другие.</li><li>Кликните в поле на компьютере, куда должно попасть значение.</li><li>Нажмите <strong>Ввести</strong> на телефоне. После обратного отсчёта в три секунды — он даётся, чтобы вы успели кликнуть в нужное поле — значение вводится посимвольно.</li></ol>",
            "<h3>Подключено, но ничего не вводится</h3>",
            "<p>Почти всегда причина одна: компьютер когда-то ранее сопрягал ваш телефон <em>как обычный телефон</em>, поэтому так и не включил для него службу клавиатуры (HID). Соединение работает, а нажатия клавиш никуда не попадают.</p>",
            "<ol><li>Удалите сопряжение на компьютере («Удалить устройство»).</li><li>Удалите его и на телефоне тоже («Забыть» в настройках Bluetooth). Важны обе стороны.</li><li>Откройте экран 💻 в Sekuvo и оставьте его открытым.</li><li>Сопрягите заново, начиная <strong>с компьютера</strong>.</li><li>Чтобы проверить в Windows: <em>Диспетчер устройств → Устройства HID</em> теперь должен показывать устройство Bluetooth HID.</li></ol>",
            "<p>В macOS первое подключение может открыть <strong>Мастер настройки клавиатуры</strong>, который просит нажать клавишу рядом с shift. Пока это окно не закрыто, macOS ничего не обрабатывает — это частая причина «подключено, но тихо» на Mac.</p>",
            "<h3>Скорость и как её проверить</h3>",
            "<p>Нажатия клавиш отправляются по одному, поэтому длинный секрет действительно занимает время — диалоговое окно показывает оценку. Предлагаются три скорости, и то, что безопасная стоит по умолчанию, — намеренное решение. Прежде чем повышать скорость, используйте <strong>⏱ Тест скорости</strong>: он вводит десять одинаковых блоков, разделённых пробелами, и сообщает измеренные символы в секунду. Если хотя бы один блок отличается, эта скорость небезопасна на данном компьютере — выберите на ступень ниже.</p>",
            "<p>Тест скорости служит и диагностикой: ничего не введено — проблема в сопряжении, символы перепутаны — в раскладке, ввод обрывается на середине — в скорости.</p>",
            "<p>Во время ввода вы видите индикатор прогресса и кнопку <strong>Остановить</strong>. Если очередь отправки зависает, Sekuvo повторяет попытку с растущей паузой, а если это всё равно не помогает, <em>останавливается и сообщает вам</em>, на каком символе — секрет никогда не вводится наполовину молча.</p>",
        ]),
        ("lock", "Как работает блокировка", [
            "<p>Хранилище блокируется в тот момент, когда гаснет экран, на котором оно открыто — складывание складного телефона тоже считается. В этот момент ключ стирается из памяти; названия записей могут по-прежнему отображаться в списке, но ничего нельзя расшифровать.</p>",
            "<p>Выход из приложения при включённом экране <em>не</em> блокирует его. Это намеренно: приложение, клавиатура и автозаполнение используют общий сеанс, иначе переключение в браузер, чтобы вставить пароль, оставило бы вас снаружи посреди задачи.</p>",
        ]),
        ("quick", "Быстрый доступ — осознанный компромисс", [
            "<p>Записи, которые вы явно отмечаете как «использовать в клавиатуре без пароля», сохраняются повторно, зашифрованные отдельным ключом устройства, чтобы клавиатура могла их прочитать <em>при заблокированном хранилище</em>.</p>",
            "<p>Компромисс сформулирован прямо: такие записи защищены блокировкой экрана вашего телефона, а не основным паролем. Не держите там пароли. Отметка по умолчанию выключена; единственное исключение — новые записи типа «Повседневное», которые начинаются отмеченными, потому что имена и номера телефонов — это именно то, что вы хотите иметь под рукой; любую из них можно выключить.</p>",
        ]),
        ("backup", "Резервные копии и восстановление", [
            "<p>Системное резервное копирование (резервная копия Google, перенос устройства) намеренно отключено, поэтому существует ровно один способ, которым ваше хранилище покидает телефон, и это тот, который выбираете вы: <strong>Настройки → Создать зашифрованную копию</strong>.</p>",
            "<p>Вы задаёте <em>пароль резервной копии</em> — сделайте его отличным от основного пароля, потому что именно пароль резервной копии в итоге вводится на компьютерах. В результате получается один файл <code>.vaultbak</code>, который вы сохраняете где угодно: на Диске, SD-карте, флешке.</p>",
            "<p>Файл не привязан к устройству: его собственная соль и параметры получения ключа хранятся в заголовке. Файл плюс пароль резервной копии восстанавливают всё на любом телефоне, даже после сброса до заводских настроек. Восстанавливайте через <strong>Настройки → Восстановить из резервной копии</strong> или с экрана приветствия при новой установке.</p>",
            "<p>Восстановление предлагает <em>добавить к существующим</em> или <em>заменить всё</em>. Оба варианта проверяются прежде, чем что-либо будет записано — неверный пароль не проходит проверку подлинности, и ничего не удаляется, пока новые данные не подтверждены.</p>",
        ]),
        ("transfer", "Перенос секретов с компьютера", [
            "<p>Ручной ввод длинного ключа на телефоне — это где случаются ошибки. Sekuvo переносит их как зашифрованный конверт, двумя способами: текстом, который вы вставляете, или QR-кодами, которые вы сканируете.</p>",
            "<p><strong>На телефоне:</strong> кнопка ➕ предлагает «Импорт через QR» и «Импорт из текста». Импорт через QR открывает камеру; кадры декодируются на устройстве, а многокадровые переносы показывают прогресс по мере сбора.</p>",
            "<h3>Инструмент на стороне компьютера</h3>",
            "<p>Инструмент, который строит эти конверты, — это один HTML-файл, и это намеренно <strong>скачиваемый файл, а не сайт</strong>. sekuvo.com никогда не спросит у вас секрет; страница, которая делала бы это, была бы неотличима от фишингового сайта.</p>",
            "<ol><li>Откройте проект на GitHub и перейдите в раздел <strong>Releases</strong>.</li><li>Скачайте <code>aktar.html</code> из последней версии.</li><li>Проверьте его SHA-256 по значению, опубликованному рядом: <code>shasum -a 256 aktar.html</code> на macOS или Linux, <code>certutil -hashfile aktar.html SHA256</code> на Windows.</li><li>Откройте файл двойным щелчком. Он работает с вашего диска — адресная строка показывает <code>file://</code>, а не сайт.</li><li>Вставьте свой текст, задайте пароль переноса, и он создаст конверт как текст или как QR-коды.</li><li>На телефоне отсканируйте или вставьте, введите тот же пароль и выберите добавить или заменить.</li></ol>",
            "<p>Всё шифрование происходит внутри вашего браузера, на вашей машине. Также есть <code>vault-clip.py</code> для командной строки, который делает то же самое из буфера обмена или файла и может рисовать QR-коды прямо в терминале.</p>",
            "<h3>Если вы предпочитаете не использовать инструмент</h3>",
            "<p>Конверт — открытый формат, а не что-то, что может создать только Sekuvo: PBKDF2-HMAC-SHA256 с 310 000 раундами, AES-256-GCM, обёрнутый в небольшой объект JSON. Вы можете собрать его сами примерно тридцатью строками, которые уже прочитали, и вставить результат в «Импорт из текста» — приложение не может определить, какой инструмент его создал, и ему это неважно.</p>",
            "<p>Рецепт находится в репозитории: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (написан на турецком языке).</p>",
        ]),
        ("log", "Журнал использования", [
            "<p>Sekuvo записывает, какое поле какой записи, куда и когда было отправлено: в буфер обмена, на компьютер по Bluetooth (с именем целевого устройства) или введено в приложение через клавиатуру. Когда компьютер скомпрометирован, это отвечает на вопрос «что туда попало, что нужно поменять».</p>",
            "<p>Журнал зашифрован тем же ключом, что и ваши записи, и <strong>значения в него никогда не записываются</strong> — только тип события, название поля и получатель. Удаление записи удаляет и её журнал, а очистить всё можно из Настроек.</p>",
        ]),
        ("generator", "Генератор паролей", [
            "<p>Доступен через значок 🎲 на главном экране или рядом с полем пароля при редактировании записи. Использует криптографический источник случайности, создаёт от 8 до 64 символов, позволяет выбирать классы символов, может убирать похожие друг на друга символы и показывает результирующую энтропию в битах.</p>",
        ]),
    ],
)

G["ur"] = dict(
    nav_label="رہنما",
    title="Sekuvo — رہنما",
    desc="Sekuvo کیسے استعمال کریں: پہلی بار چلانا، آٹو فل، کی بورڈ، بلوٹوتھ کے ذریعے کمپیوٹر میں ٹائپنگ، بیک اپس اور منتقلی۔",
    h1="رہنما",
    lede="Sekuvo جو کچھ کرتا ہے، اسی ترتیب میں جس میں آپ کو غالباً ضرورت پڑے گی۔ یہاں کسی چیز کے لیے اکاؤنٹ یا انٹرنیٹ کنکشن درکار نہیں۔",
    back="← sekuvo.com پر واپس",
    sections=[
        ("start", "پہلی بار چلانا", [
            "<p>پہلی بار کھولنے پر آپ ایک <strong>ماسٹر پاس ورڈ</strong> سیٹ کرتے ہیں۔ آپ کا محفوظ کردہ ہر راز اس سے حاصل کردہ کلید سے مرمز ہوتا ہے، اس لیے یہ واحد چیز ہے جسے Sekuvo آپ کے لیے بحال نہیں کر سکتا — اسے آگے بڑھنے سے پہلے کسی محفوظ جگہ لکھ لیں۔</p>",
            "<p>کیا آپ کے پاس کسی دوسرے فون کا بیک اپ ہے؟ ویلکم اسکرین پر <strong>«میرے پاس بیک اپ ہے — اسے بحال کریں»</strong> دبائیں۔ آپ پہلے اس ڈیوائس کے لیے ماسٹر پاس ورڈ سیٹ کریں گے، پھر فائل منتخب کرنے والا خود بخود کھلے گا اور آپ کے اندراجات واپس آ جائیں گے۔</p>",
            "<p>اگر آپ کے فون میں فنگر پرنٹ یا چہرے کا سینسر ہے، تو Sekuvo سیٹ اپ کے فوراً بعد اسے استعمال کرنے کی پیشکش کرتا ہے۔ یہ صرف سہولت کی ایک تہہ ہے: ماسٹر پاس ورڈ ہمیشہ کام کرتا ہے، اور یہی وہ چیز ہے جو فیکٹری ری سیٹ کے بعد بھی باقی رہتی ہے۔</p>",
        ]),
        ("entries", "آپ کیا محفوظ کر سکتے ہیں", [
            "<p>چار قسم کے اندراجات اس کا بیشتر حصہ ڈھانپتے ہیں جو لوگ ایک والٹ میں رکھتے ہیں:</p>",
            "<ul><li><strong>اکاؤنٹ / پاس ورڈ</strong> — صارف نام، پاس ورڈ، ویب سائٹ یا ایپ۔</li><li><strong>روزمرہ</strong> — نام، فون، ای میل، پتہ۔ وہ چیزیں جو فارمز ہر وقت مانگتے ہیں۔</li><li><strong>کارڈ</strong> — کارڈ نمبر، میعاد ختم، CVV، IBAN۔</li><li><strong>محفوظ نوٹ</strong> — آزاد متن، اسکرپٹس، کلیدوں، بازیابی کوڈز، اور کنفیگ فائلوں کے لیے ذیلی اقسام کے ساتھ۔</li></ul>",
            "<p>اکاؤنٹ اور روزمرہ اندراجات <strong>اپنی مرضی کی فیلڈز</strong> بھی قبول کرتے ہیں: کوئی بھی «نام + قدر» جوڑا جو آپ چاہیں۔ اپنی مرضی کی فیلڈز بالکل اسی طرح مرمز ہوتی ہیں جیسے بلٹ ان فیلڈز، اور ہر اس جگہ ظاہر ہوتی ہیں جہاں باقی فیلڈز ظاہر ہوتی ہیں۔</p>",
        ]),
        ("channels", "کلپ بورڈ کے بغیر راز استعمال کرنا", [
            "<p>کلپ بورڈ کو دوسری ایپس پڑھ سکتی ہیں، اور یہی وہ جگہ ہے جہاں راز چوری ہوتے ہیں۔ اسی لیے Sekuvo قدر کو براہ راست منزل تک پہنچانے کے تین طریقے پیش کرتا ہے۔ کاپی کرنا اب بھی ممکن ہے — کلپ بورڈ 45 سیکنڈ بعد خودکار طور پر صاف ہو جاتا ہے — لیکن نیچے دیے گئے تین چینلز ہی اس ایپ کے وجود کی وجہ ہیں۔</p>",
        ]),
        ("autofill", "آٹو فل (فون کے اندر)", [
            "<p>Sekuvo اینڈرائیڈ کی آٹو فل سروس کے طور پر کام کر سکتا ہے، اس لیے لاگ ان اور کارڈ فارمز آپ کے اندراجات براہ راست پیش کرتے ہیں۔</p>",
            "<p><strong>فعال کرنے کے لیے:</strong> Sekuvo → سیٹنگز → <em>آٹو فل فعال کریں</em> → سسٹم کی فہرست سے Sekuvo منتخب کریں۔ اس فہرست کا نام ڈیوائس کے مطابق مختلف ہوتا ہے: Samsung اور اینڈرائیڈ 14+ پر یہ <em>پاس ورڈز، پاس کیز اور آٹو فل ← پسندیدہ سروس</em> ہے، خالص اینڈرائیڈ پر <em>آٹو فل سروس</em>۔</p>",
            "<p>اس کے بعد، کسی بھی ایپ میں صارف نام، پاس ورڈ، یا کارڈ فیلڈ پر ٹچ کرنے سے آپ کے متعلقہ اندراجات کی بورڈ کے اوپر ظاہر ہوں گے۔ اگر والٹ مقفل ہے تو پہلے تالا کھولنے کا مرحلہ آتا ہے — مقفل ہونے تک سسٹم کو بالکل کچھ نہیں دیا جاتا۔</p>",
        ]),
        ("keyboard", "Sekuvo کی بورڈ (فون کے اندر)", [
            "<p>کی بورڈ ایڈ آن کسی بھی ایپ کے کسی بھی فیلڈ میں محفوظ کردہ قدریں بغیر کاپی کیے ٹائپ کرتا ہے۔</p>",
            "<p><strong>فعال کرنے کے لیے:</strong> Sekuvo → سیٹنگز → <em>کی بورڈ فعال کریں</em> → سسٹم کی فہرست میں اسے فعال کریں، پھر جب بھی ضرورت ہو کی بورڈ سوئچر سے «Sekuvo کی بورڈ» منتخب کریں۔</p>",
            "<p>حال ہی میں استعمال شدہ اندراجات اوپر رہتے ہیں اور 🔍 عنوانات، صارف ناموں اور پتوں میں تلاش کرتا ہے۔ والٹ مقفل ہونے پر، کی بورڈ صرف فوری رسائی کے لیے نشان زدہ اندراجات دکھاتا ہے — نیچے دیکھیں۔</p>",
        ]),
        ("bluetooth", "بلوٹوتھ کے ذریعے کمپیوٹر میں ٹائپ کرنا", [
            "<p>آپ کا فون بلوٹوتھ کی بورڈ کے طور پر کام کر سکتا ہے اور آپ کے کمپیوٹر کے کرسر پوزیشن میں راز ٹائپ کر سکتا ہے۔ کمپیوٹر پر کچھ بھی انسٹال نہیں ہوتا، یہ Windows، macOS اور Linux پر کام کرتا ہے، اور قدر کبھی کلپ بورڈ یا نیٹ ورک کو نہیں چھوتی۔ اینڈرائیڈ 9 یا نیا درکار ہے۔</p>",
            "<h3>مرحلہ وار</h3>",
            "<ol><li>Sekuvo میں اندراج کھولیں اور جس فیلڈ کو ٹائپ کرنا ہے اس کے پاس 💻 آئیکن دبائیں۔ <strong>اس اسکرین کو کھلا رکھیں</strong> — فون خود کو صرف اسی وقت کی بورڈ کے طور پر ظاہر کرتا ہے جب یہ کھلی ہو۔</li><li>کمپیوٹر پر، فون کو نیا بلوٹوتھ ڈیوائس شامل کریں: Windows پر <em>سیٹنگز ← بلوٹوتھ اور ڈیوائسز ← ڈیوائس شامل کریں ← بلوٹوتھ</em>، یا macOS پر <em>سسٹم سیٹنگز ← بلوٹوتھ</em>۔</li><li>دونوں طرف جوڑے کا کوڈ تصدیق کریں۔</li><li>فون پر واپس، اپنا کمپیوٹر فہرست سے منتخب کریں اور «منسلک» ظاہر ہونے کا انتظار کریں۔</li><li><strong>کمپیوٹر</strong> کا کی بورڈ لے آؤٹ منتخب کریں — فون کا نہیں۔ کمپیوٹر خود کی کوڈز کی تشریح کرتا ہے، اس لیے غلط لے آؤٹ @ \" ? جیسے حروف کو خاموشی سے کچھ اور بنا دیتا ہے۔</li><li>کمپیوٹر پر اس فیلڈ میں کلک کریں جہاں قدر جانی چاہیے۔</li><li>فون پر <strong>ٹائپ کریں</strong> دبائیں۔ تین سیکنڈ کی گنتی کے بعد — یہ آپ کو اس فیلڈ پر کلک کرنے کا وقت دینے کے لیے ہے — قدر ایک ایک حرف کر کے ٹائپ ہوتی ہے۔</li></ol>",
            "<h3>منسلک ہے لیکن کچھ ٹائپ نہیں ہو رہا</h3>",
            "<p>تقریباً ہمیشہ ایک ہی وجہ ہوتی ہے: کمپیوٹر نے پہلے کبھی آپ کے فون کو <em>ایک عام فون کے طور پر</em> جوڑا تھا، اس لیے اس کے لیے کبھی کی بورڈ سروس (HID) فعال نہیں کی۔ کنکشن کام کرتا ہے مگر کی اسٹروکس کہیں نہیں پہنچتیں۔</p>",
            "<ol><li>کمپیوٹر پر جوڑا ہٹائیں («ڈیوائس ہٹائیں»)۔</li><li>فون پر بھی ہٹائیں («بھول جائیں» بلوٹوتھ سیٹنگز میں)۔ دونوں طرف اہم ہیں۔</li><li>Sekuvo میں 💻 اسکرین کھولیں اور اسے کھلا رہنے دیں۔</li><li><strong>کمپیوٹر سے شروع کر کے</strong> دوبارہ جوڑیں۔</li><li>Windows پر تصدیق کے لیے: <em>Device Manager ← Human Interface Devices</em> میں اب ایک Bluetooth HID ڈیوائس نظر آنی چاہیے۔</li></ol>",
            "<p>macOS پر پہلا کنکشن <strong>Keyboard Setup Assistant</strong> کھول سکتا ہے، جو shift کے پاس والی کوئی کلید دبانے کو کہتا ہے۔ جب تک وہ ونڈو بند نہ ہو، macOS کچھ بھی پروسیس نہیں کرتا — Mac پر «منسلک لیکن خاموش» کی یہی عام وجہ ہے۔</p>",
            "<h3>رفتار اور اسے کیسے چیک کریں</h3>",
            "<p>کی اسٹروکس ایک ایک کر کے بھیجی جاتی ہیں، اس لیے ایک لمبے راز میں واقعی وقت لگتا ہے — ڈائیلاگ ایک اندازہ دکھاتا ہے۔ تین رفتاریں پیش کی جاتی ہیں، اور محفوظ رفتار کا ڈیفالٹ ہونا جان بوجھ کر ہے۔ رفتار بڑھانے سے پہلے <strong>⏱ اسپیڈ ٹیسٹ</strong> استعمال کریں: یہ خالی جگہوں سے الگ دس ایک جیسے بلاکس ٹائپ کرتا ہے اور ناپے گئے حروف فی سیکنڈ بتاتا ہے۔ اگر ایک بھی بلاک مختلف ہو، تو یہ رفتار اس کمپیوٹر پر محفوظ نہیں — ایک درجہ نیچے جائیں۔</p>",
            "<p>اسپیڈ ٹیسٹ تشخیص کے طور پر بھی کام کرتا ہے: کچھ ٹائپ نہ ہونا جوڑے کا مسئلہ ہے، حروف کا بگڑنا لے آؤٹ کا مسئلہ ہے، اور ٹائپنگ کا رک جانا رفتار کا مسئلہ ہے۔</p>",
            "<p>ٹائپنگ کے دوران آپ ایک پیش رفت بار اور <strong>روکیں</strong> بٹن دیکھتے ہیں۔ اگر بھیجنے کی قطار اٹک جائے، تو Sekuvo بڑھتے ہوئے وقفے کے ساتھ دوبارہ کوشش کرتا ہے، اور اگر پھر بھی ناکام ہو تو <em>رک جاتا ہے اور آپ کو بتاتا ہے</em> کہ کس حرف پر — کوئی راز خاموشی سے آدھا ٹائپ ہو کر نہیں رہتا۔</p>",
        ]),
        ("lock", "لاک کیسے کام کرتا ہے", [
            "<p>والٹ اس اسکرین کے بند ہوتے ہی مقفل ہو جاتا ہے جس پر یہ کھلا ہے — فولڈ ایبل فون بند کرنا بھی اس میں شامل ہے۔ اس لمحے کلید میموری سے مٹا دی جاتی ہے؛ اندراجات کے عنوانات فہرست میں نظر آتے رہ سکتے ہیں، لیکن کچھ بھی ڈی کرپٹ نہیں کیا جا سکتا۔</p>",
            "<p>اسکرین آن رہنے پر ایپ سے باہر نکلنا اسے <em>نہیں</em> مقفل کرتا۔ یہ جان بوجھ کر ہے: ایپ، کی بورڈ، اور آٹو فل ایک ہی سیشن شیئر کرتے ہیں، ورنہ پاس ورڈ پیسٹ کرنے کے لیے براؤزر پر سوئچ کرنا آپ کو کام کے بیچ میں باہر بند کر دیتا۔</p>",
        ]),
        ("quick", "فوری رسائی — ایک سوچی سمجھی مصالحت", [
            "<p>وہ اندراجات جنہیں آپ واضح طور پر «پاس ورڈ کے بغیر کی بورڈ میں استعمال کریں» کے طور پر نشان زد کرتے ہیں دوبارہ محفوظ کیے جاتے ہیں، ایک الگ ڈیوائس کلید سے مرمز، تاکہ کی بورڈ انہیں <em>والٹ مقفل ہونے پر بھی</em> پڑھ سکے۔</p>",
            "<p>یہ مصالحت واضح طور پر بیان کی گئی ہے: ایسے اندراجات کی حفاظت آپ کے فون کے اسکرین لاک سے ہوتی ہے، آپ کے ماسٹر پاس ورڈ سے نہیں۔ پاس ورڈز کو اس میں شامل نہ کریں۔ یہ نشان بائے ڈیفالٹ غیر فعال ہے؛ واحد استثنا نئے <strong>روزمرہ</strong> اندراجات ہیں، جو نشان زدہ شروع ہوتے ہیں کیونکہ نام اور فون نمبر بالکل وہی ہیں جو آپ ہاتھ کے قریب رکھنا چاہتے ہیں — آپ ان میں سے کسی کو بھی بند کر سکتے ہیں۔</p>",
        ]),
        ("backup", "بیک اپس اور بحالی", [
            "<p>سسٹم بیک اپ (Google بیک اپ، ڈیوائس منتقلی) جان بوجھ کر غیر فعال ہے، اس لیے آپ کے والٹ کے فون سے باہر نکلنے کا صرف ایک راستہ ہے، اور یہ وہی ہے جو آپ منتخب کرتے ہیں: <strong>سیٹنگز ← مرمز بیک اپ بنائیں</strong>۔</p>",
            "<p>آپ ایک <em>بیک اپ پاس ورڈ</em> منتخب کرتے ہیں — اسے اپنے ماسٹر پاس ورڈ سے مختلف رکھیں، کیونکہ بیک اپ پاس ورڈ ہی آخرکار کمپیوٹرز پر ٹائپ ہوتا ہے۔ نتیجے میں ایک ہی <code>.vaultbak</code> فائل ملتی ہے جسے آپ جہاں چاہیں محفوظ کرتے ہیں: Drive، SD کارڈ، یا USB ڈرائیو۔</p>",
            "<p>فائل ڈیوائس سے آزاد ہے: اس کا اپنا سالٹ اور کلید حاصل کرنے کے پیرامیٹرز اس کے ہیڈر میں رہتے ہیں۔ فائل اور بیک اپ پاس ورڈ مل کر فیکٹری ری سیٹ کے بعد بھی کسی بھی فون پر سب کچھ بحال کر دیتے ہیں۔ بحالی <strong>سیٹنگز ← بیک اپ سے بحال کریں</strong> سے کریں، یا نئی تنصیب پر ویلکم اسکرین سے۔</p>",
            "<p>بحالی <em>موجودہ میں شامل کریں</em> یا <em>سب کچھ تبدیل کریں</em> کی پیشکش کرتی ہے۔ کچھ بھی لکھے جانے سے پہلے دونوں کی تصدیق کی جاتی ہے — غلط پاس ورڈ تصدیق کے مرحلے پر ناکام ہو جاتا ہے، اور نئے ڈیٹا کی تصدیق ہونے تک کچھ حذف نہیں ہوتا۔</p>",
        ]),
        ("transfer", "کمپیوٹر سے راز لانا", [
            "<p>فون پر لمبی کلید ہاتھ سے ٹائپ کرنا وہ جگہ ہے جہاں غلطیاں ہوتی ہیں۔ Sekuvo انہیں ایک مرمز شدہ لفافے کے طور پر، دو طریقوں سے منتقل کرتا ہے: متن جو آپ پیسٹ کرتے ہیں، یا QR کوڈز جو آپ اسکین کرتے ہیں۔</p>",
            "<p><strong>فون پر:</strong> ➕ بٹن <em>QR کے ذریعے درآمد کریں</em> اور <em>متن سے درآمد کریں</em> پیش کرتا ہے۔ QR درآمد کیمرہ کھولتی ہے؛ فریمز ڈیوائس پر ڈی کوڈ ہوتے ہیں، اور کئی فریموں والی منتقلی جمع ہوتے ہوئے پیش رفت دکھاتی ہے۔</p>",
            "<h3>کمپیوٹر کی طرف کا ٹول</h3>",
            "<p>وہ ٹول جو یہ لفافے بناتا ہے ایک ہی HTML فائل ہے، اور یہ جان بوجھ کر <strong>ایک ڈاؤن لوڈ ہے، ویب سائٹ نہیں</strong>۔ sekuvo.com آپ سے کبھی راز نہیں مانگتا؛ ایسا کرنے والا صفحہ بالکل فشنگ سائٹ جیسا لگے گا۔</p>",
            "<ol><li>GitHub پر پروجیکٹ کھولیں اور <strong>Releases</strong> پر جائیں۔</li><li>تازہ ترین ورژن سے <code>aktar.html</code> ڈاؤن لوڈ کریں۔</li><li>اس کے پاس شائع شدہ قدر سے اس کا SHA-256 چیک کریں: macOS یا Linux پر <code>shasum -a 256 aktar.html</code>، Windows پر <code>certutil -hashfile aktar.html SHA256</code>۔</li><li>فائل پر ڈبل کلک کر کے کھولیں۔ یہ آپ کی ڈسک سے چلتا ہے — ایڈریس بار میں <code>file://</code> نظر آتا ہے، کوئی ویب سائٹ نہیں۔</li><li>اپنا متن پیسٹ کریں، ایک منتقلی پاس ورڈ سیٹ کریں، اور یہ لفافہ متن یا QR کوڈز کے طور پر بناتا ہے۔</li><li>فون پر، اسکین یا پیسٹ کریں، وہی پاس ورڈ درج کریں، اور شامل کرنے یا تبدیل کرنے کا انتخاب کریں۔</li></ol>",
            "<p>تمام خفیہ کاری آپ کے براؤزر کے اندر، آپ کی مشین پر ہوتی ہے۔ کمانڈ لائن کے لیے <code>vault-clip.py</code> بھی موجود ہے، جو کلپ بورڈ یا فائل سے وہی کام کرتا ہے اور ٹرمینل میں QR کوڈز بنا سکتا ہے۔</p>",
            "<h3>اگر آپ ٹول استعمال نہیں کرنا چاہتے</h3>",
            "<p>لفافہ ایک کھلا فارمیٹ ہے، ایسی چیز نہیں جسے صرف Sekuvo بنا سکتا ہے: PBKDF2-HMAC-SHA256 310,000 راؤنڈز کے ساتھ، AES-256-GCM، ایک چھوٹے JSON آبجیکٹ میں لپٹا ہوا۔ آپ اسے خود تقریباً تیس لائنوں میں بنا سکتے ہیں جو آپ پہلے ہی پڑھ چکے ہیں، اور نتیجہ <em>متن سے درآمد کریں</em> میں پیسٹ کر سکتے ہیں — ایپ کو معلوم نہیں ہو سکتا کہ اسے کس ٹول نے بنایا، اور اسے اس کی پرواہ بھی نہیں۔</p>",
            "<p>ترکیب ریپوزٹری میں ہے: <a href=\"https://github.com/afgover/Vault/blob/HEAD/docs/kendi-zarfini-uret.md\">docs/kendi-zarfini-uret.md</a> (ترکی زبان میں لکھی گئی)۔</p>",
        ]),
        ("log", "استعمال کا لاگ", [
            "<p>Sekuvo ریکارڈ کرتا ہے کہ کس اندراج کی کون سی فیلڈ، کہاں اور کب گئی: کلپ بورڈ میں، بلوٹوتھ کے ذریعے کمپیوٹر میں (منزل ڈیوائس کے نام کے ساتھ)، یا کی بورڈ کے ذریعے کسی ایپ میں ٹائپ کی گئی۔ جب کوئی کمپیوٹر خراب ہو جائے، تو یہ اس سوال کا جواب دیتا ہے «وہاں کیا گیا، مجھے کیا تبدیل کرنے کی ضرورت ہے»۔</p>",
            "<p>لاگ اسی کلید سے مرمز ہے جیسے آپ کے اندراجات، اور <strong>قدریں کبھی اس میں نہیں لکھی جاتیں</strong> — صرف واقعے کی قسم، فیلڈ کا نام، اور منزل۔ اندراج حذف کرنا اس کا لاگ بھی حذف کر دیتا ہے، اور آپ سیٹنگز سے سب کچھ صاف کر سکتے ہیں۔</p>",
        ]),
        ("generator", "پاس ورڈ جنریٹر", [
            "<p>ہوم اسکرین پر 🎲 آئیکن سے، یا کسی اندراج میں ترمیم کرتے وقت پاس ورڈ فیلڈ کے پاس سے قابل رسائی۔ یہ کرپٹوگرافک بے ترتیبی کا ذریعہ استعمال کرتا ہے، 8 سے 64 حروف پیدا کرتا ہے، حروف کی کلاسیں منتخب کرنے دیتا ہے، ملتے جلتے حروف ہٹا سکتا ہے، اور نتیجے میں ملنے والی اینٹروپی بٹس میں دکھاتا ہے۔</p>",
        ]),
    ],
)

SHOTS = {
    "start":     ["01-karsilama.png"],
    "entries":   ["02-liste.png", "10-ekleme-menusu.png", "03-uzun-anahtar.png"],
    "channels":  ["04-detay.png"],
    "autofill":  ["07-ayarlar.png"],
    "quick":     ["11-duzenleme.png"],
    "backup":    ["08-yedekleme.png"],
    "transfer":  ["06-aktarim.png"],
    "log":       ["09-gunluk.png"],
    "generator": ["05-uretici.png"],
}

CAPTIONS = {
    "en": {
        "01-karsilama.png": "The welcome screen: set a master password, or restore a backup you already have.",
        "02-liste.png": "The entry list, with search and type filters.",
        "10-ekleme-menusu.png": "Adding something: four entry types, plus the two import routes.",
        "04-detay.png": "An entry. The password stays masked; the icons beside each field copy it or type it into a computer.",
        "07-ayarlar.png": "Settings — where autofill and the keyboard are switched on.",
        "11-duzenleme.png": "Editing an entry. The quick-access switch sits at the bottom with its cost spelled out beside it.",
        "08-yedekleme.png": "Backup and restore live together in Settings.",
        "06-aktarim.png": "The wizard for bringing secrets over from a computer.",
        "03-uzun-anahtar.png": "A 386-character SSH key, kept whole. The fingerprint below it lets you check a value without reading it out.",
        "09-gunluk.png": "The usage log: what went where and when — never the value itself.",
        "05-uretici.png": "The generator, with the resulting entropy shown in bits.",
    },
    "tr": {
        "01-karsilama.png": "Karşılama ekranı: ana parolanı belirle ya da elindeki yedeği geri yükle.",
        "02-liste.png": "Kayıt listesi; arama ve tür süzgeçleriyle.",
        "10-ekleme-menusu.png": "Ekleme menüsü: dört kayıt türü ve iki içe aktarma yolu.",
        "04-detay.png": "Bir kayıt. Şifre maskeli kalır; her alanın yanındaki simgeler onu kopyalar ya da bilgisayara yazar.",
        "07-ayarlar.png": "Ayarlar — otomatik doldurma ve klavye buradan açılır.",
        "11-duzenleme.png": "Kayıt düzenleme. Hızlı erişim anahtarı altta, bedeli yanında yazılı.",
        "08-yedekleme.png": "Yedekleme ve geri yükleme Ayarlar'da yan yana durur.",
        "06-aktarim.png": "Bilgisayardan sır getirme sihirbazı.",
        "03-uzun-anahtar.png": "386 karakterlik bir SSH anahtarı, bölünmeden. Altındaki parmak izi, değeri okumadan doğrulamanı sağlar.",
        "09-gunluk.png": "Kullanım günlüğü: ne nereye, ne zaman gitti — değerin kendisi asla.",
        "05-uretici.png": "Şifre üretici; sonucun entropisi bit olarak görünür.",
    },
    "es": {
        "01-karsilama.png": "La pantalla de bienvenida: define una contraseña maestra o restaura una copia que ya tengas.",
        "02-liste.png": "La lista de entradas, con búsqueda y filtros por tipo.",
        "10-ekleme-menusu.png": "Al añadir: cuatro tipos de entrada y las dos vías de importación.",
        "04-detay.png": "Una entrada. La contraseña sigue oculta; los iconos junto a cada campo la copian o la escriben en un ordenador.",
        "07-ayarlar.png": "Ajustes — desde aquí se activan el autocompletado y el teclado.",
        "11-duzenleme.png": "Editando una entrada. El interruptor de acceso rápido está abajo, con su coste explicado al lado.",
        "08-yedekleme.png": "Copia y restauración conviven en Ajustes.",
        "06-aktarim.png": "El asistente para traer secretos desde un ordenador.",
        "03-uzun-anahtar.png": "Una clave SSH de 386 caracteres, entera. La huella bajo ella permite verificar un valor sin leerlo.",
        "09-gunluk.png": "El registro de uso: qué fue a dónde y cuándo — nunca el valor.",
        "05-uretici.png": "El generador, con la entropía resultante en bits.",
    },
    "hi": {
        "01-karsilama.png": "स्वागत स्क्रीन: मास्टर पासवर्ड तय करें, या पहले से मौजूद बैकअप पुनर्स्थापित करें।",
        "02-liste.png": "एंट्री सूची — खोज और प्रकार फ़िल्टर के साथ।",
        "10-ekleme-menusu.png": "कुछ जोड़ते समय: चार एंट्री प्रकार और दो आयात रास्ते।",
        "04-detay.png": "एक एंट्री। पासवर्ड ढका रहता है; हर फ़ील्ड के पास के आइकन उसे कॉपी करते हैं या कंप्यूटर में टाइप करते हैं।",
        "07-ayarlar.png": "सेटिंग्स — ऑटोफ़िल और कीबोर्ड यहीं से चालू होते हैं।",
        "11-duzenleme.png": "एंट्री संपादित करते हुए। त्वरित पहुँच का स्विच नीचे है, उसकी क़ीमत साथ में लिखी है।",
        "08-yedekleme.png": "बैकअप और पुनर्स्थापना सेटिंग्स में साथ-साथ रहते हैं।",
        "06-aktarim.png": "कंप्यूटर से राज़ लाने का सहायक।",
        "03-uzun-anahtar.png": "386 अक्षरों की SSH कुंजी, पूरी। नीचे दी फ़िंगरप्रिंट से मान को पढ़े बिना जाँचा जा सकता है।",
        "09-gunluk.png": "उपयोग लॉग: क्या कहाँ और कब गया — मान कभी नहीं।",
        "05-uretici.png": "पासवर्ड जनरेटर, परिणामी एन्ट्रॉपी बिट में।",
    },
    "ar": {
        "01-karsilama.png": "شاشة الترحيب: حدّد كلمة مرور رئيسية، أو استعد نسخة احتياطية لديك.",
        "02-liste.png": "قائمة المدخلات، مع البحث ومرشّحات الأنواع.",
        "10-ekleme-menusu.png": "عند الإضافة: أربعة أنواع من المدخلات، وطريقتا الاستيراد.",
        "04-detay.png": "مدخلة. تبقى كلمة المرور محجوبة؛ والأيقونات بجوار كل حقل تنسخه أو تكتبه في حاسوب.",
        "07-ayarlar.png": "الإعدادات — ومنها يُفعَّل الملء التلقائي ولوحة المفاتيح.",
        "11-duzenleme.png": "تحرير مدخلة. مفتاح الوصول السريع في الأسفل، وثمنه مكتوب بجانبه.",
        "08-yedekleme.png": "النسخ الاحتياطي والاستعادة معًا في الإعدادات.",
        "06-aktarim.png": "معالج جلب الأسرار من حاسوب.",
        "03-uzun-anahtar.png": "مفتاح SSH من 386 محرفًا، كاملًا. والبصمة تحته تتيح التحقق من القيمة دون قراءتها.",
        "09-gunluk.png": "سجل الاستخدام: ما الذي ذهب وإلى أين ومتى — لا القيمة نفسها أبدًا.",
        "05-uretici.png": "مولّد كلمات المرور، وتظهر الإنتروبيا الناتجة بالبتّات.",
    },
    "zh": {
        "01-karsilama.png": "欢迎界面：设置主密码，或恢复你已有的备份。",
        "02-liste.png": "条目列表，支持搜索和按类型筛选。",
        "10-ekleme-menusu.png": "添加内容：四种条目类型，以及两种导入方式。",
        "04-detay.png": "一个条目。密码保持遮盖状态；每个字段旁的图标可复制它或将其输入到电脑。",
        "07-ayarlar.png": "设置 — 在这里开启自动填充和键盘。",
        "11-duzenleme.png": "编辑一个条目。快速访问开关位于底部，其代价就写在旁边。",
        "08-yedekleme.png": "备份与恢复在设置中并列显示。",
        "06-aktarim.png": "从电脑带回密文的向导。",
        "03-uzun-anahtar.png": "一段 386 字符的 SSH 密钥，完整保存。下方的指纹可以在不读出该值的情况下核对它。",
        "09-gunluk.png": "使用记录：什么内容在何时去了哪里 — 但从不记录值本身。",
        "05-uretici.png": "密码生成器，以比特数显示生成结果的熵值。",
    },
    "fr": {
        "01-karsilama.png": "L'écran d'accueil : définis un mot de passe principal, ou restaure une sauvegarde que tu as déjà.",
        "02-liste.png": "La liste des entrées, avec recherche et filtres par type.",
        "10-ekleme-menusu.png": "Lors de l'ajout : quatre types d'entrées, plus les deux voies d'importation.",
        "04-detay.png": "Une entrée. Le mot de passe reste masqué ; les icônes à côté de chaque champ le copient ou le saisissent sur un ordinateur.",
        "07-ayarlar.png": "Paramètres — c'est ici que se règlent la saisie automatique et le clavier.",
        "11-duzenleme.png": "Modification d'une entrée. L'interrupteur d'accès rapide est en bas, avec son coût expliqué à côté.",
        "08-yedekleme.png": "Sauvegarde et restauration cohabitent dans les Paramètres.",
        "06-aktarim.png": "L'assistant pour ramener des secrets depuis un ordinateur.",
        "03-uzun-anahtar.png": "Une clé SSH de 386 caractères, entière. L'empreinte en dessous permet de vérifier une valeur sans la lire.",
        "09-gunluk.png": "Le journal d'utilisation : quoi est allé où et quand — jamais la valeur elle-même.",
        "05-uretici.png": "Le générateur, avec l'entropie résultante affichée en bits.",
    },
    "bn": {
        "01-karsilama.png": "স্বাগত স্ক্রিন: একটি মূল পাসওয়ার্ড সেট করুন, অথবা আপনার আগের একটি ব্যাকআপ পুনরুদ্ধার করুন।",
        "02-liste.png": "এন্ট্রি তালিকা, খোঁজা ও টাইপ অনুযায়ী ফিল্টারসহ।",
        "10-ekleme-menusu.png": "কিছু যোগ করার সময়: চার ধরনের এন্ট্রি, এবং দুটি ইম্পোর্ট পথ।",
        "04-detay.png": "একটি এন্ট্রি। পাসওয়ার্ড লুকানো থাকে; প্রতিটি ফিল্ডের পাশের আইকন সেটি কপি করে বা কম্পিউটারে টাইপ করে।",
        "07-ayarlar.png": "সেটিংস — এখান থেকেই অটোফিল ও কীবোর্ড চালু হয়।",
        "11-duzenleme.png": "একটি এন্ট্রি এডিট করা হচ্ছে। দ্রুত-অ্যাক্সেস সুইচটি নিচে, এর খরচ পাশেই লেখা আছে।",
        "08-yedekleme.png": "ব্যাকআপ ও পুনরুদ্ধার সেটিংসে পাশাপাশি থাকে।",
        "06-aktarim.png": "কম্পিউটার থেকে গোপন তথ্য আনার উইজার্ড।",
        "03-uzun-anahtar.png": "৩৮৬ অক্ষরের একটি SSH কী, সম্পূর্ণ। নিচের ফিঙ্গারপ্রিন্ট দিয়ে মানটি না পড়েই যাচাই করা যায়।",
        "09-gunluk.png": "ব্যবহারের লগ: কী কখন কোথায় গেছে — কিন্তু মানটি কখনো নয়।",
        "05-uretici.png": "জেনারেটর, ফলাফলের এনট্রপি বিট আকারে দেখানো হয়েছে।",
    },
    "pt": {
        "01-karsilama.png": "A tela de boas-vindas: defina uma senha principal, ou restaure um backup que você já tem.",
        "02-liste.png": "A lista de itens, com pesquisa e filtros por tipo.",
        "10-ekleme-menusu.png": "Ao adicionar: quatro tipos de item, mais os dois caminhos de importação.",
        "04-detay.png": "Um item. A senha permanece oculta; os ícones ao lado de cada campo a copiam ou a digitam em um computador.",
        "07-ayarlar.png": "Configurações — onde o preenchimento automático e o teclado são ativados.",
        "11-duzenleme.png": "Editando um item. O interruptor de acesso rápido fica embaixo, com seu custo explicado ao lado.",
        "08-yedekleme.png": "Backup e restauração convivem nas Configurações.",
        "06-aktarim.png": "O assistente para trazer segredos de um computador.",
        "03-uzun-anahtar.png": "Uma chave SSH de 386 caracteres, inteira. A impressão digital abaixo dela permite verificar um valor sem lê-lo.",
        "09-gunluk.png": "O registro de uso: o que foi para onde e quando — nunca o valor em si.",
        "05-uretici.png": "O gerador, com a entropia resultante mostrada em bits.",
    },
    "ru": {
        "01-karsilama.png": "Экран приветствия: задайте основной пароль или восстановите уже имеющуюся резервную копию.",
        "02-liste.png": "Список записей с поиском и фильтрами по типу.",
        "10-ekleme-menusu.png": "При добавлении: четыре типа записей плюс два пути импорта.",
        "04-detay.png": "Запись. Пароль остаётся скрытым; значки рядом с каждым полем копируют его или вводят на компьютере.",
        "07-ayarlar.png": "Настройки — здесь включаются автозаполнение и клавиатура.",
        "11-duzenleme.png": "Редактирование записи. Переключатель быстрого доступа внизу, его цена объяснена рядом.",
        "08-yedekleme.png": "Резервное копирование и восстановление живут рядом в Настройках.",
        "06-aktarim.png": "Мастер переноса секретов с компьютера.",
        "03-uzun-anahtar.png": "SSH-ключ из 386 символов, целиком. Отпечаток под ним позволяет проверить значение, не читая его.",
        "09-gunluk.png": "Журнал использования: что и куда ушло, когда — но никогда само значение.",
        "05-uretici.png": "Генератор, с результирующей энтропией в битах.",
    },
    "ur": {
        "01-karsilama.png": "ویلکم اسکرین: ماسٹر پاس ورڈ سیٹ کریں، یا اپنا موجودہ بیک اپ بحال کریں۔",
        "02-liste.png": "اندراجات کی فہرست، تلاش اور قسم کے فلٹرز کے ساتھ۔",
        "10-ekleme-menusu.png": "شامل کرتے وقت: چار قسم کے اندراجات، اور درآمد کے دو راستے۔",
        "04-detay.png": "ایک اندراج۔ پاس ورڈ چھپا رہتا ہے؛ ہر فیلڈ کے پاس آئیکنز اسے کاپی کرتے یا کمپیوٹر پر ٹائپ کرتے ہیں۔",
        "07-ayarlar.png": "سیٹنگز — یہیں سے آٹو فل اور کی بورڈ فعال ہوتے ہیں۔",
        "11-duzenleme.png": "اندراج میں ترمیم۔ فوری رسائی کا سوئچ نیچے ہے، اس کی قیمت ساتھ لکھی ہے۔",
        "08-yedekleme.png": "بیک اپ اور بحالی سیٹنگز میں ساتھ ساتھ رہتے ہیں۔",
        "06-aktarim.png": "کمپیوٹر سے راز لانے کا ویزرڈ۔",
        "03-uzun-anahtar.png": "386 حروف کی ایک SSH کلید، مکمل۔ نیچے دیا فنگر پرنٹ قدر کو پڑھے بغیر تصدیق کی اجازت دیتا ہے۔",
        "09-gunluk.png": "استعمال کا لاگ: کیا کہاں اور کب گیا — لیکن قدر خود کبھی نہیں۔",
        "05-uretici.png": "جنریٹر، نتیجے میں ملنے والی اینٹروپی بٹس میں دکھائی گئی۔",
    },
}

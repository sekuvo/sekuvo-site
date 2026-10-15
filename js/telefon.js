/*! Sekuvo telefon maketi — sekuvo.com · GPLv3
 *
 *  <sekuvo-telefon model="galaxy-s26" demo="tur" secici></sekuvo-telefon>
 *
 *  Gerçek ölçülü bir telefonun ekranında Sekuvo'nun kendisini çizer: renkler
 *  uygulamanın temasından (ui/theme/Theme.kt), metinler uygulamanın kendi
 *  çevirilerinden (telefon_metin.py → sayfaya gömülü JSON) gelir.
 *
 *  Ağ isteği yok, depolama yok. Ekranda görünen her parola, anahtar ve kart
 *  numarası bu sayfada, tarayıcının kriptografik rastgeleliğiyle üretilir;
 *  hiçbiri gerçek değildir ve hiçbir yere gitmez.
 *
 *  İkonlar: Material Icons (Apache-2.0) — @material-design-icons/svg 0.14.15,
 *  uygulamanın kullandığı Icons.Filled setinin aynısı.
 *
 *  Öznitelikler
 *    model   galaxy-s26 | iphone-18-pro | xiaomi-17
 *    tema    otomatik (varsayılan) | acik | koyu
 *    demo    tur | qr | (boş: yalnız etkileşim)
 *    olcek   gercek (varsayılan, 1:1 mm) | bir sayı (1 = gerçek boyut)
 *    secici  varsa altta model seçici çizilir
 *    veri    sayfadaki JSON'un id'si (varsayılan: telefon-veri)
 *
 *  <sekuvo-dizustu olcek="1"></sekuvo-dizustu> — aktar.html'in QR ekranını
 *  gösteren dizüstü; aynı JSON'dan aracın kendi metinlerini okur.
 */
(() => {
  "use strict";

  const IK = {
    add: "M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z",
    arrow_back: "M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z",
    badge: "M20 7h-5V4c0-1.1-.9-2-2-2h-2c-1.1 0-2 .9-2 2v3H4c-1.1 0-2 .9-2 2v11c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2zM9 12c.83 0 1.5.67 1.5 1.5S9.83 15 9 15s-1.5-.67-1.5-1.5S8.17 12 9 12zm3 6H6v-.75c0-1 2-1.5 3-1.5s3 .5 3 1.5V18zm1-9h-2V4h2v5zm5 7.5h-4V15h4v1.5zm0-3h-4V12h4v1.5z",
    battery_full: "M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z",
    bluetooth: "M17.71 7.71 12 2h-1v7.59L6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 11 14.41V22h1l5.71-5.71-4.3-4.29 4.3-4.29zM13 5.83l1.88 1.88L13 9.59V5.83zm1.88 10.46L13 18.17v-3.76l1.88 1.88z",
    casino: "M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM7.5 18c-.83 0-1.5-.67-1.5-1.5S6.67 15 7.5 15s1.5.67 1.5 1.5S8.33 18 7.5 18zm0-9C6.67 9 6 8.33 6 7.5S6.67 6 7.5 6 9 6.67 9 7.5 8.33 9 7.5 9zm4.5 4.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm4.5 4.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm0-9c-.83 0-1.5-.67-1.5-1.5S15.67 6 16.5 6s1.5.67 1.5 1.5S17.33 9 16.5 9z",
    check: "M9 16.17 4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z",
    close: "M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z",
    computer: "M20 18c1.1 0 1.99-.9 1.99-2L22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2H0v2h24v-2h-4zM4 6h16v10H4V6z",
    content_copy: "M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z",
    content_paste: "M19 2h-4.18C14.4.84 13.3 0 12 0c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm7 18H5V4h2v3h10V4h2v16z",
    credit_card: "M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z",
    data_object: "M4 7v2c0 .55-.45 1-1 1H2v4h1c.55 0 1 .45 1 1v2c0 1.65 1.35 3 3 3h3v-2H7c-.55 0-1-.45-1-1v-2c0-1.3-.84-2.42-2-2.83v-.34C5.16 11.42 6 10.3 6 9V7c0-.55.45-1 1-1h3V4H7C5.35 4 4 5.35 4 7zm17 3c-.55 0-1-.45-1-1V7c0-1.65-1.35-3-3-3h-3v2h3c.55 0 1 .45 1 1v2c0 1.3.84 2.42 2 2.83v.34c-1.16.41-2 1.52-2 2.83v2c0 .55-.45 1-1 1h-3v2h3c1.65 0 3-1.35 3-3v-2c0-.55.45-1 1-1h1v-4h-1z",
    download: "M5 20h14v-2H5v2zM19 9h-4V3H9v6H5l7 7 7-7z",
    edit: "M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a.996.996 0 0 0 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z",
    email: "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z",
    fingerprint: "M17.81 4.47c-.08 0-.16-.02-.23-.06C15.66 3.42 14 3 12.01 3c-1.98 0-3.86.47-5.57 1.41-.24.13-.54.04-.68-.2a.506.506 0 0 1 .2-.68C7.82 2.52 9.86 2 12.01 2c2.13 0 3.99.47 6.03 1.52.25.13.34.43.21.67a.49.49 0 0 1-.44.28zM3.5 9.72a.499.499 0 0 1-.41-.79c.99-1.4 2.25-2.5 3.75-3.27C9.98 4.04 14 4.03 17.15 5.65c1.5.77 2.76 1.86 3.75 3.25a.5.5 0 0 1-.12.7c-.23.16-.54.11-.7-.12a9.388 9.388 0 0 0-3.39-2.94c-2.87-1.47-6.54-1.47-9.4.01-1.36.7-2.5 1.7-3.4 2.96-.08.14-.23.21-.39.21zm6.25 12.07a.47.47 0 0 1-.35-.15c-.87-.87-1.34-1.43-2.01-2.64-.69-1.23-1.05-2.73-1.05-4.34 0-2.97 2.54-5.39 5.66-5.39s5.66 2.42 5.66 5.39c0 .28-.22.5-.5.5s-.5-.22-.5-.5c0-2.42-2.09-4.39-4.66-4.39-2.57 0-4.66 1.97-4.66 4.39 0 1.44.32 2.77.93 3.85.64 1.15 1.08 1.64 1.85 2.42.19.2.19.51 0 .71-.11.1-.24.15-.37.15zm7.17-1.85c-1.19 0-2.24-.3-3.1-.89-1.49-1.01-2.38-2.65-2.38-4.39 0-.28.22-.5.5-.5s.5.22.5.5c0 1.41.72 2.74 1.94 3.56.71.48 1.54.71 2.54.71.24 0 .64-.03 1.04-.1.27-.05.53.13.58.41.05.27-.13.53-.41.58-.57.11-1.07.12-1.21.12zM14.91 22c-.04 0-.09-.01-.13-.02-1.59-.44-2.63-1.03-3.72-2.1a7.297 7.297 0 0 1-2.17-5.22c0-1.62 1.38-2.94 3.08-2.94 1.7 0 3.08 1.32 3.08 2.94 0 1.07.93 1.94 2.08 1.94s2.08-.87 2.08-1.94c0-3.77-3.25-6.83-7.25-6.83-2.84 0-5.44 1.58-6.61 4.03-.39.81-.59 1.76-.59 2.8 0 .78.07 2.01.67 3.61.1.26-.03.55-.29.64-.26.1-.55-.04-.64-.29a11.14 11.14 0 0 1-.73-3.96c0-1.2.23-2.29.68-3.24 1.33-2.79 4.28-4.6 7.51-4.6 4.55 0 8.25 3.51 8.25 7.83 0 1.62-1.38 2.94-3.08 2.94s-3.08-1.32-3.08-2.94c0-1.07-.93-1.94-2.08-1.94s-2.08.87-2.08 1.94c0 1.71.66 3.31 1.87 4.51.95.94 1.86 1.46 3.27 1.85.27.07.42.35.35.61-.05.23-.26.38-.47.38z",
    health_and_safety: "M10.5 13H8v-3h2.5V7.5h3V10H16v3h-2.5v2.5h-3V13zM12 2 4 5v6.09c0 5.05 3.41 9.76 8 10.91 4.59-1.15 8-5.86 8-10.91V5l-8-3z",
    key: "M21 10h-8.35A5.99 5.99 0 0 0 7 6c-3.31 0-6 2.69-6 6s2.69 6 6 6a5.99 5.99 0 0 0 5.65-4H13l2 2 2-2 2 2 4-4.04L21 10zM7 15c-1.65 0-3-1.35-3-3s1.35-3 3-3 3 1.35 3 3-1.35 3-3 3z",
    keyboard_arrow_down: "M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z",
    language: "M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95a15.65 15.65 0 0 0-1.38-3.56A8.03 8.03 0 0 1 18.92 8zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56A7.987 7.987 0 0 1 5.08 16zm2.95-8H5.08a7.987 7.987 0 0 1 4.33-3.56A15.65 15.65 0 0 0 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2 0-.68.07-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z",
    laptop_mac: "M20 18c1.1 0 1.99-.9 1.99-2L22 5c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v11c0 1.1.9 2 2 2H0c0 1.1.9 2 2 2h20c1.1 0 2-.9 2-2h-4zM4 5h16v11H4V5zm8 14c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z",
    lock: "M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z",
    lock_open: "M12 17c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm6-9h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6h1.9c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm0 12H6V10h12v10z",
    note: "m22 10-6-6H4c-1.1 0-2 .9-2 2v12.01c0 1.1.9 1.99 2 1.99l16-.01c1.1 0 2-.89 2-1.99v-8zm-7-4.5 5.5 5.5H15V5.5z",
    notes: "M3 18h12v-2H3v2zM3 6v2h18V6H3zm0 7h18v-2H3v2z",
    numbers: "m20.5 10 .5-2h-4l1-4h-2l-1 4h-4l1-4h-2L9 8H5l-.5 2h4l-1 4h-4L3 16h4l-1 4h2l1-4h4l-1 4h2l1-4h4l.5-2h-4l1-4h4zm-7 4h-4l1-4h4l-1 4z",
    phone: "M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z",
    qr_code: "M3 11h8V3H3v8zm2-6h4v4H5V5zM3 21h8v-8H3v8zm2-6h4v4H5v-4zm8-12v8h8V3h-8zm6 6h-4V5h4v4zm0 10h2v2h-2zm-6-6h2v2h-2zm2 2h2v2h-2zm-2 2h2v2h-2zm2 2h2v2h-2zm2-2h2v2h-2zm0-4h2v2h-2zm2 2h2v2h-2z",
    qr_code_scanner: "M9.5 6.5v3h-3v-3h3M11 5H5v6h6V5zm-1.5 9.5v3h-3v-3h3M11 13H5v6h6v-6zm6.5-6.5v3h-3v-3h3M19 5h-6v6h6V5zm-6 8h1.5v1.5H13V13zm1.5 1.5H16V16h-1.5v-1.5zM16 13h1.5v1.5H16V13zm-3 3h1.5v1.5H13V16zm1.5 1.5H16V19h-1.5v-1.5zM16 16h1.5v1.5H16V16zm1.5-1.5H19V16h-1.5v-1.5zm0 3H19V19h-1.5v-1.5zM22 7h-2V4h-3V2h5v5zm0 15v-5h-2v3h-3v2h5zM2 22h5v-2H4v-3H2v5zM2 2v5h2V4h3V2H2z",
    refresh: "M17.65 6.35A7.958 7.958 0 0 0 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08A5.99 5.99 0 0 1 12 18c-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z",
    search: "M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z",
    sell: "m21.41 11.41-8.83-8.83c-.37-.37-.88-.58-1.41-.58H4c-1.1 0-2 .9-2 2v7.17c0 .53.21 1.04.59 1.41l8.83 8.83c.78.78 2.05.78 2.83 0l7.17-7.17c.78-.78.78-2.04-.01-2.83zM6.5 8C5.67 8 5 7.33 5 6.5S5.67 5 6.5 5 8 5.67 8 6.5 7.33 8 6.5 8z",
    settings: "M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 0 0 .12-.61l-1.92-3.32a.488.488 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54a.484.484 0 0 0-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 0 0-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z",
    shield: "M12 1 3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z",
    signal_cellular_alt: "M17 4h3v16h-3zM5 14h3v6H5zm6-5h3v11h-3z",
    sort: "M3 18h6v-2H3v2zM3 6v2h18V6H3zm0 7h12v-2H3v2z",
    star: "M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z",
    star_border: "m22 9.24-7.19-.62L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21 12 17.27 18.18 21l-1.63-7.03L22 9.24zM12 15.4l-3.76 2.27 1-4.28-3.32-2.88 4.38-.38L12 6.1l1.71 4.04 4.38.38-3.32 2.88 1 4.28L12 15.4z",
    swap_horiz: "M6.99 11 3 15l3.99 4v-3H14v-2H6.99v-3zM21 9l-3.99-4v3H10v2h7.01v3L21 9z",
    terminal: "M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16c1.1 0 2-.9 2-2V6a2 2 0 0 0-2-2zm0 14H4V8h16v10zm-2-1h-6v-2h6v2zM7.5 17l-1.41-1.41L8.67 13l-2.59-2.59L7.5 9l4 4-4 4z",
    text_fields: "M2.5 4v3h5v12h3V7h5V4h-13zm19 5h-9v3h3v7h3v-7h3V9z",
    verified: "m23 12-2.44-2.79.34-3.69-3.61-.82-1.89-3.2L12 2.96 8.6 1.5 6.71 4.69 3.1 5.5l.34 3.7L1 12l2.44 2.79-.34 3.7 3.61.82L8.6 22.5l3.4-1.47 3.4 1.46 1.89-3.19 3.61-.82-.34-3.69L23 12zm-12.91 4.72-3.8-3.81 1.48-1.48 2.32 2.33 5.85-5.87 1.48 1.48-7.33 7.35z",
    visibility: "M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z",
    visibility_off: "M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46A11.804 11.804 0 0 0 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78 3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z",
    vpn_key: "M12.65 10A5.99 5.99 0 0 0 7 6c-3.31 0-6 2.69-6 6s2.69 6 6 6a5.99 5.99 0 0 0 5.65-4H17v4h4v-4h2v-4H12.65zM7 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z",
    wifi: "m1 9 2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8 3 3 3-3a4.237 4.237 0 0 0-6 0zm-4-4 2 2a7.074 7.074 0 0 1 10 0l2-2C15.14 9.14 8.87 9.14 5 13z",
  };

  const ikon = (ad, sinif = "") =>
    `<svg class="ik ${sinif}" viewBox="0 0 24 24" aria-hidden="true"><path d="${IK[ad] || ""}"/></svg>`;

  // ── Cihazlar ─────────────────────────────────────────────────────────────
  // Gövde ölçüleri üreticinin teknik sayfalarından (mm). Ekranın fiziksel
  // boyutu köşegen + piksel oranından hesaplanır; dp genişliği cihazın
  // varsayılan ekran yoğunluğundan gelir. Arayüz dp cinsinden kurulur ve
  // ekrana ölçeklenir — yani uygulama o telefonda nasıl görünüyorsa öyle.
  const MODELLER = {
    "galaxy-s26": {
      ad: "Samsung Galaxy S26", kisa: "Galaxy S26", sistem: "android",
      govde: [71.7, 149.6], kosegen: 6.3, piksel: [1080, 2340], dpGen: 412,
      kose: 9.4, cerceve: 0.95, kesik: { tur: "delik", cap: 3.1, ust: 3.6 },
      renk: ["#3b4150", "#262a33", "#59606f"],
      dugme: [["sag", 33, 21], ["sag", 60, 12]],
    },
    "iphone-18-pro": {
      ad: "iPhone 18 Pro", kisa: "iPhone 18 Pro", sistem: "ios",
      govde: [71.9, 150.0], kosegen: 6.3, piksel: [1206, 2622], dpGen: 402,
      kose: 11.2, cerceve: 1.05, kesik: { tur: "ada", en: 20.4, boy: 6.0, ust: 1.85 },
      renk: ["#d9d8d4", "#a9a8a4", "#f3f2ef"],
      dugme: [["sol", 26, 6.5], ["sol", 38, 10], ["sol", 51, 10], ["sag", 38, 16], ["sag", 92, 13, "ince"]],
    },
    "xiaomi-17": {
      ad: "Xiaomi 17", kisa: "Xiaomi 17", sistem: "android",
      govde: [71.8, 151.1], kosegen: 6.3, piksel: [1220, 2656], dpGen: 410,
      kose: 10.2, cerceve: 0.9, kesik: { tur: "delik", cap: 3.0, ust: 3.4 },
      renk: ["#20242b", "#121418", "#3a404a"],
      dugme: [["sag", 30, 20], ["sag", 56, 11]],
    },
  };
  const MODEL_SIRASI = ["galaxy-s26", "iphone-18-pro", "xiaomi-17"];
  const PX_MM = 96 / 25.4;

  function ekranOlcusu(m) {
    // Köşegen dikdörtgenin köşegenidir (üreticilerin ölçtüğü gibi).
    const oran = m.piksel[1] / m.piksel[0];
    const kosegenMm = m.kosegen * 25.4;
    const en = kosegenMm / Math.sqrt(1 + oran * oran);
    return { en, boy: en * oran, dpBoy: Math.round(m.dpGen * oran) };
  }

  // ── Tema (Theme.kt'den birebir) ──────────────────────────────────────────
  const TEMA = {
    acik: {
      primary: "#856520", onPrimary: "#ffffff", pc: "#D9B45F", onPc: "#241A00",
      secondary: "#6A5C43", sc: "#F2E3C6", onSc: "#241A07", tertiary: "#3F5A47",
      bg: "#ffffff", onBg: "#221D13", surface: "#ffffff", onSurface: "#221D13",
      sv: "#EBE2D2", onSv: "#4E4639", scont: "#ffffff", scHigh: "#ffffff", scHighest: "#F5EFE4",
      outline: "#7F7767", outlineV: "#D1C7B4", invS: "#33302A", invOnS: "#F6EFE3",
      error: "#BA1A1A", gunduz: "1",
    },
    koyu: {
      primary: "#F0C87A", onPrimary: "#3F2E00", pc: "#6B5210", onPc: "#FFE7B0",
      secondary: "#D5C4A4", sc: "#4F452E", onSc: "#F2E0BF", tertiary: "#B2CFB6",
      bg: "#211D18", onBg: "#EDE3D3", surface: "#302A23", onSurface: "#EDE3D3",
      sv: "#4E463A", onSv: "#D3C7B2", scont: "#332D26", scHigh: "#3B342C", scHighest: "#463E35",
      outline: "#9B9282", outlineV: "#4E463A", invS: "#EDE3D3", invOnS: "#332E27",
      error: "#FFB4AB", gunduz: "0",
    },
  };

  // ── Rastgelelik: her değer bu sayfada üretilir ───────────────────────────
  const rast = (n) => {
    const a = new Uint32Array(1);
    crypto.getRandomValues(a);
    return a[0] % n;
  };
  const sec = (dz) => dz[rast(dz.length)];
  const dizi = (alfabe, n) => Array.from({ length: n }, () => sec(alfabe)).join("");
  const KUCUK = "abcdefghijkmnopqrstuvwxyz", BUYUK = "ABCDEFGHJKLMNPQRSTUVWXYZ";
  const RAKAM = "0123456789", SEMBOL = "!#$%&*+-=?@^_";
  const ALNUM = KUCUK + BUYUK + "23456789";
  const B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  const HEX = "0123456789abcdef";

  function parola(n) {
    const tum = KUCUK + BUYUK + "23456789" + SEMBOL;
    for (;;) {
      const p = dizi(tum, n);
      if (/[a-z]/.test(p) && /[A-Z]/.test(p) && /\d/.test(p) && /[^A-Za-z0-9]/.test(p)) return p;
    }
  }
  function luhn(onEk, uzunluk) {
    const govde = onEk + dizi(RAKAM, uzunluk - onEk.length - 1);
    let t = 0;
    for (let i = 0; i < govde.length; i++) {
      let d = +govde[govde.length - 1 - i];
      if (i % 2 === 0) { d *= 2; if (d > 9) d -= 9; }
      t += d;
    }
    return govde + ((10 - (t % 10)) % 10);
  }
  const satirla = (s, n) => s.match(new RegExp(`.{1,${n}}`, "g")).join("\n");

  // Ad → e-posta yerel kısmı (example.com: RFC 2606, gerçek kimseye ait değil).
  const yerel = (ad) => ad.toLocaleLowerCase("tr")
    .replace(/ı/g, "i").replace(/ş/g, "s").replace(/ç/g, "c").replace(/ğ/g, "g")
    .replace(/ü/g, "u").replace(/ö/g, "o").normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z]+/g, ".");

  // ── Biçim yardımcıları ───────────────────────────────────────────────────
  const kac = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  function bicim(s, ...a) {
    let sira = 0;
    return String(s).replace(/%(?:(\d)\$)?([sd])/g, (_, n, tur) => {
      const v = n ? a[+n - 1] : a[sira++];
      return tur === "d" && typeof v === "number" ? v.toLocaleString(bicim.dil) : v;
    });
  }
  const kalin = (s) => kac(s).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/\n/g, "<br>");
  const kartGrupla = (n) => n.replace(/(\d{4})(?=\d)/g, "$1 ");

  // QR görünümlü desen: bulucu kareler, zamanlama çizgileri, hizalama karesi
  // ve rastgele modüller. Yalnız görüntü — çözülecek bir veri taşımaz.
  function qrDesen(c, n) {
    c.width = n; c.height = n;
    const x = c.getContext("2d");
    x.fillStyle = "#fff"; x.fillRect(0, 0, n, n);
    x.fillStyle = "#111";
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) if (rast(2)) x.fillRect(i, j, 1, 1);
    const kare = (ox, oy, d) => {
      x.fillStyle = "#fff"; x.fillRect(ox - 1, oy - 1, d + 2, d + 2);
      x.fillStyle = "#111"; x.fillRect(ox, oy, d, d);
      x.fillStyle = "#fff"; x.fillRect(ox + 1, oy + 1, d - 2, d - 2);
      x.fillStyle = "#111"; x.fillRect(ox + 2, oy + 2, d - 4, d - 4);
    };
    kare(0, 0, 7); kare(n - 7, 0, 7); kare(0, n - 7, 7);
    if (n >= 25) {
      x.fillStyle = "#111"; x.fillRect(n - 9, n - 9, 5, 5);
      x.fillStyle = "#fff"; x.fillRect(n - 8, n - 8, 3, 3);
      x.fillStyle = "#111"; x.fillRect(n - 7, n - 7, 1, 1);
    }
    for (let i = 8; i < n - 8; i++) { x.fillStyle = i % 2 ? "#fff" : "#111"; x.fillRect(i, 6, 1, 1); x.fillRect(6, i, 1, 1); }
  }

  // ── Kasa: demo kayıtları ─────────────────────────────────────────────────
  function kasaUret(d) {
    const ad = sec(d.adlar);
    const eposta = (ek) => `${yerel(ad)}${ek || ""}@example.com`;
    const simdi = Date.now(), gun = 864e5;
    const tarih = (enCok) => simdi - (1 + rast(enCok)) * gun - rast(gun);
    const ay = 1 + rast(12), yil = (new Date().getFullYear() % 100) + 1 + rast(4);
    const skt = `${String(ay).padStart(2, "0")}${yil}`;
    const sshGovde = "b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW" +
      "QyNTUxOQAAACA" + dizi(B64, 250);
    const ssh = "-----BEGIN OPENSSH PRIVATE KEY-----\n" + satirla(sshGovde, 70) +
      "\n-----END OPENSSH PRIVATE KEY-----";
    const env = [
      `# prod · ${new Date(simdi - 9 * gun).toISOString().slice(0, 10)}`,
      `DATABASE_URL=postgres://app:${dizi(ALNUM, 16)}@db.internal:5432/app`,
      `STRIPE_SECRET_KEY=sk_test_${dizi(ALNUM, 24)}`,
      `OPENAI_API_KEY=sk-proj-${dizi(ALNUM + "_-", 40)}`,
      `GITHUB_TOKEN=ghp_${dizi(ALNUM, 36)}`,
      `SENTRY_DSN=https://${dizi(HEX, 32)}@o${dizi(RAKAM, 6)}.ingest.example.io/${dizi(RAKAM, 7)}`,
    ].join("\n");
    const kodlar = Array.from({ length: 10 }, () => `${dizi(RAKAM, 4)} ${dizi(RAKAM, 4)}`).join("\n");
    const E = (id, tur, baslik, alanlar, ek = {}) => {
      const eklendi = tarih(420);
      return { id, tur, baslik, alanlar, etiket: [], hizli: false, oncelik: 0,
        eklendi, guncellendi: Math.min(simdi - gun / 3, eklendi + rast(300) * gun), ...ek };
    };
    // alan: [anahtar | {ozel: ad, tur}, değer]
    return [
      E("aws", "LOGIN", d.baslik_aws, [
        ["username", "ci-deploy"],
        ["url", "console.aws.amazon.com"],
        [{ ozel: d.alan_erisim, tur: "TEXT" }, "AKIA" + dizi("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567", 16)],
        [{ ozel: d.alan_gizli, tur: "PASSWORD" }, dizi(ALNUM + "/+", 40)],
      ], { etiket: ["is"] }),
      E("banka", "LOGIN", d.baslik_banka, [
        ["username", dizi(RAKAM, 8)],
        ["password", dizi(RAKAM, 6)],
        ["url", d.banka_uygulama],
      ], { etiket: ["finans"], oncelik: 1 }),
      E("deploy", "NOTE", d.baslik_deploy, [
        [{ ozel: d.alan_parmak, tur: "TEXT" }, "SHA256:" + dizi(B64.slice(0, 62), 43)],
        ["notes", ssh],
      ], { tur2: "ANAHTAR", etiket: ["is"] }),
      E("wifi", "LOGIN", d.baslik_wifi, [
        ["password", parola(16)],
        [{ ozel: d.alan_ssid, tur: "TEXT" }, d.ssid],
      ], { etiket: ["kisisel"], hizli: true }),
      E("github", "LOGIN", "GitHub", [
        ["username", eposta(".dev")],
        ["password", parola(20)],
        ["url", "github.com"],
      ], { etiket: ["is"] }),
      E("google", "LOGIN", d.baslik_google, [
        ["username", eposta()],
        ["password", parola(18)],
        ["url", "accounts.google.com"],
      ], { etiket: ["kisisel"] }),
      E("kimlik", "EVERYDAY", d.baslik_kimlik, [
        ["fullName", ad],
        ["email", eposta()],
        ["address", bicim(d.adres, 2 + rast(40))],
      ], { etiket: ["kisisel"] }),
      E("mc", "CARD", d.baslik_mc, [
        ["cardholder", ad.toLocaleUpperCase(d.dil)],
        ["cardNumber", luhn("555555", 16)],
        ["expiry", skt],
        ["cvv", dizi(RAKAM, 3)],
      ], { etiket: ["finans"] }),
      E("netflix", "LOGIN", "Netflix", [
        ["username", eposta()],
        ["password", parola(14)],
        ["url", "netflix.com"],
      ], { etiket: ["kisisel"], hizli: true }),
      E("env", "NOTE", d.baslik_env, [["notes", env]], { tur2: "YAPILANDIRMA", etiket: ["is"] }),
      E("visa", "CARD", d.baslik_visa, [
        ["cardholder", ad.toLocaleUpperCase(d.dil)],
        ["cardNumber", luhn("424242", 16)],
        ["expiry", `${String(1 + rast(12)).padStart(2, "0")}${yil + 1}`],
        ["cvv", dizi(RAKAM, 3)],
      ], { etiket: ["finans"], hizli: true }),
      E("kodlar", "NOTE", d.baslik_kodlar, [["notes", kodlar]], { tur2: "KURTARMA", etiket: ["kisisel"] }),
    ];
  }

  function yeniKayit(d) {
    const ssh = "-----BEGIN OPENSSH PRIVATE KEY-----\n" + satirla(
      "b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW" +
      "QyNTUxOQAAACA" + dizi(B64, 250), 70) + "\n-----END OPENSSH PRIVATE KEY-----";
    const simdi = Date.now();
    return { id: "yeni", tur: "NOTE", tur2: "ANAHTAR", baslik: d.yeni_baslik,
      alanlar: [["notes", ssh]], etiket: ["is"], hizli: false, oncelik: 0,
      eklendi: simdi, guncellendi: simdi, yeni: true };
  }

  const ETIKET_RENK = { finans: "#FFB74D", kisisel: "#81C784", is: "#4FC3F7" };

  // Alan anahtarı → uygulamadaki metin anahtarı
  const ALAN_METNI = {
    fullName: "field_full_name", username: "field_username", password: "field_password",
    url: "field_url", phone: "field_phone", email: "field_email", address: "field_address",
    cardholder: "field_cardholder", cardNumber: "field_card_number", expiry: "field_expiry",
    cvv: "field_cvv", iban: "field_iban", notes: "field_notes",
  };
  const GIZLI = new Set(["password", "cvv"]);
  const OZEL_IKON = { TEXT: "text_fields", PASSWORD: "key", EMAIL: "email", PHONE: "phone",
    URL: "language", NUMBER: "numbers", MULTILINE: "notes" };
  const TUR_IKON = { LOGIN: "key", EVERYDAY: "badge", CARD: "credit_card", NOTE: "note" };
  const NOT_IKON = { GENEL: "note", BETIK: "terminal", ANAHTAR: "vpn_key", PARMAK_IZI: "fingerprint",
    KURTARMA: "health_and_safety", YAPILANDIRMA: "data_object" };
  const TUR_METNI = { LOGIN: "type_login", EVERYDAY: "type_everyday", CARD: "type_card", NOTE: "type_note" };

  // ── Biçemler ─────────────────────────────────────────────────────────────
  const CSS = `
:host { display: inline-block; vertical-align: top; -webkit-tap-highlight-color: transparent; }
*, *::before, *::after { box-sizing: border-box; }
.sarmal { display: flex; flex-direction: column; align-items: center; gap: 16px; }
.cihaz { position: relative; flex: none; }
.govde { position: absolute; inset: 0; border-radius: var(--kose); background: var(--r1);
  background-image: linear-gradient(135deg, var(--r3) 0%, var(--r1) 18%, var(--r2) 50%, var(--r1) 82%, var(--r3) 100%);
  box-shadow: 0 1px 0 rgba(255,255,255,.18) inset, 0 -1px 0 rgba(0,0,0,.35) inset,
    0 40px 80px -30px rgba(0,0,0,.6), 0 18px 36px -18px rgba(0,0,0,.5); }
.cam { position: absolute; inset: var(--cerceve); border-radius: calc(var(--kose) - var(--cerceve)); background: #050505;
  box-shadow: 0 0 0 1px rgba(0,0,0,.6) inset; }
.ekran { position: absolute; overflow: hidden; border-radius: var(--ekose); background: var(--bg); isolation: isolate; }
.ekran::after { content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 30; border-radius: inherit;
  background: linear-gradient(118deg, rgba(255,255,255,.10) 0%, rgba(255,255,255,.03) 28%, rgba(255,255,255,0) 42%); }
.kesik { position: absolute; z-index: 25; background: #000; left: 50%; transform: translateX(-50%); }
.kesik.delik { border-radius: 50%; box-shadow: 0 0 0 1.5px rgba(30,30,30,.9) inset; }
.kesik.delik::after { content: ""; position: absolute; inset: 28%; border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #2c3346 0%, #0b0d12 60%); }
.kesik.ada { border-radius: 999px; }
.dugme { position: absolute; width: calc(var(--mm) * .75); border-radius: 2px; background: var(--r2);
  background-image: linear-gradient(90deg, var(--r2), var(--r3), var(--r2)); }
.dugme.sol { right: 100%; margin-right: -1px; border-radius: 2px 0 0 2px; }
.dugme.sag { left: 100%; margin-left: -1px; border-radius: 0 2px 2px 0; }
.dugme.ince { width: calc(var(--mm) * .35); opacity: .8; }

/* uygulama: 1px = 1dp */
.uyg { position: absolute; top: 0; left: 0; transform-origin: 0 0; overflow: hidden; background: var(--bg); color: var(--onBg);
  font-family: Roboto, "Roboto Flex", system-ui, -apple-system, "Segoe UI", sans-serif; font-size: 14px; line-height: 20px;
  -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; user-select: none; }
.mono { font-family: "Roboto Mono", "Droid Sans Mono", ui-monospace, Menlo, Consolas, monospace; }
.ik { width: 24px; height: 24px; fill: currentColor; flex: none; display: block; }
[dir=rtl] .ik.ayna { transform: scaleX(-1); }

.durum { position: absolute; top: 0; left: 0; right: 0; z-index: 20; display: flex; align-items: center;
  justify-content: space-between; color: var(--onSurface); pointer-events: none; }
.durum .saat { font-weight: 500; letter-spacing: .1px; }
.durum .simgeler { display: flex; align-items: center; gap: 4px; }
.durum .simgeler .ik { width: 17px; height: 17px; }
.android .durum { height: 36px; padding: 0 22px 0 26px; font-size: 14px; }
.ios .durum { height: 54px; padding: 0 30px 0 44px; font-size: 16.5px; font-family: -apple-system, "SF Pro Text", system-ui, sans-serif; }
.ios .durum .saat { font-weight: 600; width: 64px; text-align: center; }
.ios .durum .simgeler { gap: 6px; margin-top: 1px; }
.jest { position: absolute; bottom: 0; left: 0; right: 0; z-index: 20; pointer-events: none; display: flex; justify-content: center; }
.android .jest { height: 24px; align-items: center; }
.android .jest i { width: 104px; height: 4px; border-radius: 2px; background: var(--onSurface); opacity: .42; }
.ios .jest { height: 34px; align-items: flex-end; padding-bottom: 8px; }
.ios .jest i { width: 139px; height: 5px; border-radius: 3px; background: var(--onSurface); opacity: .9; }

.sahne { position: absolute; inset: 0; display: flex; flex-direction: column; background: var(--bg);
  transition: transform .32s cubic-bezier(.2,0,0,1), opacity .32s cubic-bezier(.2,0,0,1); }
.sahne.gel { transform: translateX(30px); opacity: 0; }
[dir=rtl] .sahne.gel { transform: translateX(-30px); }
.sahne.git { transform: translateX(-30px); opacity: 0; pointer-events: none; }
[dir=rtl] .sahne.git { transform: translateX(30px); }
.sahne.geri-gel { transform: translateX(-30px); opacity: 0; }
.sahne.geri-git { transform: translateX(30px); opacity: 0; pointer-events: none; }
.ust { flex: none; background: var(--surface); }
.cubuk { height: 64px; display: flex; align-items: center; padding: 0 4px 0 4px; }
.cubuk .baslik { font-size: 22px; line-height: 28px; font-weight: 600; letter-spacing: .2px; color: var(--onSurface);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.cubuk .bas { padding-inline-start: 12px; display: flex; align-items: center; min-width: 0; flex: 1; }
.dg { width: 48px; height: 48px; display: grid; place-items: center; border-radius: 50%; color: var(--onSurface);
  cursor: pointer; position: relative; flex: none; }
.dg:hover { background: color-mix(in srgb, var(--onSurface) 8%, transparent); }
.govdeK { flex: 1; overflow-y: auto; overflow-x: hidden; scrollbar-width: none; position: relative; overscroll-behavior: contain; }
.govdeK::-webkit-scrollbar { display: none; }

.ara { margin: 0 16px; height: 56px; border: 1px solid var(--outline); border-radius: 28px; display: flex; align-items: center;
  gap: 16px; padding: 0 16px; color: var(--onSv); font-size: 16px; }
.ara .ik { color: var(--onSv); }
.ciprow { display: flex; gap: 8px; padding: 0 16px; overflow: hidden; white-space: nowrap; align-items: center; }
.cip { height: 32px; border: 1px solid var(--outline); border-radius: 10px; padding: 0 16px; display: inline-flex; align-items: center;
  gap: 8px; font-size: 14px; font-weight: 600; letter-spacing: .3px; color: var(--onSv); flex: none; }
.cip.etk { padding-inline-start: 8px; }
.nokta { width: 14px; height: 14px; border-radius: 50%; flex: none; display: inline-block; }
.cip.sm { padding: 0; border: 0; }

.liste { padding: 4px 16px 96px; }
.kart { border-radius: 14px; background: var(--scont); margin: 5px 0; display: flex; align-items: center;
  padding: 12px 14px; gap: 14px; cursor: pointer; position: relative; overflow: hidden; }
.kart:hover::before, .bas-on::before { content: ""; position: absolute; inset: 0; background: var(--onSurface); opacity: .08; border-radius: inherit; }
.kart.yeni { animation: parla 2.4s ease-out 1; }
@keyframes parla { 0%, 25% { background: color-mix(in srgb, var(--pc) 45%, var(--scont)); } 100% { background: var(--scont); } }
.rozet { width: 42px; height: 42px; border-radius: 14px; display: grid; place-items: center; flex: none; }
.rozet .ik { width: 23px; height: 23px; }
.kart .bilgi { flex: 1; min-width: 0; }
.kart .ad { font-size: 16px; line-height: 24px; font-weight: 600; letter-spacing: .15px; color: var(--onSurface);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.kart .alt { display: flex; align-items: center; gap: 6px; font-size: 12px; line-height: 18px; color: var(--onSv); margin-top: 2px; }
.simsek { font-size: 14px; }
.onc { background: var(--sc); color: var(--onSc); border-radius: 6px; padding: 1px 6px; font-size: 11px; line-height: 16px; font-weight: 500; }
.fab { position: absolute; inset-inline-end: 16px; bottom: calc(var(--alt) + 16px); width: 56px; height: 56px; border-radius: 20px;
  background: var(--pc); color: var(--onPc); display: grid; place-items: center; cursor: pointer; z-index: 6;
  box-shadow: 0 3px 5px rgba(0,0,0,.18), 0 1px 18px rgba(0,0,0,.10); }

/* detay */
.detay { padding: 16px 16px 40px; }
.etk-satir { display: flex; gap: 12px; padding-bottom: 12px; font-size: 12px; font-weight: 500; letter-spacing: .5px; color: var(--onSurface); }
.etk-satir span { display: inline-flex; align-items: center; gap: 4px; }
.alan { border: 1px solid var(--outlineV); border-radius: 14px; padding: 10px 16px; margin-bottom: 8px; }
.alan .ust-s { display: flex; align-items: center; min-height: 48px; margin: -4px -10px -4px 0; }
.alan .etiket { flex: 1; font-size: 12px; line-height: 16px; font-weight: 500; letter-spacing: .5px; color: var(--primary);
  display: flex; align-items: center; gap: 6px; min-width: 0; }
.alan .etiket .ik { width: 16px; height: 16px; }
.alan .deger { font-size: 16px; line-height: 24px; color: var(--onSurface); word-break: break-all; white-space: pre-wrap; padding-top: 2px; }
.alan .deger.cok { font-size: 14px; line-height: 21px; }
.alan .deger.gizli { letter-spacing: 2px; }
.alan .iz { font-size: 12px; font-weight: 500; letter-spacing: .5px; color: var(--primary); padding-top: 6px; }
.alan .ozet { border-top: 1px solid var(--outlineV); margin-top: 8px; padding-top: 8px; font-size: 12px; color: var(--onSv); }
.alan .ozet .mono { color: var(--onSurface); font-size: 13px; }
.kutu { border: 1px solid var(--outlineV); border-radius: 14px; padding: 8px 16px; margin-top: 16px; display: flex; align-items: center; gap: 12px; }
.kutu .ba { font-size: 12px; line-height: 16px; font-weight: 500; letter-spacing: .5px; color: var(--primary); }
.kutu .ac { font-size: 14px; line-height: 20px; color: var(--onSurface); }
.anahtar-d { width: 52px; height: 32px; border-radius: 16px; border: 2px solid var(--outline); background: var(--scHighest); position: relative; flex: none; }
.anahtar-d::after { content: ""; position: absolute; width: 16px; height: 16px; border-radius: 50%; background: var(--outline); top: 6px; inset-inline-start: 6px; }
.tarih { border: 1px solid var(--outlineV); border-radius: 14px; padding: 10px 16px; margin-top: 12px; font-size: 14px; color: var(--onSv); }
.kullanim { border: 1px solid var(--outlineV); border-radius: 14px; padding: 10px 16px; margin-top: 16px; }
.kullanim h4 { margin: 0; font-size: 14px; line-height: 20px; font-weight: 600; color: var(--onSurface); }
.kullanim p { margin: 2px 0 0; font-size: 12px; line-height: 18px; color: var(--onSv); }

/* menü, diyalog, bildirim */
.ort { position: absolute; inset: 0; z-index: 40; }
.ort.perde { background: rgba(0,0,0,.32); animation: belir .2s ease-out; }
@keyframes belir { from { opacity: 0; } }
.menu { position: absolute; inset-inline-end: 16px; bottom: calc(var(--alt) + 80px); min-width: 196px; padding: 8px 0;
  background: var(--scont); border-radius: 6px; box-shadow: 0 4px 12px rgba(0,0,0,.18), 0 1px 4px rgba(0,0,0,.12);
  transform-origin: 100% 100%; animation: menuAc .18s cubic-bezier(.2,0,0,1); }
[dir=rtl] .menu { transform-origin: 0 100%; }
@keyframes menuAc { from { opacity: 0; transform: scale(.85); } }
.menu .oge { height: 48px; display: flex; align-items: center; gap: 12px; padding: 0 12px; font-size: 14px; color: var(--onSurface); cursor: pointer; position: relative; }
.menu .oge .ik { color: var(--onSv); }
.menu hr { border: 0; border-top: 1px solid var(--outlineV); margin: 8px 0; }
.diyalog { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: calc(100% - 64px); max-width: 560px;
  background: var(--scHigh); border-radius: 28px; padding: 24px; box-shadow: 0 8px 24px rgba(0,0,0,.22); animation: diyAc .22s cubic-bezier(.2,0,0,1); }
@keyframes diyAc { from { opacity: 0; transform: translate(-50%, -46%) scale(.96); } }
.diyalog h3 { margin: 0 0 16px; font-size: 24px; line-height: 32px; font-weight: 400; color: var(--onSurface); }
.diyalog .metin { font-size: 14px; line-height: 20px; color: var(--onSv); }
.diyalog .metin b { color: var(--onSurface); }
.diyalog .eylemler { display: flex; justify-content: flex-end; gap: 8px; margin-top: 24px; }
.dugmeM { height: 40px; padding: 0 12px; border-radius: 20px; display: inline-flex; align-items: center; font-size: 14px;
  font-weight: 600; letter-spacing: .3px; color: var(--primary); cursor: pointer; }
.dugmeD { height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600;
  letter-spacing: .3px; background: var(--pc); color: var(--onPc); cursor: pointer; }
.girdi { position: relative; margin-top: 16px; height: 56px; border: 1px solid var(--outline); border-radius: 6px; display: flex;
  align-items: center; padding: 0 4px 0 16px; color: var(--onSurface); }
.girdi.odak { border: 2px solid var(--primary); padding-inline-start: 15px; }
.girdi label { position: absolute; top: -9px; inset-inline-start: 12px; padding: 0 4px; font-size: 12px; line-height: 16px; background: var(--scHigh); color: var(--onSv); }
.girdi.odak label { color: var(--primary); }
.girdi .yazi { flex: 1; font-size: 16px; letter-spacing: 3px; white-space: nowrap; overflow: hidden; }
.girdi .imlec { display: inline-block; width: 2px; height: 20px; background: var(--primary); vertical-align: middle; margin-inline-start: 1px; animation: yanip 1s steps(1) infinite; }
@keyframes yanip { 50% { opacity: 0; } }
.ilerleme { height: 4px; border-radius: 2px; background: var(--scHighest); margin: 12px 0 6px; overflow: hidden; }
.ilerleme i { display: block; height: 100%; background: var(--primary); border-radius: 2px; width: 0; transition: width .12s linear; }
.tost { position: absolute; left: 50%; bottom: calc(var(--alt) + 72px); transform: translateX(-50%); z-index: 45;
  max-width: calc(100% - 48px); display: flex; align-items: center; gap: 10px; padding: 10px 16px 10px 10px; border-radius: 24px;
  background: var(--invS); color: var(--invOnS); font-size: 14px; line-height: 20px; box-shadow: 0 2px 8px rgba(0,0,0,.2);
  animation: tostGel .25s cubic-bezier(.2,0,0,1); }
.sabit { animation: none !important; }
.tost img { width: 24px; height: 24px; border-radius: 6px; flex: none; }
@keyframes tostGel { from { opacity: 0; transform: translate(-50%, 8px); } }

/* QR tarama */
.kamera { flex: 1; position: relative; overflow: hidden; background: #0f0e0c; }
.kamera .masa { position: absolute; inset: -10%; background:
  radial-gradient(ellipse at 50% 48%, rgba(255,240,215,.18) 0%, rgba(0,0,0,0) 55%),
  linear-gradient(180deg, #1c1a17 0%, #12110f 100%); filter: blur(1px); }
.dizustu { position: absolute; left: 50%; top: 47%; width: 300px; height: 196px; transform: translate(-50%, -50%) scale(1.06) rotate(-2.5deg);
  background: #f4f1ea; border-radius: 6px; box-shadow: 0 0 0 7px #1d1d1f, 0 12px 40px rgba(0,0,0,.6);
  transition: transform 1.4s cubic-bezier(.3,.1,.2,1); overflow: hidden; }
.kamera.yakin .dizustu { transform: translate(-50%, -50%) scale(1.42) rotate(-.8deg); }
.dizustu .bar { height: 18px; background: #e4e0d6; display: flex; align-items: center; gap: 4px; padding: 0 6px; }
.dizustu .bar i { width: 6px; height: 6px; border-radius: 50%; background: #c9c3b6; }
.dizustu .bar span { margin-inline-start: 8px; flex: 1; height: 10px; border-radius: 5px; background: #f7f5f0; font: 7px/10px "Roboto Mono", monospace; color: #6f6753; padding: 0 6px; overflow: hidden; white-space: nowrap; }
.dizustu canvas { position: absolute; left: 50%; top: 58%; transform: translate(-50%, -50%); width: 128px; height: 128px; image-rendering: pixelated; }
.dizustu .kare-yazi { position: absolute; left: 0; right: 0; bottom: 6px; text-align: center; font: 7px/9px Roboto, sans-serif; color: #6f6753; }
.vizor { position: absolute; left: 50%; top: 46%; width: 230px; height: 230px; transform: translate(-50%, -50%); }
.vizor i { position: absolute; width: 34px; height: 34px; border-color: rgba(255,255,255,.92); border-style: solid; border-width: 0; transition: border-color .2s; }
.vizor i:nth-child(1) { top: 0; left: 0; border-top-width: 4px; border-left-width: 4px; border-top-left-radius: 14px; }
.vizor i:nth-child(2) { top: 0; right: 0; border-top-width: 4px; border-right-width: 4px; border-top-right-radius: 14px; }
.vizor i:nth-child(3) { bottom: 0; left: 0; border-bottom-width: 4px; border-left-width: 4px; border-bottom-left-radius: 14px; }
.vizor i:nth-child(4) { bottom: 0; right: 0; border-bottom-width: 4px; border-right-width: 4px; border-bottom-right-radius: 14px; }
.kamera.okundu .vizor i { border-color: #8fd18a; }
.qr-panel { flex: none; padding: 16px 16px calc(var(--alt) + 12px); background: var(--bg); }
.qr-panel .durumY { font-size: 16px; line-height: 24px; font-weight: 600; color: var(--onBg); }
.qr-panel .kucuk { font-size: 12px; line-height: 18px; color: var(--onSv); }
.qr-panel .dugmeD { margin-top: 12px; }

/* parmak */
/* Bilgisayar: demonun girişinde (ve Android'de sonunda) telefonun YERİNE
   çizilen dizüstü. Telefon soluyor, dizüstü cihaz kutusuna ortalanıp
   büyüyor; içeriği her zaman soldan sağa. Genişliği kutudan taşar; taşma
   payı pcGoster()'de ekrandaki boşluğa göre ölçeklenir (--pck). */
.cihaz.pcde .govde, .cihaz.pcde .cam, .cihaz.pcde .ekran, .cihaz.pcde .dugme, .cihaz.pcde .kesik { opacity: 0; }
.govde, .cam, .ekran, .dugme, .kesik { transition: opacity .4s ease; }
.pc { position: absolute; left: 50%; top: 50%; width: 400px; z-index: 80; direction: ltr; pointer-events: none;
  opacity: 0; transform: translate(-50%, -50%) scale(calc(var(--pck, 1) * .9)); transition: opacity .45s ease, transform .45s ease; }
.pc.gor { opacity: 1; transform: translate(-50%, -50%) scale(var(--pck, 1)); }
.pc-lap { position: relative; width: 352px; margin: 0 auto; }
.pc-kapak { position: relative; height: 232px; border-radius: 13px 13px 5px 5px; background: #0b0b0c; padding: 10px 10px 11px; box-sizing: border-box;
  box-shadow: 0 0 0 1.5px #3b3c40 inset, 0 0 0 1px rgba(255,255,255,.06), 0 24px 40px -18px rgba(0,0,0,.5); }
.pc-kapak::before { content: ""; position: absolute; top: 4px; left: 50%; width: 4px; height: 4px; margin-left: -2px; border-radius: 50%; background: #1f2a38; }
.pc-ekran { position: relative; height: 100%; border-radius: 3px; overflow: hidden; background: #f6f8fa; display: flex; flex-direction: column;
  color: #1f2328; font: 11px/1.4 -apple-system, "Segoe UI", Roboto, system-ui, sans-serif; }
.pc-taban { position: relative; width: 400px; margin-left: -24px; height: 12px; border-radius: 2px 2px 10px 10px;
  background: linear-gradient(180deg, #dcdbd7 0%, #b3b2ae 55%, #8f8e8a 100%); box-shadow: 0 18px 30px -14px rgba(0,0,0,.6); }
.pc-taban::before { content: ""; position: absolute; top: 0; left: 50%; width: 64px; height: 4px; margin-left: -32px; border-radius: 0 0 5px 5px; background: #a2a19d; }
.pc .krom { height: 22px; flex: none; background: #e8e8ea; display: flex; align-items: center; gap: 4px; padding: 0 8px; border-bottom: 1px solid #d4d4d8; }
.pc .krom i { width: 8px; height: 8px; border-radius: 50%; flex: none; }
.pc .krom .adres { flex: 1; margin-left: 5px; height: 14px; border-radius: 7px; background: #fff; color: #555; padding: 0 8px;
  font: 8.5px/14px "Roboto Mono", ui-monospace, monospace; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.pc .sayfa { flex: 1; padding: 12px 40px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 7px; }
.pc .logo { width: 26px; height: 26px; border-radius: 50%; background: #24292f; display: grid; place-items: center; color: #fff; font-weight: 700; font-size: 13px; }
.pc h2 { margin: 0; font-size: 14px; font-weight: 600; text-align: center; }
.pc .form { width: 100%; background: #fff; border: 1px solid #d0d7de; border-radius: 6px; padding: 10px 12px; box-sizing: border-box; display: flex; flex-direction: column; gap: 7px; }
.pc label { display: block; font-size: 9.5px; font-weight: 600; margin-bottom: 3px; }
.pc .alan { height: 24px; border: 1px solid #d0d7de; border-radius: 5px; background: #fff; padding: 0 7px; box-sizing: border-box;
  display: flex; align-items: center; font-size: 10.5px; color: #1f2328; white-space: nowrap; overflow: hidden; transition: box-shadow .15s, border-color .15s; }
.pc .alan.odak { border-color: #0969da; box-shadow: 0 0 0 2.5px rgba(9,105,218,.3); }
.pc .alan .imlec { display: inline-block; width: 1px; height: 13px; background: #1f2328; margin-left: 1px; animation: yanip 1s steps(2) infinite; }
.pc .alan .nokta { letter-spacing: 1.5px; font-size: 12px; }
.pc .gir { height: 26px; border-radius: 5px; background: #1f883d; color: #fff; display: grid; place-items: center; font-weight: 600; font-size: 11px; transition: background .2s; }
.pc .gir.tamam { background: #116329; }
.pc .tik { color: #1a7f37; font-weight: 600; font-size: 10.5px; text-align: center; min-height: 14px; }
.pc .ok { position: absolute; z-index: 5; width: 18px; height: 18px; left: 78%; top: 84%; transition: left .75s cubic-bezier(.3,0,.2,1), top .75s cubic-bezier(.3,0,.2,1), transform .12s; filter: drop-shadow(0 1px 2px rgba(0,0,0,.35)); }
.pc .ok.bas { transform: scale(.82); }
.pc .arac { width: 100%; display: flex; flex-direction: column; align-items: center; gap: 5px; }
.pc .arac .ust { width: 100%; display: flex; justify-content: space-between; align-items: center; font-size: 11px; }
.pc .arac .ust span { font-size: 8.5px; border: 1px solid #d0d7de; border-radius: 4px; padding: 0 5px; background: #fff; }
.pc .arac .btn { width: 100%; height: 22px; border-radius: 5px; background: #5d9c5b; color: #fff; display: grid; place-items: center; font-weight: 600; font-size: 10px; }
.pc .arac .uyari { font-size: 8.5px; color: #7a5a00; text-align: center; line-height: 1.3; }
.pc .arac canvas { width: 104px; height: 104px; image-rendering: pixelated; background: #fff; border: 1px solid #d0d7de; border-radius: 4px; padding: 3px; }
.pc .arac .kare { font-size: 8px; color: #57606a; text-align: center; }
@keyframes yanip { to { visibility: hidden; } }
.parmak { position: absolute; z-index: 60; width: 44px; height: 44px; margin: -22px 0 0 -22px; border-radius: 50%; pointer-events: none;
  background: radial-gradient(circle, rgba(255,255,255,.55) 0%, rgba(255,255,255,.28) 55%, rgba(255,255,255,0) 72%);
  box-shadow: 0 0 0 2px rgba(0,0,0,.18), 0 4px 14px rgba(0,0,0,.25); opacity: 0;
  transition: left .42s cubic-bezier(.3,.1,.2,1), top .42s cubic-bezier(.3,.1,.2,1), opacity .25s, transform .14s; }
.parmak.gor { opacity: 1; }
.parmak.bas { transform: scale(.78); }
[data-tema=acik] .parmak { background: radial-gradient(circle, rgba(60,45,10,.30) 0%, rgba(60,45,10,.16) 55%, rgba(60,45,10,0) 72%); box-shadow: 0 0 0 2px rgba(255,255,255,.7), 0 4px 14px rgba(0,0,0,.18); }

/* model seçici */
.secici { display: flex; gap: 6px; flex-wrap: wrap; justify-content: center; font-family: inherit; }
.secici button { all: unset; cursor: pointer; font-size: 12.5px; line-height: 1; padding: 7px 11px; border-radius: 999px;
  border: 1px solid var(--d-cizgi, rgba(150,140,120,.45)); color: var(--d-soluk, #9c927f); white-space: nowrap; }
.secici button:hover { color: var(--d-pirinc, #c9a34c); border-color: var(--d-pirinc, #c9a34c); }
.secici button[aria-pressed=true] { color: var(--d-pirinc-ink, #16130f); background: var(--d-pirinc, #c9a34c); border-color: var(--d-pirinc, #c9a34c); }
.secici button:focus-visible { outline: 2px solid var(--d-pirinc, #c9a34c); outline-offset: 2px; }
.olcu { font-size: 12px; color: var(--d-soluk, #9c927f); text-align: center; font-family: "IBM Plex Mono", ui-monospace, monospace; letter-spacing: .02em; }

@media (prefers-reduced-motion: reduce) {
  .sahne, .parmak, .dizustu, .ilerleme i { transition: none !important; }
  .menu, .diyalog, .tost, .ort.perde, .kart.yeni, .girdi .imlec { animation: none !important; }
}
`;

  // ── Bileşen ──────────────────────────────────────────────────────────────
  class SekuvoTelefon extends HTMLElement {
    static get observedAttributes() { return ["model", "tema", "demo", "olcek"]; }

    constructor() {
      super();
      this.attachShadow({ mode: "open" });
      this.durum = { ekran: "liste", secili: null, acik: new Set(), menu: false, diyalog: null, tost: null };
      this.kosu = 0;          // çalışan demo betiğinin kimliği; değişince eski betik durur
      this.hazir = false;
      this.shadowRoot.addEventListener("click", (ev) => this.tikla(ev));
    }

    connectedCallback() {
      if (this.hazir) return;
      const kimlik = this.getAttribute("veri") || "telefon-veri";
      const el = document.getElementById(kimlik);
      let veri = {};
      try { veri = el ? JSON.parse(el.textContent) : {}; } catch (_) { veri = {}; }
      this.m = veri.app || {};                 // uygulamanın metinleri
      this.d = Object.assign({ dil: veri.lang || document.documentElement.lang || "en" }, veri.demo || {});
      this.s = veri.site || {};                // sitenin kendi metinleri (seçici, ölçü)
      this.a = veri.arac || {};                // aktar.html'in kendi metinleri (bilgisayar ekranı)
      this.dir = veri.dir || document.documentElement.dir || "ltr";
      bicim.dil = this.d.dil;
      this.kasa = kasaUret(this.d);
      this.ozetle(this.kasa);
      this.hazir = true;
      this.kur();
      this.saatiKur();
      this.gozlem();
    }

    disconnectedCallback() {
      this.kosu++;
      clearInterval(this.saatSayaci);
      this.io && this.io.disconnect();
    }

    attributeChangedCallback(ad, eski, yeni) {
      if (!this.hazir || eski === yeni) return;
      if (ad === "demo") { this.durdur(); this.baslatGerekirse(); return; }
      // Model değişince betik de değişir (iPhone'da Bluetooth sahnesi yok):
      // süren demo durur, arayüz yeniden kurulur, demo baştan başlar.
      const yenidenBaslat = ad === "model" && this.oynuyor;
      if (yenidenBaslat) this.durdur();
      this.kur();
      if (yenidenBaslat) this.baslatGerekirse();
    }

    get model() { return MODELLER[this.getAttribute("model")] || MODELLER["galaxy-s26"]; }
    get modelAdi() { return MODELLER[this.getAttribute("model")] ? this.getAttribute("model") : "galaxy-s26"; }

    temaAdi() {
      const t = this.getAttribute("tema");
      if (t === "acik" || t === "koyu") return t;
      const kok = document.documentElement.getAttribute("data-theme");
      if (kok === "light") return "acik";
      if (kok === "dark") return "koyu";
      return matchMedia("(prefers-color-scheme: dark)").matches ? "koyu" : "acik";
    }

    // ── Çerçeve ────────────────────────────────────────────────────────────
    kur() {
      const m = this.model, e = ekranOlcusu(m);
      const o = parseFloat(this.getAttribute("olcek")) || 1;
      const px = (mm) => mm * PX_MM * o;
      const W = px(m.govde[0]), H = px(m.govde[1]);
      const eW = px(e.en), eH = px(e.boy);
      const eX = (W - eW) / 2, eY = (H - eH) / 2;
      const olcek = eW / m.dpGen;
      this.olcekF = olcek;
      const dpH = e.dpBoy;
      const ios = m.sistem === "ios";
      const ustBosluk = ios ? 54 : 36, altBosluk = ios ? 34 : 24;
      this.ustBosluk = ustBosluk;
      this.altBosluk = altBosluk;
      const tema = this.temaAdi(), T = TEMA[tema];
      const renkler = Object.entries(T).map(([k, v]) => `--${k}:${v}`).join(";");
      const k = m.kesik;
      const kesik = k.tur === "delik"
        ? `<div class="kesik delik" style="width:${px(k.cap)}px;height:${px(k.cap)}px;top:${px(k.ust) - px(k.cap) / 2}px"></div>`
        : `<div class="kesik ada" style="width:${px(k.en)}px;height:${px(k.boy)}px;top:${px(k.ust)}px"></div>`;
      const dugmeler = m.dugme.map(([yan, ust, boy, ek]) =>
        `<i class="dugme ${yan} ${ek || ""}" style="top:${px(ust)}px;height:${px(boy)}px"></i>`).join("");
      const secici = this.hasAttribute("secici") ? `
        <div class="secici" role="group" aria-label="${kac(this.s.secici_etiket || "Phone model")}">
          ${MODEL_SIRASI.map((id) => `<button type="button" data-model="${id}" aria-pressed="${id === this.modelAdi}">${kac(MODELLER[id].kisa)}</button>`).join("")}
        </div>
        <div class="olcu">${kac(bicim(this.s.olcu || "1:1 · %1$s × %2$s mm", m.govde[0].toLocaleString(this.d.dil), m.govde[1].toLocaleString(this.d.dil)))}</div>` : "";

      this.shadowRoot.innerHTML = `<style>${CSS}</style>
        <div class="sarmal">
          <div class="cihaz" style="width:${W}px;height:${H}px;--mm:${PX_MM * o}px;--kose:${px(m.kose)}px;--cerceve:${px(m.cerceve)}px;--ekose:${px(Math.max(m.kose - 2.3, 4))}px;--r1:${m.renk[0]};--r2:${m.renk[1]};--r3:${m.renk[2]}">
            ${dugmeler}
            <div class="govde"></div>
            <div class="cam"></div>
            <div class="ekran" style="left:${eX}px;top:${eY}px;width:${eW}px;height:${eH}px;--bg:${T.bg}">
              <div class="uyg ${ios ? "ios" : "android"}" dir="${this.dir}" data-tema="${tema}"
                   style="width:${m.dpGen}px;height:${dpH}px;transform:scale(${olcek});${renkler};--ust:${ustBosluk}px;--alt:${altBosluk}px">
                <div class="durum"><span class="saat"></span><span class="simgeler">${ikon("signal_cellular_alt")}${ikon("wifi")}${ikon("battery_full")}</span></div>
                <div class="sahneler"></div>
                <div class="katman"></div>
                <div class="jest"><i></i></div>
                <div class="parmak"></div>
              </div>
              ${kesik}
            </div>
            <div class="pc" dir="ltr" aria-hidden="true"></div>
          </div>
          ${secici}
        </div>`;
      this.uyg = this.shadowRoot.querySelector(".uyg");
      this.pc = this.shadowRoot.querySelector(".pc");
      this.sahneler = this.shadowRoot.querySelector(".sahneler");
      this.katman = this.shadowRoot.querySelector(".katman");
      this.parmak = this.shadowRoot.querySelector(".parmak");
      this.ciz(null);
      this.katmanCiz();
      this.saatYaz();
      const cihaz = this.shadowRoot.querySelector(".cihaz");
      cihaz.setAttribute("role", "img");
      cihaz.setAttribute("aria-label", this.getAttribute("aria-label") || `${m.ad} — Sekuvo`);
      if (!this._temaDinle) {
        this._temaDinle = true;
        matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => this.kur());
      }
    }

    saatYaz() {
      const s = this.shadowRoot.querySelector(".saat");
      if (s) s.textContent = new Date().toLocaleTimeString(this.d.dil, { hour: "2-digit", minute: "2-digit", hour12: false });
    }
    saatiKur() { this.saatSayaci = setInterval(() => this.saatYaz(), 20000); }

    // ── Ekranlar ───────────────────────────────────────────────────────────
    t(k) { return this.m[k] || k; }
    turEtiketi(tur) { return this.t(TUR_METNI[tur]); }
    rozet(k) {
      const renk = { LOGIN: "var(--primary)", EVERYDAY: "#63C7B2", CARD: "var(--tertiary)", NOTE: "#B08FE0" }[k.tur];
      const ad = k.tur === "NOTE" ? NOT_IKON[k.tur2 || "GENEL"] : TUR_IKON[k.tur];
      return `<span class="rozet" style="color:${renk};background:color-mix(in srgb, ${renk} 16%, transparent)">${ikon(ad, ad === "note" ? "ayna" : "")}</span>`;
    }
    noktalar(k) {
      return k.etiket.map((e) => `<i class="nokta" style="background:${ETIKET_RENK[e]}"></i>`).join("");
    }
    sirali() {
      return [...this.kasa].sort((a, b) => a.baslik.localeCompare(b.baslik, this.d.dil, { sensitivity: "base" }));
    }

    listeHTML() {
      const turler = ["LOGIN", "EVERYDAY", "CARD", "NOTE"];
      return `<div class="ust" style="padding-top:var(--ust)">
          <div class="cubuk">
            <div class="bas"><span class="baslik">Sekuvo</span><span class="dg" style="margin-inline-start:4px">${ikon("sort", "ayna")}</span></div>
            <span class="dg">${ikon("fingerprint")}</span><span class="dg">${ikon("swap_horiz")}</span>
            <span class="dg">${ikon("casino")}</span><span class="dg">${ikon("lock")}</span><span class="dg">${ikon("settings")}</span>
          </div>
        </div>
        <div class="govdeK liste-k" data-kaydir="liste">
          <div class="ara">${ikon("search")}<span>${kac(this.t("home_search_hint"))}</span></div>
          <div class="ciprow" style="margin-top:8px">${turler.map((t) => `<span class="cip">${kac(this.turEtiketi(t))}</span>`).join("")}</div>
          <div class="ciprow" style="margin-top:4px">${["finans", "kisisel", "is"].map((e) =>
            `<span class="cip etk"><i class="nokta" style="background:${ETIKET_RENK[e]}"></i>${kac(this.d["etiket_" + e] || e)}</span>`).join("")}
            <span class="dg" style="color:var(--onSurface)">${ikon("sell", "ayna")}</span></div>
          <div class="liste">
            ${this.sirali().map((k) => `
              <div class="kart${k.yeni ? " yeni" : ""}" data-hedef="kayit:${k.id}">
                ${this.rozet(k)}
                <div class="bilgi"><div class="ad">${kac(k.baslik)}</div>
                  <div class="alt"><span>${kac(this.turEtiketi(k.tur))}</span>${this.noktalar(k)}</div></div>
                ${k.hizli && this.model.sistem !== "ios" ? `<span class="simsek">⚡</span>` : ""}
                ${k.oncelik ? `<span class="onc">${k.oncelik}</span>` : ""}
              </div>`).join("")}
          </div>
        </div>
        <div class="fab" data-hedef="fab">${ikon("add")}</div>`;
    }

    alanEtiketi(a) {
      if (typeof a === "string") return this.t(ALAN_METNI[a]);
      return a.ozel;
    }

    detayHTML(id) {
      // iOS'ta olmayan özellikler çizilmez: Bluetooth klavye, Sekuvo Klavyesi
      // (hızlı erişim) ve kullanım günlüğü — olmayan özellik gösterilmez.
      const ios = this.model.sistem === "ios";
      const k = this.kasa.find((x) => x.id === id);
      if (!k) return this.listeHTML();
      const tarihB = (ms) => new Date(ms).toLocaleString(this.d.dil, { day: "numeric", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit", hour12: false });
      const etiketler = k.etiket.length ? `<div class="etk-satir">${k.etiket.map((e) =>
        `<span><i class="nokta" style="width:13px;height:13px;background:${ETIKET_RENK[e]}"></i>${kac(this.d["etiket_" + e] || e)}</span>`).join("")}</div>` : "";
      const alanlar = k.alanlar.map(([anahtar, deger], i) => {
        const ozel = typeof anahtar === "object";
        const ad = ozel ? `o${i}` : anahtar;
        const gizli = ozel ? anahtar.tur === "PASSWORD" : GIZLI.has(anahtar);
        const acik = this.durum.acik.has(`${id}:${ad}`);
        let gorunen = deger;
        if (anahtar === "cardNumber") gorunen = kartGrupla(deger);
        if (anahtar === "expiry") gorunen = `${deger.slice(0, 2)}/${deger.slice(2)}`;
        const cok = deger.includes("\n");
        const etiketEk = anahtar === "cardNumber" ? ` · ${deger[0] === "4" ? "Visa" : "Mastercard"}` : "";
        const etiketIkon = ozel ? ikon(OZEL_IKON[anahtar.tur] || "text_fields") : "";
        const metin = gizli && !acik ? "••••••••" : gorunen;
        const oz = (k.ozet || {})[ad];
        const ozMetni = oz ? `${oz.slice(0, 4)} ${oz.slice(4, 8)} … ${oz.slice(-4)}` : "…";
        const altSatir = cok
          ? `<div class="ozet">${kac(bicim(this.t("detail_fingerprint_len"), deger.length))}<br><span class="mono">${ozMetni}</span></div>`
          : (!gizli ? `<div class="iz">${kac(this.t("detail_show_fingerprint"))}</div>` : "");
        return `<div class="alan">
          <div class="ust-s"><span class="etiket">${etiketIkon}${kac(this.alanEtiketi(anahtar) + etiketEk)}</span>
            ${gizli ? `<span class="dg" data-hedef="alan:${ad}:goz">${ikon(acik ? "visibility_off" : "visibility")}</span>` : ""}
            <span class="dg" data-hedef="alan:${ad}:kopya">${ikon("content_copy")}</span>
            ${ios ? "" : `<span class="dg" data-hedef="alan:${ad}:pc">${ikon("computer")}</span>`}</div>
          <div class="deger mono${cok ? " cok" : ""}${gizli && !acik ? " gizli" : ""}">${kac(metin)}</div>
          ${altSatir}
        </div>`;
      }).join("");
      return `<div class="ust" style="padding-top:var(--ust)">
          <div class="cubuk"><span class="dg" data-hedef="geri">${ikon("arrow_back", "ayna")}</span>
            <div class="bas" style="padding-inline-start:4px"><span class="baslik">${kac(k.baslik)}</span></div>
            <span class="dg">${ikon("edit")}</span></div>
        </div>
        <div class="govdeK" data-kaydir="detay">
          <div class="detay">
            ${etiketler}${alanlar}
            ${ios ? "" : `<div class="kutu"><div style="flex:1"><div class="ba">${kac(this.t("detail_quick_title"))}</div>
              <div class="ac">${kac(this.t(k.hizli ? "detail_quick_on" : "detail_quick_off"))}</div></div>
              <span class="anahtar-d" style="${k.hizli ? "background:var(--primary);border-color:var(--primary)" : ""}"></span></div>`}
            <div class="tarih">${kac(bicim(this.t("detail_dates"), tarihB(k.eklendi), tarihB(k.guncellendi)))}</div>
            ${ios ? "" : `<div class="kullanim"><h4>${kac(this.t("detail_usage_title"))}</h4><p>${kac(this.t("detail_usage_empty"))}</p></div>`}
          </div>
        </div>`;
    }

    qrHTML() {
      return `<div class="kamera" data-kamera>
          <div class="masa"></div>
          <div class="dizustu"><div class="bar"><i></i><i></i><i></i><span>file:///…/aktar.html</span></div>
            <canvas width="41" height="41"></canvas><div class="kare-yazi"></div></div>
          <div class="vizor"><i></i><i></i><i></i><i></i></div>
        </div>
        <div class="qr-panel">
          <div class="durumY">${kac(this.t("qr_status_aim"))}</div>
          <div class="kucuk">${kac(bicim(this.t("qr_camera_analysis"), "1280×720"))}</div>
          <div class="ilerleme" hidden><i></i></div>
          <div class="dugmeD" data-hedef="qr:iptal">${kac(this.t("qr_cancel"))}</div>
        </div>`;
    }

    // Sahne değişimi: Material "paylaşılan X ekseni" geçişi
    ciz(yon) {
      const yeni = document.createElement("div");
      yeni.className = "sahne";
      yeni.style.paddingBottom = this.durum.ekran === "qr" ? "0" : `var(--alt)`;
      yeni.innerHTML = this.durum.ekran === "detay" ? this.detayHTML(this.durum.secili)
        : this.durum.ekran === "qr" ? this.qrHTML() : this.listeHTML();
      const eski = this.sahneler.lastElementChild;
      const hareketsiz = matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (eski && yon && !hareketsiz) {
        yeni.classList.add(yon === "ileri" ? "gel" : "geri-gel");
        this.sahneler.appendChild(yeni);
        // eslint-disable-next-line no-unused-expressions
        yeni.offsetWidth;
        yeni.classList.remove("gel", "geri-gel");
        eski.classList.add(yon === "ileri" ? "git" : "geri-git");
        setTimeout(() => eski.remove(), 340);
      } else {
        this.sahneler.innerHTML = "";
        this.sahneler.appendChild(yeni);
      }
      if (this.durum.ekran === "liste" && this.listeKaydirma) {
        const k = yeni.querySelector("[data-kaydir=liste]");
        if (k) k.scrollTop = this.listeKaydirma;
      }
      if (this.durum.ekran === "qr") this.qrCiz();
      return yeni;
    }

    katmanCiz() {
      const d = this.durum;
      let h = "";
      if (d.menu) {
        const turler = ["LOGIN", "EVERYDAY", "CARD", "NOTE"];
        h += `<div class="ort" data-hedef="perde"><div class="menu">
          ${turler.map((t) => `<div class="oge">${ikon(TUR_IKON[t], t === "NOTE" ? "ayna" : "")}${kac(this.turEtiketi(t))}</div>`).join("")}
          <hr><div class="oge" data-hedef="menu:qr">${ikon("qr_code_scanner")}${kac(this.t("home_import_qr"))}</div>
          <div class="oge">${ikon("content_paste")}${kac(this.t("home_import_text"))}</div></div></div>`;
      }
      // Aynı diyalog/bildirim yeniden çizilirken giriş animasyonu tekrarlanmaz.
      const sabitD = d.diyalog && d.diyalog === this._sonDiyalog ? " sabit" : "";
      const sabitT = d.tost && d.tost === this._sonTost ? " sabit" : "";
      this._sonDiyalog = d.diyalog;
      this._sonTost = d.tost;
      if (d.diyalog) h += `<div class="ort perde${sabitD}">${this.diyalogHTML(d.diyalog).replace('class="diyalog"', `class="diyalog${sabitD}"`)}</div>`;
      if (d.tost) h += `<div class="tost${sabitT}"><img src="/img/icon-180.png" alt="">${kac(d.tost)}</div>`;
      this.katman.innerHTML = h;
    }

    diyalogHTML(g) {
      if (g.tur === "bt") {
        const sure = bicim(this.t("bt_duration_seconds"), Math.max(1, Math.round(g.n / 9)));
        const govde = g.asama === "baglan" ? kac(bicim(this.t("bt_connecting"), this.d.bt_cihaz))
          : `${kac(bicim(this.t("bt_connected"), this.d.bt_cihaz))}<br><br>` + (g.asama === "bitti"
            ? kac(bicim(this.t("bt_done_summary"), g.n, sure, 9))
            : `${kac(bicim(this.t("bt_typing_progress"), g.yazilan, g.n))}<div class="ilerleme"><i style="width:${(100 * g.yazilan) / g.n}%"></i></div>`);
        return `<div class="diyalog"><h3>${kac(bicim(this.t("bt_title"), g.alan))}</h3>
          <div class="metin">${govde}</div>
          <div class="eylemler"><span class="dugmeM" data-hedef="diyalog:kapat">${kac(this.t("bt_close"))}</span></div></div>`;
      }
      if (g.tur === "ice") {
        return `<div class="diyalog"><h3>${kac(this.t("paste_title_qr"))}</h3>
          <div class="metin">${kalin(bicim(this.t("paste_qr_ready"), g.uzunluk))}</div>
          <div class="girdi odak"><label>${kac(this.t("paste_label_backup_password"))}</label>
            <span class="yazi">${"•".repeat(g.yazilan)}<span class="imlec"></span></span>
            <span class="dg" style="color:var(--onSv)">${ikon("visibility")}</span></div>
          <div class="eylemler"><span class="dugmeM" data-hedef="diyalog:kapat">${kac(this.t("paste_btn_cancel"))}</span>
            <span class="dugmeM" data-hedef="diyalog:ice-aktar">${kac(this.t(g.mesgul ? "paste_btn_importing" : "paste_btn_import"))}</span></div></div>`;
      }
      return "";
    }

    // Kameradaki dizüstü ekranının QR'ı (görüntü; çözülmez)
    qrCiz() {
      const c = this.shadowRoot.querySelector(".dizustu canvas");
      if (c) qrDesen(c, 41);
    }

    // ── Eylemler (kullanıcı tıklaması ve demo aynı yoldan geçer) ──────────
    tikla(ev) {
      const sb = ev.target.closest("[data-model]");
      if (sb) { this.setAttribute("model", sb.dataset.model); return; }
      const el = ev.target.closest("[data-hedef]");
      if (!el || !ev.isTrusted) return;
      this.kullaniciDokundu();
      this.eylem(el.dataset.hedef);
    }

    eylem(h) {
      const d = this.durum;
      const [tur, a, b] = h.split(":");
      if (tur === "kayit") {
        const l = this.sahneler.querySelector("[data-kaydir=liste]");
        this.listeKaydirma = l ? l.scrollTop : 0;
        d.ekran = "detay"; d.secili = a; this.ciz("ileri");
      } else if (tur === "geri") {
        d.ekran = "liste"; d.secili = null; this.ciz("geri");
      } else if (tur === "alan" && b === "goz") {
        const anahtar = `${d.secili}:${a}`;
        d.acik.has(anahtar) ? d.acik.delete(anahtar) : d.acik.add(anahtar);
        const kay = this.sahneler.lastElementChild.querySelector("[data-kaydir=detay]");
        const y = kay ? kay.scrollTop : 0;
        this.sahneler.lastElementChild.innerHTML = this.detayHTML(d.secili);
        const kay2 = this.sahneler.lastElementChild.querySelector("[data-kaydir=detay]");
        if (kay2) kay2.scrollTop = y;
      } else if (tur === "alan" && b === "kopya") {
        const k = this.kasa.find((x) => x.id === d.secili);
        const alan = k && k.alanlar.find(([an], i) => (typeof an === "object" ? `o${i}` : an) === a);
        if (!alan) return;
        const sablon = this.model.sistem === "ios"
          ? (this.s.ios_kopyalandi || "%1$s copied · this iPhone only, cleared in 45 s")
          : (this.s.kopyalandi || "%1$s copied · clipboard clears in 45 s, or when you return to the app");
        const no = (this.tostKosu = (this.tostKosu || 0) + 1);
        d.tost = bicim(sablon, this.alanEtiketi(alan[0]));
        this.katmanCiz();
        setTimeout(() => { if (this.tostKosu === no) { d.tost = null; this.katmanCiz(); } }, 2600);
      } else if (tur === "alan" && b === "pc") {
        const k = this.kasa.find((x) => x.id === d.secili);
        const alan = k && k.alanlar.find(([an], i) => (typeof an === "object" ? `o${i}` : an) === a);
        if (!alan) return;
        this.btYaz(this.alanEtiketi(alan[0]), alan[1].length);
      } else if (tur === "fab") {
        d.menu = true; this.katmanCiz();
      } else if (tur === "perde") {
        d.menu = false; this.katmanCiz();
      } else if (tur === "menu" && a === "qr") {
        d.menu = false; this.katmanCiz();
        d.ekran = "qr"; this.ciz("ileri");
        this.qrAkisi();
      } else if (tur === "qr" && a === "iptal") {
        this.qrKosu = (this.qrKosu || 0) + 1;
        d.ekran = "liste"; this.ciz("geri");
      } else if (tur === "diyalog" && a === "kapat") {
        this.btKosu = (this.btKosu || 0) + 1;
        this.qrKosu = (this.qrKosu || 0) + 1;
        const ice = d.diyalog && d.diyalog.tur === "ice";
        d.diyalog = null; this.katmanCiz();
        if (ice) { d.ekran = "liste"; this.ciz("geri"); }
      } else if (tur === "diyalog" && a === "ice-aktar") {
        this.iceAktar();
      }
    }

    async btYaz(alanAdi, n) {
      const no = (this.btKosu = (this.btKosu || 0) + 1);
      const d = this.durum;
      const ayni = () => this.btKosu === no;
      const bekle = (ms) => new Promise((c) => setTimeout(c, ms));
      d.diyalog = { tur: "bt", alan: alanAdi, n, yazilan: 0, asama: "baglan" };
      this.katmanCiz();
      await bekle(800); if (!ayni()) return;
      d.diyalog.asama = "yaz"; this.katmanCiz();
      await bekle(1000); if (!ayni()) return;   // 1 sn geri sayım (bt_before_start)
      const adim = Math.max(1, Math.round(n / 14));
      while (d.diyalog && d.diyalog.yazilan < n) {
        d.diyalog.yazilan = Math.min(n, d.diyalog.yazilan + adim);
        this.katmanCiz();
        await bekle(90); if (!ayni()) return;
      }
      if (!d.diyalog) return;
      d.diyalog.asama = "bitti"; this.katmanCiz();
    }

    async qrAkisi() {
      const no = (this.qrKosu = (this.qrKosu || 0) + 1);
      const ayni = () => this.qrKosu === no && this.durum.ekran === "qr";
      const bekle = (ms) => new Promise((c) => setTimeout(c, ms));
      await bekle(380);
      const kam = this.shadowRoot.querySelector("[data-kamera]");
      if (!kam || !ayni()) return;
      kam.classList.add("yakin");
      await bekle(1250); if (!ayni()) return;
      const toplam = 3;
      const durumY = this.shadowRoot.querySelector(".qr-panel .durumY");
      const il = this.shadowRoot.querySelector(".qr-panel .ilerleme");
      const kareYazi = this.shadowRoot.querySelector(".kare-yazi");
      for (let i = 1; i <= toplam; i++) {
        this.qrCiz();
        if (kareYazi) kareYazi.textContent = `${i}/${toplam}`;
        await bekle(520); if (!ayni()) return;
        durumY.textContent = bicim(this.t("qr_status_received"), i, toplam);
        il.hidden = false; il.firstElementChild.style.width = `${(100 * i) / toplam}%`;
      }
      kam.classList.add("okundu");
      durumY.textContent = this.t("qr_status_done");
      await bekle(650); if (!ayni()) return;
      this.durum.diyalog = { tur: "ice", uzunluk: 1180 + rast(400), yazilan: 0, mesgul: false };
      this.katmanCiz();
    }

    async parolaYaz(n) {
      const g = this.durum.diyalog;
      if (!g || g.tur !== "ice") return;
      for (let i = 0; i < n; i++) {
        g.yazilan++;
        this.katmanCiz();
        await new Promise((c) => setTimeout(c, 85 + rast(70)));
        if (this.durum.diyalog !== g) return;
      }
    }

    async iceAktar() {
      const g = this.durum.diyalog;
      if (!g || g.tur !== "ice" || g.mesgul) return;
      if (g.yazilan === 0) { await this.parolaYaz(20); }
      g.mesgul = true; this.katmanCiz();
      await new Promise((c) => setTimeout(c, 900));
      if (this.durum.diyalog !== g) return;
      this.durum.diyalog = null;
      this.kasa = this.kasa.filter((k) => k.id !== "yeni").map((k) => ({ ...k, yeni: false }));
      const yeni0 = yeniKayit(this.d);
      this.kasa.push(yeni0);
      this.ozetle([yeni0]);
      this.durum.ekran = "liste";
      this.listeKaydirma = 0;
      this.ciz("geri");
      const cogul = this.m.vm_import_added || {};
      this.durum.tost = bicim(cogul.one || cogul.other || "%1$d", 1);
      this.katmanCiz();
      const yeni = this.sahneler.lastElementChild.querySelector(".kart.yeni");
      if (yeni) yeni.scrollIntoView({ block: "center" });
      setTimeout(() => { this.durum.tost = null; this.katmanCiz(); }, 2600);
    }

    // Çok satırlı değerlerin SHA-256 parmak izi, uygulamadaki gibi gerçek
    // değerden hesaplanır (yalnız bu tarayıcıda).
    async ozetle(kayitlar) {
      if (!(window.crypto && crypto.subtle)) return;
      for (const k of kayitlar) {
        for (let i = 0; i < k.alanlar.length; i++) {
          const [an, deger] = k.alanlar[i];
          if (!deger.includes("\n")) continue;
          const ad = typeof an === "object" ? `o${i}` : an;
          const b = new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(deger)));
          (k.ozet = k.ozet || {})[ad] = [...b].map((x) => x.toString(16).padStart(2, "0")).join("");
          if (this.durum.ekran === "detay" && this.durum.secili === k.id) {
            const sahne = this.sahneler.lastElementChild;
            const kay = sahne && sahne.querySelector("[data-kaydir=detay]");
            const y = kay ? kay.scrollTop : 0;
            if (sahne) { sahne.innerHTML = this.detayHTML(k.id); const k2 = sahne.querySelector("[data-kaydir=detay]"); if (k2) k2.scrollTop = y; }
          }
        }
      }
    }

    // ── Demo betikleri ────────────────────────────────────────────────────
    betik(ad) {
      if (ad === "qr") {
        return [
          ["bekle", 1400], ["dokun", "fab"], ["bekle", 900], ["dokun", "menu:qr"], ["bekle", 4800],
          ["parola", 18], ["bekle", 350], ["dokun", "diyalog:ice-aktar"], ["bekle", 4200], ["sifirla"],
        ];
      }
      // Tur önce bilgisayar ekranıyla açılır, sonra telefona geçer.
      // Android: tarayıcıdaki giriş formunda parola alanına tıklanır; telefon
      // parolayı Bluetooth ile yazar; sonunda formun dolduğu görülür.
      // iPhone: Bluetooth klavye yok (iOS izin vermez). Bilgisayar aktar.html'in
      // QR'ını gösterir, telefon onu okur (bilgisayardan telefona — iOS'ta olan
      // yön); detayda parola panoya kopyalanır (yalnız bu iPhone'da, 45 sn).
      const ios = this.model.sistem === "ios";
      const giris = ios
        ? [["pc", "qr"], ["bekle", 2600], ["pc", null], ["bekle", 700],
           ["dokun", "fab"], ["bekle", 900], ["dokun", "menu:qr"], ["bekle", 4800],
           ["parola", 18], ["bekle", 350], ["dokun", "diyalog:ice-aktar"], ["bekle", 3600]]
        : [["pc", "giris"], ["bekle", 1400], ["pcTikla"], ["bekle", 900], ["pc", null], ["bekle", 800]];
      const cikis = ios
        ? [["dokun", "alan:password:kopya"], ["bekle", 3000]]
        : [["dokun", "alan:password:pc"], ["bekle", 4200], ["dokun", "diyalog:kapat"], ["bekle", 400],
           ["pc", "yaz"], ["bekle", 900], ["pcYaz"], ["bekle", 1600], ["pc", null], ["bekle", 600]];
      return [
        ...giris,
        ["dokun", "kayit:github"], ["bekle", 1400],
        ["dokun", "alan:password:goz"], ["bekle", 1500],
        ...cikis,
        ["dokun", "geri"], ["bekle", 1000],
        ["kaydir", "liste", 360], ["bekle", 900],
        ["dokun", "kayit:visa"], ["bekle", 1300],
        ["dokun", "alan:cvv:goz"], ["bekle", 1400],
        ["dokun", "geri"], ["bekle", 800],
        ["kaydir", "liste", 0], ["bekle", 900],
        ["dokun", "kayit:deploy"], ["bekle", 1300],
        ["kaydir", "detay", 220], ["bekle", 1700],
        ["dokun", "geri"], ["bekle", 900],
        ["dokun", "fab"], ["bekle", 1600], ["dokun", "perde"], ["bekle", 900],
        ["sifirla"],
      ];
    }

    async oynat(ad) {
      const no = ++this.kosu;
      const bekle = (ms) => new Promise((coz, red) => setTimeout(() => (this.kosu === no ? coz() : red(DUR)), ms));
      try {
        for (;;) {
          for (const [islem, x, y] of this.betik(ad)) {
            if (this.kosu !== no) return;
            if (islem === "bekle") await bekle(x);
            else if (islem === "dokun") await this.dokun(x, bekle);
            else if (islem === "kaydir") this.kaydir(x, y);
            else if (islem === "parola") await this.parolaYaz(x);
            else if (islem === "pc") x ? this.pcGoster(x) : this.pcGizle();
            else if (islem === "pcTikla") await this.pcTikla(bekle);
            else if (islem === "pcYaz") await this.pcYaz(bekle);
            else if (islem === "sifirla") this.sifirla();
          }
        }
      } catch (e) {
        if (e !== DUR) throw e;
      }
    }

    async dokun(hedef, bekle) {
      const el = this.shadowRoot.querySelector(`[data-hedef="${hedef}"]`);
      if (!el) return;
      const kap = el.closest(".govdeK");
      if (kap) {
        const r = el.getBoundingClientRect(), kr = kap.getBoundingClientRect();
        if (r.top < kr.top + 8 || r.bottom > kr.bottom - 8) {
          kap.scrollTo({ top: kap.scrollTop + (r.top - kr.top) - kr.height / 3, behavior: "smooth" });
          await bekle(450);
        }
      }
      const u = this.uyg.getBoundingClientRect(), r = el.getBoundingClientRect();
      const x = (r.left + r.width / 2 - u.left) / this.olcekF;
      const y = (r.top + r.height / 2 - u.top) / this.olcekF;
      const p = this.parmak;
      if (!p.classList.contains("gor")) {
        p.style.transition = "none"; p.style.left = `${x + 40}px`; p.style.top = `${y + 70}px`;
        // eslint-disable-next-line no-unused-expressions
        p.offsetWidth; p.style.transition = "";
      }
      p.classList.add("gor");
      p.style.left = `${x}px`; p.style.top = `${y}px`;
      await bekle(460);
      p.classList.add("bas"); el.classList.add("bas-on");
      await bekle(150);
      p.classList.remove("bas"); el.classList.remove("bas-on");
      this.eylem(hedef);
      await bekle(220);
      if (hedef === "geri" || hedef.startsWith("kayit") || hedef === "menu:qr") p.classList.remove("gor");
    }

    kaydir(ad, y) {
      const k = this.sahneler.lastElementChild && this.sahneler.lastElementChild.querySelector(`[data-kaydir="${ad}"]`);
      if (k) k.scrollTo({ top: y, behavior: "smooth" });
    }

    sifirla() {
      this.kasa = kasaUret(this.d);
      this.ozetle(this.kasa);
      this.durum = { ekran: "liste", secili: null, acik: new Set(), menu: false, diyalog: null, tost: null };
      this.listeKaydirma = 0;
      this.btKosu = (this.btKosu || 0) + 1;
      this.qrKosu = (this.qrKosu || 0) + 1;
      this.parmak.classList.remove("gor");
      this.pcGizle();
      this.ciz(null);
      this.katmanCiz();
    }

    // ── Bilgisayar ekranı (demonun girişi ve Android'de sonu) ──────────────
    pcHTML(tur) {
      const ok = `<svg class="ok" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3l14 10-6 1 4 7-3 2-4-7-5 4z" fill="#111" stroke="#fff" stroke-width="1.5" stroke-linejoin="round"/></svg>`;
      const krom = (adres) => `<div class="krom"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i><span class="adres">${adres}</span></div>`;
      const lap = (adres, icerik) => `<div class="pc-lap"><div class="pc-kapak"><div class="pc-ekran">${krom(adres)}<div class="sayfa">${icerik}</div></div></div><div class="pc-taban"></div></div>`;
      if (tur === "qr") {
        const a = this.a;
        return lap("file:///Users/…/Downloads/aktar.html", `<div class="arac">
            <div class="ust"><b>🔐 ${kac(a.h1 || "Sekuvo Transfer")}</b><span>${this.d.dil === "tr" ? "Türkçe" : "English"} ▾</span></div>
            <div class="btn">${kac(a.btnQr || "Encrypt and show the QR")}</div>
            <div class="uyari">${a.uyariQr || ""}</div>
            <canvas></canvas>
            <div class="kare"></div>
          </div>`);
      }
      // Giriş formu: üçüncü taraf bir site, metinleri İngilizce (sayfa dilinden bağımsız).
      // "giris": alan boş, imleç tıklayacak. "yaz": alan odakta, parola telefon
      // tarafından harf harf yazılacak (pcYaz).
      const k = this.kasa.find((x) => x.id === "github");
      const alan = (ad) => (k && (k.alanlar.find(([a]) => a === ad) || [])[1]) || "";
      const yaz = tur === "yaz";
      return lap("https://github.com/login", `
          <div class="logo">G</div><h2>Sign in</h2>
          <div class="form">
            <div><label>Username or email address</label><div class="alan kullanici">${kac(alan("username"))}</div></div>
            <div><label>Password</label><div class="alan parola${yaz ? " odak" : ""}"><span class="nokta"></span><span class="imlec" style="${yaz ? "" : "visibility:hidden"}"></span></div></div>
            <div class="gir">Sign in</div>
            <div class="tik"></div>
          </div>`) + (yaz ? "" : ok);
    }

    pcGoster(tur) {
      if (!this.pc) return;
      this.pcGizle();
      this.pc.innerHTML = this.pcHTML(tur);
      // eslint-disable-next-line no-unused-expressions
      this.pc.offsetWidth;
      // Dizüstü (400 px) cihaz kutusundan taşar; iki yandaki boşluk kadar
      // izin verilir, yoksa küçültülür (mobilde ve dar sütunda).
      const kutu = this.pc.parentElement.getBoundingClientRect();
      const bos = Math.max(0, Math.min(kutu.left, document.documentElement.clientWidth - kutu.right) - 12);
      const k = Math.min(1, (kutu.width + 2 * bos) / 400);
      this.pc.style.setProperty("--pck", k.toFixed(3));
      this.pc.classList.add("gor");
      this.pc.parentElement.classList.add("pcde");
      if (tur === "qr") {
        const c = this.pc.querySelector("canvas"), y = this.pc.querySelector(".kare");
        let kare = 0;
        const ilerle = () => { kare = (kare % 3) + 1; qrDesen(c, 57); y.textContent = bicim(this.a.kareCok || "%1$d/%2$d", kare, 3, 2); };
        ilerle();
        this.pcSayac = setInterval(ilerle, 1000);
      }
    }

    pcGizle() {
      if (!this.pc) return;
      clearInterval(this.pcSayac); this.pcSayac = null;
      this.pc.classList.remove("gor");
      this.pc.parentElement.classList.remove("pcde");
    }

    /** Bilgisayarda parola harf harf yazılır (telefon Bluetooth klavyedir), sonra onay. */
    async pcYaz(bekle) {
      const nokta = this.pc && this.pc.querySelector(".alan.parola .nokta");
      if (!nokta) return;
      const k = this.kasa.find((x) => x.id === "github");
      const n = Math.min(20, ((k && (k.alanlar.find(([a]) => a === "password") || [])[1]) || "").length || 16);
      for (let i = 1; i <= n; i++) {
        nokta.textContent = "•".repeat(i);
        await bekle(75);
      }
      await bekle(400);
      const imlec = this.pc.querySelector(".alan.parola .imlec"), gir = this.pc.querySelector(".gir"), tik = this.pc.querySelector(".tik");
      if (imlec) imlec.style.visibility = "hidden";
      if (gir) gir.classList.add("tamam");
      if (tik) tik.textContent = "✓ Password typed by the phone";
    }

    /** Fare imleci parola alanına gider ve tıklar; alan odak alır. */
    async pcTikla(bekle) {
      const ok = this.pc && this.pc.querySelector(".ok"), alan = this.pc && this.pc.querySelector(".alan.parola");
      if (!ok || !alan) return;
      const pr = this.pc.getBoundingClientRect(), r = alan.getBoundingClientRect();
      ok.style.left = `${((r.left + r.width * 0.42 - pr.left) / pr.width) * 100}%`;
      ok.style.top = `${((r.top + r.height * 0.55 - pr.top) / pr.height) * 100}%`;
      await bekle(800);
      ok.classList.add("bas");
      await bekle(130);
      ok.classList.remove("bas");
      alan.classList.add("odak");
      const imlec = alan.querySelector(".imlec");
      if (imlec) imlec.style.visibility = "";
    }

    // ── Görünürlük, etkileşim, hareket tercihi ─────────────────────────────
    gozlem() {
      this.gorunur = false;
      if ("IntersectionObserver" in window) {
        this.io = new IntersectionObserver((g) => {
          this.gorunur = g.some((x) => x.isIntersecting);
          this.gorunur ? this.baslatGerekirse() : this.durdur();
        }, { threshold: 0.35 });
        this.io.observe(this);
      } else {
        this.gorunur = true;
        this.baslatGerekirse();
      }
      document.addEventListener("visibilitychange", () => {
        document.hidden ? this.durdur() : this.baslatGerekirse();
      });
    }

    baslatGerekirse() {
      const ad = this.getAttribute("demo");
      if (!ad || !this.gorunur || document.hidden || this.elle || this.oynuyor) return;
      if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
      this.oynuyor = true;
      this.sifirla();
      this.oynat(ad);
    }

    durdur() {
      this.kosu++;
      this.oynuyor = false;
      this.parmak && this.parmak.classList.remove("gor");
      this.pcGizle();
    }

    kullaniciDokundu() {
      // Kullanıcı dokununca demo çekilir; 12 sn dokunulmazsa yeniden başlar.
      if (this.oynuyor) { this.durdur(); }
      this.elle = true;
      clearTimeout(this.elleSayaci);
      this.elleSayaci = setTimeout(() => { this.elle = false; this.baslatGerekirse(); }, 12000);
    }
  }

  // ── Dizüstü: aktar.html'in QR ekranı ──────────────────────────────────────
  // Renkler ve metinler aracın kendisinden (aktar.html yalnız tr/en konuşur).
  // Kareler araçtaki gibi döner; telefon maketiyle yan yana kullanılır.
  const DIZ_CSS = `
:host { display: inline-block; vertical-align: top; direction: ltr; }
/* Çizim yönsüz, ekrandaki araç tr/en (LTR). Sağdan sola sayfada 440 px'lik
   gövde 352 px'lik kutunun SAĞINA yaslanıp sola taşıyordu (ar'da 60 px yatay
   kaydırma); direction: ltr bunu kapatır. */
.lap { position: relative; width: 440px; transform-origin: 0 0; }
.kapak { position: relative; height: 282px; border-radius: 16px 16px 6px 6px; background: #0b0b0c; padding: 13px 12px 14px;
  box-shadow: 0 0 0 1.5px #3b3c40 inset, 0 0 0 1px rgba(255,255,255,.06); }
.kapak::before { content: ""; position: absolute; top: 5px; left: 50%; width: 4px; height: 4px; margin-left: -2px; border-radius: 50%; background: #1f2a38; }
.ekran { width: 100%; height: 100%; border-radius: 3px; overflow: hidden; background: #141414; display: flex; flex-direction: column; }
.taban { position: relative; width: 500px; margin-left: -30px; height: 14px; border-radius: 2px 2px 12px 12px;
  background: linear-gradient(180deg, #dcdbd7 0%, #b3b2ae 55%, #8f8e8a 100%); box-shadow: 0 20px 34px -16px rgba(0,0,0,.65); }
.taban::before { content: ""; position: absolute; top: 0; left: 50%; width: 76px; height: 5px; margin-left: -38px; border-radius: 0 0 6px 6px; background: #a2a19d; }
.krom { height: 24px; flex: none; background: #2a2a2d; display: flex; align-items: center; gap: 5px; padding: 0 8px; }
.krom i { width: 8px; height: 8px; border-radius: 50%; flex: none; }
.krom .adres { flex: 1; margin-left: 8px; height: 15px; border-radius: 8px; background: #1b1b1e; color: #a7a7ac;
  font: 8.5px/15px "Roboto Mono", ui-monospace, monospace; padding: 0 9px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sayfa { flex: 1; padding: 8px 30px 6px; color: #e6e6e6; display: flex; flex-direction: column; align-items: center; gap: 6px; overflow: hidden;
  font: 9.5px/1.4 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
.ust { width: 100%; display: flex; justify-content: space-between; align-items: center; }
.ust b { font-size: 11.5px; }
.ust span { font-size: 8px; border: 1px solid #3a3a3a; border-radius: 4px; padding: 0 5px; background: #1d1d1d; color: #ddd; }
.btn { width: 100%; height: 19px; flex: none; border-radius: 5px; background: #5d9c5b; color: #fff; display: grid; place-items: center; font-weight: 600; font-size: 9px; }
.uyari { color: #d9a640; text-align: center; font-size: 8px; line-height: 1.35; }
.uyari b { color: #f0c46a; font-weight: 700; }
canvas { width: 132px; height: 132px; flex: none; image-rendering: pixelated; background: #fff; border-radius: 4px; padding: 4px; }
.kare { color: #a9a9a9; font-size: 7.5px; text-align: center; line-height: 1.3; }
`;

  class SekuvoDizustu extends HTMLElement {
    connectedCallback() {
      if (this.hazir) return;
      this.hazir = true;
      const el = document.getElementById(this.getAttribute("veri") || "telefon-veri");
      let v = {};
      try { v = el ? JSON.parse(el.textContent) : {}; } catch (_) { v = {}; }
      const a = v.arac || {};
      this.a = a;
      const o = parseFloat(this.getAttribute("olcek")) || 1;
      this.style.width = `${440 * o}px`;
      this.style.height = `${296 * o}px`;
      const r = this.attachShadow({ mode: "open" });
      r.innerHTML = `<style>${DIZ_CSS}</style>
        <div class="lap" style="transform:scale(${o})" role="img" aria-label="${kac(this.getAttribute("aria-label") || "aktar.html")}">
          <div class="kapak"><div class="ekran" dir="ltr">
            <div class="krom"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i>
              <span class="adres">file:///Users/…/Downloads/aktar.html</span></div>
            <div class="sayfa">
              <div class="ust"><b>🔐 ${kac(a.h1 || "Sekuvo")}</b><span>${v.lang === "tr" ? "Türkçe" : "English"} ▾</span></div>
              <div class="btn">${kac(a.btnQr || "")}</div>
              <div class="uyari">${a.uyariQr || ""}</div>
              <canvas></canvas>
              <div class="kare"></div>
            </div>
          </div></div>
          <div class="taban"></div>
        </div>`;
      this.tuval = r.querySelector("canvas");
      this.yazi = r.querySelector(".kare");
      this.toplam = 3;
      this.kare = 0;
      this.ilerle();
      const hareketsiz = matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (hareketsiz) return;
      const basla = () => { if (!this.sayac) this.sayac = setInterval(() => this.ilerle(), 1000); };
      const dur = () => { clearInterval(this.sayac); this.sayac = null; };
      if ("IntersectionObserver" in window) {
        this.io = new IntersectionObserver((g) => (g.some((x) => x.isIntersecting) ? basla() : dur()));
        this.io.observe(this);
      } else basla();
    }
    disconnectedCallback() { clearInterval(this.sayac); this.sayac = null; this.io && this.io.disconnect(); }
    ilerle() {
      this.kare = (this.kare % this.toplam) + 1;
      qrDesen(this.tuval, 57);
      this.yazi.textContent = bicim(this.a.kareCok || "%1$d/%2$d", this.kare, this.toplam, 2);
    }
  }

  const DUR = Symbol("dur");
  if (!customElements.get("sekuvo-telefon")) customElements.define("sekuvo-telefon", SekuvoTelefon);
  if (!customElements.get("sekuvo-dizustu")) customElements.define("sekuvo-dizustu", SekuvoDizustu);
})();

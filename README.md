# QR Code Generator mit Logo

Dies ist ein einfaches QR-Code-Generator-Programm, das mit **Python** und **PyQt5** entwickelt wurde. Das Programm ermöglicht es dir, einen QR-Code basierend auf einer URL oder einem Text zu generieren und in der Mitte des QR-Codes ein benutzerdefiniertes Logo zu platzieren.

## Funktionsübersicht

- Eingabefeld zur Eingabe einer URL oder eines Textes.
- Möglichkeit, ein Logo hochzuladen und es in der Mitte des generierten QR-Codes anzuzeigen.
- Generierung des QR-Codes mit höherer Fehlerkorrektur, um das Logo zu unterstützen.
- Speichern und Anzeigen des QR-Codes in der App.

## Anforderungen

Stelle sicher, dass du die folgenden Python-Bibliotheken installiert hast:

- **PyQt5**: Für die GUI.
- **qrcode[pil]**: Zum Erstellen des QR-Codes.
- **Pillow (PIL)**: Um das Logo auf den QR-Code zu setzen.

Installiere alle benötigten Pakete mit:

```bash
pip install -r requirements.txt

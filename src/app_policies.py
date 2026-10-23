# Erzeugt die Datenschutzerklärungen der Apps: drift/datenschutz/ und instinct/datenschutz/
# Aufruf aus dem Repo-Ordner: python3 src/app_policies.py
import os

MARK = 'M251,118 L116,338 L92,382 L160,350 L184,336 L250,225 L325,352 L270,356 L425,409Z'
MAIL = '<a href="mailto:altitude.built@gmail.com">altitude.built@gmail.com</a>'
STAND = 'Oktober 2026'


def page(title, desc, body, up='../../'):
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title} · Altitude Built</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0E1520">
<link rel="icon" type="image/png" href="{up}Altitude-Built_Zeichen_512.png">
<link rel="stylesheet" href="{up}legal.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{up}" aria-label="Altitude Built, zur Startseite"><svg viewBox="84 110 348 306" aria-hidden="true"><path fill="#F4ECDF" d="{MARK}"/></svg><span>Altitude Built</span></a>
  <a class="back" href="{up}#apps">Zu den Apps</a>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
  <span>© 2026 Altitude Built · Tirol</span>
  <nav aria-label="Rechtliches"><a href="{up}impressum.html">Impressum</a><a href="{up}datenschutz.html">Datenschutz Website</a></nav>
</div></footer>
</body>
</html>
'''


VERANTWORTLICH = f'''  <section>
    <h2>Verantwortlich</h2>
    <dl>
      <dt>Name</dt><dd>Christian Pfeifer (Altitude Built)</dd>
      <dt>Wohnort</dt><dd>Innsbruck, Österreich</dd>
      <dt>E-Mail</dt><dd>{MAIL}</dd>
    </dl>
  </section>'''

PLAY = '''  <section>
    <h2>Google Play</h2>
    <p>Die App wird über Google Play verteilt. Für Installation und Updates verarbeitet Google eigene Daten nach der <a href="https://policies.google.com/privacy">Datenschutzerklärung von Google</a>. Ich erhalte über die Play Console nur zusammengefasste Statistiken (zum Beispiel Anzahl der Installationen) und technische Absturzberichte, die keine Namen oder Kontaktdaten enthalten.</p>
  </section>'''

RECHTE = f'''  <section>
    <h2>Deine Rechte</h2>
    <p>Du hast nach der DSGVO das Recht auf Auskunft (Art. 15), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). Eine erteilte Einwilligung kannst du jederzeit widerrufen. Schreib dafür einfach an {MAIL}.</p>
    <p>Du kannst dich außerdem bei der Aufsichtsbehörde beschweren. In Österreich ist das die Datenschutzbehörde, Barichgasse 40–42, 1030 Wien, <a href="https://www.dsb.gv.at">www.dsb.gv.at</a>.</p>
  </section>

  <section>
    <h2>Änderungen</h2>
    <p>Wenn sich an der App etwas ändert, das den Datenschutz betrifft, wird diese Erklärung angepasst. Es gilt immer die Fassung auf dieser Seite.</p>
  </section>

  <p class="stand">Stand: {STAND}</p>'''

DRIFT = f'''  <div class="eyebrow">Datenschutz · App</div>
  <h1>Drift Weather</h1>
  <p class="lead">Drift braucht kein Konto, enthält kein Tracking und keine Werbung, und Altitude Built betreibt keinen eigenen Server. Damit du Wetterdaten bekommst, schickt die App die Koordinaten deines Orts direkt an Wetterdienste. Was genau passiert, steht hier.</p>

{VERANTWORTLICH}

  <section>
    <h2>Standort</h2>
    <p>Drift fragt nach der Berechtigung für den <strong>ungefähren Standort</strong>. Eine genaue GPS-Position wird nicht verwendet. Die Berechtigung ist freiwillig: Du kannst Orte auch über die Suche hinzufügen. Erlaubst du den Standort, ermittelt dein Handy die ungefähre Position, und die App fragt damit das Wetter für deinen aktuellen Ort ab.</p>
    <p>Rechtsgrundlage ist deine Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), die du in den Android-Einstellungen jederzeit zurücknehmen kannst.</p>
  </section>

  <section>
    <h2>Wetterabfragen</h2>
    <p>Für Vorhersage, Warnungen, Pollen und UV-Index sendet die App die Koordinaten des gewählten Orts an die folgenden Dienste. Dabei sieht der jeweilige Dienst technisch bedingt auch die IP-Adresse deines Geräts. Name, Konto oder Geräte-Kennungen werden nicht übertragen.</p>
    <ul>
      <li><strong>GeoSphere Austria</strong> (Wien): Vorhersage und amtliche Warnungen, <a href="https://www.geosphere.at">geosphere.at</a></li>
      <li><strong>Deutscher Wetterdienst</strong> über den Dienst <strong>Bright Sky</strong>: Vorhersage, <a href="https://brightsky.dev">brightsky.dev</a></li>
      <li><strong>Open-Meteo</strong>: Vorhersage, Modellvergleich, Pollen, Zeitzonen und Nullgradgrenze, <a href="https://open-meteo.com">open-meteo.com</a></li>
      <li><strong>currentuvindex.com</strong>: UV-Index, <a href="https://currentuvindex.com">currentuvindex.com</a></li>
      <li>In Testversionen gegebenenfalls weitere Wetterdienste, die dort zur Erprobung eingebunden sind</li>
    </ul>
    <p>Welche Dienste abgefragt werden, hängt vom Ort und von deinen Einstellungen ab. Damit Widgets und Hinweise aktuell bleiben, macht die App diese Abfragen auch regelmäßig im Hintergrund. Wie die Dienste mit den Anfragen umgehen, regeln ihre eigenen Datenschutzbestimmungen.</p>
    <p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, weil die Abfragen nötig sind, um dir das Wetter für deine Orte anzuzeigen.</p>
  </section>

  <section>
    <h2>Ortssuche</h2>
    <p>Für die Ortssuche und für Ortsnamen nutzt Drift den Ortsdienst deines Android-Geräts. Auf den meisten Geräten wird er von den Google Play-Diensten bereitgestellt. Dabei gehen dein Suchbegriff oder die Koordinaten an Google, siehe <a href="https://policies.google.com/privacy">Datenschutzerklärung von Google</a>.</p>
  </section>

  <section>
    <h2>Auf deinem Gerät</h2>
    <p>Orte, Profile, Einstellungen und zwischengespeicherte Wetterdaten speichert die App nur auf deinem Gerät. Hinweise wie die Regenwarnung oder der Vorabend-Hinweis werden am Gerät berechnet und als lokale Mitteilung angezeigt. Es gibt keinen Push-Server.</p>
    <p>Wenn du in Android die Sicherung in deinem Google-Konto eingeschaltet hast, kann Android diese App-Daten dort mitsichern. Das steuerst du in den Android-Einstellungen.</p>
    <p>Teilst du eine Wetterkarte, öffnet sich das Teilen-Menü von Android, und du entscheidest selbst, an welche App sie geht.</p>
    <p>Wenn du die App deinstallierst, werden diese Daten von deinem Gerät gelöscht.</p>
  </section>

{PLAY}

{RECHTE}'''

INSTINCT = f'''  <div class="eyebrow">Datenschutz · App</div>
  <h1>Instinct</h1>
  <p class="lead">Instinct hat keine Berechtigung für den Internet-Zugriff. Android lässt die Tastatur deshalb keine Verbindung ins Internet aufbauen. Alles, was du tippst, wird ausschließlich auf deinem Gerät verarbeitet.</p>

{VERANTWORTLICH}

  <section>
    <h2>Was die Tastatur verarbeitet</h2>
    <p>Wie jede Tastatur bekommt Instinct mit, was du tippst. Android weist beim Aktivieren darauf hin. Instinct braucht diese Eingaben, um Wörter zu erkennen, zu korrigieren und vorzuschlagen. Die Verarbeitung passiert auf deinem Gerät, nichts davon wird an Altitude Built oder an andere geschickt.</p>
    <p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, weil die Verarbeitung für die Funktion der Tastatur nötig ist.</p>
  </section>

  <section>
    <h2>Was auf deinem Gerät gespeichert wird</h2>
    <ul>
      <li><strong>Meine Wörter:</strong> Wörter und Wortfolgen, die Instinct von dir lernt. Du kannst sie in der App ansehen und löschen.</li>
      <li><strong>Tipp-Modell:</strong> wo du die Tasten typischerweise triffst, damit die Erkennung zu deinen Fingern passt.</li>
      <li><strong>Statistik:</strong> wie oft Instinct richtig lag und welche Wörter du häufig verwendest.</li>
      <li><strong>Zwischenablage:</strong> zuletzt kopierte Texte und angeheftete Einträge. Inhalte, die Android als vertraulich kennzeichnet, etwa aus Passwort-Managern, werden nicht übernommen.</li>
      <li><strong>Einstellungen</strong> wie Theme, Tastenstil und ein eigenes Hintergrundfoto, wenn du eines auswählst.</li>
    </ul>
  </section>

  <section>
    <h2>Wo Instinct nichts lernt</h2>
    <ul>
      <li>In Passwort-Feldern sowie in Feldern für E-Mail- und Internetadressen</li>
      <li>In Feldern, in denen eine App personalisiertes Lernen abschaltet, zum Beispiel in privaten Browser-Tabs</li>
      <li>Wenn du den Inkognito-Modus der Tastatur einschaltest</li>
    </ul>
  </section>

  <section>
    <h2>Sicherung</h2>
    <p>Damit Gelerntes bei einem neuen Handy oder einer Neuinstallation nicht verloren geht, gibt es zwei Wege:</p>
    <ul>
      <li><strong>Android-Sicherung:</strong> Wenn du in Android die Sicherung in deinem Google-Konto oder die Übertragung auf ein neues Gerät nutzt, nimmt Android Meine Wörter, Tipp-Modell, Statistik und Einstellungen mit. Das steuerst du in den Android-Einstellungen.</li>
      <li><strong>Sicherungsdatei:</strong> Nur wenn du in der App auf „Jetzt sichern“ tippst, legt Instinct im Ordner Dokumente/Instinct auf deinem Gerät die Datei instinct-sicherung.txt an. Sie bleibt auch nach dem Deinstallieren erhalten, damit du Gelerntes wiederherstellen kannst. Du kannst sie jederzeit löschen. Andere Apps mit Zugriff auf deine Dateien können sie lesen.</li>
    </ul>
  </section>

  <section>
    <h2>Mess-Modus</h2>
    <p>Der Mess-Modus ist standardmäßig ausgeschaltet. Schaltest du ihn ein, zeichnet Instinct für jedes Wort die Tipp-Positionen und das Ergebnis auf, damit sich die Erkennung verbessern lässt. Die Aufzeichnung bleibt auf deinem Gerät und kommt nie in eine Sicherung. Sie verlässt das Gerät nur, wenn du sie selbst als Datei exportierst und weitergibst.</p>
  </section>

  <section>
    <h2>Berechtigungen</h2>
    <p>Instinct verwendet nur die Berechtigung für die Vibration beim Tippen. Es gibt keinen Zugriff auf Internet, Standort, Kontakte, Kamera oder Mikrofon.</p>
    <p>Wenn du die App deinstallierst, werden alle Daten von deinem Gerät gelöscht, außer einer Sicherungsdatei, die du selbst im Ordner Dokumente/Instinct angelegt hast.</p>
  </section>

{PLAY}

{RECHTE}'''

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for slug, title, body in [('drift', 'Datenschutz Drift Weather', DRIFT), ('instinct', 'Datenschutz Instinct', INSTINCT)]:
    d = os.path.join(root, slug, 'datenschutz'); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(page(title, f'Datenschutzerklärung der App {title.split(" ", 1)[1]} von Altitude Built.', body))
    print('ok', slug)

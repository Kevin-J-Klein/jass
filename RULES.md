# Jass-Regeln (Schieber)

Diese Datei ist die **verbindliche Spezifikation** der Regeln. Claude Code und alle
Tests richten sich danach. Wo etwas fehlt oder unklar ist, wird gefragt, nicht geraten.

> **Kevin:** Fülle alle Stellen mit `TODO` aus. Schreib die Regeln so, wie ihr sie
> spielt, auch wenn andere es anders machen. Je konkreter, desto besser:
> Beispiele mit echten Karten helfen dem Agenten und werden direkt zu Tests.

## 1. Spieler und Teams

- 4 Spieler, 2 Teams. Partner sitzen sich gegenüber.
- Gespielt wird im Gegenuhrzeigersinn.
- TODO: Wer gibt in der ersten Runde? Wie wechselt der Geber?

## 2. Karten

36 Karten in 4 Farben mit je 9 Karten.

| Deutschschweizer Karten | Französische Karten |
| --- | --- |
| Eicheln | TODO |
| Rosen | TODO |
| Schellen | TODO |
| Schilten | TODO |

Werte pro Farbe, von hoch nach tief (ohne Trumpf): Ass, König, Ober, Under, Banner, 9, 8, 7, 6

- TODO: Bezeichnungen der französischen Karten (Dame, Bube, 10 …) ergänzen

## 3. Ablauf einer Runde

1. Karten mischen und je 9 Karten verteilen.
2. TODO: Wer bestimmt den Trumpf? (z.B. in der ersten Runde, wer die Rosen 7 hat?)
3. Der Ansager wählt einen Trumpf oder **schiebt** zum Partner, der dann wählen muss.
   - TODO: Darf der Partner zurückschieben?
4. Wer beginnt mit dem ersten Stich?
   - TODO
5. 9 Stiche werden gespielt, danach wird gezählt.

## 4. Trumpfarten

- Eine der vier Farben als Trumpf
- **Obenabe:** kein Trumpf, die höchste Karte der ausgespielten Farbe gewinnt
- **Undenufe:** kein Trumpf, die tiefste Karte der ausgespielten Farbe gewinnt
- TODO: Weitere Arten (z.B. Slalom) vorerst nicht, oder doch?

## 5. Reihenfolge der Trumpfkarten

Von hoch nach tief: Under (Puur), Nell (9), Ass, König, Ober, Banner, 8, 7, 6

- TODO: bestätigen oder korrigieren

## 6. Spielregeln im Stich

- **Farbe angeben:** Wer die ausgespielte Farbe hat, muss sie spielen.
  - Ausnahme: Man darf jederzeit Trumpf spielen, auch wenn man Farbe hätte.
  - TODO: bestätigen
- **Under-Regel:** Wird Trumpf ausgespielt und man hat als einzigen Trumpf den Under,
  muss man ihn nicht spielen.
  - TODO: bestätigen
- **Untertrumpfen:** Liegt bereits ein Trumpf im Stich, darf man keinen tieferen
  Trumpf spielen, ausser man hat nichts anderes.
  - TODO: bestätigen, und gilt es auch, wenn man die ausgespielte Farbe hätte?
- **Stich gewinnen:** Der höchste Trumpf gewinnt. Ohne Trumpf im Stich gewinnt die
  höchste Karte der ausgespielten Farbe (bei Undenufe die tiefste).
- Wer den Stich gewinnt, spielt den nächsten aus.

## 7. Kartenwerte (Punkte)

| Karte | Trumpffarbe | Andere Farbe | Obenabe | Undenufe |
| --- | --- | --- | --- | --- |
| Ass | 11 | 11 | 11 | 0 |
| König | 4 | 4 | 4 | 4 |
| Ober | 3 | 3 | 3 | 3 |
| Under | 20 | 2 | 2 | 2 |
| Banner (10) | 10 | 10 | 10 | 10 |
| 9 | 14 | 0 | 0 | 0 |
| 8 | 0 | 0 | 8 | 8 |
| 7 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 11 |

- Letzter Stich: 5 Punkte
- Match (alle 9 Stiche): 100 Bonuspunkte, also 257 statt 157
- Summe pro Runde: 157 Punkte (152 Karten + 5 letzter Stich)
- TODO: Tabelle prüfen

## 8. Einstellungen pro Spielraum

| Einstellung | Optionen | Standard |
| --- | --- | --- |
| Kartenbild | deutsch, französisch | TODO |
| Trumpf-Faktoren | an, aus | aus |
| Zielpunktzahl | frei wählbar | 1000 |

Faktoren, wenn eingeschaltet:

| Trumpfart | Faktor |
| --- | --- |
| TODO | ×1 |
| TODO | ×2 |
| Obenabe, Undenufe | TODO |

## 9. Spielende

- Das Team, das zuerst die Zielpunktzahl erreicht, gewinnt.
- TODO: Wird sofort bedankt (mitten in der Runde), oder erst am Rundenende gezählt?
- TODO: Was passiert, wenn beide Teams in derselben Runde über die Zielpunktzahl kommen?

## 10. Später (nicht im MVP)

- Weis (Drei-, Vier-, Fünfblatt, Vier Gleiche …)
- Stöck (König und Ober im Trumpf)
- Weitere Varianten wie Differenzler oder Coiffeur

## 11. Beispiele

Konkrete Situationen, die zu Tests werden. Format: Trumpf, gespielte Karten der Reihe
nach, erwarteter Gewinner des Stichs.

1. Trumpf Rosen. Gespielt: Eicheln Ass, Eicheln König, Rosen 6, Eicheln 9.
   Gewinner: Rosen 6 (Trumpf schlägt Farbe).
2. Obenabe. Gespielt: Schellen 8, Schellen Ass, Rosen Ass, Schellen 10.
   Gewinner: Schellen Ass (Rosen ist nicht die ausgespielte Farbe).
3. TODO: eigene Beispiele, besonders für Grenzfälle wie Untertrumpfen und Under-Regel

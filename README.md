# Menù di Ferragosto · Sacconi Road, Maltignano

Sito statico a pagina singola con il menù di Ferragosto e il QR code per aprirlo dal tavolo.

## Contenuto

| File | Cosa fa |
| --- | --- |
| `index.html` | Il menù: hero, sei portate con foto, sezione QR |
| `qr.html` | Cartoncino da stampare con il solo QR code (formato 5:7, ~105 mm in stampa) |
| `assets/*.jpg` | Foto delle portate (1200×900) e foto di Sacconi Road usata come sfondo in trasparenza |
| `assets/qr-menu.svg` / `.png` | QR code (correzione errore H) verso la pagina pubblicata |

## Le portate

1. Affettati misti con fichi caramellati
2. Chichì
3. Cacciannanz
4. Porchettina di pancia croccante con salse verde, rossa e gialla
5. Misticanza di stagione con citronette
6. Verdure alla brace

## Pubblicazione (GitHub Pages)

Il QR punta a `https://g95g95.github.io/menu-ferragosto-maltignano/`.

Il deploy è automatico via GitHub Actions (`.github/workflows/pages.yml`): parte a ogni push su
`main` e pubblica la root del repo. Lo si può lanciare anche a mano dalla tab Actions
(«Run workflow»).

Il deploy gira solo da `main` perché l'environment `github-pages` autorizza il solo branch di
default: le modifiche vanno quindi unite in `main` per andare online.

Se l'indirizzo cambia (dominio proprio, altro host), rigenera il QR con:

```bash
pip install qrcode pillow
python3 tools/make_qr.py "https://nuovo-indirizzo/"
```

## Anteprima locale

```bash
python3 -m http.server 8000
# poi apri http://localhost:8000
```

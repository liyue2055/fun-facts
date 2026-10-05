#!/usr/bin/env python3
"""Build a self-contained fun-facts HTML page with embedded images."""
import base64, os

ROOT = os.path.expanduser("~/workspace/fun-facts")
IMG = os.path.join(ROOT, "images")

FACTS = [
    ("00-berries", "Bananas are berries, but strawberries aren\u2019t.",
     "Botanically, a berry is defined by how it develops from a flower. Bananas qualify; strawberries technically don\u2019t."),
    ("01-brain", "Your brain itself can\u2019t feel pain.",
     "The brain has no pain receptors. Headaches happen because surrounding tissues\u2014blood vessels, nerves, muscles, and membranes\u2014can generate pain."),
    ("02-moon", "The \u201cdark side\u201d of the Moon isn\u2019t actually always dark. \U0001f319",
     "The Moon rotates, so both sides receive sunlight. The far side is simply the side we don\u2019t normally see from Earth."),
    ("03-venus", "A day on Venus is longer than a year on Venus.",
     "Venus takes about 243 Earth days to rotate once, but only about 225 Earth days to orbit the Sun."),
    ("04-height", "You\u2019re slightly taller in the morning.",
     "While you sleep, the discs between your vertebrae decompress. During the day, gravity compresses them again, so you can be roughly 1\u20132 cm shorter by evening."),
    ("05-cleopatra", "Cleopatra lived closer to the Moon landing than to the construction of the Great Pyramid.",
     "The Great Pyramid was built around 2560 BCE. Cleopatra lived around 69\u201330 BCE, while humans landed on the Moon in 1969 CE."),
    ("06-eiffel", "The Eiffel Tower changes height.",
     "When heated by the Sun, the iron expands. Its height can increase by roughly 15 cm under strong temperature changes."),
    ("07-senses", "You have more than five senses.",
     "Balance, temperature, pain, body position (proprioception), and internal sensations such as hunger are generally considered additional senses."),
    ("08-oxford", "Oxford University is older than the Aztec Empire.",
     "Teaching existed at Oxford by around 1096. The Aztec Empire emerged centuries later, in the 15th century."),
    ("09-cloud", "A cloud can weigh hundreds of thousands of kilograms. \u2601\ufe0f",
     "A typical cumulus cloud can contain hundreds of tons of water\u2014but spread over a huge volume, with tiny droplets suspended in air."),
    ("10-chess", "There are more possible chess games than atoms in the observable universe.",
     "The number of possible chess game sequences is estimated at around 10<sup>120</sup>, vastly exceeding estimates of roughly 10<sup>80</sup> atoms in the observable universe."),
    ("11-petrichor", "The smell after rain has a name: petrichor.",
     "That earthy smell comes partly from compounds released by soil and plants, including a molecule called geosmin."),
    ("12-blindspot", "Your eyes have a blind spot, but you usually don\u2019t notice it.",
     "That\u2019s where the optic nerve leaves the eye, creating a small area with no photoreceptors. Your brain fills in the missing information."),
    ("13-mpemba", "Hot water can sometimes freeze faster than cold water.",
     "This is known as the Mpemba effect. It can occur under particular conditions, although it isn\u2019t universal and scientists still study exactly which mechanisms dominate."),
    ("14-tickle", "The reason you can\u2019t tickle yourself is actually fascinating.",
     "Your brain predicts the sensory consequences of your own movements and reduces the response to sensations it expects. Basically, your brain says, \u201cYeah, I know you\u2019re doing that.\u201d \U0001f604"),
]

def img_tag(slug):
    p = os.path.join(IMG, slug + ".png")
    if not os.path.exists(p):
        return '<div class="noimg"></div>'
    b64 = base64.b64encode(open(p, "rb").read()).decode()
    return f'<img src="data:image/png;base64,{b64}" alt="" loading="lazy">'

cards = []
for i, (slug, title, text) in enumerate(FACTS, 1):
    cards.append(f"""<article class="card">
      <div class="pic">{img_tag(slug)}</div>
      <div class="body">
        <div class="num">{i:02d}</div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
    </article>""")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>15 things you (probably) didn't know</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: Georgia, 'Times New Roman', serif; background: #f7f2e9; color: #2b2620; margin: 0; padding: 0; }}
  header {{ text-align: center; padding: 56px 20px 32px; }}
  header h1 {{ font-size: 2.2rem; margin: 0 0 8px; letter-spacing: -0.5px; }}
  header p {{ color: #8a7f6d; font-style: italic; margin: 0; }}
  main {{ max-width: 860px; margin: 0 auto; padding: 0 20px 64px; }}
  .card {{ display: flex; gap: 24px; background: #fffdf8; border: 1px solid #e8dfcd; border-radius: 14px; margin: 22px 0; overflow: hidden; box-shadow: 0 2px 10px rgba(90,70,40,.06); }}
  .card:nth-child(even) {{ flex-direction: row-reverse; }}
  .pic {{ flex: 0 0 300px; min-height: 220px; }}
  .pic img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
  .noimg {{ width: 100%; height: 100%; background: #e8dfcd; }}
  .body {{ padding: 22px 26px 22px 4px; flex: 1; }}
  .card:nth-child(even) .body {{ padding: 22px 4px 22px 26px; }}
  .num {{ font-size: .8rem; color: #b39b6d; letter-spacing: 2px; }}
  h2 {{ font-size: 1.25rem; margin: 6px 0 10px; line-height: 1.35; }}
  p {{ margin: 0; line-height: 1.65; color: #4d4436; }}
  sup {{ font-size: .65em; }}
  footer {{ text-align: center; color: #8a7f6d; font-size: .85rem; padding-bottom: 40px; font-style: italic; }}
  @media (max-width: 640px) {{
    .card, .card:nth-child(even) {{ flex-direction: column; }}
    .pic {{ flex: none; height: 220px; }}
    .body, .card:nth-child(even) .body {{ padding: 4px 22px 22px; }}
  }}
</style>
</head>
<body>
<header>
  <h1>15 things you (probably) didn&rsquo;t know</h1>
  <p>A little illustrated cabinet of curiosities</p>
</header>
<main>
{''.join(cards)}
</main>
<footer>Made with curiosity &mdash; illustrations generated for each fact.</footer>
</body>
</html>"""

out = os.path.join(os.path.join(ROOT, "site", "index.html"))
open(out, "w").write(html)
print(f"wrote {out} ({os.path.getsize(out)//1024} KB)")

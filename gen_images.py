import base64, json, os, sys, time
sys.path.insert(0, os.path.expanduser("~/workspace/skills/meta-model-api/bin"))
from _client import post

STYLE = "Flat vector editorial illustration, bold minimalist style, warm muted palette, almost no text in the image. "

FACTS = [
    ("berries", "Banana plant with a botanical cross-section showing berry structure, strawberries beside it crossed out subtly"),
    ("brain", "Glowing human brain floating serenely while pain signals bounce off it, nerves and vessels around it lit up instead"),
    ("moon", "The Moon rotating in space with sunlight hitting both the near side and far side, Earth small in the distance"),
    ("venus", "Planet Venus with a very slow rotation arrow around it and a faster orbit arrow around the Sun"),
    ("height", "Side-by-side silhouette of a person measured tall in the morning sun and slightly shorter at night, spine highlighted"),
    ("cleopatra", "Timeline illustration: Egyptian pyramid, then Cleopatra, then a Moon rocket — pyramid far from Cleopatra, rocket close"),
    ("eiffel", "The Eiffel Tower with visible heat shimmer waves, subtly stretching taller under a hot sun"),
    ("senses", "Human head silhouette with icons radiating: balance, thermometer, pain, body position, hunger"),
    ("oxford", "Medieval Oxford college building beside an Aztec stepped pyramid, Oxford glowing older on a timeline"),
    ("cloud", "A giant fluffy cumulus cloud with a heavy weight label, tiny water droplets visible, vast sky"),
    ("chess", "A chessboard dissolving into a starry cosmos, infinite game paths branching like galaxies"),
    ("petrichor", "Rain drops hitting dry soil, earthy scent swirls rising, close-up of soil and a sprout"),
    ("blindspot", "Close-up of a human eye with the optic nerve exit point marked, brain filling in the gap with imagined detail"),
    ("mpemba", "Two glasses side by side, one steaming hot and one cold, the hot one forming ice crystals first"),
    ("tickle", "A playful brain character shrugging while a hand tries to tickle a laughing person, prediction lines from brain to hand"),
]

out = os.path.expanduser("~/workspace/fun-facts/images")
for i, (slug, desc) in enumerate(FACTS):
    path = os.path.join(out, f"{i:02d}-{slug}.png")
    if os.path.exists(path):
        print(f"skip {slug} (exists)"); continue
    print(f"[{i+1}/15] {slug}...", flush=True)
    try:
        data = post("/images/generations", {"model": "muse-image-1.0", "prompt": STYLE + desc, "size": "1536x864"})
        with open(path, "wb") as f:
            f.write(base64.b64decode(data["data"][0]["b64_json"]))
        print(f"  saved {os.path.getsize(path)//1024} KB")
    except Exception as e:
        print(f"  FAILED: {e}")
    time.sleep(2)
print("done")

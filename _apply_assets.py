import os, shutil
from PIL import Image, ImageDraw
os.chdir(r"C:\Users\Mihai\Desktop\concurs")
shutil.copy("index.html", "index.v3-backup.html")

# hero background: hero-alt.jpg -> 1920 wide optimized
im = Image.open("assets/hero-alt.jpg").convert("RGB")
cream = im.getpixel((20, 20))
w = 1920
im = im.resize((w, round(im.size[1] * w / im.size[0])), Image.LANCZOS)
im.save("assets/hero-bg.jpg", quality=74, optimize=True, progressive=True)
cream_hex = "#%02X%02X%02X" % cream

# logo: first icon of logo.jpg, rounded, transparent corners
lg = Image.open("assets/logo.jpg").convert("RGB")
W, H = lg.size
box = (int(W * 0.048), int(H * 0.365), int(W * 0.205), int(H * 0.645))
c = lg.crop(box)
s = min(c.size)
c = c.crop(((c.size[0] - s) // 2, (c.size[1] - s) // 2, (c.size[0] + s) // 2, (c.size[1] + s) // 2)).resize((128, 128), Image.LANCZOS)
m = Image.new("L", (128, 128), 0)
ImageDraw.Draw(m).rounded_rectangle((0, 0, 127, 127), radius=30, fill=255)
c = c.convert("RGBA"); c.putalpha(m)
c.save("assets/logo.png", optimize=True)

# aside illustration: centre of social.jpg
so = Image.open("assets/social.jpg").convert("RGB")
W, H = so.size
so = so.crop((int(W * 0.18), int(H * 0.08), int(W * 0.84), int(H * 0.92))).resize((720, round(720 * (H * 0.84) / (W * 0.66))), Image.LANCZOS)
so.save("assets/aside.jpg", quality=78, optimize=True, progressive=True)

s = open("index.html", encoding="utf-8").read()
n0 = len(s)

def rep(a, b):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b, 1)

# favicon + logo
rep("href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%2314284B'/%3E%3Cpath d='M4 22h24M7 22a9 9 0 0 1 18 0' stroke='%23F2A33A' stroke-width='2.5' fill='none'/%3E%3C/svg%3E\"", "type=\"image/png\" href=\"assets/logo.png\"")
a = s.index('<svg width="28" height="28"'); b = s.index("</svg>", a) + 6
s = s[:a] + '<img src="assets/logo.png" width="28" height="28" alt="">' + s[b:]

# hero CSS
rep(".hero{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,72px);align-items:center;padding:clamp(36px,6vw,84px) 0}",
    ".hb{background:%s url(assets/hero-bg.jpg) right center/cover no-repeat;min-height:clamp(420px,44vw,640px);display:flex;align-items:center}.hero{padding:clamp(36px,6vw,84px) clamp(18px,4vw,48px);width:100%%}.hero>div{max-width:min(560px,48%%)}.ex{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,72px);align-items:center}.ex h2{margin-bottom:12px}.ex img{width:100%%;border-radius:10px;border:1px solid var(--line);margin-bottom:18px}.ex p{max-width:32em}" % cream_hex)
rep(".aside h3{font-size:1.1rem;margin-bottom:10px}", ".aside h3{font-size:1.1rem;margin-bottom:10px}.aside img{width:100%;border-radius:10px;border:1px solid var(--line);margin-bottom:18px}")
rep("@media(max-width:900px){.hero,.fg,.rg{grid-template-columns:1fr}",
    "@media(max-width:900px){.hb{background-size:175% auto;background-position:78% 100%}.hero{padding-bottom:50vw}.hero>div{max-width:none}.ex{grid-template-columns:1fr}.fg,.rg{grid-template-columns:1fr}")

# hero markup: text in image hero, sample brief moves to its own section
a = s.index('<div class="w hero">'); b = s.index('<div class="dark">')
old = s[a:b]
p0 = old.index('<div class="plate">')
text = old[len('<div class="w hero">'):p0]
plate = old[p0:]
plate = plate[:plate.rindex("</div></div>")] + "</div>"  # drop hero wrapper close
new = ('<div class="hb"><div class="w hero">' + text + '</div></div>'
       '<div class="w sec ex"><div class="plate-wrap">' + plate + '</div><div><h2>Așa arată rezultatul</h2>'
       '<p>Un brief de o pagină cu faptele oficiale, argumentul pentru rolul ales și suma pusă în context, fiecare cifră cu sursa ei. Exemplul din stânga este calculat pentru o companie fictivă.</p>'
       '<div class="row"><button class="btn p" id="go2">Încearcă cu exemplul</button></div></div></div>')
s = s[:a] + new + s[b:]

# aside image on form screen
rep('<div class="aside"><h3>Ce primești</h3>', '<div class="aside"><img src="assets/aside.jpg" alt="" width="720" loading="lazy"><h3>Ce primești</h3>')
# JS
rep('$("go").onclick=()=>show(1);', '$("go").onclick=()=>show(1);$("go2").onclick=()=>{show(1);$("ex1").click()};')

open("index.html", "w", encoding="utf-8").write(s)
print("ok", n0, len(s), cream_hex)
for f in ("hero-bg.jpg", "logo.png", "aside.jpg"):
    print(f, os.path.getsize("assets/" + f))

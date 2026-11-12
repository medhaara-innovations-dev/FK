import json
from ok import *
P=json.load(open('palette.json')); R=P['ramps']; RO=P['roles']
def g(r,s): return next(x['hex'] for x in R[r] if x['step']==s)
def H(k): return RO[k]['hex']
FONT='/usr/share/fonts/truetype/sand-box/google'
CSS=f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1440px;background:#fff;font-family:Mulish,sans-serif;color:{H('text-secondary')};padding:64px 72px 72px;font-size:15px;line-height:1.5}}
h1{{font:800 40px/1.15 Poppins;color:{H('text-heading')};letter-spacing:-.01em}}
h2{{font:700 22px/1.3 Poppins;color:{H('text-heading')};margin:44px 0 6px}}
h3{{font:700 16px/1.3 Poppins;color:{H('text-primary')}}}
.eyebrow{{font:700 12px/1 Mulish;letter-spacing:.12em;text-transform:uppercase;color:{H('text-link')};margin-bottom:12px}}
.lead{{font-size:17px;max-width:900px;margin-top:12px}}
.sub{{font-size:14px;color:{H('text-muted')};margin-bottom:16px;max-width:1000px}}
.ramp{{display:grid;gap:8px}}
.sw{{border-radius:14px;overflow:hidden;border:1px solid {g('neutral',200)};background:#fff;position:relative}}
.chip{{height:120px;padding:10px 12px;display:flex;flex-direction:column;justify-content:space-between}}
.chip .st{{font:700 15px/1 Poppins}}
.chip .cr{{font:600 12px/1.3 Mulish}}
.meta{{padding:10px 12px 12px}}
.meta .hx{{font:700 14px/1.2 Poppins;color:{H('text-primary')}}}
.meta .nm{{font-size:12px;color:{H('text-muted')};margin-top:3px;line-height:1.35}}
.doc{{position:absolute;top:8px;right:8px;font:800 12px/1 Mulish;padding:4px 7px;border-radius:99px;background:{g('lime',100)};color:{g('primary',950)};border:1px solid {g('lime',400)}}}
.row{{display:flex;gap:24px}}
.card{{border:1px solid {g('neutral',200)};border-radius:18px;padding:20px 22px;background:#fff}}
.note{{background:{g('primary',50)};border:1px solid {g('primary',100)};border-radius:18px;padding:20px 24px}}
.note b{{color:{H('text-primary')}}}
ul.c{{padding-left:18px}} ul.c li{{margin:4px 0}}
table{{border-collapse:collapse;width:100%}}
td,th{{text-align:left;padding:9px 10px;border-bottom:1px solid {g('neutral',200)};font-size:14px;vertical-align:middle}}
th{{font:700 12px/1.2 Mulish;letter-spacing:.06em;text-transform:uppercase;color:{H('text-muted')}}}
.mini{{display:inline-block;width:22px;height:22px;border-radius:6px;vertical-align:middle;border:1px solid rgba(5,0,17,.12);margin-right:8px}}
.pass{{font:800 12px/1 Mulish;padding:4px 8px;border-radius:99px;background:{g('success',100)};color:{g('success',700)}}}
.fail{{font:800 12px/1 Mulish;padding:4px 8px;border-radius:99px;background:{g('error',100)};color:{g('error',700)}}}
.mono{{font-family:'DejaVu Sans Mono',monospace;font-size:12px}}
.rt td{{padding:7px 5px;font-size:13px}}
"""
def txtc(h): return '#FFFFFF' if cr(h,'#FFFFFF')>=cr(h,'#050011') else '#050011'
def swatch(r,s,label=None):
    h=s['hex']; t=txtc(h)
    best=f"{s['cw']}:1 on white" if t=='#050011' else f"{s['cw']}:1 white text"
    return f"""<div class="sw">{'<span class="doc">DOC</span>' if s['doc'] else ''}<div class="chip" style="background:{h};color:{t}"><span class="st">{label or s['step']}</span><span class="cr">{best}<br>L {s['L']:.2f} · C {s['C']:.2f}</span></div>
<div class="meta"><div class="hx">{h}</div><div class="nm">{r}-{s['step']}{'<br>'+s['doc'] if s['doc'] else ''}</div></div></div>"""
def ramprow(r,cols=None):
    st=R[r]; n=len(st)
    return f'<div class="ramp" style="grid-template-columns:repeat({cols or n},1fr)">'+''.join(swatch(r,s) for s in st)+'</div>'
def Lchart(series,w=1296,h=220):
    # series: list of (label,color,[(x_label,L)],dash)
    labels=series[0][2]; n=len(labels); pad=48
    xs=lambda i:pad+i*(w-2*pad)/(n-1); ys=lambda L:h-30-(L)*(h-50)
    svg=[f'<svg width="{w}" height="{h}" style="display:block">']
    for L in (0,.25,.5,.75,1):
        svg.append(f'<line x1="{pad}" x2="{w-pad}" y1="{ys(L)}" y2="{ys(L)}" stroke="{g("neutral",200)}"/><text x="8" y="{ys(L)+4}" font-size="12" fill="{H("text-muted")}" font-family="Mulish">L {L}</text>')
    for lab,col,pts,dash in series:
        idx={l:i for i,(l,_) in enumerate(labels)}
        path=' '.join(f"{'M' if j==0 else 'L'}{xs(p[2] if len(p)>2 else idx[p[0]])},{ys(p[1])}" for j,p in enumerate(pts))
        svg.append(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="3" {"stroke-dasharray=\"7 6\"" if dash else ""}/>')
        for p in pts:
            x=xs(p[2] if len(p)>2 else idx[p[0]]); svg.append(f'<circle cx="{x}" cy="{ys(p[1])}" r="6" fill="#fff" stroke="{col}" stroke-width="3"/>')
            if dash: svg.append(f'<text x="{x+9 if x<w-120 else x-70}" y="{ys(p[1])-9}" font-size="12" font-weight="700" fill="{col}" font-family="Mulish">{p[3]}</text>')
    for i,(l,_) in enumerate(labels):
        svg.append(f'<text x="{xs(i)}" y="{h-8}" font-size="12" text-anchor="middle" fill="{H("text-muted")}" font-family="Mulish" font-weight="700">{l}</text>')
    svg.append('</svg>'); return ''.join(svg)
def page(name,body):
    open(f'html/{name}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
import os; os.makedirs('html',exist_ok=True)

# ---------- 01 PRIMARY ----------
pr=R['primary']
newpts=[(str(s['step']),s['L']) for s in pr]
docs=[('#EBE6F7','10',.934),('#AC9FCC','25',.729),('#2D0B84','Main',.313),('#3D2184','75',.352),('#130438','100',.183)]
# doc points placed at x index of nearest new step by L
def nearest(L): return min(range(len(pr)),key=lambda i:abs(pr[i]['L']-L))
docpts=[(None,L,i*2.5,f'doc {lab}') for i,(h,lab,L) in enumerate(docs)]
docrow=''.join(f'<div class="sw"><div class="chip" style="background:{h};color:{txtc(h)}"><span class="st">{lab}</span><span class="cr">L {hex2oklch(h)[0]:.2f}</span></div><div class="meta"><div class="hx">{h}</div><div class="nm">{m}</div></div></div>' for h,lab,m in
 [('#EBE6F7','10','→ primary-100 (kept)'),('#AC9FCC','25','→ replaced by 300/400 (it was greyer than the ramp)'),('#2D0B84','Main','→ primary-800 (kept, headings)'),('#3D2184','75','→ removed: lighter than Main, out of order'),('#130438','100','→ primary-950 (kept)')])
page('01-primary',f"""<div class="eyebrow">FamilyKit palette · 01</div><h1>Primary · Royal Purple</h1>
<p class="lead">One 11-step ramp built in OKLCH around the brand purple <b>#2D0B84</b>. Each step is an even jump in lightness, so 100→200 feels the same size as 700→800. Steps marked <b>DOC</b> are the exact original values.</p>
<h2>New ramp</h2><p class="sub">Contrast shown is against white (dark text on light swatches, white text on dark swatches). 600 and darker pass 4.5:1 with white, so they're safe for text and buttons.</p>
{ramprow('primary')}
<h2>What the doc had</h2><p class="sub">The doc's 5 steps weren't in order. "75" (#3D2184) is lighter than "Main", and "25" was much greyer than the rest.</p>
<div class="ramp" style="grid-template-columns:repeat(5,1fr)">{docrow}</div>
<h2>Lightness check (OKLCH L)</h2><p class="sub">Solid line: new ramp, evenly stepped. Dashed orange: the doc's 5 steps in their stated order (10, 25, Main, 75, 100). The line goes back up at "75", which is the ordering bug.</p>
<div class="card" style="padding:12px 0">{Lchart([('new','#4A13B7',newpts,False),('doc','#DC680F',docpts,True)])}</div>
<div class="row" style="margin-top:24px">
<div class="note" style="flex:1"><h3>Where each step is used</h3><ul class="c" style="margin-top:8px">
<li><b>700 #4A13B7</b>: primary button, links. It's the current landing button colour, now part of the ramp.</li>
<li><b>800 #2D0B84</b>: all headings and button hover. This is the brand Main colour.</li>
<li><b>900 / 950</b>: pressed state, dark bands, the footer.</li>
<li><b>50–200</b>: tinted sections, selected rows, chips.</li></ul></div>
<div class="note" style="flex:1"><h3>Rules</h3><ul class="c" style="margin-top:8px">
<li>Text on white: use 600 or darker (≥ 6.2:1).</li>
<li>Never use 400–500 for text; they're only for decoration and illustrations.</li>
<li>The old #3A0E94 hover and #2E0B78 pressed are now 800 and 900.</li></ul></div></div>""")

# ---------- 02 ACCENTS ----------
page('02-accents',f"""<div class="eyebrow">FamilyKit palette · 02</div><h1>Accents · Lavender &amp; Lime</h1>
<p class="lead">Two accent families. <b>Lavender</b> (#B294FF) is the soft, friendly partner to the purple. <b>Lime</b> (#EFFF94) is the bright highlight. The doc's "Accent 1 Yellow" #DAD05A is now <b>lime-400</b>, a deeper step of the same family, not a third accent.</p>
<h2>Lavender · Accent 2</h2><p class="sub">Doc value is step 400. Lavender-500 #996DF8 is the focus ring (3.6:1 on white, which passes the 3:1 rule for UI parts).</p>
{ramprow('lavender')}
<h2>Lime · Accent 1</h2><p class="sub">Doc Lime is step 100 and doc Yellow is step 400. Lime is a background colour only. Put primary-950 text on it, never white.</p>
{ramprow('lime')}
<div class="row" style="margin-top:28px">
<div class="note" style="flex:1.3"><h3>Why the yellow became a lime step</h3><ul class="c" style="margin-top:8px">
<li>The doc named both colours "Accent 1", and they're only 11° apart in hue. Used side by side, they look like a mismatch rather than two choices.</li>
<li>As one family, the yellow gives the lime a darker partner for borders, hover and illustration shading.</li>
<li>Neither colour works as text on white (1.1:1 and 1.6:1), so both stay as fills.</li></ul></div>
<div class="card" style="flex:1;display:flex;flex-direction:column;gap:12px">
<h3>Approved pairings</h3>
<div style="background:{g('primary',800)};border-radius:14px;padding:16px 18px;color:#fff;font:600 15px Mulish">Lime on Main purple <span style="background:{g('lime',100)};color:{g('primary',950)};padding:5px 12px;border-radius:99px;font:700 13px Poppins;margin-left:8px">New · Early access</span></div>
<div style="background:{g('lime',100)};border:1px solid {g('lime',400)};border-radius:14px;padding:14px 18px;color:{g('primary',950)};font:600 15px Mulish">primary-950 text on lime-100 · {cr(g('primary',950),g('lime',100)):.1f}:1</div>
<div style="background:{g('lavender',100)};border-radius:14px;padding:14px 18px;color:{g('primary',800)};font:600 15px Mulish">primary-800 on lavender-100 · {cr(g('primary',800),g('lavender',100)):.1f}:1</div>
<div style="background:{g('lavender',400)};border-radius:14px;padding:14px 18px;color:{g('primary',950)};font:600 15px Mulish">primary-950 on lavender-400 · {cr(g('primary',950),g('lavender',400)):.1f}:1</div>
</div></div>""")

# ---------- 03 NEUTRALS ----------
oldg='#9B9B9D'
page('03-neutrals',f"""<div class="eyebrow">FamilyKit palette · 03</div><h1>Neutrals · Purple-tinted greys</h1>
<p class="lead">12 steps from white to the doc's near-black <b>#050011</b>. Every grey carries a faint purple tint (hue ≈ 298), matching the doc's Light Grey, Dark Grey and Black, so the greys sit naturally beside the brand purple.</p>
<h2>Ramp</h2><p class="sub">Text-safe steps on white: 600 (5.5:1) and darker. 400–500 are for icons, placeholders and disabled states only.</p>
{ramprow('neutral',12)}
<h2>The doc's "Grey" #9B9B9D</h2><p class="sub">It was the only colour in the doc with no purple tint, and at 2.8:1 on white it fails as text.</p>
<div class="row">
<div class="card" style="flex:1"><div style="display:flex;gap:14px;align-items:center"><span class="mini" style="width:56px;height:56px;border-radius:12px;background:{oldg}"></span><div><h3>Doc Grey {oldg}</h3><div class="sub" style="margin:2px 0 0">{cr(oldg,'#FFFFFF'):.2f}:1 on white · no tint</div></div><span class="fail" style="margin-left:auto">FAILS AS TEXT</span></div>
<p style="margin-top:14px;color:{oldg};font-size:15px">Last updated 2 days ago · Aadhaar card · Riya</p></div>
<div class="card" style="flex:1"><div style="display:flex;gap:14px;align-items:center"><span class="mini" style="width:56px;height:56px;border-radius:12px;background:{g('neutral',400)}"></span><div><h3>neutral-400 {g('neutral',400)}</h3><div class="sub" style="margin:2px 0 0">same lightness, tinted · decoration and disabled only</div></div><span class="pass" style="margin-left:auto">FOR ICONS</span></div>
<p style="margin-top:14px;color:{g('neutral',600)};font-size:15px">Last updated 2 days ago · Aadhaar card · Riya <span class="pass" style="margin-left:6px">neutral-600 text · {cr(g('neutral',600),'#FFFFFF'):.1f}:1</span></p></div></div>
<h2>Text roles</h2>
<div class="card" style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px">
{''.join(f'<div><div class="eyebrow" style="color:{H("text-muted")}">{lab}</div><div style="font:{f};color:{h}">{s}</div><div class="sub" style="margin:6px 0 0">{ref} {h} · {cr(h,"#FFFFFF"):.1f}:1</div></div>' for lab,f,h,s,ref in [
('Heading','800 24px/1.2 Poppins',H('text-heading'),'Your family vault','primary-800'),
('Text primary','700 17px/1.4 Mulish',H('text-primary'),'Riya’s passport','neutral-900'),
('Text secondary (body)','400 16px/1.5 Mulish',H('text-secondary'),'Store and share every family document safely.','neutral-700'),
('Text muted','500 14px/1.5 Mulish',H('text-muted'),'Added 12 Oct 2026 · 2.4 MB','neutral-600')])}
</div>""")

# ---------- 04 SEMANTIC ----------
rows=''
for s in ['success','error','warning','info']:
    st=R[s]; b=g(s,500)
    rows+=f"""<h2 style="margin-top:32px">{s.title()}</h2><p class="sub">Doc base {b} = {s}-500 ({cr(b,'#FFFFFF'):.2f}:1 on white{' — fails as text' if cr(b,'#FFFFFF')<4.5 else ' — passes, but 700 is still used for text, to match the others'}). Text uses <b>{s}-700 {g(s,700)}</b> ({cr(g(s,700),g(s,50)):.1f}:1 on its 50 tint). Solid fills with white text use {s}-600 ({cr(g(s,600),'#FFFFFF'):.1f}:1).</p>
<div class="ramp" style="grid-template-columns:repeat(8,1fr)">{''.join(swatch(s,x) for x in st)}</div>"""
demo=''.join(f"""<div class="card" style="flex:1;padding:16px 18px"><div style="font:700 15px Mulish;color:{g(s,500)}">{s.title()} base as text</div><div style="margin:4px 0 10px">{('<span class="fail">' if cr(g(s,500),'#FFFFFF')<4.5 else '<span class="pass">')}{cr(g(s,500),'#FFFFFF'):.2f}:1</span></div>
<div style="font:700 15px Mulish;color:{g(s,700)}">{s.title()}-700 as text</div><div style="margin-top:4px"><span class="pass">{cr(g(s,700),'#FFFFFF'):.2f}:1</span></div></div>""" for s in ['success','error','warning','info'])
page('04-semantic',f"""<div class="eyebrow">FamilyKit palette · 04</div><h1>Semantic · Success, Error, Warning, Info</h1>
<p class="lead">The doc's hues are kept. Each is now an 8-step ramp: <b>50</b> background · <b>100–200</b> borders · <b>500</b> the doc base (icons, charts) · <b>600</b> solid fill · <b>700</b> text · <b>900</b> the doc's dark value.</p>
<div class="row" style="margin-top:24px">{demo}</div>
{rows}""")

# ---------- 05 ROLES + CONTRAST ----------
groups=[('Surfaces',['bg','bg-subtle','surface','surface-raised','surface-tint','surface-inverse']),
('Borders',['border','border-strong','border-focus']),
('Text',['text-heading','text-primary','text-secondary','text-muted','text-disabled','text-link','text-on-primary','text-on-accent']),
('Action',['primary','primary-hover','primary-pressed','primary-subtle','focus-ring','disabled-bg','disabled-fg']),
('Accent',['accent','accent-hover','accent-strong','accent-2','accent-2-subtle']),
('Status',[f'{s}-{r}' for s in ['success','error','warning','info'] for r in ['fg','bg','border','solid']])]
def rtable(gs):
    out=''
    for gname,keys in gs:
        out+=f'<tr><th colspan="3" style="padding-top:16px">{gname}</th></tr>'+''.join(f'<tr><td class="mono" style="white-space:nowrap">--fk-{k}</td><td style="white-space:nowrap"><span class="mini" style="background:{RO[k]["hex"]}"></span>{RO[k]["hex"]}</td><td style="color:{H("text-muted")};white-space:nowrap">{RO[k]["ref"]}</td></tr>' for k in keys)
    return f'<table class="rt">{out}</table>'
pairs=[('Heading on white',H('text-heading'),'#FFFFFF','text'),('Text primary on white',H('text-primary'),'#FFFFFF','text'),
('Body (neutral-700) on white',H('text-secondary'),'#FFFFFF','text'),('Muted (neutral-600) on white',H('text-muted'),'#FFFFFF','text'),
('Muted on primary-50',H('text-muted'),g('primary',50),'text'),('Doc Grey #9B9B9D on white','#9B9B9D','#FFFFFF','text'),
('neutral-400 on white (disabled only)',g('neutral',400),'#FFFFFF','text'),('Doc "75" #3D2184 on white','#3D2184','#FFFFFF','text'),
('White on primary-700 (button)','#FFFFFF',H('primary'),'text'),('White on primary-800 (hover)','#FFFFFF',H('primary-hover'),'text'),
('White on primary-900 (pressed)','#FFFFFF',H('primary-pressed'),'text'),('White on primary-600','#FFFFFF',g('primary',600),'text'),
('primary-950 on lime-100 (accent)',g('primary',950),g('lime',100),'text'),('White on lime-100','#FFFFFF',g('lime',100),'text'),
('Focus ring lavender-500 vs white',H('focus-ring'),'#FFFFFF','ui'),('Old focus #8B5CF6 vs white','#8B5CF6','#FFFFFF','ui')]
for s in ['success','error','warning','info']:
    pairs+= [(f'{s}-500 (doc base) on white',g(s,500),'#FFFFFF','text'),(f'{s}-700 on {s}-50',g(s,700),g(s,50),'text'),(f'White on {s}-600',"#FFFFFF",g(s,600),'text')]
crows=[]
for lab,f,b,kind in pairs:
    c=cr(f,b)
    if kind=='ui': res=('<span class="pass">PASS 3:1 UI</span>' if c>=3 else '<span class="fail">FAIL 3:1 UI</span>')
    else: res=('<span class="pass">AA</span>' if c>=4.5 else '<span class="fail">AA</span>')+' '+('<span class="pass">AAA</span>' if c>=7 else '<span class="fail">AAA</span>')+' '+('<span class="pass">Large</span>' if c>=3 else '<span class="fail">Large</span>')
    crows.append(f'<tr><td><span style="display:inline-block;background:{b};color:{f};border:1px solid {g("neutral",200)};border-radius:8px;padding:3px 9px;font:700 13px Mulish;margin-right:10px;min-width:44px;text-align:center">{"Aa" if kind=="text" else "◯"}</span>{lab}</td><td style="font:700 14px Poppins;color:{H("text-primary")}">{c:.2f}:1</td><td style="white-space:nowrap">{res}</td></tr>')
crowA=''.join(crows[:14]); crowB=''.join(crows[14:])
page('05-roles-contrast',f"""<div class="eyebrow">FamilyKit palette · 05</div><h1>Role tokens &amp; contrast</h1>
<p class="lead">Components use <b>role tokens</b> (what a colour is for), never raw ramp steps. The current landing tokens map straight across. The button stays <b>#4A13B7</b>, now as primary-700. WCAG 2.2 limits: AA text 4.5:1, AAA 7:1, large text and UI parts 3:1.</p>
<h2>Role tokens</h2><div class="row" style="align-items:flex-start">
<div class="card" style="flex:1">{rtable(groups[:3])}</div>
<div class="card" style="flex:1">{rtable(groups[3:5])}</div>
<div class="card" style="flex:1">{rtable(groups[5:])}</div></div>
<h2>Contrast results</h2><p class="sub">The Aa chip shows each pairing as it looks. Red pills are fails; the doc's Grey, the doc's success, warning and info bases, and white on lime are the ones that fail as text.</p>
<div class="row" style="align-items:flex-start">
<div class="card" style="flex:1"><table><tr><th>Pairing</th><th>Ratio</th><th>Result</th></tr>{crowA}</table></div>
<div class="card" style="flex:1"><table><tr><th>Pairing</th><th>Ratio</th><th>Result</th></tr>{crowB}</table></div></div>
</div>""")

# ---------- 06 IN USE ----------
def btn(lab,bg,fg,bd=None,extra=''):
    return f'<button style="height:52px;padding:0 28px;border-radius:999px;font:600 16px Poppins;background:{bg};color:{fg};border:{"2px solid "+bd if bd else "0"};{extra}">{lab}</button>'
def alert(s,title,msg,icon):
    return f'''<div style="display:flex;gap:14px;align-items:flex-start;background:{H(s+"-bg")};border:1px solid {H(s+"-border")};border-left:5px solid {H(s+"-solid")};border-radius:14px;padding:14px 18px">
<span style="flex:none;width:26px;height:26px;border-radius:50%;background:{H(s+"-solid")};color:#fff;font:800 14px/26px Poppins;text-align:center">{icon}</span>
<div><div style="font:700 15px/1.3 Mulish;color:{H(s+"-fg")}">{title}</div><div style="font-size:14px;color:{H("text-secondary")};margin-top:2px">{msg}</div></div></div>'''
doccard=lambda t,who,meta,tag,tagc: f'''<div style="border:1px solid {H("border")};border-radius:20px;padding:18px;background:#fff;display:flex;gap:14px;align-items:center">
<div style="width:52px;height:52px;border-radius:14px;background:{H("surface-tint")};display:flex;align-items:center;justify-content:center"><div style="width:22px;height:28px;border-radius:4px;border:2.5px solid {H("primary")}"></div></div>
<div style="flex:1"><div style="font:700 16px Mulish;color:{H("text-primary")}">{t}</div><div style="font-size:14px;color:{H("text-muted")}">{who} · {meta}</div></div>
<span style="font:700 12px/1 Mulish;padding:6px 10px;border-radius:99px;{tagc}">{tag}</span></div>'''
page('06-in-use',f"""<div class="eyebrow">FamilyKit palette · 06</div><h1>The palette in use</h1>
<p class="lead">A sample FamilyKit screen built only from role tokens.</p>
<div style="margin-top:28px;border:1px solid {H('border')};border-radius:24px;overflow:hidden;background:{H('bg-subtle')}">
 <div style="height:76px;background:#fff;border-bottom:1px solid {H('border')};display:flex;align-items:center;padding:0 32px;gap:36px">
  <div style="font:800 22px Poppins;color:{H('text-heading')}">Family<span style="color:{g('primary',600)}">Kit</span></div>
  <div style="display:flex;gap:6px;font:600 15px Mulish">
   <span style="padding:9px 16px;border-radius:99px;background:{H('primary-subtle')};color:{H('text-heading')}">Documents</span>
   <span style="padding:9px 16px;color:{H('text-secondary')}">Reminders</span><span style="padding:9px 16px;color:{H('text-secondary')}">Family</span><span style="padding:9px 16px;color:{H('text-secondary')}">Sharing</span></div>
  <div style="margin-left:auto;display:flex;gap:14px;align-items:center"><span style="background:{H('accent')};color:{H('text-on-accent')};border:1px solid {H('accent-strong')};font:700 12px/1 Mulish;padding:7px 12px;border-radius:99px">BETA</span>
  <span style="width:40px;height:40px;border-radius:50%;background:{H('accent-2')};color:{H('text-on-accent')};font:700 15px/40px Poppins;text-align:center">RS</span></div></div>
 <div style="display:grid;grid-template-columns:1.25fr 1fr;gap:28px;padding:32px">
  <div style="display:flex;flex-direction:column;gap:14px">
   <div style="font:800 28px Poppins;color:{H('text-heading')}">Your family vault</div>
   <div style="color:{H('text-secondary')};font-size:16px;margin-top:-6px">12 documents · 4 family members</div>
   {doccard('Aadhaar card','Riya Sharma','PDF · 1.2 MB','Verified',f'background:{H("success-bg")};color:{H("success-fg")};border:1px solid {H("success-border")}')}
   {doccard('Passport','Arjun Sharma','Expires 02 Jan 2027','Expires soon',f'background:{H("warning-bg")};color:{H("warning-fg")};border:1px solid {H("warning-border")}')}
   {doccard('Health insurance','Family plan','Shared with 2 people','Shared',f'background:{H("info-bg")};color:{H("info-fg")};border:1px solid {H("info-border")}')}
   <div style="background:{H('surface-inverse')};border-radius:20px;padding:22px 24px;display:flex;align-items:center;gap:18px;margin-top:6px">
    <div style="flex:1"><div style="font:700 18px Poppins;color:#fff">Invite your family</div><div style="font-size:14px;color:{g('primary',200)}">Everyone gets their own private space.</div></div>
    {btn('Send invite',H('accent'),H('text-on-accent'))}</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:14px">
   <div style="font:700 18px Poppins;color:{H('text-primary')}">Alerts</div>
   {alert('success','Document uploaded','Riya’s Aadhaar card is saved and encrypted.','✓')}
   {alert('warning','Passport expires in 52 days','Set a renewal reminder so you don’t miss it.','!')}
   {alert('error','Upload failed','The file is over 20 MB. Try a smaller scan.','×')}
   {alert('info','New: share with a link','Send a document to anyone for 24 hours.','i')}
   <div style="font:700 18px Poppins;color:{H('text-primary')};margin-top:10px">Buttons</div>
   <div class="card" style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">
    {btn('Get Early Access',H('primary'),'#fff')}{btn('Hover',H('primary-hover'),'#fff')}{btn('Pressed',H('primary-pressed'),'#fff')}
    {btn('Focus',H('primary'),'#fff',extra=f'box-shadow:0 0 0 3px #fff,0 0 0 6px {H("focus-ring")}')}
    {btn('Secondary','#fff',H('primary'),H('primary'))}{btn('Disabled',H('disabled-bg'),H('disabled-fg'))}
    {btn('Delete',H('error-solid'),'#fff')}{btn('Accent',H('accent'),H('text-on-accent'),H('accent-strong'))}
   </div></div></div></div>""")

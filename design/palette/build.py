import json
from ok import *
W='#FFFFFF'
def interp(pts,x):
    pts=sorted(pts)
    if x<=pts[0][0]: return pts[0][1]
    if x>=pts[-1][0]: return pts[-1][1]
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        if x0<=x<=x1: return y0+(y1-y0)*(x-x0)/(x1-x0)

def ramp(spec, anchors, cpts, hpts):
    """spec: list of (step,L); anchors: {step:(hex,docname)}"""
    out=[]
    for step,L in spec:
        if step in anchors:
            h,doc=anchors[step]; out.append(dict(step=step,hex=h.upper(),doc=doc))
        else:
            out.append(dict(step=step,hex=oklch2hex(L,interp(cpts,L),interp(hpts,L)),doc=None))
    for s in out:
        L,C,H=hex2oklch(s['hex']); s.update(L=round(L,3),C=round(C,3),H=round(H,1),
            cw=round(cr(s['hex'],W),2),ck=round(cr(s['hex'],'#050011'),2))
    return out

# ---------- PRIMARY ----------
prim=ramp([(50,.975),(100,.934),(200,.875),(300,.795),(400,.705),(500,.61),(600,.514),(700,.405),(800,.313),(900,.245),(950,.183)],
  {100:('#EBE6F7','Primary 10'),600:('#7543C7','Doc text colour'),700:('#4A13B7','Kept: current landing button'),800:('#2D0B84','Primary Main'),950:('#130438','Primary 100')},
  [(.183,.093),(.245,.14),(.313,.175),(.405,.215),(.514,.195),(.61,.165),(.705,.13),(.795,.09),(.875,.05),(.934,.023),(.975,.01)],
  [(.183,287),(.313,283),(.405,286),(.514,293),(.7,296),(.975,298)])
# ---------- LAVENDER ----------
lav=ramp([(50,.975),(100,.945),(200,.89),(300,.815),(400,.737),(500,.645),(600,.555),(700,.47),(800,.39),(900,.31)],
  {400:('#B294FF','Accent 2 Lavender')},
  [(.31,.13),(.47,.2),(.555,.22),(.645,.2),(.737,.153),(.815,.11),(.89,.06),(.945,.03),(.975,.013)],
  [(.31,293),(.737,295.3),(.975,296)])
# ---------- LIME ----------
lime=ramp([(50,.987),(100,.965),(200,.93),(300,.89),(400,.843),(500,.76),(600,.66),(700,.56),(800,.46),(900,.36)],
  {100:('#EFFF94','Accent 1 Lime'),400:('#DAD05A','Accent 1 Yellow')},
  [(.36,.08),(.46,.1),(.56,.12),(.66,.13),(.76,.135),(.843,.139),(.89,.14),(.93,.14),(.965,.133),(.987,.06)],
  [(.36,106),(.843,104.5),(.93,112),(.965,115.9),(.987,116)])
# ---------- NEUTRAL ----------
neu=ramp([(0,1),(50,.975),(100,.942),(200,.89),(300,.80),(400,.69),(500,.60),(600,.52),(700,.414),(800,.31),(900,.21),(950,.097)],
  {0:('#FFFFFF','White'),100:('#EDEAF3','Light Grey'),700:('#4D485A','Dark Grey'),950:('#050011','Black')},
  [(.097,.052),(.21,.045),(.31,.036),(.414,.03),(.52,.028),(.6,.025),(.69,.02),(.8,.016),(.89,.013),(.942,.012),(.975,.006)],
  [(.097,298.5),(.414,297.8),(.942,301.3),(.975,300)])
# ---------- SEMANTIC ----------
def solveL(H,C,target,lo=.2,hi=.8):
    # highest L whose contrast with white >= target
    for _ in range(40):
        mid=(lo+hi)/2
        if cr(oklch2hex(mid,C,H),W)>=target: lo=mid
        else: hi=mid
    return lo
sem={}
for name,t,b,d in [('success','#F2FFF3','#0FB21D','#125C19'),('error','#FFEBEB','#C71010','#5C1B12'),
                   ('info','#F2FDFF','#0BA2C4','#124E5C'),('warning','#FFF8F2','#DC680F','#5C3212')]:
    Lb,Cb,Hb=hex2oklch(b); Ld,Cd,Hd=hex2oklch(d); Lt,Ct,Ht=hex2oklch(t)
    L600=min(solveL(Hb,Cb,4.6),Lb-.04)
    L700=min(solveL(interp([(Ld,Hd),(Lb,Hb)],.5) if False else Hb,Cb*0.85,6.6),L600-.06)
    if Lt>.97:
        spec=[(50,Lt),(100,.955),(200,.9),(300,.82),(500,Lb),(600,L600),(700,L700),(900,Ld)]; tstep=50
    else:  # doc tint is darker than the other three: it becomes step 100, 50 is generated
        spec=[(50,.985),(100,Lt),(200,.9),(300,.82),(500,Lb),(600,L600),(700,L700),(900,Ld)]; tstep=100; Lt,Ct=.985,Ct*.4
    sem[name]=ramp(spec,{tstep:(t,name.title()+' 10'),500:(b,name.title()+' base'),900:(d,name.title()+' 100')},
        [(Ld,Cd),(L700,Cb*.85),(Lb,Cb),(.82,Cb*.55),(.9,Cb*.3),(.955,Cb*.15),(Lt,Ct)],
        [(Ld,Hd),(Lb,Hb),(Lt,Ht)])
pal=dict(primary=prim,lavender=lav,lime=lime,neutral=neu,**sem)
def g(r,s): return next(x['hex'] for x in pal[r] if x['step']==s)
roles={
 'bg':('neutral',0),'bg-subtle':('neutral',50),'surface':('neutral',0),'surface-raised':('primary',50),'surface-tint':('primary',100),
 'surface-inverse':('primary',950),
 'border':('neutral',200),'border-strong':('neutral',300),'border-focus':('lavender',500),
 'text-primary':('neutral',900),'text-secondary':('neutral',700),'text-muted':('neutral',600),'text-disabled':('neutral',400),
 'text-heading':('primary',800),'text-link':('primary',700),'text-on-primary':('neutral',0),'text-on-accent':('primary',950),'text-on-inverse':('neutral',0),
 'primary':('primary',700),'primary-hover':('primary',800),'primary-pressed':('primary',900),'primary-subtle':('primary',100),'focus-ring':('lavender',500),
 'accent':('lime',100),'accent-hover':('lime',200),'accent-strong':('lime',400),'accent-2':('lavender',400),'accent-2-subtle':('lavender',100),
 'disabled-bg':('neutral',100),'disabled-fg':('neutral',500),
}
for s in ['success','error','warning','info']:
    roles[f'{s}-fg']=(s,700); roles[f'{s}-bg']=(s,50); roles[f'{s}-border']=(s,200); roles[f'{s}-solid']=(s,600); roles[f'{s}-icon']=(s,600); roles[f'{s}-strong']=(s,900)
rolehex={k:g(*v) for k,v in roles.items()}
json.dump(dict(meta=dict(name='FamilyKit colour palette',version='1.0',date='2026-11-11',space='OKLCH-built, sRGB hex output',
     note='doc = colour taken unchanged from the founder colour document (or the current landing button). Contrast cw = vs #FFFFFF, ck = vs #050011.'),
     ramps=pal,roles={k:dict(ref=f'{v[0]}-{v[1]}',hex=rolehex[k]) for k,v in roles.items()}),open('palette.json','w'),indent=1)
# tokens.css
L=['/* FamilyKit colour tokens v1.0 (2026-11-11). Generated from palette.json, built in OKLCH.',
   '   "doc" = unchanged value from the founder colour document. */',':root{']
for r,steps in pal.items():
    L.append(f'  /* {r} */')
    for s in steps:
        L.append(f'  --fk-{r}-{s["step"]}:{s["hex"]};'+(f' /* doc: {s["doc"]} */' if s['doc'] else ''))
L.append('\n  /* ---- Semantic roles (use these in components, not raw ramps) ---- */')
for k,v in roles.items():
    L.append(f'  --fk-{k}:var(--fk-{v[0]}-{v[1]}); /* {rolehex[k]} */')
L.append('\n  /* ---- Legacy landing tokens, remapped (tokens.css v1) ---- */')
for k,v in [('heading','text-heading'),('ink','text-primary'),('body','text-secondary'),
            ('muted','text-muted'),('focus','focus-ring'),('dark','surface-inverse')]:
    L.append(f'  --fk-{k}:var(--fk-{v});')
L+=['  --fk-lav-50:var(--fk-primary-50); --fk-lav-100:var(--fk-lavender-100); --fk-lav-200:var(--fk-lavender-200); --fk-lav-300:var(--fk-lavender-300);','}']
# NB: --fk-primary stays = primary-700 (#4A13B7) via roles above
open('tokens.css','w').write('\n'.join(L)+'\n')
for r,steps in pal.items():
    print(r,' '.join(f"{s['step']}:{s['hex']}{'*' if s['doc'] else ''}(L{s['L']},C{s['C']},w{s['cw']})" for s in steps))

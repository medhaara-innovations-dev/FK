import math
def s2l(c):
    c/=255; return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def l2s(c):
    c = 12.92*c if c<=0.0031308 else 1.055*c**(1/2.4)-0.055
    return c
def hex2rgb(h): h=h.lstrip('#'); return [int(h[i:i+2],16) for i in (0,2,4)]
def rgb2hex(r): return '#'+''.join('%02X'%max(0,min(255,round(x*255))) for x in r)
def hex2oklch(h):
    r,g,b=[s2l(x) for x in hex2rgb(h)]
    l=0.4122214708*r+0.5363325363*g+0.0514459929*b
    m=0.2119034982*r+0.6806995451*g+0.1073969566*b
    s=0.0883024619*r+0.2817188376*g+0.6299787005*b
    l,m,s=[x**(1/3) if x>=0 else -(-x)**(1/3) for x in (l,m,s)]
    L=0.2104542553*l+0.7936177850*m-0.0040720468*s
    a=1.9779984951*l-2.4285922050*m+0.4505937099*s
    b=0.0259040371*l+0.7827717662*m-0.8086757660*s
    return L, math.hypot(a,b), math.degrees(math.atan2(b,a))%360
def oklch2lin(L,C,H):
    a=C*math.cos(math.radians(H)); b=C*math.sin(math.radians(H))
    l=(L+0.3963377774*a+0.2158037573*b)**3
    m=(L-0.1055613458*a-0.0638541728*b)**3
    s=(L-0.0894841775*a-1.2914855480*b)**3
    return [4.0767416621*l-3.3077115913*m+0.2309699292*s,
            -1.2684380046*l+2.6097574011*m-0.3413193965*s,
            -0.0041960863*l-0.7034186147*m+1.7076147010*s]
def oklch2hex(L,C,H):
    lo,hi=0,C
    rgb=oklch2lin(L,C,H)
    if all(-1e-6<=x<=1+1e-6 for x in rgb): return rgb2hex([l2s(min(1,max(0,x))) for x in rgb])
    for _ in range(40):
        mid=(lo+hi)/2; rgb=oklch2lin(L,mid,H)
        if all(-1e-6<=x<=1+1e-6 for x in rgb): lo=mid
        else: hi=mid
    return rgb2hex([l2s(min(1,max(0,x))) for x in oklch2lin(L,lo,H)])
def lum(h):
    r,g,b=[s2l(x) for x in hex2rgb(h)]; return 0.2126*r+0.7152*g+0.0722*b
def cr(a,b):
    x,y=sorted([lum(a),lum(b)],reverse=True); return (x+0.05)/(y+0.05)

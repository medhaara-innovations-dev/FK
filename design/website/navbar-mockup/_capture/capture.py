import asyncio, json, subprocess, time, os, sys
from playwright.async_api import async_playwright
ROOT='/workspace/fk-landing/site'; OUT=ROOT+'/_capture/shots'; os.makedirs(OUT,exist_ok=True)
srv=subprocess.Popen([sys.executable,'-m','http.server','18731','--bind','127.0.0.1'],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
URL='http://127.0.0.1:18731/index.html'
MEASURE='''() => { const r=s=>{const e=document.querySelector(s); if(!e) return null; const b=e.getBoundingClientRect(); const cs=getComputedStyle(e); return {x:Math.round(b.x),y:Math.round(b.y),w:Math.round(b.width),h:Math.round(b.height),font:cs.fontFamily.split(',')[0]+' '+cs.fontWeight+' '+cs.fontSize}};
 return {nav:r('#nav'),logo:r('#nav .nav__logo img'),links:r('.nav__links'),link:r('.nav__links a'),cta:r('.nav__cta'),menuBtn:r('.nav__menu-btn'),close:r('.mmenu__close'),mlink:r('.mmenu__links a'),mcta:r('.mmenu__bottom .btn'),trust:r('.mmenu__trust'),mlogo:r('.mmenu__top img'),fontsOK:document.fonts.check('600 15px Poppins')&&document.fonts.check('400 15px Mulish')} }'''
async def main():
  m={}
  async with async_playwright() as p:
    b=await p.chromium.launch()
    # desktop
    pg=await (await b.new_context(viewport={'width':1440,'height':900},device_scale_factor=2)).new_page()
    await pg.goto(URL); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
    clip={'x':0,'y':0,'width':1440,'height':128}
    await pg.screenshot(path=f'{OUT}/d-default.png',clip=clip); m['d_default']=await pg.evaluate(MEASURE)
    await pg.hover('.nav__links a:nth-child(2)'); await pg.wait_for_timeout(300); await pg.screenshot(path=f'{OUT}/d-hover-link.png',clip=clip)
    await pg.hover('.nav__cta'); await pg.wait_for_timeout(300); await pg.screenshot(path=f'{OUT}/d-hover-btn.png',clip=clip)
    await pg.mouse.move(700,600)
    await pg.keyboard.press('Tab'); await pg.keyboard.press('Tab'); await pg.keyboard.press('Tab'); await pg.wait_for_timeout(300)
    await pg.screenshot(path=f'{OUT}/d-focus-link.png',clip=clip)
    for _ in range(4): await pg.keyboard.press('Tab')
    await pg.wait_for_timeout(300); await pg.screenshot(path=f'{OUT}/d-focus-btn.png',clip=clip)
    await pg.evaluate("document.activeElement.blur()")
    await pg.evaluate("window.scrollTo({top:document.getElementById('how').offsetTop-200,behavior:'instant'})"); await pg.wait_for_timeout(700)
    await pg.screenshot(path=f'{OUT}/d-scrolled.png',clip={'x':0,'y':0,'width':1440,'height':104}); m['d_scrolled']=await pg.evaluate(MEASURE)
    # mobile
    ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True)
    pg=await ctx.new_page(); await pg.goto(URL); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
    await pg.screenshot(path=f'{OUT}/m-closed.png',clip={'x':0,'y':0,'width':390,'height':128}); m['m_closed']=await pg.evaluate(MEASURE)
    await pg.evaluate("window.scrollTo({top:900,behavior:'instant'})"); await pg.wait_for_timeout(600)
    await pg.screenshot(path=f'{OUT}/m-scrolled.png',clip={'x':0,'y':0,'width':390,'height':104})
    await pg.evaluate("window.scrollTo({top:0,behavior:'instant'})"); await pg.wait_for_timeout(400)
    st=await pg.add_style_tag(content=".nav__logo,.nav__cta,.nav__menu-btn{outline:1.5px dashed #C71010!important;outline-offset:0!important}")
    await pg.wait_for_timeout(200); await pg.screenshot(path=f'{OUT}/m-targets.png',clip={'x':0,'y':0,'width':390,'height':104})
    await st.evaluate("e=>e.remove()"); await pg.wait_for_timeout(200)
    await pg.tap('.nav__menu-btn'); await pg.wait_for_timeout(500)
    await pg.screenshot(path=f'{OUT}/m-open.png'); m['m_open']=await pg.evaluate(MEASURE)
    await b.close()
  srv.terminate(); print(json.dumps(m,indent=1))
asyncio.run(main())

# Renders html/07-typography.html (FamilyKit app typography specimen, v1.2) to 07-typography@2x.png at deviceScaleFactor 2.
# Optional: python3 render_typography.py --scale 1.3 /tmp/out.png  -> same page at 130% text scale (layout check only).
import asyncio, sys
from playwright.async_api import async_playwright
SCALE=1.0; OUT='/workspace/fk-palette/07-typography@2x.png'
if '--scale' in sys.argv: SCALE=float(sys.argv[sys.argv.index('--scale')+1]); OUT=sys.argv[-1]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1400,'height':900},device_scale_factor=2)
        await pg.goto('file:///workspace/fk-palette/html/07-typography.html')
        if SCALE!=1.0: await pg.add_style_tag(content=f"html{{font-size:{SCALE*100:.0f}%}}")
        await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
        print(await pg.evaluate("""()=>{const r={};for(const f of document.fonts){if(f.status==='loaded')r[f.family+' '+f.weight]=f.status};
          for(const s of ["600 24px Poppins","500 12px Poppins","400 15px Mulish","600 13px Mulish"]) r['check '+s]=document.fonts.check(s); return r}"""))
        # overflow check: any text element wider than its box?
        print('overflowing elements:', await pg.evaluate("""()=>[...document.querySelectorAll('.phone *')].filter(e=>e.scrollWidth>e.clientWidth+1&&getComputedStyle(e).overflow!=='hidden').map(e=>e.className+': '+e.textContent.trim().slice(0,30))"""))
        await pg.screenshot(path=OUT,full_page=True)
        print(OUT, await pg.evaluate("[document.body.scrollWidth, document.body.scrollHeight]"))
        await b.close()
asyncio.run(main())

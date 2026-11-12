import asyncio
from playwright.async_api import async_playwright
D='/workspace/fk-landing/site/_capture'; R='/workspace/fk-landing/review'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for name,out,w in [('desktop','01-navbar-desktop@2x.png',1536),('mobile','02-navbar-mobile@2x.png',940)]:
      pg=await (await b.new_context(viewport={'width':w,'height':800},device_scale_factor=2)).new_page()
      await pg.goto(f'file://{D}/{name}.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f'{R}/{out}',full_page=True)
    await b.close()
asyncio.run(main())

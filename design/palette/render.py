import asyncio
from playwright.async_api import async_playwright
names=['01-primary','02-accents','03-neutrals','04-semantic','05-roles-contrast','06-in-use']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':900},device_scale_factor=2)
        for n in names:
            await pg.goto(f'file:///workspace/fk-palette/html/{n}.html'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'/workspace/fk-palette/{n}@2x.png',full_page=True)
            print(n, await pg.evaluate("document.body.scrollHeight"))
        await b.close()
asyncio.run(main())

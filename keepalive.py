import asyncio
from playwright.async_api import async_playwright

URLS = [
    "https://crypto-security-monitor.streamlit.app/",
    # thêm app khác của thầy ở đây nếu cần, mỗi app một dòng
]

async def visit(page, url):
    await page.goto(url, wait_until="networkidle", timeout=60000)
    try:
        btn = page.get_by_text("Yes, get this app back up", exact=False)
        if await btn.count() > 0:
            await btn.first.click()
            print(f"WAKE  {url}  (da danh thuc app dang ngu)")
            await page.wait_for_timeout(30000)
        else:
            print(f"OK    {url}")
    except Exception as e:
        print(f"WARN  {url}  ({e})")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for url in URLS:
            await visit(page, url)
        await browser.close()

asyncio.run(main())

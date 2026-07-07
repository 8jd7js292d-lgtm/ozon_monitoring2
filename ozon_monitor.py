from playwright.async_api import async_playwright


async def check_ozon(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()

        await page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        await page.wait_for_timeout(5000)

        text = await page.locator("body").inner_text()

        await browser.close()

    return [text[:1000]]
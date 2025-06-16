from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url, save_dir="output/screenshots"):
    os.makedirs(save_dir, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text('body')
        page.screenshot(path=f"{save_dir}/chapter1.png", full_page=True)
        browser.close()
    return content

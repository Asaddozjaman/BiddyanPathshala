from playwright.sync_api import sync_playwright
import os
import shutil

def test_android_app_download():
    with sync_playwright() as p:
        download_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_dir, exist_ok=True)

        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        page.goto("https://biddyanpathshala.com")
        page.wait_for_timeout(2000)
        print("Opened homepage:", page.url)

        download_button = page.locator("a.button:has-text('Android Apps')")
        download_button.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)

        with page.expect_download() as download_info:
            download_button.click()
        download = download_info.value

        temp_path = download.path()
        final_path = os.path.join(download_dir, download.suggested_filename)
        shutil.move(temp_path, final_path)

        print(f"Download successful. File saved to: {final_path}")

        browser.close()

if __name__ == "__main__":
    test_android_app_download()

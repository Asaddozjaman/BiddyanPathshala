from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to Biddyan Pathshala homepage
        page.goto("https://biddyanpathshala.com")
        page.wait_for_timeout(2000)
        print("Opened homepage:", page.url)

        # Click the login button
        page.click('a.login')
        print("Clicked the login button.")
        page.wait_for_timeout(3000)

        page.click("#student_login_option")
        page.wait_for_timeout(1000)

        page.fill('#student_id', '77')
        page.wait_for_timeout(1000)
        page.fill('#student_pass', 'KPiktzmt')
        page.wait_for_timeout(1000)
        page.click('#student_login_submit')
        page.wait_for_timeout(2000)
        print("Login successful. Dashboard URL:", page.url)

        page.goto("https://biddyanpathshala.com")
        assert page.url == "https://biddyanpathshala.com/"
        print("Navigated to Home Page:", page.url)
        page.wait_for_timeout(2000)

        browser.close()

if __name__ == "__main__":
    run()

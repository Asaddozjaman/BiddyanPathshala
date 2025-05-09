from playwright.sync_api import sync_playwright

def teacher_login():
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

        page.click("#teacher_login_option")
        page.wait_for_timeout(1000)

        page.fill('#user_name', 'asad@biddyan')
        page.wait_for_timeout(1000)
        page.fill('#user_pass', '12345')
        page.wait_for_timeout(1000)
        page.click('#teacher_login_submit')
        page.wait_for_timeout(5000)
        print("Login successful. Dashboard URL:", page.url)
        page.wait_for_timeout(4000)
        assert page.url == "https://biddyanpathshala.com/dashboard/"
        print("Navigated to Dashboard:", page.url)
        print("Navigated to Home Page:", page.url)


        browser.close()

if __name__ == "__main__":
    teacher_login()

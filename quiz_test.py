from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://biddyanpathshala.com/login/")
        page.wait_for_timeout(2000)

        # Login as teacher
        page.click("#teacher_login_option")
        page.wait_for_timeout(1000)

        page.fill('#user_name', 'asad@biddyan')
        page.wait_for_timeout(1000)
        page.fill('#user_pass', '12345')
        page.wait_for_timeout(1000)
        page.click('#teacher_login_submit')
        page.wait_for_timeout(3000)
        print("Login successful. Dashboard URL:", page.url)

        # Go to home page
        page.goto("https://biddyanpathshala.com")
        assert page.url == "https://biddyanpathshala.com/"
        print("Navigated to Home Page:", page.url)
        page.wait_for_timeout(2000)

        # Click on Quiz button
        page.click('a[href="https://quiz.biddyanpathshala.com"]')
        page.wait_for_timeout(5000)
        print("Navigated to Quiz Page:", page.url)

        # Click on "Biddyan Quiz 2024"
        page.click('button[data-id="9"]')
        page.wait_for_timeout(3000)
        print("Clicked Biddyan Quiz 2024")

        # Click the Result button
        page.click('#result')
        page.wait_for_timeout(3000)
        print("Clicked Result button")

        # Return to Biddyan Quiz 2024 page
        page.click('svg.ionicon.s-ion-icon')
        page.wait_for_timeout(3000)
        print("Returned to Biddyan Quiz 2024 page")

        # Click the Applicants button
        page.click('#app_list')
        page.wait_for_timeout(4000)
        print("Applicants page opened")

        # Return from Applicants page
        page.click('svg.ionicon.s-ion-icon')
        page.wait_for_timeout(3000)
        print("Returned from Applicants to Biddyan Quiz 2024 page")

        browser.close()

if __name__ == "__main__":
    run()

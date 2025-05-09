from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to home page
        page.goto("https://biddyanpathshala.com")
        assert page.url == "https://biddyanpathshala.com/"
        print("Navigated to Home Page:", page.url)
        page.wait_for_timeout(2000)

        # Click on online exam button
        page.click('a[href="https://test.biddyanpathshala.com"]')
        page.wait_for_timeout(3000)
        print("Navigated to Quiz Page:", page.url)

        # Login as student
        page.click("#student_login_option")
        page.wait_for_timeout(1000)

        page.fill('#student_id', '77')
        page.click('#student_login_submit')
        page.wait_for_timeout(3000) 
        print("Login successful. Dashboard URL:", page.url)

        # Click the "Open" button
        page.click('button.button.my_report[data-exam_sl="42"][data-sid="77"]')
        print("Vieww result sheet successfully")
        page.wait_for_timeout(3000) 

        # Click the "Close" button
        page.click('div#close-btn')
        print("CClose result sheet successfully")
        page.wait_for_timeout(2000)

        browser.close()

if __name__ == "__main__":
    run()

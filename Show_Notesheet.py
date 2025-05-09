from playwright.sync_api import sync_playwright

def login_and_goto_note_sheet(page):
    # Login
    page.goto("https://biddyanpathshala.com/login/")
    page.click("#teacher_login_option")
    page.fill('#user_name', 'asad@biddyan')
    page.fill('#user_pass', '12345')
    page.click('#teacher_login_submit')
    print("Login successful. Dashboard URL:", page.url)

    # Go to home page
    page.goto("https://biddyanpathshala.com")
    assert page.url == "https://biddyanpathshala.com/"
    print("Navigated to Home Page:", page.url)

    # Go to Note Sheet
    page.click('a[href="https://sheet.biddyanpathshala.com"]')
    page.wait_for_timeout(3000)
    print("Navigated to Note Sheet Page:", page.url)

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Phase 1: Login and go to Note Sheet
        login_and_goto_note_sheet(page)

        # View the lecture (Eye icon)
        page.click('svg.ionicon.s-ion-icon[viewBox="0 0 512 512"]')
        page.wait_for_timeout(3000)
        print("Lecture sheet viewed successfully")

        # Return to Login page after viewing
        page.goto("https://biddyanpathshala.com/login/")
        print("Returned to Login page")

        # Phase 2: Login again and go to Note Sheet
        login_and_goto_note_sheet(page)

        # Download the lecture sheet
        page.click('a.button[download]')
        page.wait_for_timeout(3000)
        print("Lecture sheet downloaded successfully")

        browser.close()

if __name__ == "__main__":
    run()

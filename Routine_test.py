from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to home page
        page.goto("https://biddyanpathshala.com")
        page.wait_for_timeout(2000)
        print("Navigated to Home Page:", page.url)

        # View 1st routine
        page.click('button.routine_student[data-session="2025"][data-class="06"][data-dep="1"][data-batch="A"]')
        print("Opened 1st routine")
        page.wait_for_timeout(3000)

        # Close 1st routine
        page.click('path[d="M368 368L144 144M368 144L144 368"]')
        print("Closed 1st routine")
        page.wait_for_timeout(2000)

        # View 2nd routine
        page.click('button.routine_student[data-session="2025"][data-class="06"][data-dep="2"][data-batch="A"]')
        print("Opened 2nd routine")
        page.wait_for_timeout(3000)

        # Close 2nd routine
        page.click('path[d="M368 368L144 144M368 144L144 368"]')
        print("Closed 2nd routine")
        page.wait_for_timeout(2000)

        # View 3rd routine
        page.click('button.routine_student[data-session="2025"][data-class="07"][data-dep="1"][data-batch="A"]')
        print("Opened 3rd routine")
        page.wait_for_timeout(3000)

        # Close 3rd routine
        page.click('path[d="M368 368L144 144M368 144L144 368"]')
        print("Closed 3rd routine")
        page.wait_for_timeout(2000)

        browser.close()

if __name__ == "__main__":
    run()

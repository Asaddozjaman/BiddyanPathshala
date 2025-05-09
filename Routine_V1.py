from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://biddyanpathshala.com")
        page.wait_for_timeout(2000)
        print("Navigated to Home Page:", page.url)
        assert "biddyanpathshala.com" in page.url, "Failed to open homepage"

        routines = [
            ('button.routine_student[data-session="2025"][data-class="06"][data-dep="1"][data-batch="A"]', "1st"),
            ('button.routine_student[data-session="2025"][data-class="06"][data-dep="2"][data-batch="A"]', "2nd"),
            ('button.routine_student[data-session="2025"][data-class="07"][data-dep="1"][data-batch="A"]', "3rd")
        ]

        for selector, label in routines:
            assert page.is_visible(selector), f"{label} routine button not found"
            page.click(selector)
            print(f"Opened {label} routine")

            page.wait_for_timeout(3000)
            assert page.is_visible('path[d="M368 368L144 144M368 144L144 368"]'), f"{label} routine modal did not open"

            page.click('path[d="M368 368L144 144M368 144L144 368"]')
            print(f"Closed {label} routine")
            page.wait_for_timeout(2000)

        browser.close()

if __name__ == "__main__":
    run()

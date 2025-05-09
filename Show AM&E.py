from playwright.sync_api import sync_playwright

def view_academic_members_and_employees():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://biddyanpathshala.com")
        page.wait_for_timeout(2000)
        print("Opened homepage:", page.url)

        faculty_heading = page.locator('text=Academic Members and Employees')
        faculty_heading.scroll_into_view_if_needed()

        scroll_height = page.evaluate("document.documentElement.scrollHeight")
        current_scroll_position = 0
        scroll_step = 100

        while current_scroll_position < scroll_height:
            page.evaluate(f"window.scrollTo(0, {current_scroll_position})")
            current_scroll_position += scroll_step
            page.wait_for_timeout(500)

        members = page.locator(".faculty-heading + ul li")
        member_names = members.all_text_contents()
        print("Academic Members and Employees:")
        for name in member_names:
            print(name)

        browser.close()

if __name__ == "__main__":
    view_academic_members_and_employees()

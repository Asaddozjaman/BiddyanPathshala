from playwright.sync_api import sync_playwright

def student_login_tests_v1():
    user_ids = [
        "asa", "77", "", "77"
    ]
    passwords = [
        "KPiktzmt", "12345", "", "KPiktzmt"
    ]
    expected = [0, 0, 0, 1]  # 1 = success, 0 = fail
    actual = [0] * len(user_ids)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        for i in range(len(user_ids)):
            print(f"\n Test {i+1}: Trying student ID: '{user_ids[i]}' with password: '{passwords[i]}'")

            # Step 1: Go to homepage
            page.goto("https://biddyanpathshala.com")
            page.wait_for_timeout(1000)

            # Step 2: Click login
            page.click('a.login')
            page.wait_for_timeout(1000)

            # Step 3: Choose student login
            page.click("#student_login_option")
            page.wait_for_timeout(500)

            # Step 4: Enter credentials
            page.fill('#student_id', user_ids[i])
            page.fill('#student_pass', passwords[i])
            page.wait_for_timeout(500)

            # Step 5: Submit form
            page.click('#student_login_submit')
            page.wait_for_timeout(2000)

            # Step 6: Check result
            current_url = page.url
            print("After login attempt, URL is:", current_url)

            if current_url == "https://biddyanpathshala.com/dashboard/":
                actual[i] = 1
                print("Login successful.")
            else:
                print("Login failed.")

            # Step 7: Go back to homepage to reset login state
            page.goto("https://biddyanpathshala.com")
            page.wait_for_timeout(1000)

        browser.close()

        # Print summary
        print("\n=== Test Summary ===")
        for i in range(len(user_ids)):
            result = "Passed" if actual[i] == expected[i] else "Failed"
            print(f"Test {i+1}: {result} | Expected: {expected[i]} | Actual: {actual[i]}")

if __name__ == "__main__":
    student_login_tests_v1()

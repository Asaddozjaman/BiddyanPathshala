from playwright.sync_api import sync_playwright

def teacher_login_tests_v1():
    usernames = [
        "asad@biddyan", "as@biddyan", "as@biddyan", "", "asad@biddyan"
    ]
    passwords = [
        "125", "12345", "125", "", "12345"
    ]
    expected = [1, 0, 0, 0, 0]  # 1 = success, 0 = fail
    actual = [0] * len(usernames)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        for i in range(len(usernames)):
            print(f"\n Test {i+1}: Trying username: '{usernames[i]}' and password: '{passwords[i]}'")

            # Step 1: Go to home page
            page.goto("https://biddyanpathshala.com")
            page.wait_for_timeout(1000)

            # Step 2: Click login
            page.click('a.login')

            # Step 3: Choose teacher login
            page.click("#teacher_login_option")

            # Step 4: Enter credentials
            page.fill('#user_name', usernames[i])
            page.fill('#user_pass', passwords[i])

            # Step 5: Submit form
            page.click('#teacher_login_submit')
            page.wait_for_timeout(1000)

            # Step 6: Check result
            current_url = page.url
            print("After login attempt, URL is:", current_url)

            if current_url == "https://biddyanpathshala.com/dashboard/":
                actual[i] = 1
                print("Login successful.")
            else:
                print("Login failed.")

            # Step 7: Go back to homepage to reset state for next login
            page.goto("https://biddyanpathshala.com")
            page.wait_for_timeout(2000)

        browser.close() 

        # Summary
        print("\n=== Test Summary ===")
        for i in range(len(usernames)):
            result = "Passed" if actual[i] == expected[i] else "Failed"
            print(f"Test {i+1}: {result} | Expected: {expected[i]} | Actual: {actual[i]}")

if __name__ == "__main__":
    teacher_login_tests_v1()

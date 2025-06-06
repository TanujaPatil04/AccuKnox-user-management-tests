import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.admin_user_page import AdminUserPage

@pytest.mark.asyncio
async def test_user_management_flow():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        login_page = LoginPage(page)
        admin_page = AdminUserPage(page)

        # 1. Login and Navigate to Admin
        await login_page.goto()
        await login_page.login("Admin", "admin123")
        await admin_page.navigate_to_admin()

        # 2. Add a New User
        await admin_page.add_user(
            role="ESS",
            emp_name="Linda Anderson",
            username="accuknox_testuser",
            status="Enabled",
            password="Test@1234"
        )

        # 3. Search the Newly Created User
        await admin_page.search_user("accuknox_testuser")

        # 4. Edit User Details (change status to Disabled)
        await admin_page.edit_user("accuknox_testuser", new_status="Disabled")

        # 5. Validate Updated Details
        await admin_page.validate_user_status("accuknox_testuser", "Disabled")

        # 6. Delete the User
        await admin_page.delete_user("accuknox_testuser")

        await browser.close()

class AdminUserPage:
    def __init__(self, page):
        self.page = page

    async def navigate_to_admin(self):
        await self.page.click('span:has-text("Admin")')
        await self.page.wait_for_selector('h6:has-text("System Users")')

    async def add_user(self, role, emp_name, username, status, password):
        await self.page.click('button:has-text("Add")')
        await self.page.click('label:has-text("User Role") + div')
        await self.page.click(f'div[role="option"]:has-text("{role}")')
        await self.page.fill('input[placeholder="Type for hints..."]', emp_name)
        await self.page.wait_for_selector(f'div[role="option"]:has-text("{emp_name}")')
        await self.page.click(f'div[role="option"]:has-text("{emp_name}")')
        await self.page.fill('input[autocomplete="off"]', username)
        await self.page.click('label:has-text("Status") + div')
        await self.page.click(f'div[role="option"]:has-text("{status}")')
        pw_fields = self.page.locator('input[type="password"]')
        await pw_fields.nth(0).fill(password)
        await pw_fields.nth(1).fill(password)
        await self.page.click('button:has-text("Save")')
        await self.page.wait_for_selector('div.oxd-toast-content')

    async def search_user(self, username):
        await self.page.fill('div.oxd-form-row input[autocomplete="off"]', username)
        await self.page.click('button:has-text("Search")')
        await self.page.wait_for_selector(f'div.oxd-table-cell:has-text("{username}")')

    async def edit_user(self, username, new_status):
        row = self.page.locator(f'div.oxd-table-row:has-text("{username}")')
        await row.locator('button:has([class*="bi-pencil"])').click()
        await self.page.click('label:has-text("Status") + div')
        await self.page.click(f'div[role="option"]:has-text("{new_status}")')
        await self.page.click('button:has-text("Save")')
        await self.page.wait_for_selector('div.oxd-toast-content')

    async def validate_user_status(self, username, expected_status):
        await self.search_user(username)
        row = self.page.locator(f'div.oxd-table-row:has-text("{username}")')
        assert expected_status in await row.inner_text()

    async def delete_user(self, username):
        row = self.page.locator(f'div.oxd-table-row:has-text("{username}")')
        await row.locator('button:has([class*="bi-trash"])').click()
        await self.page.click('button:has-text("Yes, Delete")')
        await self.page.wait_for_selector('div.oxd-toast-content')

class LoginPage:
    def __init__(self, page):
        self.page = page

    async def goto(self):
        await self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    async def login(self, username, password):
        await self.page.fill('input[name="username"]', username)
        await self.page.fill('input[name="password"]', password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_selector('span:has-text("Admin")')

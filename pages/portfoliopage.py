class portfoliotech:
    def __init__(self,page):
        self.page=page
        self.portfolio=page.locator("//a[text()='Portfolio']")

    def portfolio_clicking(self):
        self.portfolio.click()
        




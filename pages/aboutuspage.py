# class abouttranktech:
#     def __init__(self,page):
#         self.page=page
#         self.about=page.locator("(//a[text()='About us'])[1]")
#         self.about_title=page.locator("//div//h2[text()='Welcome to Trank Technologies!']")
#     def about_clicking(self):
#         self.about.click()
#         if(self.about_title.is_visible()):
#             print("Landed to about us page")
#             self.page.go_back()
#         else:
#             print("Failed to land into correct page")
class blogtranktech:
    def __init__(self,page):
        self.page=page
        self.blog=page.locator("(//a[text()='Blog'])[1]")
        self.blog_title=page.locator("//div//h2[text()='Latest Blogs']")
        self.appdev=page.locator('//a[@href="/blog/category/app-development/"]')
        self.appdev_title=page.locator("//h1[@class='page-title']//span[contains(text(),'App Development')]")  
        self.webdev=page.locator('//a[@href="/blog/category/web-development/"]')
        self.webdev_title=page.locator("//h1[@class='page-title']//span[contains(text(),'Web Development')]")
        self.softdev=page.locator('//a[@href="/blog/category/software-development/"]')
        self.softdev_title=page.locator("//h1[@class='page-title']//span[contains(text(),'Software Development')]")
        self.digimarket=page.locator('//a[@href="/blog/category/digital-marketing/"]')
        self.digimarket_title=page.locator("//h1[@class='page-title']//span[contains(text(),'Digital Marketing')]")
        self.emailmarket=page.locator('//a[@href="/blog/category/email-marketing/"]')
        self.emailmarket_title=page.locator("//h1[@class='page-title']//span[contains(text(),'Email Marketing')]")
        self.ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.ai_title=page.locator("//h1[@class='page-title']//span[contains(text(),'Artificial Intelligence')]")
        self.uiux_design=page.locator('//a[@href="/blog/category/ui-ux-design/"]')
        self.uiux_design_title=page.locator("//h1[@class='page-title']//span[contains(text(),'UI UX Design')]")
#blog categories
        self.content_marketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.contentmarket_title=page.locator("//h1[@class='page-title']//span[text()='Content Marketing']")
        self.crmdevelopment=page.locator('//div[@class="category-tags"]//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.crmdevelop_title=page.locator("//h1[@class='page-title']//span[text()='CRM Development']")
        self.ecommdevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.ecommdevelopment_title=page.locator("//h1[@class='page-title']//span[text()='ECommerce Development']")
        self.graphic_design=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.graphic_design_title=page.locator("//h1[@class='page-title']//span[text()='Graphic Design']")
        self.sw_IT_company=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.sw_IT_company_title=page.locator("//h1[@class='page-title']//span[text()='Software & IT Company']")
        

    def blog_clicking(self):
        self.blog_list=[self.appdev,self.webdev,self.softdev,self.digimarket,self.emailmarket,self.ai,self.uiux_design]  
        for i in self.blog_list:
            self.blog.click()
            i.click()
        if(self.appdev_title.is_visible()):
            print("Landed to App dev page page")
            self.page.go_back()
        elif(self.webdev_title.is_visible()):
            print("Landed to web dev page")
            self.page.go_back()
        elif(self.softdev_title.is_visible()):
            print("Landed to software dev page")
            self.page.go_back()
        elif(self.digimarket_title.is_visible()):
            print("Landed to digital marketing page")
            self.page.go_back()
        elif(self.emailmarket_title.is_visible()):
            print("Landed to email marketing page")
            self.page.go_back()
        elif(self.ai_title.is_visible()):
            print("Landed to AI page")
            self.page.go_back()
        elif(self.uiux_design_title.is_visible()):
            print("Landed to UI UX design page")
            self.page.go_back()
        else:
            print("Failed to land into correct page")

    #blog categories
    def blog_category_clicking(self):
        self.blog_category_list=[self.content_marketing,self.crmdevelopment,self.ecommdevelopment,self.graphic_design,self.sw_IT_company]
        for i in self.blog_category_list:
            self.blog.click()
            i.click()
        if(self.contentmarket_title.is_visible()):
            print("Landed to content marketing page")
            self.page.go_back()
        elif(self.crmdevelop_title.is_visible()):
            print("Landed to Crm dev page")
            self.page.go_back()
        elif(self.ecommdevelopment_title.is_visible()):
            print("Landed to ecommerce dev page")
            self.page.go_back()
        elif(self.graphic_design_title.is_visible()):
            print("Landed to graphic design page")
            self.page.go_back()
        elif(self.sw_IT_company_title.is_visible()):
            print("Landed to software IT company page")
            self.page.go_back()
        else:
            print("Failed to land into correct page")
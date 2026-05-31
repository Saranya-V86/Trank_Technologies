class home_footer:
    def __init__(self,page):
        self.page=page
        #Web development
        self.footer_webdev=page.locator('//div[@class="cm-footer-bottom"]//a[@href="https://www.tranktechnologies.com/web-development-company"]')
        self.footer_web_dev_title=page.locator("//li[text()='Web Development']")
        self.footer_cms_website=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.footer_cms_website_title=page.locator("//li[text()='CMS Development']")
        
        self.footer_ecommerce_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.website_dev=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.website_dev_title=page.locator("//li[text()='Website Development']")

        self.footer_customweb_portal=page.locator('//div[@class="cm-footer-bottom"]//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.footer_customweb_title=page.locator("//li[text()='Custom Web Development']")
        ##UI UX design
        self.footer_mob_app_dev=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.footer_mobapp_title=page.locator("//li[text()='Mobile App Design']")
        self.footer_responsive_web=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.footer_responsiveweb_title=page.locator("//li[text()='Responsive Design']")
        self.footer_branddesign=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.footer_brand_design_title=page.locator("//li[text()='Brand Identity']")
        ## App development
        self.footer_ios_app_dev=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.footer_iosappdev_title=page.locator("//li[text()='iOS App Development']")
        
        self.footer_android_app=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.footer_androidapp_title=page.locator("//li[text()='Android Development']")
        self.android_app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/android-app-development-company"])[1]')
        # page.locator("(//a[text()='Android App Development'])[2]")
        
        self.adroid_app_dev_title=page.locator('//li[text()="Android Development Delhi"]')
        self.app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.app_development_title=page.locator("//li[text()='Android Development Delhi']")

        self.footer_hybrid_mobapp=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.footer_hybridmobapp_title=page.locator("//li[text()='Hybrid App Development']")
        self.footer_cross_platform=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.footer_cross_platform_title=page.locator("//li[text()='Cross Platform Development']")
        self.progressive_web=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.footer_progressive_web_title=page.locator("//li[text()='Progressive App Development']")
        ## Graphic design
        self.footer_logodesign=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.footer_logodesign_title=page.locator("//li[text()='Logo Design']")
        self.footer_bannerdesign=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.footer_bannerdesign_title=page.locator("//li[text()='Banner Design']")
        self.footer_packaging_design=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.footer_packagingdesign_title=page.locator("//li[text()='Package Design']")
        self.footer_businesscard=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        self.footer_businesscard_title=page.locator("//li[text()='Business Card Design']")
        self.ecommerce_dropdown=page.locator('(//i[@aria-hidden="true"])[3]')
        self.androidapp_dropdown=page.locator('(//span[@class="toggle-btn"])[2]')

    def footer_clicking(self):
            self.footer_list=[self.footer_webdev,self.footer_customweb_portal,self.footer_mob_app_dev,self.footer_responsive_web,self.footer_branddesign,
                              self.footer_ios_app_dev,self.footer_android_app,self.footer_hybrid_mobapp,self.footer_cross_platform,self.progressive_web,self.footer_logodesign,self.footer_bannerdesign,
                              self.footer_packaging_design,self.footer_businesscard]
            
    # Handle regular links
            for i in self.footer_list:
                i.click()
                self.page.wait_for_timeout(2000)
                self.page.go_back()
                self.page.wait_for_timeout(2000)
    
    # Handle ecommerce dropdown
            self.ecommerce_dropdown.click()
            self.page.wait_for_timeout(500)
            with self.page.context.expect_page() as child_wind_info:
                self.website_dev.click()
                new_page = child_wind_info.value
                new_page.wait_for_load_state()
                new_page.close()
    
    # Handle android app dropdown
            self.androidapp_dropdown.click()
            self.page.wait_for_timeout(500)
            self.listofapp=[self.android_app_dev,self.app_development]
            for j in self.listofapp:
                with self.page.context.expect_page() as child_wind_info:
                    j.click()
                    new_page = child_wind_info.value
                    new_page.wait_for_load_state()
                    new_page.close()
            
                     
            
        #     for i in self.footer_list:
        # #  Ecommerce dropdown
        #         if i == self.ecommerce_dropdown:
        #             i.click()
        #             self.page.wait_for_timeout(500)
        #             with self.page.context.expect_page() as child_popup:
        #                 self.website_dev.click()
        #                 new_page = child_popup.value
        #                 new_page.wait_for_load_state()
        #                 new_page.close()

        # #  Android app dropdown
        #         elif i == self.androidapp_dropdown:
        #             i.click()
        #             self.page.wait_for_timeout(500)
        #         self.listofapp = [self.android_app_dev, self.app_development]
        #         for j in self.listofapp:
        #             with self.page.context.expect_page() as child_popup:
        #                 j.click()
        #                 new_page = child_popup.value
        #                 new_page.wait_for_load_state()
        #                 new_page.close()

        # #  Regular links
        #         else:
        #             i.click()
        #             self.page.wait_for_timeout(2000)
        #             self.page.go_back()
        #             self.page.wait_for_timeout(2000)
            
            
            
           
            
            #     elif(self.footer_web_dev_title.is_visible()):
            #         print("Successfully landed to Web development page")
            #         self.page.go_back()
            # # elif(self.footer_ecommerce_title.is_visible()):
            # #     print("Successfully landed to Ecommerce dev page")
            # #     self.page.go_back()
            #     elif(self.footer_customweb_title.is_visible()):
            #         print("Successfully landed to Custom web page")
            #         self.page.go_back()
            #     elif(self.footer_mobapp_title.is_visible()):
            #         print("Successfully landed to Mob application page")
            #         self.page.go_back()
            #     elif(self.footer_responsiveweb_title.is_visible()):
            #         print("Successfully landed to Responsive web page")
            #         self.page.go_back()
            #     elif(self.footer_brand_design_title.is_visible()):
            #         print("Successfully landed to Brand design page")
            #         self.page.go_back()
            #     elif(self.footer_iosappdev_title.is_visible()):
            #         print("Successfully landed to IOS page")
            #         self.page.go_back()
            #     elif(self.footer_androidapp_title.is_visible()):
            #         print("Successfully landed to Android app page")
            #         self.page.go_back()
            #     elif(self.footer_hybridmobapp_title.is_visible()):
            #         print("Successfully landed to Hybrid mob app page")
            #         self.page.go_back()
            #     elif(self.footer_cross_platform_title.is_visible()):
            #         print("Successfully landed to Cross platform page")
            #         self.page.go_back()
            #     elif(self.footer_progressive_web_title.is_visible()):
            #         print("Successfully landed to Progressive web page")
            #         self.page.go_back()
            #     elif(self.footer_logodesign_title.is_visible()):
            #         print("Successfully landed to Logo design page")
            #         self.page.go_back()
            #     elif(self.footer_bannerdesign_title.is_visible()):
            #         print("Successfully landed to Banner design page")
            #         self.page.go_back()
            #     elif(self.footer_packagingdesign_title.is_visible()):
            #         print("Successfully landed to Packaging design page")
            #         self.page.go_back()
            #     elif(self.footer_businesscard_title.is_visible()):
            #         print("Successfully landed to Business card design page")
            #         self.page.go_back()
            #     else:
            #         print("Failed to land into correct page")



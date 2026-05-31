# class vertical:
#     def __init__(self,page):
#         self.page=page
#         self.verticals = page.locator("(//a[text()='Verticals'])[1]")
#         self.trading = page.locator('//strong[text()="Trading"]')
#         self.stock_trade=page.locator('(//a[text()="Stock Trading"])[1]')
#         self.algo_trade=page.locator('(//a[text()="Algo Trading"])[1]')
#         self.paper_trade=page.locator("(//a[text()='Paper Trading'])[1]")
#         self.custom_trade=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
#         self.cfd_trade=page.locator("(//a[text()='CFD Trading'])[1]")
#         self.web_portal_trade=page.locator("(//a[text()='Web Portal Trading'])[1]")
#         self.trade_app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
#         self.stocktrading_title=page.locator("//li[text()='Stock Trading']")
#         self.algotrading_title=page.locator("//li[text()='Algo Trading']")
#         self.papertrading_title=page.locator("//li[text()='Paper Trading']")
#         self.customtrading_title=page.locator("//li[text()='Custom Trading']")
#         self.cfdtrading_title=page.locator("//li[text()='CFD Trading']")
#         self.webportaltrading_title=page.locator("//li[text()='Trading Web Portal']")
#         self.tradingmassach_title=page.locator("//li[text()='Trading in Massachusetts']")
#         # retail and commerce
#         self.retail_ecommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
#     # ecommerce_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
#         self.ecommerce_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
#         self.ecommerceapp_title=page.locator("//h1[contains(text(),'eCommerce App Development')]")
#         #Health care
#         self.health_care=page.locator("//a//strong[text()='Healthcare']")
#         self.diet_nutrition=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
#         self.health_tracking=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
#         self.diet_nut_title=page.locator("//li[text()='Diet & Nutritions']")
#         self.health_track_title=page.locator("//li[text()='Health Tracking App']")
#         #Fintech
#         self.fin_tech=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
#         self.pos_sw_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
#         self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
#         self.possw_title=page.locator("//li[contains(text(),'POS Software Development')]")
#         self.crypto_title=page.locator("//li[text()='Crypto']")
#         #customapp
#         self.custom_app=page.locator('(//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/custom-mob.png"])[1]')
#         self.desktop_app=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
#         self.crm_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
#         self.hrm_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
#         self.erp_app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
#         self.travel=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
#         self.elearning=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
#         self.dating_app=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
#         self.real_estate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
#         self.crmsw_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
#         self.desktopapp_title=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[3]')
#         self.crmdev_title=page.locator("(//a[text()='CRM Development'])[3]")
#         self.hrmdev_title=page.locator("(//a[text()='HRM Development'])[3]")
#         self.erpdev_title=page.locator("//li[text()='ERP App Development']")
#         self.travel_title=page.locator("//li[text()='Travel App Development']")
#         self.elearning_title=page.locator("//li[text()='E-Learning']")
#         self.dating_title=page.locator("//li[text()='Dating App']")
#         self.realestate_title=page.locator("//li[text()='Real Estate']")
#         self.crmswdev_title=page.locator("//h1[contains(text(),'CRM Software Development ')]")


#     def verticals_mouse_hover(self):
#         self.verticals.hover()
#         # self.page.wait_for_timeout(3000)
#     def trading_mouse_hover(self):
#         self.trading.hover()
#         # self.page.wait_for_timeout(3000)
#     def trade_clicking(self):
#         self.vert_list=[self.stock_trade,self.algo_trade,self.paper_trade,self.custom_trade,self.cfd_trade,
#                         self.web_portal_trade,self.trade_app_dev]
#         for i in self.vert_list:
#             self.verticals_mouse_hover()
#             self.trading_mouse_hover()
#             # self.page.wait_for_timeout(3000)
#             i.click()
            
#             if(self.stocktrading_title.is_visible()):
#                 print("Successfully landed to stock trading page")
#                 self.page.go_back()
#             elif(self.algotrading_title.is_visible()):
#                 print("Successfully landed to algo trading page")
#                 self.page.go_back()
#             elif(self.papertrading_title.is_visible()):
#                 print("Successfully landed to paper trading page")
#                 self.page.go_back()
#             elif(self.customtrading_title.is_visible()):
#                 print("Successfully landed to custom trading page")
#                 self.page.go_back()
#             elif(self.cfdtrading_title.is_visible()):
#                 print("Successfully landed to CFD trading page")
#                 self.page.go_back()
#             elif(self.webportaltrading_title.is_visible()):
#                 print("Successfully landed to Web Portal trading page")
#                 self.page.go_back()
#             elif(self.tradingmassach_title.is_visible()):
#                 print("Successfully landed to trading page")
#                 self.page.go_back()
#             else:
#                 print("Failed to land to correct page")

# # Retail ecommerce
#     def retail_ecommerce_hover(self):
#         self.retail_ecommerce.hover()
   
#     def retail_ecommerce_clicking(self):
#         self.retail_ecomm_list=[self.ecommerce_app]
#         for i in self.retail_ecomm_list:
#             self.verticals_mouse_hover()
#             self.retail_ecommerce_hover()
#             # self.page.wait_for_timeout(3000)
#             i.click()
            
#             if(self.ecommerceapp_title.is_visible()):
#                 print("Successfully landed to retail and ecommerce trading page")
#                 self.page.go_back()
#             else:
#                 print("Failed to land to correct page")

# # Health Care
#     def health_care_hover(self):
#         self.health_care.hover()
   
#     def health_care_clicking(self):
#         self.health_care_list=[self.diet_nutrition,self.health_tracking]
#         for i in self.health_care_list:
#             self.verticals_mouse_hover()
#             self.health_care_hover()
#             # self.page.wait_for_timeout(3000)
#             i.click()
            
#             if(self.diet_nut_title.is_visible()):
#                 print("Successfully landed to Diet and Nutrient page")
#                 self.page.go_back()
#             elif(self.health_track_title.is_visible()):
#                 print("Successfully landed into Health track page")
#                 self.page.go_back()
#             else:
#                 print("Failed to land to correct page")

# # Fintech
#     def fintech_hover(self):
#         self.fin_tech.hover()
   
#     def fin_tech_clicking(self):
#         self.fin_tech_list=[self.pos_sw_dev,self.crypto]
#         for i in self.fin_tech_list:
#             self.verticals_mouse_hover()
#             self.fintech_hover()
#             # self.page.wait_for_timeout(3000)
#             i.click()
            
#             if(self.possw_title.is_visible()):
#                 print("Successfully landed to pos sw page")
#                 self.page.go_back()
#             elif(self.crypto_title.is_visible()):
#                 print("Successfully landed into crypto dev page")
#                 self.page.go_back()
#             else:
#                 print("Failed to land to correct page")

# # Custom App
#     def custom_app_hover(self):
#         self.custom_app.hover()
   
#     def custom_app_clicking(self):
#         self.custom_app_list=[self.desktop_app,self.crm_dev,self.hrm_dev,self.erp_app_dev,self.travel,self.elearning,
#                               self.dating_app,self.real_estate,self.crmsw_dev,self.desktop_app]
#         for i in self.custom_app_list:
#             self.verticals_mouse_hover()
#             self.custom_app_hover()
#             # self.page.wait_for_timeout(3000)
#             i.click()
            
#             if(self.desktopapp_title.is_visible()):
#                 print("Successfully landed in desktop page")
#                 self.page.go_back()
#             elif(self.crmdev_title.is_visible()):
#                 print("Successfully landed CRM dev page")
#                 self.page.go_back()
#             elif(self.hrmdev_title.is_visible()):
#                 print("Successfully landed HRM dev page")
#                 self.page.go_back()
#             elif(self.erpdev_title.is_visible()):
#                 print("Successfully landed ERP dev page")
#                 self.page.go_back()
#             elif(self.travel_title.is_visible()):
#                 print("Successfully landed Travel page")
#                 self.page.go_back()
#             elif(self.elearning_title.is_visible()):
#                 print("Successfully landed Elearning page")
#                 self.page.go_back()
#             elif(self.dating_title.is_visible()):
#                 print("Successfully landed Dating page")
#                 self.page.go_back()
#             elif(self.realestate_title.is_visible()):
#                 print("Successfully landed Real estate page")
#                 self.page.go_back()
#             elif(self.crmswdev_title.is_visible()):
#                 print("Successfully landed CRM sw dev page")
#                 self.page.go_back()
#             else:
#                 print("Failed to land to correct page")
            
# class technology:
#     def __init__(self,page):
#         self.page=page
#         self.technologies=page.locator("(//a[text()='Technologies'])[1]")
#         self.ecommerce_dev=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ecomm-mob.png"]')
#         self.magento_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
#         self.opencart_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
#         self.codeignite_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
#         self.wordpress_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
#         self.big_commerce=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
#         self.shopify_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
#         self.cscart_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
#         self.node_js_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
#         self.nop_commerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
#         self.woo_commerce=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
#         self.laravel_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
#         self.prestashop_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
#         self.drupal_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
#         self.wix_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
#         self.joomla_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
#         self.express_js_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
#         self.magentodev_title=page.locator("//li[text()='Magento Development']")
#         self.opencartdev_title=page.locator("//li[text()='OpenCart Development']")
#         self.codeigniter_title=page.locator("//li[text()='Codeigniter Development']")
#         self.wordpress_title=page.locator("//li[text()='Wordpress Development']")
#         self.bigcommerce_title=page.locator("//li[text()='Big Commerce Development']")
#         self.shopify_title=page.locator("//li[text()='Shopify Development']")
#         self.cscart_title=page.locator("//li[text()='CS-Cart Development']")
#         self.nodejs_title=page.locator("//li[text()='Node JS Development']")
#         self.nopcommerce_title=page.locator("//li[text()='Nop Commerce Development']")
#         self.woocommerce_title=page.locator("//li[text()='Woo Commerce Development']")
#         self.laraveldev_title=page.locator("//li[text()='Laravel Development']")
#         self.prestashop_title=page.locator("//li[text()='Prestashop Development']")
#         self.drupal_title=page.locator("//li[text()='Drupal Development']")
#         self.wix_title=page.locator("//li[text()='Wix Development']")
#         self.joomla_title=page.locator("//li[text()='Joomla Development']")
#         self.reactjs_title=page.locator("//li[text()='React JS Development']")
#         self.expressjs_title=page.locator("//li[text()='Express JS Development']")
# #Mobile app development
#         self.mobile_app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-development-company"])[1]')
#         self.react_native_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
#         self.enterprise_app=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
#         self.xmarian_app=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
#         self.kotlin_app=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
#         self.flutter_app=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
#         self.ionic_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
#         self.swift_app=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
#         self.appointment_book=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
#         self.reactivenative_title=page.locator("//li[text()='React Native Development']")
#         self.enterprise_title=page.locator("//li[text()='Enterprise Development']")
#         self.xarmin_title=page.locator("//li[text()='Xarmin Development']")
#         self.kotlin_title=page.locator("//li[text()='Kotlin Development']")
#         self.flutter_title=page.locator("//li[text()='Flutter Development']")
#         self.iconic_title=page.locator("//li[text()='Iconic Development']")
#         self.swift_title=page.locator("//li[text()='Swift Development']")
#         self.appointment_title=page.locator("//li[text()='Appointment Development']")

        
#     def technologies_mouse_hover(self):
#         self.technologies.hover()
#         # self.page.wait_for_timeout(3000)
#     def ecommerce_mouse_hover(self):
#         self.ecommerce_dev.hover()
#         # self.page.wait_for_timeout(3000)
#     def ecomm_clicking(self):
#         self.ecomm_dev_list=[self.magento_dev,self.opencart_dev,self.codeignite_dev,self.wordpress_dev,self.big_commerce,self.shopify_dev,
#     self.cscart_dev,self.node_js_dev,self.nop_commerce,self.woo_commerce,self.laravel_dev,self.prestashop_dev,self.drupal_dev,self.wix_dev,self.joomla_dev,self.express_js_dev]
#         for i in self.ecomm_dev_list:
#             self.technologies_mouse_hover()
#             self.ecommerce_mouse_hover()
#             i.click()
        
#             if(self.magentodev_title.is_visible()):
#                 print("Successfully landed in Magento dev page")
#                 self.page.go_back()
#             elif(self.opencartdev_title.is_visible()):
#                 print("Successfully landed in Opencart dev page")
#                 self.page.go_back()
#             elif(self.codeigniter_title.is_visible()):
#                 print("Successfully landed in Codeigniter dev page")
#                 self.page.go_back()
#             elif(self.wordpress_title.is_visible()):
#                 print("Successfully landed in Wordpress dev page")
#                 self.page.go_back()
#             elif(self.bigcommerce_title.is_visible()):
#                 print("Successfully landed in Big commerce dev page")
#                 self.page.go_back()
#             elif(self.shopify_title.is_visible()):
#                 print("Successfully landed in Shopify dev page")
#                 self.page.go_back()
#             elif(self.cscart_title.is_visible()):
#                 print("Successfully landed in CS cart dev page")
#                 self.page.go_back()
#             elif(self.nodejs_title.is_visible()):
#                 print("Successfully landed in Node js dev page")
#                 self.page.go_back()
#             elif(self.nopcommerce_title.is_visible()):
#                 print("Successfully landed in NOP commerce dev page")
#                 self.page.go_back()
#             elif(self.woocommerce_title.is_visible()):
#                 print("Successfully landed in WOO commerce dev page")
#                 self.page.go_back()
#             elif(self.laraveldev_title.is_visible()):
#                 print("Successfully landed in Laravel dev page")
#                 self.page.go_back()
#             elif(self.drupal_title.is_visible()):
#                 print("Successfully landed in Drupal dev page")
#                 self.page.go_back()
#             elif(self.wix_title.is_visible()):
#                 print("Successfully landed in Wix dev page")
#                 self.page.go_back()
#             elif(self.joomla_title.is_visible()):
#                 print("Successfully landed in Joomla dev page")
#                 self.page.go_back()
#             elif(self.reactjs_title.is_visible()):
#                 print("Successfully landed in React JS dev page")
#                 self.page.go_back()
#             elif(self.expressjs_title.is_visible()):
#                 print("Successfully landed in Express JS dev page")
#                 self.page.go_back()
#             else:
#                 print("Failed to land in correct page")


#     def mob_app_dev_hover(self):
#         self.mobile_app_dev.hover()
#         # self.page.wait_for_timeout(3000)
#     def mobile_app_dev_clicking(self):
#         self.mobile_app_list=[self.react_native_dev,self.enterprise_app,self.xmarian_app,self.kotlin_app,
#                               self.flutter_app,self.ionic_dev,self.swift_app,self.appointment_book]

#         for i in self.mobile_app_list:
#             self.technologies_mouse_hover()
#             self.mob_app_dev_hover()
#             i.click()
#             if(self.reactivenative_title.is_visible()):
#                 print("Successfully landed in Reactive native dev page")
#                 self.page.go_back()
#             elif(self.enterprise_title.is_visible()):
#                 print("Successfully landed in enterprise page")
#                 self.page.go_back()
#             elif(self.xarmin_title.is_visible()):
#                 print("Successfully landed in Xarmin dev page")
#                 self.page.go_back()
#             elif(self.kotlin_title.is_visible()):
#                 print("Successfully landed in Kotlin dev page")
#                 self.page.go_back()
#             elif(self.flutter_title.is_visible()):
#                 print("Successfully landed in Flutter dev page")
#                 self.page.go_back()
#             elif(self.iconic_title.is_visible()):
#                 print("Successfully landed in ReactivIconic dev page")
#                 self.page.go_back()
#             elif(self.swift_title.is_visible()):
#                 print("Successfully landed in Swift dev page")
#                 self.page.go_back()
#             elif(self.appointment_title.is_visible()):
#                 print("Successfully landed in Appointment dev page")
#                 self.page.go_back()
#             else:
#                 print("Failed to land in correct page")

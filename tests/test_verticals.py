from pages.verticalspage import vertical
import pytest

@pytest.mark.smoke
def test_vertical_tech(page):
    ver=vertical(page)
    ver.trade_clicking()
    ver.retail_ecommerce_clicking()
    ver.health_care_clicking()
    ver.fin_tech_clicking()
    ver.custom_app_clicking()


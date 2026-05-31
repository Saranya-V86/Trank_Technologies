from pages.homefooterpage import home_footer
import pytest

@pytest.mark.smoke
def test_footer(page):
    ft=home_footer(page)
    ft.footer_clicking()
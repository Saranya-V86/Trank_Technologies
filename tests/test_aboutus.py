from pages.aboutuspage import abouttranktech
import pytest

@pytest.mark.smoke
def test_aboutus(page):
    abt=abouttranktech(page)
    abt.about_clicking()
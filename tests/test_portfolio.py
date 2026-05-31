from pages.portfoliopage import portfoliotech
import pytest

@pytest.mark.smoke

def test_port(page):
    por=portfoliotech(page)
    por.portfolio_clicking()
    
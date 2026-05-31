from pages.blogpage import blogtranktech
import pytest

@pytest.mark.smoke
def test_blog_tech(page):
    blg=blogtranktech(page)
    blg.blog_clicking()
    blg.blog_category_clicking()
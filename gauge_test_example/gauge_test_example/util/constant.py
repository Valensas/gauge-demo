import os
import logging
os.getenv('gauge_environment')

BASE_URL = os.environ.get('BASE_URL')

PRODUCT_CATEGORY_LIST = [
    "smartphones",
    "laptops",
    "fragrances",
    "skincare",
    "groceries",
    "home-decoration"
]
from getgauge.python import data_store, step
from util.constant import BASE_URL, PRODUCT_CATEGORY_LIST
import requests
import logger_lib.logger as log
logger = log.getLogger(__name__)


@step("Get all products")
def get_all_products():
    url_suffix = "products"
    url = BASE_URL + url_suffix
    response = requests.get(url=url)
    if not response.ok:
        msg = "Endpoint test error case is failed for url: {}".format(
            url
        )
        logger.error_and_throw_exception(msg)
    success_msg = "Products received successfully"
    all_products = response.json()
    if "all_products" not in data_store.scenario:
        data_store.scenario["all_products"] = {}
    data_store.scenario["all_products"] = all_products["products"]
    logger.info(success_msg)


@step("Check categories of products")
def check_categories():
    all_products = data_store.scenario["all_products"]
    for selected_product in all_products:
        if selected_product["category"] not in PRODUCT_CATEGORY_LIST:
            msg = "product {} is not in the category list".format(
                selected_product["category"]
            )
            logger.error_and_throw_exception(msg)
    success_msg = "All product categories checked"
    logger.info(success_msg)


@step("Check product stock quantity as <number_of_products>")
def check_stock(number_of_products):
    all_products = data_store.scenario["all_products"]
    for selected_product in all_products:
        if int(number_of_products) > selected_product["stock"]:
            msg = "The stock quantity of product {} remains {}".format(
                selected_product["category"], selected_product["stock"]
            )
            logger.error_and_throw_exception(msg)
    success_msg = "Product stocks are up to date"
    logger.info(success_msg)


@step("Find the cheapest product price")
def find_cheapest_product():
    all_products = data_store.scenario["all_products"]
    products_price = []
    for selected_product in all_products:
        products_price.append(selected_product["price"])
    msg = "The cheapest product price is {}".format(
        min(products_price)
    )
    logger.info(msg)

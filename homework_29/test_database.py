from operations import create_table, add_product, get_products, update_product, delete_product
from database import get_connection
from assertpy import assert_that, soft_assertions
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    create_table()

def test_db_connection():
    connection = get_connection()
    assert connection is not None
    connection.close()

@pytest.mark.parametrize(
    "name, category, animal_type, price, quantity",
    [
        ("Whiskas", "Food", "Cat", 120.00, 20),
        ("Royal Canin", "Food", "Dog", 0, 10),
        ("Toy", "Accessories", "Cat", 50.00, 0),
        ("Unknown", "Food", "Cat", None, 5),
    ]
)
def test_add_product(name, category, animal_type, price, quantity):
    add_product(name, category, animal_type, price, quantity)
    products = get_products()
    product = next(product for product in products if product[1] == name)

    with soft_assertions():
        assert_that(product[1]).described_as(
            "Product name should match"
        ).is_equal_to(name)

        assert_that(product[2]).described_as(
            "Product category should match"
        ).is_equal_to(category)

        assert_that(product[3]).described_as(
            "Animal type should match"
        ).is_equal_to(animal_type)

        assert_that(product[4]).described_as(
            "Product price should match"
        ).is_equal_to(price)

        assert_that(product[5]).described_as(
            "Product quantity should match"
        ).is_equal_to(quantity)


@pytest.mark.parametrize(
    "new_price, new_quantity",
    [
        (200.00, 30),
        (0, 0),
        (None, 10),
    ]
)
def test_update_product(new_price, new_quantity):
    name = "Update test product"

    add_product(name, "Food", "Cat", 100.00, 10)

    products = get_products()
    product = next(product for product in products if product[1] == name)
    product_id = product[0]

    update_product(product_id, new_price, new_quantity)

    updated_products = get_products()
    updated_product = next(
        product for product in updated_products if product[0] == product_id
    )

    with soft_assertions():
        assert_that(updated_product[4]).described_as(
            f"Price should be {new_price}"
        ).is_equal_to(new_price)

        assert_that(updated_product[5]).described_as(
            f"Quantity should be {new_quantity}"
        ).is_equal_to(new_quantity)

def test_delete_product():
    name = "Delete test product"

    add_product(name, "Food", "Cat", 100.00, 10)

    products = get_products()
    product = next(product for product in products if product[1] == name)
    product_id = product[0]

    delete_product(product_id)

    deleted_products = get_products()

    with soft_assertions():
        assert_that(
            any(product[0] == product_id for product in deleted_products)
        ).described_as(
            f"Product with ID {product_id} should be deleted"
        ).is_false()

def test_select_product():
    name = "Select test product"

    add_product(name, "Food", "Cat", 150.00, 15)

    products = get_products()
    product = next(product for product in products if product[1] == name)

    with soft_assertions():
        assert_that(product[1]).described_as(
            "Product name should match"
        ).is_equal_to(name)

        assert_that(product[2]).described_as(
            "Product category should match"
        ).is_equal_to("Food")

        assert_that(product[3]).described_as(
            "Animal type should match"
        ).is_equal_to("Cat")

        assert_that(product[4]).described_as(
            "Product price should match"
        ).is_equal_to(150.00)

        assert_that(product[5]).described_as(
            "Product quantity should match"
        ).is_equal_to(15)
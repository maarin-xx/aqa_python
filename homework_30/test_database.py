from operations import create_table, add_product, get_products, update_product, delete_product
from database import get_connection
from assertpy import assert_that, soft_assertions
import pytest
import allure

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    create_table()

@allure.epic("Dockerizate everything - Product Management")
@allure.feature("Product CRUD")
@allure.story("Database Connection")
@allure.title("Verify database connection")
@allure.description("Verify that the application can successfully connect to PostgreSQL database.")
@allure.severity(allure.severity_level.BLOCKER) #if there is no connection to the database, no products operations will work
@allure.tag("database", "postgresql", "connection")
def test_db_connection():
    connection = get_connection()
    assert connection is not None
    connection.close()

@allure.epic("Dockerizate everything - Product Management")
@allure.feature("Product CRUD")
@allure.story("Add Product")
@allure.title("Verify that a product can be added")
@allure.description("Verify that product details are correctly saved in PostgreSQL database")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("database", "postgresql", "insert")
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
    with allure.step(f"Add product: {name} to database"):
        add_product(name, category, animal_type, price, quantity)

    with allure.step("Retrieve products from database"):
        products = get_products()

    with allure.step(f"Find product: {name}"):
        product = next(product for product in products if product[1] == name)

    with allure.step("Verify product details"):
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

@allure.epic("Dockerizate everything - Product Management")
@allure.feature("Product CRUD")
@allure.story("Update Product")
@allure.title("Verify that a product can be updated")
@allure.description("Verify that price and quantity are correctly saved in PostgreSQL database after update")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("database", "postgresql", "update")
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

    with allure.step("Add product to database"):
        add_product(name, "Food", "Cat", 100.00, 10)

    with allure.step("Get product ID"):
        products = get_products()
        product = next(product for product in products if product[1] == name)
        product_id = product[0]

    with allure.step("Update product details"):
        update_product(product_id, new_price, new_quantity)

    with allure.step("Retrieve updated product"):
        updated_products = get_products()
        updated_product = next(
            product for product in updated_products if product[0] == product_id
        )

    with allure.step("Verify updated product details"):
        with soft_assertions():
            assert_that(updated_product[4]).described_as(
                f"Price should be {new_price}"
            ).is_equal_to(new_price)

            assert_that(updated_product[5]).described_as(
                f"Quantity should be {new_quantity}"
            ).is_equal_to(new_quantity)

@allure.epic("Dockerizate everything - Product Management")
@allure.feature("Product CRUD")
@allure.story("Delete Product")
@allure.title("Verify that a product can be deleted")
@allure.description("Verify that product can be deleted from PostgreSQL database")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("database", "postgresql", "delete")
def test_delete_product():
    name = "Delete test product"

    with allure.step("Add product to database"):
        add_product(name, "Food", "Cat", 100.00, 10)

    with allure.step("Get product ID"):
        products = get_products()
        product = next(product for product in products if product[1] == name)
        product_id = product[0]

    with allure.step("Delete product from database"):
        delete_product(product_id)

    with allure.step("Retrieve products from database"):
        deleted_products = get_products()

    with allure.step("Verify product was deleted"):
        with soft_assertions():
            assert_that(
                any(product[0] == product_id for product in deleted_products)
            ).described_as(
                f"Product with ID {product_id} should be deleted"
            ).is_false()

@allure.epic("Dockerizate everything - Product Management")
@allure.feature("Product CRUD")
@allure.story("Select Product")
@allure.title("Verify that a product can be selected")
@allure.description("Verify that valid data selected from PostgreSQL database for specific product")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("database", "postgresql", "select")
def test_select_product():
    name = "Select test product"

    with allure.step("Add product to database"):
        add_product(name, "Food", "Cat", 150.00, 15)

    with allure.step("Retrieve product from database"):
        products = get_products()
        product = next(product for product in products if product[1] == name)

    with allure.step("Verify selected product details"):
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
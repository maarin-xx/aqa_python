import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
from assertpy import assert_that, soft_assertions
from marshmallow import Schema, fields, ValidationError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("test_search.log", encoding="utf-8")
    ],
    force=True
)

class CarsSchema(Schema):
    brand = fields.String(required=True)
    engine_volume = fields.Float(required=True)
    price = fields.Float(required=True)
    year = fields.Integer(required=True, strict=True)


def check_status_code(response, expected_status_code):
    try:
        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, "
            f"got {response.status_code}"
        )
    except AssertionError as error:
        logging.error(f"Status code check failed: {error}")
        raise

@pytest.fixture(scope="class")
def authorized_session():
    session = requests.Session()
    response = session.post(
        "http://127.0.0.1:8080/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    check_status_code(response, 200)

    token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

class TestCarsSearch:

    def test_login_success(self):
        logging.info("Starting successful login test")
        response = requests.post(
            "http://127.0.0.1:8080/auth",
            auth=HTTPBasicAuth("test_user", "test_pass")
        )

        check_status_code(response, 200)

        assert "access_token" in response.json()

        assert isinstance(response.json()["access_token"], str)
        assert len(response.json()["access_token"]) > 0
        logging.info("Login successful")

    @pytest.mark.parametrize(
        "limit, expected_count",
        [
            (1, 1),
            (5, 5),
            (10, 10),
        ]
    )
    def test_cars_response(self, authorized_session, limit, expected_count):
        logging.info(f"Checking cars response: limit={limit}")

        response = authorized_session.get(
            "http://127.0.0.1:8080/cars",
            params={"limit": limit}
        )

        check_status_code(response, 200)

        cars = response.json()

        with soft_assertions():
            assert_that(cars).is_instance_of(list)
            assert_that(len(cars)).is_equal_to(expected_count)

        logging.info(f"Cars response is valid: received {len(cars)} cars")

    @pytest.mark.parametrize(
        "sort_by",
        ["price", "brand", "year", "engine_volume"]
    )
    def test_cars_sorting(self, authorized_session, sort_by):
        logging.info(f"Checking cars sorting: sort_by={sort_by}")

        response = authorized_session.get(
            "http://127.0.0.1:8080/cars",
            params={"sort_by": sort_by}
        )

        check_status_code(response, 200)

        cars = response.json()
        values = [car[sort_by] for car in cars]

        assert values == sorted(values), (
            f"Cars are not sorted by '{sort_by}'"
        )

        logging.info(f"Cars are correctly sorted by '{sort_by}'")
    def test_type_of_data(self, authorized_session):
        logging.info("Checking data types in cars response")

        response = authorized_session.get(
            "http://127.0.0.1:8080/cars"
        )

        check_status_code(response, 200)

        cars = response.json()
        schema = CarsSchema(many=True)

        try:
            schema.load(cars)
        except ValidationError as error:
            logging.error(f"Data validation failed: {error.messages}")
            raise

        logging.info(f"Data types are valid for {len(cars)} cars")

    def test_unauthorized_access(self):

        logging.info("Checking access to cars without authorization")

        response = requests.get("http://127.0.0.1:8080/cars")

        check_status_code(response, 401)

        logging.info("Unauthorized access correctly rejected")

    def test_login_unknown_user(self):
        logging.info("Checking login with an unknown username")

        response = requests.post(
            "http://127.0.0.1:8080/auth",
            auth=HTTPBasicAuth("unknown_user", "test_pass")
        )

        check_status_code(response, 401)

        logging.info("Login correctly rejected for an unknown user")

    def test_login_wrong_password(self):

        logging.info("Checking login with a wrong password")

        response = requests.post(
            "http://127.0.0.1:8080/auth",
            auth=HTTPBasicAuth("test_user", "wrong_pass")
        )

        check_status_code(response, 401)

        logging.info("Login correctly rejected with a wrong password")

    def test_invalid_token(self):
        logging.info("Checking login with an invalid token")

        response = requests.get(
            "http://127.0.0.1:8080/cars",
            headers={"Authorization": "Bearer invalid_token"}
        )
        check_status_code(response, 422)
        logging.info("Login correctly rejected with a wrong password")



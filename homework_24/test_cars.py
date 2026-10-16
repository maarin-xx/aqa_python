import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("test_search.log", encoding="utf-8")
    ],
    force=True
)


@pytest.fixture(scope="class")
def authorized_session():
    session = requests.Session()
    response = session.post(
        "http://127.0.0.1:8080/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200

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

        assert response.status_code == 200

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

        try:
            assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )

            cars = response.json()

            assert isinstance(cars, list)
            assert len(cars) == expected_count

            for car in cars:
                assert "brand" in car
                assert "engine_volume" in car
                assert "year" in car
                assert "price" in car

        except AssertionError as error:
            logging.error(f"Test failed: {error}")
            raise

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

        try:
            assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )

            cars = response.json()

            values = [car[sort_by] for car in cars]
            assert values == sorted(values), (
            f"Cars are not sorted by '{sort_by}'"
        )

        except AssertionError as error:
            logging.error(f"Cars sorting test failed: {error}")
            raise

        logging.info(f"Cars are correctly sorted by '{sort_by}'")


    def test_type_of_data(self, authorized_session):

        logging.info("Checking data types in cars response")

        response = authorized_session.get("http://127.0.0.1:8080/cars"
        )
        try:
            assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )

            cars = response.json()

            for car in cars:
                assert isinstance(car["brand"], str), (
                    f"Expected brand to be str, got {type(car['brand']).__name__}"
                )
                assert isinstance(car["engine_volume"], (int, float)), (
                    f"Expected engine_volume to be numeric, got {type(car['engine_volume']).__name__}"
                )
                assert isinstance(car["year"], int), (
                    f"Expected year to be int, got {type(car['year']).__name__}"
                )
                assert isinstance(car["price"], (int, float)), (
                    f"Expected price to be numeric, got {type(car['price']).__name__}"
                )
        except AssertionError as error:
            logging.error(f"Data types test failed: {error}")
            raise

        logging.info(f"Data types are valid for {len(cars)} cars")

    def test_unauthorized_access(self):

        logging.info("Checking access to cars without authorization")

        response = requests.get("http://127.0.0.1:8080/cars")

        try:
            assert response.status_code == 401, (
                f"Expected status code 401, got {response.status_code}"
            )

        except AssertionError as error:
            logging.error(f"Unauthorized access test failed: {error}")
            raise

        logging.info("Unauthorized access correctly rejected")

    def test_login_unknown_user(self):
        logging.info("Checking login with an unknown username")

        response = requests.post(
            "http://127.0.0.1:8080/auth",
            auth=HTTPBasicAuth("unknown_user", "test_pass")
        )

        try:
            assert response.status_code == 401, (
                f"Expected status code 401, got {response.status_code}"
            )

        except AssertionError as error:
            logging.error(f"Unknown user login test failed: {error}")
            raise

        logging.info("Login correctly rejected for an unknown user")

    def test_login_wrong_password(self):

        logging.info("Checking login with a wrong password")

        response = requests.post(
            "http://127.0.0.1:8080/auth",
            auth=HTTPBasicAuth("test_user", "wrong_pass")
        )

        try:
            assert response.status_code == 401, (
                f"Expected status code 401, got {response.status_code}"
            )

        except AssertionError as error:
            logging.error(f"Login with a wrong password test failed: {error}")
            raise

        logging.info("Login correctly rejected with a wrong password")

    def test_invalid_token(self):
        logging.info("Checking login with an invalid token")

        response = requests.get(
            "http://127.0.0.1:8080/cars",
            headers={"Authorization": "Bearer invalid_token"}
        )
        try:
            assert response.status_code == 422, (
                f"Expected status code 422, got {response.status_code}"
            )
        except AssertionError as error:
            logging.error(f"Login with a wrong password test failed: {error}")
            raise
        logging.info("Login correctly rejected with a wrong password")






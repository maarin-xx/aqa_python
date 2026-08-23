from homework_10 import log_event
import pytest
import re

class Test_login():


    @pytest.mark.parametrize(
        "name, status",
        [
            ("Maryna", "success"),
            ("Olena", "expired"),
            ("Kate", "failed"),
            ('Nina', 'something went wrong'),
            ('user123', 'failed'),
            ('',''),
            (None,None),
            ('Катерина', "success")
        ]
    )
    def test_login_last_row(self, name, status):

        log_event(name, status)
        expected_row = f'Login event - Username: {name}, Status: {status}'
        with open('login_system.log') as f:
            last_row = f.readlines()[-1]

        assert expected_row in last_row, f'expected_row: {expected_row}, but last_row: {last_row}'


    def test_log_starts_with_timestamp(self):

        name = 'Helga'
        status = 'success'
        log_event(name, status)
        with open('login_system.log') as f:
            last_row = f.readlines()[-1]
        start_of_the_row = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', last_row)
        assert start_of_the_row, f'there is no timestamp in the last record'



    @pytest.mark.parametrize(
        "name, status",
        [
            ("Maryna", "success"),
            ('Катерина', "success")
        ]
    )
    def test_log_ends_with_log_message(self, name, status):

        log_event(name, status)
        with open('login_system.log') as f:
            last_row = f.readlines()[-1]

        expected_row = f'Login event - Username: {name}, Status: {status}'
        clean_row = last_row.strip()
        assert clean_row.endswith(expected_row), f'not ended with {expected_row}'


    def test_log_three_records(self):

        test_data = [
            ("Maryna", "success"),
            ("Olena", "expired"),
            ("Kate", "failed"),
        ]

        for name, status in test_data:
            log_event(name, status)

        with open("login_system.log") as f:
            rows = f.readlines()[-3:]

        for name, status in test_data:
            expected_row = f"Login event - Username: {name}, Status: {status}"

            assert any(
                expected_row in row for row in rows
            ), f"{expected_row} was not found"

    # def test_login_if_level_recorded(self, name, status):
    #     log_event( name, status)
    #     expected_row = f'Login event - Username: {name}, Status: {status}'
    #     with open('login_system.log') as f:
    #         last_row = f.readlines()[-1]
    #
    #     if status == "success":
    #         assert expected_row in last_row, f'info level with status = {status} wasn\'t recorded'
    #     elif status == "expired":
    #         assert expected_row in last_row, f'warning level with status = {status} wasn\'t recorded'
    #     else:
    #         assert expected_row in last_row, f'error level with status = {status} wasn\'t recorded'

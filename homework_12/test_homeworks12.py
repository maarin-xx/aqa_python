import assertpy
import homeworks as hw
import functions as f


class Test_TeamLead:

    #перевірити чи є всі атрибути
    def test_check_attr(self):

        team_lead = hw.TeamLead('Timka', 12000, 'backend1', 4,  programming_language='python')

        attr = ['name', 'salary', 'department', 'programming_language']
        result = all(hasattr(team_lead, attr) for attr in attr)
        assert result == True, f'Team lead does not havee all atributes from {attr}'

    #перевірити чи є обʼкт isinstance всіх класів
    def test_team_lead_is_instance_of_all_classes(self):

        team_lead = hw.TeamLead('Timka', 12000, 'backend1', 4, programming_language='python')

        assertpy.assert_that(team_lead, f'team_lead is not an instance of TeamLead').is_instance_of(hw.TeamLead)
        assertpy.assert_that(team_lead, f'team_lead is not an instance of  Manager').is_instance_of(hw.Manager)
        assertpy.assert_that(team_lead, f'team_lead is not an instance of  Developer').is_instance_of(hw.Developer)
        assertpy.assert_that(team_lead, f'team_lead is not an instance of  Employee').is_instance_of(hw.Employee)

        # assert isinstance(team_lead, hw.TeamLead)
        # assert isinstance(team_lead, hw.Manager)
        # assert isinstance(team_lead, hw.Developer)
        # assert isinstance(team_lead, hw.Employee)

    # перевірити типи змінних атрибутів
    def test_types_of_attributes(self):

        team_lead = hw.TeamLead('Timka', 'a', None, 4.2, programming_language='python')

        with assertpy.soft_assertions():

            assertpy.assert_that(team_lead.name, f'team_lead.name: {team_lead.name} is not a string').is_instance_of(str)
            assertpy.assert_that(
                isinstance(team_lead.salary, (int, float)),
                f'team_lead.salary: {team_lead.salary} is not a number'
            ).is_true()
            assertpy.assert_that(team_lead.department, f'team_lead.department: {team_lead.department} is not a string').is_instance_of(str)
            assertpy.assert_that(team_lead.team_size, f'team_lead.team_size: {team_lead.team_size} is not a integer').is_instance_of(int)
            assertpy.assert_that(team_lead.programming_language,f'team_lead.programming_language: {team_lead.programming_language} is not a string').is_instance_of(str)
            #
            # # assert isinstance(team_lead.name, str), f'{team_lead.name} is not a string'
            # # assert isinstance(team_lead.salary, (int, float)), f'{team_lead.salary} is not a number'
            # # assert isinstance(team_lead.department, str), f'{team_lead.department} is not a string'
            # # assert isinstance(team_lead.team_size, int), f'{team_lead.team_size} is not a' 'integer'
            # assert isinstance(team_lead.programming_language, str), f'{team_lead.programming_language} is not a string'

"""
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
"""
class Test_list:

    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    lst2_exp =['1', '12', 'False', '6', 'Python', 'Lorem Ipsum']

    def test_new_list_is_a_list(self):

        lst_result = hw.new_list_with_str_only(self.lst1)

        assert isinstance(lst_result, list), f'{lst_result} is not a list'

    def test_new_list_contains_only_strings(self):

        lst_result = hw.new_list_with_str_only(self.lst1)

        assert all(isinstance(item, str) for item in lst_result)


    def test_result_of_a_new_list(self):

        lst_result = hw.new_list_with_str_only(self.lst1)

        assert lst_result == self.lst2_exp, f'{lst_result} != {self.lst2_exp}'






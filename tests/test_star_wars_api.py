import allure

from utils.api import StarWarsApi
from utils.checking import Checking


@allure.epic('Test Star Wars Api')
class TestStarWarsApi:
    """Класс содержащий тест по работе с персонажами Star Wars Api"""

    @allure.description('Test get personages')
    def test_get_personages(self):
        """Тест по получению персонажей"""
        print("Метод GET")
        films_one_personage = StarWarsApi.get_films_one_personage()  # отправка метода Get
        Checking.check_status_code(films_one_personage, 200)
        Checking.check_json_fields(films_one_personage, ['name', 'height', 'mass', 'hair_color',
                                                         'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld',
                                                         'films', 'species', 'vehicles', 'starships', 'created',
                                                         'edited', 'url'])
        Checking.check_json_value(films_one_personage, 'name', "Darth Vader")
        Checking.check_json_search_word_in_value(films_one_personage, 'name', 'Darth')
        StarWarsApi.get_check_films_other_personages()  # отправка метода Get

        print('Тестирование по Star Wars Api прошло успешно!')

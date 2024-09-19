from utils.http_methods import HttpMethods


class StarWarsApi:
    """Методы для тестирования Star Wars Api"""

    all_films_one_personage = None  # Фильмы персонажа, по которым будет идти сравнение

    @staticmethod
    def get_films_one_personage():
        """Метод для получения фильмов одного персонажа"""
        number_id_person = 4
        get_url = f"https://swapi.dev/api/people/{number_id_person}/"
        result_get = HttpMethods.get(get_url)
        value_result = result_get.json()
        print(get_url)
        print(f'Статус-код: {result_get.status_code}')
        print(f'{number_id_person} персонаж: {value_result}')
        StarWarsApi.all_films_one_personage = value_result.get('films')
        return result_get

    @staticmethod
    def get_count_all_personages():
        """Метод для получения общего количества персонажей"""
        get_url = f"https://swapi.dev/api/people/"
        result_get = HttpMethods.get(get_url)
        value_result = result_get.json().get('count')
        return value_result

    @staticmethod
    def get_check_films_other_personages():
        """Метод для получения персонажей по похожим фильмам"""
        all_personages = []
        count_all_personages = StarWarsApi.get_count_all_personages()
        page = 1
        while len(all_personages) < count_all_personages:
            get_url = f"https://swapi.dev/api/people/?page={page}"
            result_get = HttpMethods.get(get_url)
            value_result = result_get.json().get('results')
            for person in value_result:
                all_personages.append(person)
                print(get_url)
                print(f'Статус-код: {result_get.status_code}')
                print(person)
                other_person_films = person.get('films')  # Фильмы персонажей
                other_name_person = person.get('name')  # Имена персонажей
                identical_films = set(StarWarsApi.all_films_one_personage).intersection(set(other_person_films))
                if identical_films and other_name_person != 'Darth Vader':  # Поиск совпадений по фильмам
                    with open('person.txt', 'a', encoding='utf-8') as f:
                        f.writelines(f"{other_name_person}\n")
            page += 1

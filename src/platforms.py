from abc import ABC, abstractmethod
import requests
import json

class Platforms(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass



class HeadHunterAPI(Platforms):
    def get_vacancies(self, *user_vac):
        params = {
            "text": user_vac
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacancies_list = json.loads(data)
        return vacancies_list

    def print_vacancies_info(self, vacancies_list):
        for vacancy in vacancies_list["items"]:
            name = vacancy['name']
            employer = vacancy['employer']['name']
            if vacancy['salary'] == None:
                salary = 0
            else:
                salary = vacancy['salary']['from']
            vac_url = vacancy['alternate_url']
            print(name, employer, salary, vac_url)



class SuperJobAPI(Platforms): #класс для получения вакансий c SuperJob по API

    def get_vacancies(self, *user_vac):
        headers = {
            "X-Api-App-Id": "v3.r.136446695.b852b584d27663ca132ce773bedeea5ed4074623.fef0ac59fe0370387c6acf8ab72cbddf6308dcd1"
        }
        url = 'https://api.superjob.ru/2.0/vacancies/'
        params = {
            "keyword": user_vac,
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.content.decode()
        vacancies_list = json.loads(data)
        return vacancies_list

    def print_vacancies(self, vacancies_list):
        """
        Метод для вывода вакансий с платформы SuperJob
        """
        for vacancy in vacancies_list['objects']:
            try:
                name = vacancy['profession']
                employer = vacancy['client']['title']
                salary = vacancy['payment_to']
                url = vacancy['link']
            except KeyError:
                pass
            else:
                print(name, employer, salary, url)

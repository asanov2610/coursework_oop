
from platforms import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy, created_hh_vacancy, FileOperation, created_sj_vacancy

print("Привет! Начнем поиск вакансий!")
FileOperation.del_vacancy()
print("Выбери платформу для поиска: HeadHunter - введи 1, Superjob - введи 2")
platform_answer = int(input())

if platform_answer == 1: #поиск вакансий на HeadHunter
    print("Введи поисковый запрос")
    key_word = str(input()).lower()
    hh = HeadHunterAPI()
    vacant = hh.get_vacancies(key_word)
    print(hh.print_vacancies_info(vacant))
    created_hh_vacancy(vacant)
    print("Показать топ вакансий? (да/нет)") #вывод топ по зарплате
    top_answer = str(input()).lower()
    if top_answer == 'да':
        print('Укажите количество вакансий')
        top_count = int(input())
        print(Vacancy.compare_salary(top_count))
    else:
        pass
    print('Нужна ли сортировка по работодателю? (да/нет)') #сортировка по работодателю
    employer_answer = str(input()).lower()
    if employer_answer == 'да':
        print('Укажите название работодателя')
        employer = str(input())
        print(FileOperation.find_vacancy(employer))
    else:
        pass


elif platform_answer == 2: #поиск вакансий на Superjob
    print("Введи поисковый запрос")
    key_word = str(input()).lower()
    sj = SuperJobAPI()
    vacant = sj.get_vacancies(key_word)
    print(sj.print_vacancies_info(vacant))
    created_sj_vacancy(vacant)
    print("Вывести топ вакансий по з/п? (да/нет)") #вывод топ по зарплате
    top_answer = str(input()).lower()
    if top_answer == 'да':
        print('Укажите количество вакансий')
        top_count = int(input())
        print(Vacancy.compare_salary(top_count))
    else:
        pass
    print('Нужна ли сортировка по работодателю? (да/нет)') #сортировка по работодателю
    employer_answer = str(input()).lower()
    if employer_answer == 'да':
        print('Введите название работодателя')
        employer = str(input())
        print(FileOperation.find_vacancy(employer))
    else:
        pass


else:
    print("Нет такой платформы, начните поиск заново")
    exit()
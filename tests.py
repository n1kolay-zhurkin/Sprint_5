import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector() 

    



# add_new_book
@pytest.mark.parametrize('name', [
    'Книга',
    'A' * 40
])
def test_add_new_book_valid_name_added(collector, name):
    collector.add_new_book(name)
    assert name in collector.books_genre
    assert collector.books_genre[name] == ''


# set_book_genre + get_book_genre
def test_set_and_get_book_genre_success(collector):
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')
    assert collector.get_book_genre('Дюна') == 'Фантастика'

# get_books_with_specific_genre
def test_get_books_with_specific_genre_returns_books(collector):
    collector.add_new_book('Оно')
    collector.add_new_book('Сияние')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Сияние', 'Ужасы')

    books = collector.get_books_with_specific_genre('Ужасы')
    assert books == ['Оно', 'Сияние']

# get_books_genre
def test_get_books_genre_returns_dict(collector):
    collector.add_new_book('Дюна')
    assert collector.get_books_genre() == {'Дюна': ''}

# get_books_for_children
def test_get_books_for_children_excludes_age_rating_genres(collector):
    collector.add_new_book('Чебурашка')
    collector.add_new_book('Оно')

    collector.set_book_genre('Чебурашка', 'Мультфильмы')
    collector.set_book_genre('Оно', 'Ужасы')

    books_for_children = collector.get_books_for_children()
    assert books_for_children == ['Чебурашка']

# add_book_in_favorites
def test_add_book_in_favorites_success(collector):
    collector.add_new_book('Дюна')
    collector.add_book_in_favorites('Дюна')
    assert collector.get_list_of_favorites_books() == ['Дюна']

# delete_book_from_favorites
def test_delete_book_from_favorites_removes_book(collector):
    collector.add_new_book('Дюна')
    collector.add_book_in_favorites('Дюна')
    collector.delete_book_from_favorites('Дюна')
    assert collector.get_list_of_favorites_books() == []

# get_list_of_favorites_books
def test_get_list_of_favorites_books_empty(collector):
    assert collector.get_list_of_favorites_books() == []

# Проверка: у добавленной книги нет жанра
def test_added_book_has_no_genre(collector):
    collector.add_new_book('Дюна')
    assert collector.get_book_genre('Дюна') == ''
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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_books_genre_init_true(self):
        book_collector = BooksCollector()
        book_collector.books_genre['1984'] = 'Антиутопия'
        assert book_collector.books_genre['1984'] == 'Антиутопия'

    @pytest.mark.parametrize('book_name, genre', [('1984', 'Фантастика'), ('Мы', 'Детективы')])
    def test_set_book_genre_in_books_genre_success(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    @pytest.mark.parametrize('book_name, genre', [('1984', 'Фантастика'), ('Мы', 'Детективы')])
    def test_get_book_genre_existing_book(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_non_existent_genre(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        non_existent_genre_books = collector.get_books_with_specific_genre('1984')
        assert non_existent_genre_books == []

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.add_new_book('Мы')

        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Мы', 'Детективы')

        expected_genre_dict = {
            '1984': 'Фантастика',
            'Мы': 'Детективы',
        }

        assert collector.get_books_genre() == expected_genre_dict

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Приключения Алисы')
        collector.set_book_genre('Приключения Алисы', 'Фантастика')

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Ужасы')

        collector.add_new_book('Мы')
        collector.set_book_genre('Мы', 'Детективы')

        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Комедии')

        books_for_children = collector.get_books_for_children()

        expected_books_for_children = ['Приключения Алисы', 'Незнайка']

        assert books_for_children == expected_books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        book_name = '1984'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')

        assert book_name not in collector.favorites

        collector.add_book_in_favorites(book_name)

        assert book_name in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        book_name = '1984'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')

        collector.add_book_in_favorites(book_name)

        assert book_name in collector.favorites

        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        collector.add_new_book('Мы')
        collector.set_book_genre('Мы', 'Детективы')

        assert collector.get_list_of_favorites_books() == []

        collector.add_book_in_favorites('1984')

        assert collector.get_list_of_favorites_books() == ['1984']
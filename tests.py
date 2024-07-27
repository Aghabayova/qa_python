import pytest

from main import BooksCollector


class TestBooksCollector:

        # 1. проверяем добавление новой книги
    def test_add_new_book_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Особо опасен')
        assert 'Особо опасен' in collector.books_genre

        # 2. Проверяем установку жанра книге
    @pytest.mark.parametrize('book_name, genre', [
        ('Космические приключения', 'Фантастика'),
        ('Ночь живых мертвецов', 'Ужасы'),
        ('Криминальная драма', 'Детективы'),
        ('Веселые истории', 'Комедии')
    ])
    def test_set_book_genre_genre_added(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre
        # 3. Проверяем получение жанра книги по её имени
    def test_get_book_genre_genre_recieved(self):
        collector = BooksCollector()
        collector.add_new_book('Потерянные города')
        collector.set_book_genre('Потерянные города', 'Фантастика')
        assert collector.get_book_genre('Потерянные города') == 'Фантастика'

        # 4. Проверяем вывод списка книг с определённым жанром
    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Космические приключения']),
        ('Ужасы', ['Ночь живых мертвецов']),
        ('Детективы', ['Криминальная драма']),
        ('Комедии', ['Веселые истории'])
    ])
    def test_get_books_with_specific_genre_specific_genres_received(self, genre, expected_books):
        collector = BooksCollector()
        for book_name in expected_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert all(book in books_with_genre for book in expected_books)

        # 5. проверяем получение словаря books_genre
    @pytest.mark.parametrize('name, genre', [
        ('Тайна старого маяка', 'Детективы'),
        ('Потерянные города', 'Фантастика'),
        ('Веселые истории', 'Комедии')
    ])
    def test_get_books_genre_list_received(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre()[name] == genre

        # 6. проверяем возвращение книги подходящей детям
    def test_get_books_for_kids_books_recieved(self):
        collector = BooksCollector()
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        assert 'Винни-Пух' in collector.get_books_for_children()

        # 7. Проверяем добавление книги в Избранное
    def test_add_book_to_favorites_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения в стране чудес')
        collector.set_book_genre('Приключения в стране чудес', 'Фантастика')
        collector.add_book_in_favorites('Приключения в стране чудес')
        assert 'Приключения в стране чудес' in collector.favorites

        # 8. Проверяем удаление книги из Избранного
    def test_delete_book_from_favorites_deleted_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения в стране чудес')
        collector.set_book_genre('Приключения в стране чудес', 'Фантастика')
        collector.add_book_in_favorites('Приключения в стране чудес')
        collector.delete_book_from_favorites('Приключения в стране чудес')
        assert 'Приключения в стране чудес' not in collector.favorites

        # 9. проверяем получение списка Избранных книг
    @pytest.mark.parametrize('book_name, genre', [
        ('Тайна старого маяка', 'Детективы'),
        ('Космические приключения', 'Фантастика'),
        ('Веселые истории', 'Комедии')
    ])
    def test_get_list_of_favorite_books_list_received(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

        # 10. проверяем, что книги с возрастным рейтингом отсутствуют в списке книг для детей
    @pytest.mark.parametrize('name, genre', [
        ('Ночные охотники', 'Ужасы'),
        ('Проклятие старого особняка', 'Детективы')
    ])
    def test_age_rating_books_not_in_books_for_kids_list_is_empty(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name not in collector.get_books_for_children()

        # 11. Проверяем, что у добавленной книги нет жанра
    def test_newly_added_book_has_no_genre_genre_is_missing(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

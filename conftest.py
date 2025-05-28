import pytest

from books_collector import BooksCollector

@pytest.fixture(scope='function')
def books_collector():
    books_collector = BooksCollector()
    return books_collector

@pytest.fixture(scope='function')
def add_books_collector(books_collector):
    book = ['книга1', 'книга2', 'книга3', 'книга4', 'книга5']
    for name_book in book:
        books_collector.add_new_book(name_book)
    return books_collector.books_genre

@pytest.fixture(scope='function')
def set_book_genre(books_collector, add_books_collector):
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    n = 0
    for name_book in books_collector.books_genre:
        geners = genre[n]
        books_collector.set_book_genre(name_book, geners)
        n = n+1    
    return books_collector.books_genre

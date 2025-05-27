import pytest

from books_collector import BooksCollector

@pytest.fixture(scope='session')
def books_collector():
    books_collector = BooksCollector()
    return books_collector

@pytest.fixture(scope='session')
def add_books_collector(books_collector):
    book = 'книга1'
    books_collector.add_new_book(book)
    return books_collector.books_genre


def test_set_book_genre_true_genre_and_true_book(books_collector,add_books_collector):
    name_book = 'книга1'
    genre = 'Фантастика'
    books_collector.set_book_genre(name_book, genre)
    assert books_collector.books_genre == {'книга1':'Фантастика'}

def test_set_book_genre_not_genre_true_book(books_collector,add_books_collector):
    name_book = 'книга1'
    genre = 'сказки'
    books_collector.set_book_genre(name_book, genre)
    assert books_collector.books_genre == {'книга1':'Фантастика'}

def test_set_book_genre_not_book_true_gener(books_collector,add_books_collector):
    name_book = 'книга2'
    genre = 'Ужасы'
    books_collector.set_book_genre(name_book, genre)
    assert books_collector.books_genre == {'книга1':'Фантастика'}

def test_get_book_genre_true_book(books_collector,add_books_collector):
    name_book = 'книга1'
    assert books_collector.get_book_genre(name_book) == 'Фантастика'

def test_get_book_genre_not_book(books_collector,add_books_collector):
    name_book = 'книга2'
    assert books_collector.get_book_genre(name_book) == None   

def test_get_books_with_specific_genre_fanasy(books_collector,add_books_collector):
    genre = 'Фантастика'
    assert books_collector.get_books_with_specific_genre(genre) == ['книга1']

def test_get_books_genre(books_collector,add_books_collector):
    assert books_collector.get_books_genre() == {'книга1':'Фантастика'}

def test_get_books_for_children(books_collector,add_books_collector):
    assert books_collector.get_books_for_children() == ['книга1']

def test_add_book_in_favorites(books_collector,add_books_collector):
    books_collector.add_book_in_favorites('книга1')
    assert books_collector.favorites == ['книга1']

def test_delete_book_from_favorites(books_collector,add_books_collector):
    books_collector.delete_book_from_favorites('книга1')
    assert  books_collector.favorites == []

def test_get_list_of_favorites_books(books_collector,add_books_collector):
    assert books_collector.get_list_of_favorites_books() == []

@pytest.mark.parametrize('name_book', ['book_1', 'book_2', 'book_3'])
def test_add_new_book_true(books_collector,add_books_collector,name_book):
    books_collector.add_new_book(name_book)
    assert name_book in books_collector.books_genre
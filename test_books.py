import pytest
#from books_collector import BooksCollector


class TestBooksCollector:


    def test_add_new_book_true(self, books_collector):
        name_book = 'book_1'
        books_collector.add_new_book(name_book)
        assert name_book in books_collector.books_genre

    @pytest.mark.parametrize('book,gener', [['книга1','Фантастика'],['книга2','Ужасы'],['книга3', 'Детективы'],['книга4', 'Мультфильмы'],['книга5','Комедии']])
    def test_set_book_genre_true_genre_and_true_book(self, books_collector,add_books_collector, book, gener):
        #genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        #book = 'книга1'
        #gener = 'Детективы'
        books_collector.set_book_genre(book, gener)
        assert books_collector.books_genre[book] == gener

    def test_get_book_genre_true_book(self, books_collector,add_books_collector,set_book_genre):
        name_book = 'книга1'
        assert books_collector.get_book_genre(name_book) == 'Фантастика'

    def test_get_book_genre_not_book(self, books_collector,add_books_collector):
        name_book = 'book'
        assert books_collector.get_book_genre(name_book) == None   

    def test_get_books_with_specific_genre(self, books_collector,add_books_collector, set_book_genre):
        genre = 'Фантастика'
        assert books_collector.get_books_with_specific_genre(genre) == ['книга1']

    def test_get_books_genre(self, books_collector,add_books_collector,set_book_genre):
        assert books_collector.get_books_genre() == {'книга1': 'Фантастика', 'книга2': 'Ужасы','книга3': 'Детективы','книга4': 'Мультфильмы','книга5': 'Комедии'}

    def test_get_books_for_children(self, books_collector,add_books_collector, set_book_genre):
        assert books_collector.get_books_for_children() == ['книга1', 'книга4', 'книга5']

    def test_add_book_in_favorites(self, books_collector,add_books_collector):
        books_collector.add_book_in_favorites('книга1')
        assert books_collector.favorites == ['книга1']

    def test_delete_book_from_favorites(self, books_collector,add_books_collector):
        books_collector.delete_book_from_favorites('книга1')
        assert  'книга1' not in books_collector.favorites

    def test_get_list_of_favorites_books(self, books_collector,add_books_collector):
        books_collector.add_book_in_favorites('книга1')
        books_collector.add_book_in_favorites('книга2')
        assert books_collector.get_list_of_favorites_books() == ['книга1', 'книга2']

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_sets_genre_correctly(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.set_book_genre("book", "Фантастика")
        assert collector.books_genre["book"] == "Фантастика"

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.set_book_genre("book", "Фантастика")
        assert collector.get_book_genre("book") == "Фантастика"

    def test_get_books_with_specific_genre_returns_books_of_genre(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.set_book_genre("book", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["book"]

    def test_get_books_genre_returns_all_books_with_genres(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.set_book_genre("book", "Фантастика")
        assert collector.get_books_genre() == {"book": "Фантастика"}

    def test_get_books_for_children_returns_only_children_books(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.add_new_book("book2")
        collector.set_book_genre("book", "Фантастика")
        collector.set_book_genre("book2", "Ужасы")
        assert collector.get_books_for_children() == ["book"]

    def test_add_book_to_favorites_adds_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.add_book_in_favorites("book")
        assert "book" in collector.favorites

    def test_remove_book_from_favorites_removes_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.add_book_in_favorites("book")
        collector.delete_book_from_favorites("book")
        assert "book" not in collector.favorites

    def test_get_favorites_books_list_returns_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("book")
        collector.add_book_in_favorites("book")
        assert collector.get_list_of_favorites_books() == ["book"]

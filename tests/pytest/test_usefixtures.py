import pytest


# Фикстура для очистки данных из базы данных
@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


# Фикстура для заполнения данных в базу данных
@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")


# Фикстура для заполнения данных в базу данных
@pytest.fixture
def check_books_database():
    print("[FIXTURE] Проверяем создалась ли база данных")


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    ...


@pytest.mark.usefixtures(
    'clear_books_database',     # 3-я срабатывает
    'fill_books_database'       # 4-я срабатывает или нет если уже у метода вызвана 
)
class TestLibrary:
    @pytest.mark.usefixtures('fill_books_database')     # 2-я срабатывает
    @pytest.mark.usefixtures('check_books_database')    # 1-я срабатывает
    def test_read_book_from_library(self):
        ...


    @pytest.mark.usefixtures(
            'fill_books_database',      # 1-я срабатывает
            'check_books_database'      # 2-я срабатывает
            )    
    def test_delete_book_from_library(self):
        ...
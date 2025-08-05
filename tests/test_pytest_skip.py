import sys
import pytest


@pytest.mark.skip(reason="Фича в разработке") # Указываем маркировку, которая пропустит данный автотест
def test_feature_in_development():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Требуется Python 3.8 или выше")
def test_python_version():
    pass


SYSTEM_VERSION = "v1.2.0"  # Для примера укажем версию тестируемой системы


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",  # Пропустим автотес, если версия системы равна v1.3.0
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():  # В текущей конфигурации этот тест запустится
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",  # Пропустим автотес, если версия системы равна v1.2.0
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():  # Этот автотест не запустится
    pass
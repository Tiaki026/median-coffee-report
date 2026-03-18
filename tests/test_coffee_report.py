import csv

import pytest

from coffee_report.coffee_report import median_coffee_report, get_report


def test_median_coffee_report_basic(tmp_path):
    """
    Проверяет базовую функциональность отчёта median-coffee:
    - вычисление медианы для двух студентов
    - сортировка по убыванию медианы
    """

    file = tmp_path / "test.csv"
    with open(file, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])
        writer.writerow(["Алексей", "450"])
        writer.writerow(["Алексей", "500"])
        writer.writerow(["Алексей", "550"])
        writer.writerow(["Дарья", "200"])
        writer.writerow(["Дарья", "250"])
        writer.writerow(["Дарья", "300"])

    result = median_coffee_report([str(file)])

    assert len(result) == 2
    assert result[0]["student"] == "Алексей"
    assert result[0]["median_coffee"] == 500
    assert result[1]["student"] == "Дарья"
    assert result[1]["median_coffee"] == 250
    assert result[0]["median_coffee"] > result[1]["median_coffee"]


def test_median_coffee_report_even_number_of_values(tmp_path):
    """
    Проверяет случай с чётным количеством значений.
    Медиана должна вычисляться как среднее двух центральных чисел.
    """

    file = tmp_path / "test.csv"
    with open(file, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])
        writer.writerow(["Иван", "100"])
        writer.writerow(["Иван", "200"])
        writer.writerow(["Иван", "300"])
        writer.writerow(["Иван", "400"])

    result = median_coffee_report([str(file)])
    assert result[0]["median_coffee"] == 250.0


def test_median_coffee_report_multiple_files(tmp_path):
    """
    Проверяет, что отчёт корректно объединяет данные из нескольких файлов.
    """

    file1 = tmp_path / "file1.csv"
    with open(file1, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])
        writer.writerow(["Иван", "100"])
        writer.writerow(["Иван", "200"])

    file2 = tmp_path / "file2.csv"
    with open(file2, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])
        writer.writerow(["Иван", "300"])
        writer.writerow(["Мария", "400"])

    result = median_coffee_report([str(file1), str(file2)])

    assert len(result) == 2
    assert result[0]["student"] == "Мария"
    assert result[0]["median_coffee"] == 400
    assert result[1]["student"] == "Иван"
    assert result[1]["median_coffee"] == 200


def test_median_coffee_report_empty_file(tmp_path):
    """
    Проверяет обработку пустого файла (только заголовок).
    В этом случае не будет ни одного студента, отчёт должен быть пустым списком.
    """

    file = tmp_path / "empty.csv"
    with open(file, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])

    result = median_coffee_report([str(file)])
    assert result == []


def test_get_report_valid():
    """Проверяет, что get_report возвращает функцию для существующего отчёта."""

    func = get_report("median-coffee")
    assert callable(func)
    assert func.__name__ == "median_coffee_report"


def test_get_report_invalid():
    """Проверяет, что get_report выбрасывает KeyError для неизвестного отчёта."""

    with pytest.raises(KeyError, match="Неизвестный отчёт: unknown"):
        get_report("unknown")

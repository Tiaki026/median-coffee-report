import csv

import pytest

from coffee_report.utils import read_csv_files


def test_read_csv_files_single_file(tmp_path):
    """
    Проверяет чтение одного корректного CSV-файла.
    Создаётся временный файл с двумя записями.
    Ожидается, что функция вернёт список словарей,
    где поле coffee_spent преобразовано в int.
    """

    file = tmp_path / "test.csv"
    with open(file, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "student",
                "date",
                "coffee_spent",
                "sleep_hours",
                "study_hours",
                "mood",
                "exam",
            ]
        )
        writer.writerow(
            ["Иван", "2024-06-01", "600", "3.0", "15", "зомби", "Математика"]
        )
        writer.writerow(
            ["Иван", "2024-06-02", "650", "2.5", "17", "зомби", "Математика"]
        )

    records = read_csv_files([str(file)])

    assert len(records) == 2
    assert records[0]["student"] == "Иван"
    assert records[0]["coffee_spent"] == 600
    assert isinstance(records[0]["coffee_spent"], int)


def test_read_csv_files_multiple_files(tmp_path):
    """
    Проверяет чтение нескольких файлов.
    Создаются два файла с записями разных студентов.
    Ожидается, что функция объединит записи из всех файлов.
    """

    file1 = tmp_path / "data1.csv"
    with open(file1, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])
        writer.writerow(["Иван", "100"])
        writer.writerow(["Иван", "200"])

    file2 = tmp_path / "data2.csv"
    with open(file2, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])
        writer.writerow(["Мария", "300"])
        writer.writerow(["Мария", "400"])

    records = read_csv_files([str(file1), str(file2)])

    assert len(records) == 4
    students = [r["student"] for r in records]
    assert students.count("Иван") == 2
    assert students.count("Мария") == 2


def test_read_csv_files_file_not_found():
    """
    Проверяет, что при передаче несуществующего файла
    выбрасывается исключение FileNotFoundError с нужным сообщением.
    """

    with pytest.raises(
        FileNotFoundError, match="Файл не найден: no_exist.csv"
    ):
        read_csv_files(["no_exist.csv"])


def test_read_csv_files_malformed_csv(tmp_path):
    """
    Проверяет реакцию на повреждённый CSV (например, битые данные).
    В текущей реализации любое исключение при чтении превращается в RuntimeError.
    """

    file = tmp_path / "bad.csv"
    with open(file, "w", encoding="utf-8") as f:
        f.write("student,coffee_spent\nИван,сто\n")

    with pytest.raises(RuntimeError, match="Ошибка при чтении файла"):
        read_csv_files([str(file)])

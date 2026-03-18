import csv
from typing import Any, Dict, List


def read_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Читает несколько CSV-файлов и возвращает список записей (словарей).
    """

    records = []
    for path in file_paths:
        try:
            with open(path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row["coffee_spent"] = int(row["coffee_spent"])
                    records.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {path}")
        except Exception as e:
            raise RuntimeError(f"Ошибка при чтении файла {path}: {e}")
    return records

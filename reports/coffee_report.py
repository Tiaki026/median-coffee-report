import statistics
from collections import defaultdict
from operator import itemgetter
from typing import Any, Callable, Dict, List

from .utils import read_csv_files


def median_coffee_report(files: List[str]) -> List[Dict[str, Any]]:
    """
    Формирует отчёт "median-coffee": медианная сумма
    трат на кофе по каждому студенту за весь период сессии.

    Возвращает список словарей с ключами 'student' и 'median_coffee',
    отсортированный по убыванию.
    """

    records = read_csv_files(files)

    student_spent = defaultdict(list)
    for rec in records:
        student_spent[rec["student"]].append(rec["coffee_spent"])

    result = []
    for student, spent_list in student_spent.items():
        median_val = statistics.median(spent_list)
        result.append({"student": student, "median_coffee": median_val})

    result.sort(key=itemgetter("median_coffee"), reverse=True)
    return result


REPORTS = {
    "median-coffee": median_coffee_report,
}


def get_report(report_name: str) -> Callable:
    """Возвращает функцию отчёта по имени или выбрасывает KeyError."""

    if report_name not in REPORTS:
        raise KeyError(
            f"Неизвестный отчёт: {report_name}. Доступные: {list(REPORTS.keys())}"
        )
    return REPORTS[report_name]

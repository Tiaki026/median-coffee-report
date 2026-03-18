import argparse
import sys

from tabulate import tabulate

from reports.coffee_report import get_report


def main():
    parser = argparse.ArgumentParser(
        description="Формирование отчётов по данным о подготовке к экзаменам."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Список CSV-файлов для обработки",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Название отчёта (например, median-coffee)",
    )
    args = parser.parse_args()

    for f in args.files:
        try:
            open(f, "r").close()
        except FileNotFoundError:
            print(f"Ошибка: файл '{f}' не существует.", file=sys.stderr)
            sys.exit(1)

    try:
        report_func = get_report(args.report)
    except KeyError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    try:
        data = report_func(args.files)
    except Exception as e:
        print(f"Ошибка при формировании отчёта: {e}", file=sys.stderr)
        sys.exit(1)

    headers = {"student": "Student", "median_coffee": "Median coffee"}
    table_data = [[row["student"], row["median_coffee"]] for row in data]
    print(tabulate(table_data, headers.values(), tablefmt="grid"))


if __name__ == "__main__":
    main()

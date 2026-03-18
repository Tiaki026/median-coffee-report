# Median Coffee Report - Отчет о потреблении кофе.


```bash
python main.py --files data/programming.csv data/math.csv data/physics.csv --report median-coffee
```


Тесты
```
$ pytest tests/  
```
Пример вывода удачных тестов
для удобства вывода тестов был создан pytest.ini
```
collected 10 items                                                                                                                                

tests/test_coffee_report.py::test_median_coffee_report_basic PASSED                                                                         [ 10%]
tests/test_coffee_report.py::test_median_coffee_report_even_number_of_values PASSED                                                         [ 20%]
tests/test_coffee_report.py::test_median_coffee_report_multiple_files PASSED                                                                [ 30%]
tests/test_coffee_report.py::test_median_coffee_report_empty_file PASSED                                                                    [ 40%]
tests/test_coffee_report.py::test_get_report_valid PASSED                                                                                   [ 50%]
tests/test_coffee_report.py::test_get_report_invalid PASSED                                                                                 [ 60%]
tests/test_utils.py::test_read_csv_files_single_file PASSED                                                                                 [ 70%]
tests/test_utils.py::test_read_csv_files_multiple_files PASSED                                                                              [ 80%]
tests/test_utils.py::test_read_csv_files_file_not_found PASSED                                                                              [ 90%]
tests/test_utils.py::test_read_csv_files_malformed_csv PASSED                                                                               [100%]

=============================================================== 10 passed in 0.07s ===============================================================
```

# Лабораторная работа №2 - задача 5: Представитель большинства

## Описание
Цель - использовать метод "Разделяй и властвуй" для разработки алгоритма проверки, со- держится ли во входной последовательности элемент, который встречается боль- ше половины раз, за время O(nlogn).

## Структура проекта
- `src/` — исходный код программы.
- `tests/` — автоматические тесты для проверки работы кода.

## Запуск проекта
1. Функция majority_num(): реализует подход «разделяй и властвуй» для поиска кандидата на элемент большинства.
2. Функция find_majority_num(): Вызывает majority_num() для получения потенциального кандидата из всего массива. 
3. Входные данные взяты из файла input.txt, использую алгоритм сортировки слиянием. Результаты записываются в файл output.txt

## Автор
    Буй Тхук Хуен

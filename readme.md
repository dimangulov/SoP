# SoP
Дополнительные задания для школы программирования HH
<br>
Язык: Python<br>
Версия языка: 2.7<br>
Задание 1 - find_nearest_points.py<br>
Задание 2 - find_balance.py<br>

Оба скрипта поддерживают стардартные потоки ввода-вывода<br>

Пример вызова скрипта с перенаправлением в Windows:<br>
python scrip-name.py < input-file.txt<br>
<br>
Кто использует другие ОС, думаю сами разберутся с перенаправлением потоков )<br>
<br>
Для ручного ввода данные необходимо ввести данные, далее нажать клавишу "Enter",<br>
далее для Windows сочетание клавиш Ctrl+Z, для Unix Ctrl+D.<br>
<br>
<i>Далее для Windows</i><br>
Протестировать работоспособность первого задания можно выполнив команду:<br>
python find_nearest_points.py < points.txt<br>
<br>
Протестировать работоспособность второго задания можно выполнив команду:<br>
python find_balance.py < balance_test_1.txt<br>
<br>
<b>Задание №1 -  Минимальное расстояние</b><br>
Дан набор из N точек на плоскости (для простоты можно считать, что у всех точек целочисленные координаты).
Найдите минимальное расстояние между двумя точками из этого набора.

Пример входных данных:<br>
10 10<br>
20 10<br>
20 15<br>

Пример выходных данных:<br>
5<br>
<br>
Решение:<br>

1) Сортируем точки сначала по координате X, а при равных X по Y.<br>
2) Рекурсивно делим все точки на две части, соотвественно каждую часть еще на две части и т.д.<br>
3) Выбираем наименьшее из расстояний между точками в левой и правой частях.<br>
4) Далее обрабатываем точки которые находились на границе деления.<br>
5) Выбираем точки которые находятся от границы деления по X не дальше наименьшего<br>
расстояния, для каждой точки определяем точки которые находятся по X и Y не дальше наименьшего расстояния.
Рассчитываем расстояния между точками и выбираем наименьшее.

<br>
<b>Задание №2 -  Баланс весов</b><br>
Дана конечная последовательность натуральных чисел.
Считая их массами имеющихся в наличии предметов, определить, можно ли все эти предметы положить на весы так, чтобы весы
 находились в равновесии. Вывести вариант расположения.
Определить, можно ли из них отобрать какое-то количество предметов с суммарным весом 100 (вывести yes или no, в зависимости от результата).

Пример входных данных:<br>
2 4 3 6 5<br>
<br>
Пример выходных данных:<br>
2 3 5 - 4 6<br>
no<br>
<br>
Решение:<br>
1) Сортируем все числа по возрастанию<br>
2) Проверяем что сумма всех чисел делится на 2 без остатка<br>
3) Находим половину от всей суммы, эту половину мы и будем искать для левой и правой частей<br>
4) Далее в цикле проходим по графу чисел (первая версия была реализована как рекурсия, но при колчестве чисел свыше 1000,
приложение достигало максимума вложенности функций, версия с циклом сложнее и медленее но работает для большого количества
чисел)<br>
<br>
для чисел 2 3 4 5 6 7 8 9<br>
Граф выглядит примерно следующим образом:<br>
2 - 3 - 4 - 5 - 6 - 7 - 8 - 9<br>
| - 4 - 5 - 6 - 7 - 8 - 9<br>
| - 5 - 6 - 7 - 8 - 9<br>
| - 6 - 7 - 8 - 9<br>
| - 7 - 8 - 9<br>
| - 8 - 9<br>
| - 9<br>
  <br>
3 - 4 - 5 - 6 - 7 - 8 - 9<br>
| - 5 - 6 - 7 - 8 - 9<br>
| - 6 - 7 - 8 - 9<br>
| - 7 - 8 - 9<br>
| - 8 - 9<br>
| - 9<br>
  <br>
и т.д.<br>
<br>
То есть от числа 2 идут ребра ко всем числам больше 2-х, от числа 3 ко всем числам больше 3-х и т.д.<br>
<br>
Для оптимизации прохода по графу и линейной обработки графа, введена переменная bad_edges - в которой для каждого пройденного пути, 
хранится список тупиков узлов т.е. сумма не будет достигнута, сумма будет превышена, правая часть не можеть быть собрана. 

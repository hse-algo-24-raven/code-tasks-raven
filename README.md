# Задание №6+ Алгоритм пирамидальной сортировки
## Задачи  
1. В файле heap/heap.py реализовать класс *Heap*, представляющий структуру данных куча. В файле main.py реализовать функцию *heap_sort*, с использованием класса *Heap*
2. В реквесте добавить комментарий о том, какую асимптотику имеют реализованные методы класса *Heap*.
## Примечания  
- Разработку вести в отдельной ветке, созданной на основе данной. В названии ветки префикс main заменить на название команды.
- Корректность работы функции *heap_sort* проверить запустив файл test.py с модульными тестами.
- **Pull request нужно делать в ветку с заданием, не в ветку main**.

## Описание алгоритма

**Пирамидальная сортировка (сортировка кучей)** - эффективный алгоритм упорядочивания элементов, разработанный
Джоном Вильямсом в 1964 году. Алгоритм основан на использовании бинарной кучи (heap), представляющей собой бинарное дерево.

Благодаря использованию бинарной кучи, пирамидальная сортировка обладает асимптотической временной сложностью O(n log n) в среднем и 
худшем случаях. Еще одним преимуществом этой сортировки является то, что она может выполняться "на месте", без дополнительных затрат памяти.

Алгоритм построен на принципе извлечения максимального (минимального) элемента из кучи и упорядочивания оставшихся элементов. Состоит из двух
этапов:

1. Построение кучи: На этом этапе строится куча из исходных данных. Для каждой вершины в куче выполняется свойство
 упорядоченности: значение в родительском узле больше (равно) значений(ям) в дочерних узлах.
2. Извлечение max/min и перестроение: После построения кучи извлекается максимальный элемент из корня, а куча перестраивается (элементы просеиваются).

### Входные данные:

Список (list).

### Выходные данные:

Отсортированный исходный список (list).

### Области допустимых значений:

• Список должен содержать однотипные элементы, которые поддерживают сравнение. Это могут быть:

- Числа (int, float);
- Строки (str);
- Пользовательские типы с определенными методами сравнения (lt, le, gt, ge).

• Список может быть пустым (в таком случае он считается отсортированным).
# Задание №2 - Вариант 2
## Задачи  
1. В Файле main.py реализовать функцию *get_tridiagonal_determinant*, принимающую трехдиагональную целочисленную матрицу и возвращающую значение определителя данной матрицы.
## Примечания  
- Разработку вести в отдельной ветке, созданной на основе данной. В названии ветки префикс main заменить на название команды. 
- Корректность работы реализованных функций проверить запустив файл test.py с модульными тестами. 
- **Pull request нужно делать в ветку с заданием, не в ветку main**.

## Определитель матрицы

**Матрицей** размера n×m, где n-число строк, m-число столбцов, называется таблица элементов, расположенных в определенном порядке. Элементы матрицы обозначаются a<sub>ij</sub>, где i – номер строки, а j – номер столбца. Если число столбцов матрицы равно числу строк (n=m), то матрица называется квадратной.    
  
**Определитель** – это числовая характеристика квадратной матрицы. Формулы разложения определителя по строке/столбцу позволяют сводить вычисление определителей к рекурсивной процедуре, использующей вычисление определителей меньших порядков.  
  
## Трёхдиагональная матрица  
  
Трехдиагональной называют ленточную матрицу, в которой на главной диагонали расположены числа *a*, на двух соседних диагоналях расположены числа *b* и *c* соответственно. На оставшихся диагоналях матрицы расположены нули.  
  
$$  
det A =   
 \begin{vmatrix}  
  a_{1} & b_{1} & 0 & \cdots & 0 & 0 \\  
  с_{1} & a_{2} & b_{2} & \cdots & 0 & 0 \\  
  0 & с_{2} & a_{3} & \cdots & 0 & 0 \\  
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\  
  0 & 0 & 0 & \cdots & a_{n-1} & b_{n-1} \\  
  0 & 0 & 0 & \cdots & c_{n-1} & a_{n}   
 \end{vmatrix}  
$$  
  
Определитель трехдиагональной матрицы порядка *n* можно вычислить разложением по первой строке:  
  
$$  
det A_n =   
 {\begin{vmatrix}  
  a_{1} & b_{1} & 0 & \cdots & 0 & 0 \\  
  с_{1} & a_{2} & b_{2} & \cdots & 0 & 0 \\  
  0 & с_{2} & a_{3} & \cdots & 0 & 0 \\  
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\  
  0 & 0 & 0 & \cdots & a_{n-1} & b_{n-1} \\  
  0 & 0 & 0 & \cdots & c_{n-1} & a_{n}   
 \end{vmatrix}} =   
 a \cdot  {\begin{vmatrix}  
  a_{2} & b_{2} & \cdots & 0 & 0 \\  
  с_{2} & a_{3} & \cdots & 0 & 0 \\  
  \vdots & \vdots & \ddots & \vdots & \vdots  \\  
  0 & 0 & \cdots & a_{n-1} & b_{n-1} \\  
  0 & 0 & \cdots & c_{n-1} & a_{n}   
 \end{vmatrix}} -   
 b \cdot {\begin{vmatrix}  
  с_{1} & b_{2} & \cdots & 0 & 0 \\  
  0 & a_{3} & \cdots & 0 & 0 \\  
  \vdots  & \vdots & \ddots & \vdots & \vdots  \\  
  0 & 0 & \cdots & a_{n-2} & b_{n-2} \\  
  0 & 0 & \cdots & c_{n-2} & a_{n-1}   
 \end{vmatrix}}   
$$  
  
Первый полученный определитель порядка *n - 1* также является определителем трехдиагональной матрицы порядка *n - 1* :  
  
$$  
 {\begin{vmatrix}  
  a_{2} & b_{2} & \cdots & 0 & 0 \\  
  с_{2} & a_{3} & \cdots & 0 & 0 \\  
  \vdots & \vdots & \ddots & \vdots & \vdots  \\  
  0 & 0 & \cdots & a_{n-1} & b_{n-1} \\  
  0 & 0 & \cdots & c_{n-1} & a_{n}   
 \end{vmatrix}} = det A_{n-1}    
$$  
  
Полученный определитель порядка *n - 1* можно в свою очередь разложить по первому столбцу:  
  
$$    
{\begin{vmatrix}    
  с_{1} & b_{2} & \cdots & 0 & 0 \\    
  0 & a_{3} & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & \cdots & a_{n-2} & b_{n-2} \\    
  0 & 0 & \cdots & c_{n-2} & a_{n-1}     
 \end{vmatrix}}  =   
 c \cdot {\begin{vmatrix}    
  a_{3} & \cdots & 0 & 0 \\    
  \vdots & \ddots & \vdots & \vdots  \\    
  0 & \cdots & a_{n-2} & b_{n-2} \\    
  0 & \cdots & c_{n-2} & a_{n-1}     
 \end{vmatrix}} = c \cdot det A_{n-2}  
$$  
  
В результате для определителя можно получить линейное однородное рекуррентное соотношение:

$$  
det A_n =   a \cdot  det A_{n-1} - b \cdot  c \cdot   det A_{n-2}
$$  

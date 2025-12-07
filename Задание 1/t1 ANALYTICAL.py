# УРАВНЕНИЕ ЛАПЛАСА
# АНАЛИТИЧЕСКИЙ МЕТОД РЕШЕНИЯ


# ===== ФУНКЦИИ ВИЗУАЛИЗАЦИИ =====
import matplotlib.pyplot as plt
import numpy as np
      
      
# ВЫВОД ЗНАЧЕНИЙ САМОЙ МАТРИЦЫ
def display_matr(li):
     matr = li.copy()
     matr.reverse()
     for line in matr:
          text = ""
          for i in line:
               text += str(i) + "\t"
          print(text)
      
# ТЕПЛОВАЯ КАРТА
def display_heatmap(heat_map: list):
#  heat_map.reverse() - это лишнее, extent сам переворачивает по заданным параметрам.
#  ОШИБКА, КОТОРУЮ НУЖНО ВКЛЮЧИТЬ В ОТЧЕТ: Ни в коем случае нельзя использовать для отрисовки тепловую карту из одной библиотеки
#  и изолинии из другой библиотеки (тепловая карта из sns и отрисовка изолиний из plt)
     plt.imshow(heat_map, cmap="plasma", extent = [0, 1.0, 0, 1.0]) #  cmap = "YlGnBu"
     plt.contourf(heat_map, [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) # linestyles='solid', linewidths=1
     plt.title("Тепловая карта для уравнения Лапласа\nАналитический метод")
     plt.colorbar()
     plt.show()
          
      
# ===== ФУНКЦИИ ВИЗУАЛИЗАЦИИ =====

      
# СОЗДАТЬ МАТРИЦУ И ЗАПОЛНИТЬ НУЛЯМИ
def square_matr(size):
     li = []
     for y in range(size+1):
          row = []
          for x in range(size+1):
                row.append(0)
          li.append(row)
              
     return li.copy()
      
# ВСТАВКА КРАЕВЫХ УСЛОВИЙ
def fill_matr(li):
    for i in range(SIZE+1):
        li[i][SIZE] = 1
        li[SIZE][i] = 1
    li[SIZE][0] = 0.5
    li[0][SIZE] = 0.5


def analytical_function(depth, y, x):
     sinh = np.sinh
     sin = np.sin
     cos = np.cos
     PI = np.pi

     normal = 1/(SIZE) # нормализация координат, т.е. приводим их к значению от 0 до 1 внутри вычисляемой области. ЭТО НЕОБХОДИМО ДЛЯ АНАЛИТИЧЕСКОЙ ФОРМУЛЫ

     norm_x = x*normal
     norm_y = y*normal

     sum = 0
     for n in range(1, depth+1):
          Cn = (  (-2*cos(PI*n) + 2)  /  (sinh(PI*n)*PI*n)  )
          sum += Cn * (    (sinh(PI*n*norm_x) * sin(PI*n*norm_y))   +   (sinh(PI*n*norm_y) * sin(PI*n*norm_x))    )
     return sum
          
      
# u(x,y) = Σ_{n=1}^{∞} C_n · [sin(nπx)·sinh(nπy) + sin(nπy)·sinh(nπx)] - аналитический метод
# C_n = (2 - 2*cos(PI*n)) / (sinh(PI*n)*PI*n)
def heat(li: list):
     heat_map = li.copy()
     for y in range(SIZE+1):
          for x in range(SIZE+1):
               if( (x > 0 and x < SIZE) and (y > 0 and y < SIZE)):
                heat_map[y][x] = analytical_function(DEPTH, y, x)
     return heat_map.copy()
     


SIZE = int(input("Размер определяется как квадратная матрица.\nВведите размер тепловой карты (целое число): ")) # размер квадратного поля
DEPTH = int(input("Введите глубину вычисления ряда (целое число): "))

li = square_matr(SIZE)
fill_matr(li)
li = heat(li)
display_heatmap(li)


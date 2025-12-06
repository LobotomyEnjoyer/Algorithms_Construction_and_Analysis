# УРАВНЕНИЕ ЛАПЛАСА
# МЕТОД КВАДРАТОВ



# ===== ФУНКЦИИ ВИЗУАЛИЗАЦИИ =====
import matplotlib.pyplot as plt
      
      
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
def display_heatmap(li):
     heat_map = li.copy()
#  heat_map.reverse() - это лишнее, extent сам переворачивает по заданным параметрам.
#  ОШИБКА, КОТОРУЮ НУЖНО ВКЛЮЧИТЬ В ОТЧЕТ: Ни в коем случае нельзя использовать для отрисовки тепловую карту из одной библиотеки
#  и изолинии из другой библиотеки (тепловая карта из sns и отрисовка изолиний из plt)
     plt.imshow(heat_map, cmap="plasma", extent = [0, 1.0, 0, 1.0]) #  cmap = "YlGnBu"
     plt.contourf(heat_map, [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) # linestyles='solid', linewidths=1
     plt.title("Тепловая карта для уравнения Лапласа\nМетод сеток")
     plt.colorbar()
     plt.show()
          
      
# ===== ФУНКЦИИ ВИЗУАЛИЗАЦИИ =====
      
SIZE = int(input("Размер определяется как квадратная матрица.\nВведите размер тепловой карты (целое число): ")) # размер квадратного поля
ITERATIONS = int(input("Введите количество итераций (целое число): "))
      
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
      
      
# TEMP = 1/4*(LEFT+RIGHT+UP+DOWN) МЕТОД КВАДРАТОВ
def heat(li):
     heat_map = li.copy()
     for iter in range(0, ITERATIONS+1):
          for y in range(0, SIZE+1):
               for x in range(0, SIZE+1):
                    if( (x > 0 and x < SIZE) and (y > 0 and y < SIZE)):
                         heat_map[y][x] = round(1/4*(heat_map[y-1][x] + heat_map[y+1][x] + heat_map[y][x-1] + heat_map[y][x+1]), 5)
     return heat_map.copy()
      
li = square_matr(SIZE)
fill_matr(li)
li = heat(li)
display_heatmap(li)


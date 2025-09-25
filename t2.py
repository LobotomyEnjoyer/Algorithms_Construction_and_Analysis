import seaborn as sns
import matplotlib.pyplot as plt
# УРАВНЕНИЕ ЛАПЛАСА



# ВЫВОД ТЕПЛОВОЙ МАТРИЦЫ
def display_matr(li):
     matr = li.copy()
     matr.reverse()
     for line in matr:
          text = ""
          for i in line:
               text += str(i) + "\t"
          print(text)

# ТЕПЛОВАЯ КАРТА
def sns_heatmap(li):
     heat_map = li.copy()
     heat_map.reverse()
     sns.heatmap(heat_map, annot=False, cmap="YlGnBu")
     plt.title("Laplacian Heatmap")
     plt.show()


# ===== МЕТОД КВАДРАТОВ =====

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
     for y in range(SIZE+1):
          for x in range(SIZE+1):
                if(x == SIZE and y == 0) or (x == 0 and y == SIZE):
                    li[y][x] = 0.5
                elif(y == SIZE and x != SIZE) or (x == SIZE and y != SIZE) or (y == SIZE and x == SIZE):
                    li[y][x] = 1


# TEMP = 1/4*(LEFT+RIGHT+UP+DOWN) МЕТОД КВАДРАТОВ
def heat(li):
     prev_heat_map = li.copy() # НА ЭТОЙ КАРТЕ БЕРУТ ЗНАЧЕНИЯ
     heat_map = li.copy() # НА ЭТОЙ КАРТЕ ВСТАВЛЯЮТ РЕЗУЛЬТАТ
     for iter in range(0, ITERATIONS+1):
         for y in range(0, SIZE+1):
             for x in range(0, SIZE+1):
                  
                  if( (x > 0 and x < SIZE) and (y > 0 and y < SIZE)):
                       heat_map[y][x] = round(1/4*(prev_heat_map[y-1][x] + prev_heat_map[y+1][x] + prev_heat_map[y][x-1] + prev_heat_map[y][x+1]), 3)

     return heat_map.copy()

# ===== МЕТОД КВАДРАТОВ =====

li = square_matr(SIZE)
fill_matr(li)
li = heat(li)
sns_heatmap(li)


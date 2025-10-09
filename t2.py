# УРАВНЕНИЕ ЛАПЛАСА


# ===== ИНТЕГРАЛЬНЫЙ МЕТОД =====

def INTEGRAL_METHOD():
      
      import numpy as np
      from scipy.optimize import newton_krylov
      from numpy import cosh, zeros_like, mgrid, zeros

      # параметры
      nx, ny = 75, 75
      hx, hy = 1./(nx-1), 1./(ny-1)
      P_left, P_right = 0, 1
      
      P_top, P_bottom = 1, 0
      
      def residual(P):
          d2x = zeros_like(P)
          d2y = zeros_like(P)
      
          d2x[1:-1] = (P[2:]   - 2*P[1:-1] + P[:-2]) / hx/hx
          d2x[0]    = (P[1]    - 2*P[0]    + P_left)/hx/hx
          d2x[-1]   = (P_right - 2*P[-1]   + P[-2])/hx/hx
      
          d2y[:,1:-1] = (P[:,2:] - 2*P[:,1:-1] + P[:,:-2])/hy/hy
          d2y[:,0]    = (P[:,1]  - 2*P[:,0]    + P_bottom)/hy/hy
          d2y[:,-1]   = (P_top   - 2*P[:,-1]   + P[:,-2])/hy/hy
      
          return d2x + d2y - 0*cosh(P).mean()**2
      
      # решение
      guess = zeros((nx, ny), float)
      sol = newton_krylov(residual, guess, method='lgmres', verbose=1)
      print('Residual: %g' % abs(residual(sol)).max())
      
      # визуализация
      import matplotlib.pyplot as plt
      x, y = mgrid[0:1:(nx*1j), 0:1:(ny*1j)]
      plt.pcolor(x, y, sol)
      plt.title("Тепловая карта для уравнения Лапласа")
      plt.colorbar()
      plt.show()
      
# ===== ИНТЕГРАЛЬНЫЙ МЕТОД =====






# ===== МЕТОД КВАДРАТОВ =====

def SQUARES_METHOD():

      # ===== ФУНКЦИИ ВИЗУАЛИЗАЦИИ =====

      import seaborn as sns
      import matplotlib.pyplot as plt
      
      
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
          #  heat_map.reverse() - это лишнее, extent сам переворачивает по заданным параметрам.
          #  ОШИБКА, КОТОРУЮ НУЖНО ВКЛЮЧИТЬ В ОТЧЕТ: Ни в коем случае нельзя использовать для отрисовки тепловую карту из одной библиотеки
          #  и изолинии из другой библиотеки (тепловая карта из sns и отрисовка изолиний из plt)
           plt.imshow(heat_map, cmap="plasma", extent = [0, 1.0, 0, 1.0]) #  cmap = "YlGnBu"
           plt.contourf(heat_map, [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) # linestyles='solid', linewidths=1
           plt.title("Тепловая карта для уравнения Лапласа")
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
           for y in range(SIZE+1):
                for x in range(SIZE+1):
                      if(x == SIZE and y == 0) or (x == 0 and y == SIZE):
                          li[y][x] = 0.5
                      elif(y == SIZE and x != SIZE) or (x == SIZE and y != SIZE) or (y == SIZE and x == SIZE):
                          li[y][x] = 1
      
      
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
      sns_heatmap(li)

# ===== МЕТОД КВАДРАТОВ =====





choice = int(input("Выберите метод решения:\n" \
"1) Интегральный метод.\n" \
"2) Метод квадратов.\n" \
"0) Выход из программы.\n"))

match choice:
     case 1:
          INTEGRAL_METHOD()
     case 2:
          SQUARES_METHOD()
     case _:
          pass

# УРАВНЕНИЕ ЛАПЛАСА

# МЕТОД КВАДРАТОВ
SIZE = 5
ITERATIONS = 100

def square_matr(size):
        li = []
        for y in range(size+1):
            row = []
            for x in range(size+1):
                row.append(0)
            li.append(row)
        
        return li.copy()


def fill_matr(li):
     for y in range(SIZE+1):
          for x in range(SIZE+1):
                if(x == SIZE and y == 0) or (x == 0 and y == SIZE):
                    li[y][x] = 0.5
                elif(y == SIZE and x != SIZE) or (x == SIZE and y != SIZE) or (y == SIZE and x == SIZE):
                    li[y][x] = 1

def display_matr(li):
     matr = li.copy()
     matr.reverse()

     for line in matr:
        #   print(line)
          text = ""
          for i in line:
               text += str(i) + "\t"
          print(text)


# TEMP = 1/4*(LEFT+RIGHT+UP+DOWN)
def heat(li):
     LEFT = 0
     RIGHT = SIZE
     UP = SIZE
     DOWN = 0

     prev_heat_map = li.copy() # НА ЭТОЙ КАРТЕ БЕРУТ ЗНАЧЕНИЯ
     heat_map = li.copy() # НА ЭТОЙ КАРТЕ ВСТАВЛЯЮТ РЕЗУЛЬТАТ
     for iter in range(0, ITERATIONS+1):
         for y in range(0, SIZE+1):
             for x in range(0, SIZE+1):
                  
                  if( (x > 0 and x < SIZE) and (y > 0 and y < SIZE)):
                       heat_map[y][x] = round(1/4*(prev_heat_map[y-1][x] + prev_heat_map[y+1][x] + prev_heat_map[y][x-1] + prev_heat_map[y][x+1]), 5)
                 
                #  if(x == 0 and y == 0): #ЛЕВЫЙ-НИЖНИЙ УГОЛ
                #       heat_map[y][x] = 1/4*(prev_heat_map[y][x+1] + prev_heat_map[y+1][x])


                #  elif(y == 0 and (x != 0 and x != SIZE)): #НИЗ
                #       heat_map[y][x] = 1/4*(prev_heat_map[y][x-1] + prev_heat_map[y+1][x] + prev_heat_map[y][x+1])


                #  elif(x == SIZE and y == 0): #ПРАВЫЙ-НИЖНИЙ УГОЛ
                #       heat_map[y][x] = 1/4*(prev_heat_map[y][x-1] + prev_heat_map[y+1][x])
                    

                #  elif(x == 0 and (y != 0 and y != SIZE)): #ЛЕВО
                #       heat_map[y][x] = 1/4*(prev_heat_map[y-1][x] + prev_heat_map[y][x+1] + prev_heat_map[y+1][x])
                 

                #  elif(x == SIZE and (y != 0 and y != SIZE)): #ПРАВО
                #       heat_map[y][x] = 1/4*(prev_heat_map[y][x-1] + prev_heat_map[y+1][x] + prev_heat_map[y-1][x])
                

                #  elif(y == SIZE and x == 0): #ЛЕВЫЙ-ВЕРХНИЙ УГОЛ
                #       heat_map[y][x] = 1/4*(prev_heat_map[y-1][x] + prev_heat_map[y][x+1])
                
                
                #  elif(x == SIZE and y == SIZE): #ПРАВЫЙ-ВЕРХНИЙ УГОЛ
                #       heat_map[y][x] = 1/4*(prev_heat_map[y][x-1] + prev_heat_map[y-1][x])
                

                #  elif(y == SIZE and (x != 0 and x != SIZE)): #ВЕРХ
                #       heat_map[y][x] = 1/4*(prev_heat_map[y-1][x] + prev_heat_map[y][x+1] + prev_heat_map[y][x-1])
                

                #  else: #ВНУТРИ
                #       heat_map[y][x] = 1/4*(prev_heat_map[y-1][x] + prev_heat_map[y+1][x] + prev_heat_map[y][x-1] + prev_heat_map[y][x-1])

     return heat_map.copy()
          

li = square_matr(SIZE)
fill_matr(li)

li = heat(li)

display_matr(li)
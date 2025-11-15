# МНОГОЧЛЕН (ДИОФАНТОВОЕ УРАВНЕНИЕ)



choice = int(input("Выберите метод решения:" \
"1) МЕТОД ПЕРЕБОРА" \
"2) ГЕНЕТИЧЕСКИЙ АЛГОРИТМ" \
"0) ВЫХОД"))




match choice:
    case 1: # МЕТОД ПЕРЕБОРА (ЦИКЛОМ)
     START = 0
     STOP = 31

     count = 0
     for a in range(START, STOP):
         for b in range(START, STOP):
             for c in range(START, STOP):
                 for d in range(START, STOP):
                     if(a + 2*b + 3*c + 4*d == 30):
                         count += 1

     print(f"in [{START}, {STOP}) total answers found: {count}")
    case 2: #  ГЕНЕТИЧЕСКИЙ АЛГОРИТМ
     pass
    case 0:
     print("Выход")
    case _:
     print("Выход")
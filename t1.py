# МНОГОЧЛЕН

# МЕТОД ПЕРЕБОРА (ЦИКЛОМ)

START = 0
STOP = 31

count = 0
for a in range(START, STOP):
    for b in range(START, STOP):
        for c in range(START, STOP):
            for d in range(START, STOP):
                if( a + 2*b + 3*c + 4*d == 30):
                    count += 1

print(f"in [{START}, {STOP}) total answers found: {count}")
# Study case for students --------------------------------
# Simple Cross mutliplication table for python learning

def print_table(nb) :

    index = 1
    print("------ TABLE OF ", nb, " ----------")

    while index <= 10:
        cur_val = nb * index
        print(nb, " multiplied by ",index, " : ", cur_val )
        index += 1

for main_idx in range(1,11):
    print_table(main_idx)

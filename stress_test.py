from datetime import datetime
import time
import matplotlib.pyplot as plt
from tests.functions import main_func


def first_time():
    start = time.time()
    for i in range(5):
        main_func("stress_input/2.txt")
    finish = time.time()
    result_time_1 = (finish - start)/5
    return result_time_1

def second_time():
    start = time.time()
    for i in range(5):
        main_func("stress_input/3.txt")
    finish = time.time()
    result_time_2 = (finish - start)/5
    return result_time_2

def third_time():
    start = time.time()
    for i in range(5):
        main_func("stress_input/4.txt")
    finish = time.time()
    result_time_3 = (finish - start)/5
    return result_time_3

time_one = first_time()
time_two = second_time()
time_three = third_time()

data = {'4000 symbols': time_one, '8000 symbols': time_two, '12000 symbols': time_three}
names = list(data.keys())
values = list(data.values())
fig, axs = plt.subplots()
axs.plot(names, values)
plt.savefig(f'graphic_{datetime.now():%H-%M-%S}.png')
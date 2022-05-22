from my_minipack.loading import ft_progress
import time

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)

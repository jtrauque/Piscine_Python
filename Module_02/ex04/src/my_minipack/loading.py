import time

def ft_progress(lst):
    start = time.time()
    size = len(lst)
    t = 0.0
    endloop = 0.0
    for n, ele in enumerate(lst):
        startloop = time.time()
        t = (time.time() - start)
        count = int(30 * (n + 1) / size)
        print("ETA: %5.2fs [%3d%%] [%s>%s] %4d/%d | elapsed time %5.2fs" 
                %(endloop * (size - n), (n + 1) / size * 100, count * "=", (30 - count) * " ",
                    n, size, t))
        yield ele
        if endloop == 0.0:
            endloop = time.time() - startloop

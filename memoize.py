import time

input_map = {}

def sleep_n_spell(sleep_time, out):
    res = input_map.get((sleep_time, out), None)

    if res:
        return res
    else:
        time.sleep(sleep_time)
        input_map[sleep_time,out] = (sleep_time, out)

        return sleep_time, out

if __name__ == '__main__':
    print(sleep_n_spell(5, 3))
    print(sleep_n_spell(5, 3))

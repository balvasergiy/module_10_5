import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as file:
        while True:
            line = file.readline()
            for line in file:
                all_data.append(line)
            if line == '':
                break
        file.close()
list_files = [f'./file {i}.txt' for i in range(1, 5)]

if __name__ == '__main__':

    # Линейный вызов(lin)

    start_lin = datetime.datetime.now()
    for files in list_files:
        read_info(files)

    end_lin = datetime.datetime.now()
    print(f'{end_lin - start_lin} (линейный)')

    # Многопроцессный(mp)

    start_mp = datetime.datetime.now()
    with Pool(processes=6) as pool:
        result = pool.map(read_info, list_files)
    end_mp = datetime.datetime.now()
    print(f'{end_mp - start_mp} (многопроцессный)')
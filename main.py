import time
import logging
import requests
import threading
import multiprocessing

logging.basicConfig(level=logging.DEBUG)

ile_zle = 0
def make_request(n = 0):
    try: print(f'Wątek {n} ->', requests.get('https://api.ipify.org/', timeout=30).text)
    except:
        global ile_zle
        ile_zle += 1
    #time.sleep(1)

def make_requests(count = 1):
    threads = []
    for i in range(count): threads.append(threading.Thread(target=make_request, args=(i, )))
    for t in threads: t.start()
    for t in threads: t.join()

def do_pool(requests_count = 1):
    pool = multiprocessing.Pool(processes = multiprocessing.cpu_count() - 1 or 1)
    for i in range(0, requests_count): pool.apply_async(make_request, args=(0,))
    pool.close()
    pool.join()

if __name__ == "__main__":
    s = time.time()
    for i in range(1): do_pool(500)
    #make_requests(500)
    t = round(time.time() - s, 2)
    print(f'KONIEC -> {t}s, tyle zle ->', ile_zle)
    print('CPUS ->', multiprocessing.cpu_count())

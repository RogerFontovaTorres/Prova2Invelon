from threading import Thread, Barrier

barrier = Barrier(5)
threads = {}
sentences = {0: "are made of coffee?", 1: "Do you know", 2: "it!", 3: "that our bodies", 4: "- Try drinking"}


def wait_thread(key):
    if key == 3:
        threads[1].join()
    elif key == 0:
        threads[3].join()
    elif key == 4:
        threads[0].join()
    elif key == 2:
        threads[4].join()


def wait_all_threads():
    barrier.wait()


def wait_and_print(key):
    wait_all_threads()
    wait_thread(key)
    print(sentences[key], end=" ")


def initialize_and_start_threads():
    for i in range(5):
        threads[i] = Thread(target=wait_and_print, args=(i,))
        threads[i].start()


def join_threads():
    for i in range(5):
        threads[i].join()


def concurrency_with_coffee():
    print("- I'm tired, Bob!", end=" ")
    initialize_and_start_threads()
    join_threads()
    print("- You're right!")


if __name__ == '__main__':
    concurrency_with_coffee()


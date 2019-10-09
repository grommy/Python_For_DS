import logging
import time
import concurrent.futures

# https://realpython.com/intro-to-python-threading/#what-is-a-thread

"""
17:20:37: Testing update. Starting value is 0.
17:20:37: Thread 0: starting update
17:20:37: Thread 1: starting update
17:20:38: Thread 0: finishing update
17:20:38: Thread 1: finishing update
17:20:38: Testing update. Ending value is 1.
"""


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        # self.value += 1  # for correct answer
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)

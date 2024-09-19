from select_by_name import select_by_name
from select_by_range import select_by_range

import time

start_time = time.time()

# test = select_by_name("Stockholm")
test = select_by_range("Kristianstad", "0.0", "100000.0")

end_time = time.time()

print(test)

print(f"Execution time: {end_time - start_time} seconds")
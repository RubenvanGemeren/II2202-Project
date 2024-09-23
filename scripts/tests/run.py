from select_by_name import select_by_name
from join_by_name import join_by_name
from group_by_name import group_by_name

import time


start = time.time()

select_name = select_by_name("Stockholm")

join_name = join_by_name()

grp_name = group_by_name()


print(grp_name)

end = time.time()

print(f"Time taken: {end - start}")

from functools import reduce
from itertools import accumulate
num = [2, 4, 6, 8, 10]
cumulative_sum = list(accumulate(num))
print(cumulative_sum)
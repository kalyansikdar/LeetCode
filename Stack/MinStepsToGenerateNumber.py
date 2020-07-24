# Given an int n. You can use only 2 operations:
# multiply by 2
# integer division by 3 (e.g. 10 / 3 = 3)
# Find the minimum number of steps required to generate n from 1.

# Example 1
# Input: 10
# Output: 6
# Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
# 6 steps required, as we have used 5 multiplications by 2, and one division by 3

# Example 2:
# Input: 3
# Output: 7
# Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
# 7 steps required, as we have used 5 multiplications by 2 and 2 divisions by 3.

# using deque for removing first element from the queue in constant time (popleft)
from collections import deque
def num_steps(n):
  # initialize queue with 1
  queue = deque([1])
  no_of_steps = 0

  while queue:
    no_of_elements_to_remove = len(queue)

    no_of_steps += 1

    for i in range(no_of_elements_to_remove):
      cur_number = queue.popleft()

      muliply_by_2 = int(cur_number * 2)
      divide_by_3 = int(cur_number / 3)

      if(muliply_by_2 == n or divide_by_3 == n): return no_of_steps

      # append multiplication and division results to queue
      queue.append(muliply_by_2)
      if(divide_by_3 > 0): queue.append(divide_by_3)

print (num_steps(3))

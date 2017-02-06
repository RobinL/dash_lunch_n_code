import numpy as np
nums = np.arange(1,1000)
sum(nums[(nums % 3 ==0) | (nums % 5 == 0)])

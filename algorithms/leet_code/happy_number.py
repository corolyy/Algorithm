'''202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def divide_and_sum(n):
            num_list = map(lambda x: int(x), str(n))
            return reduce(lambda x, y: x + y * y, num_list, 0)

        assert isinstance(n, int) and n > 0

        exist_num = {n} # to avoid endless loop
        while True:
            n = divide_and_sum(n)
            if n == 1:
                return True
            if n in exist_num:
                return False
            else:
                exist_num.add(n)


print Solution().isHappy(19) # --》 True
import array as arr
class Solution(object):
    val = arr.array('i', [1, 2, 5, 6, 7, 3, 3])
    def arrayRankTransform(self):
        val = arr.array('i', [1, 2, 5, 6, 7, 3, 3])
        for x in val:
            if x > val:
                print(x)
        """
        :type arr: List[int]
        :rtype: List[int]
        """
a = Solution()
a.arrayRankTransform()
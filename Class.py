class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)


    def getLength(self):
        return 2 * self.getLength()
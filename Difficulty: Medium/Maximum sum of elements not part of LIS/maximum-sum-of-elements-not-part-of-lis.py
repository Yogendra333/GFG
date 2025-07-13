class Solution:

    def __init__(self):
        self.mp = {}

    def insert(self, val):
        keys = sorted(self.mp.keys())
        len_val = 1
        sum_val = val

        # Find the best LIS ending at a value less than current
        for k in keys:
            if k >= val:
                break
            if self.mp[k][0] + 1 > len_val:
                len_val = self.mp[k][0] + 1
                sum_val = self.mp[k][1] + val

        # Remove all dominated entries (length <= current and key > val)
        toerase = []
        for k in keys:
            if k > val and self.mp[k][0] <= len_val:
                toerase.append(k)

        for k in toerase:
            del self.mp[k]

        self.mp[val] = [len_val, sum_val]

    def nonLisMaxSum(self, arr):
        self.mp.clear()
        for num in arr:
            self.insert(num)
        total_sum = sum(arr)
        lis_sum = max([v[1] for v in self.mp.values()], default=0)
        return total_sum - lis_sum
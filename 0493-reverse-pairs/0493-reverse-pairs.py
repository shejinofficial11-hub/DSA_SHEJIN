class Solution:
    def reversePairs(self, nums):
        return self.sort(nums, 0, len(nums) - 1)

    def sort(self, nums, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = 0

        count += self.sort(nums, left, mid)
        count += self.sort(nums, mid + 1, right)

        j = mid + 1

        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1

            count += j - mid - 1

        self.merge(nums, left, mid, right)

        return count

    def merge(self, nums, left, mid, right):
        temp = []

        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        for i in range(len(temp)):
            nums[left + i] = temp[i]
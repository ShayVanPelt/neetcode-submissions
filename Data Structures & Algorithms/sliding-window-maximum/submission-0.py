class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        queue = []

        for n in nums:
            queue.append(n)
        queue.reverse()

        temp = [0] * k
        for i in range(k):
            temp[i] = queue.pop()
            
        output.append(self.largest(temp, k))

        while queue:
            for x in range(k-1):
                temp[x] = temp[x+1]
            temp[k-1] = queue.pop()
            output.append(self.largest(temp, k))
            
        return output

    def largest(self, temp: list[int], k: int):
        largest = temp[0]
        for x in temp:
            if x >= largest:
                largest = x
        return largest
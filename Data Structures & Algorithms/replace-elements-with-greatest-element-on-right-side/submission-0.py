class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = [0] * n
        largest = -1
        for x in range(n-1,-1,-1):
            output[x] = largest
            largest = max(arr[x], largest)
        return output
      
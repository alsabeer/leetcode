class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []
        for i in numbers:
            k = target - i
            if k in numbers:
                arr.append(numbers.index(i) + 1)
                if target - i in arr:
                    arr.append(numbers.index(i)+2)
                else:
                    arr.append(numbers.index(target - i) + 1)
                if arr[0] == arr[1]:
                    arr[1] = arr[0] +1
                return arr
        return []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in visited:
                return [visited[nums[i]], i]
            visited[complement] = i
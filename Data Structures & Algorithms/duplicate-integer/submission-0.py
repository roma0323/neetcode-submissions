class Solution:

  def hasDuplicate(self, nums: list[int]) -> bool:
    seen = set()  # Hash set for O(1) lookups
    for num in nums:
      if num in seen:  # O(1) average time check
        return True
      seen.add(num)  # O(1) insertion
    return False
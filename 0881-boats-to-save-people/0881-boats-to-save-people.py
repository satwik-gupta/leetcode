class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        minBoatRequired = 0
        r = len(people) - 1
        l = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                minBoatRequired += 1
                l += 1
                r -= 1
            else:
                minBoatRequired += 1
                r -= 1
        return minBoatRequired
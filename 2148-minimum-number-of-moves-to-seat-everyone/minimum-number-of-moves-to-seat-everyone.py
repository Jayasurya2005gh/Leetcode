class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats = sorted(seats)
        students = sorted(students)
        count = 0

        for i in range(len(students)):
            count += abs(seats[i] - students[i])
        return count
        
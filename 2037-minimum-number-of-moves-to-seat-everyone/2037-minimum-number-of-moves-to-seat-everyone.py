class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()    # 의자 위치를 정렬
        students.sort() # 학생 위치를 정렬
        return sum(abs(seat - student) for seat, student in zip(seats, students))
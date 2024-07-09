class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        for arrival, time in customers:
            start_time = max(current_time, arrival)
            finish_time = start_time + time
            waiting_time = finish_time - arrival
            total_waiting_time += waiting_time
            current_time = finish_time
        return total_waiting_time / len(customers)
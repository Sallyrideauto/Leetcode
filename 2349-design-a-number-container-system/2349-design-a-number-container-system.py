import heapq

class NumberContainers:

    def __init__(self):
        # 각 인덱스에 해당하는 최신 숫자를 저장하는 딕셔너리
        self.index2num = {}
        # 각 숫자에 대해 해당 숫자를 가진 인덱스들을 최소 힙으로 저장하는 딕셔너리
        self.num2idx = {}

    def change(self, index: int, number: int) -> None:
        # 인덱스에 대한 최신 숫자 업데이트
        self.index2num[index] = number
        
        # 만약 해당 숫자에 대한 힙이 없다면 초기화
        if number not in self.num2idx:
            self.num2idx[number] = []
        
        # 해당 숫자에 대해 인덱스를 최소 힙에 삽입
        heapq.heappush(self.num2idx[number], index)

    def find(self, number: int) -> int:
        # 주어진 숫자에 대해 힙이 존재하지 않으면 -1 반환
        if number not in self.num2idx:
            return -1
        
        heap = self.num2idx[number]
        
        # 힙의 최상단 요소(가장 작은 인덱스)가 최신 데이터인지 확인
        while heap:
            idx = heap[0]
            # 만약 인덱스의 최신 값이 주어진 숫자와 일치한다면 유효한 데이터이므로 반환
            if self.index2num.get(idx, None) == number:
                return idx
            else:
                # 최신 값이 아니라면 stale한 데이터이므로 힙에서 제거
                heapq.heappop(heap)
        
        # 힙에 유효한 인덱스가 없으면 -1 반환
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)

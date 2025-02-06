import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간 기준 정렬
    length = len(jobs)
    answer = 0
    n = 0  # 현재 시간
    heap = []  # 수행 시간이 짧은 작업을 관리하는 최소 힙
    idx = 0  # jobs 리스트에서 작업을 가져올 인덱스
    
    while idx < length or heap:
        # 현재 시간까지 요청된 모든 작업을 힙에 추가
        while idx < length and jobs[idx][0] <= n:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))  # 수행 시간 기준 최소 힙
            idx += 1
        
        if heap:  # 실행할 작업이 있다면
            duration, request_time = heapq.heappop(heap)
            n += duration  # 작업 수행 후 시간 업데이트
            answer += n - request_time  # 대기 시간 + 실행 시간
        else:  # 실행할 작업이 없다면 현재 시간을 다음 작업 요청 시간으로 업데이트
            n = jobs[idx][0]

    return answer // length
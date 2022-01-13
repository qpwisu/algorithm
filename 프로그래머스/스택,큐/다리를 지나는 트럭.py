#문제가 이상하다 1초마다 한대씩 다리에 진입이 가능하다 queue를 이용
def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    answer = 0
    while len(truck_weights):
        answer+=1 
        bridge.pop(0)
        if truck_weights[0]+sum(bridge) <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    answer+=bridge_length
    
    return answer

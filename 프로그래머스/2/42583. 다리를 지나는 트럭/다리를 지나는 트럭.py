from collections import deque 
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    now_bridge = deque()
    now_weight = 0 
    
    while truck_weights:
        answer +=1 
        
        truck = truck_weights[0]
        if now_bridge:
            if now_bridge[0][1] == answer:
                now_weight -= now_bridge[0][0] 
                now_bridge.popleft()
        
        if weight >= now_weight+ truck:
            print([truck,answer+bridge_length])
            now_bridge.append([truck,answer+bridge_length])
            truck_weights.popleft()
            now_weight += truck
        

            
        if not truck_weights:
            break
        
    print(now_bridge)
    return now_bridge[-1][1]
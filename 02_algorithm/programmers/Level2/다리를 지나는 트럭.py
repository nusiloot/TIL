def solution(bridge_length, weight, truck_weights):
    answer = 0
    # goal_in = [] # 다리를 지난 트럭 list
    bridge_status = [0] * bridge_length # 다리 길이만큼 리스트 생성
    while True:
        answer += 1
        if sum(bridge_status):
            for i in range(bridge_length-1, -1, -1):
                if i == bridge_length-1:
                    if bridge_status[i]:
                        bridge_status[bridge_length-1] = 0
                        # goal_in.append(bridge_status[i])
                else:
                    bridge_status[i+1] = bridge_status[i]
                    bridge_status[i] = 0
        if not sum(bridge_status) and not len(truck_weights):
            break# 탈출조건
        if truck_weights:
            if truck_weights[0] + sum(bridge_status) <= weight:
                pop_element = truck_weights[0]
                truck_weights.pop(0)
                bridge_status[0] += pop_element
    return answer

print(solution(3, 10, [7, 4, 5, 6]))
# solution(100, 100, [10])
# solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
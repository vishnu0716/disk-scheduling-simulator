def fcfs(requests, head):
    movement = 0
    current = head
    order = []

    for req in requests:
        order.append(req)
        movement += abs(req - current)
        current = req

    return movement, order

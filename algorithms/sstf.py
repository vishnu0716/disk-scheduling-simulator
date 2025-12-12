def sstf(requests, head):
    requests = requests.copy()
    current = head
    movement = 0
    order = []

    while requests:
        # Find the request with the minimum seek time
        nearest = min(requests, key=lambda x: abs(x - current))
        movement += abs(nearest - current)
        order.append(nearest)
        current = nearest
        requests.remove(nearest)

    return movement, order

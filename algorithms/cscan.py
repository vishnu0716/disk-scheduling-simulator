def cscan(requests, head, disk_size=200):
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    order = []
    movement = 0
    current = head

    # Move to the right first
    for r in right:
        order.append(r)
        movement += abs(r - current)
        current = r

    # Jump to beginning of disk
    if left:
        movement += abs((disk_size - 1) - current)
        current = 0

    # Continue servicing remaining requests
    for r in left:
        order.append(r)
        movement += abs(r - current)
        current = r

    return movement, order

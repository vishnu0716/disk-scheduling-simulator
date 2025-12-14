def scan(requests, head, disk_size=200, direction="right"):
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    order = []
    movement = 0
    current = head

    if direction == "right":
        for r in right:
            order.append(r)
            movement += abs(r - current)
            current = r

        movement += abs(disk_size - current)
        current = disk_size

        for r in reversed(left):
            order.append(r)
            movement += abs(r - current)
            current = r

    else:
        for r in reversed(left):
            order.append(r)
            movement += abs(r - current)
            current = r

        movement += abs(current - 0)
        current = 0

        for r in right:
            order.append(r)
            movement += abs(r - current)
            current = r

    return movement, order

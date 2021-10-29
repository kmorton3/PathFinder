# Solving using A* pathfinding
# F = G + H
# G is the distance between the current node and the start node
# H is the heuristic - estimated distance from the current node to
# the end node, = a^2 + b^2

__version__ = '0.2'
__author__ = 'Keith Morton'

openList = []
closedList = []


class Node:
    def __init__(self, location, parent):
        self.location = location
        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0


def child_in_list(child, used_list):
    for node in used_list:
        if child.location == node.location:
            return True
    return False


def a_star_pathing(board, start, end):
    starting_node = Node(start, None)
    starting_node.f = starting_node.g = starting_node.h = 0
    ending_node = Node(end, None)
    ending_node.f = ending_node.g = ending_node.h = 0
    openList.append(starting_node)

    while len(openList) > 0:
        current_node = openList[0]
        if current_node.parent is None:
            current_node.g = 0
        else:
            current_node.g = current_node.parent.g + 1
        current_node.h = ((ending_node.location[0] - current_node.location[0] ** 2)
                          + (ending_node.location[1] - current_node.location[1] ** 2))
        current_node.f = current_node.g + current_node.h

        current_index = 0
        for index, node in enumerate(openList):
            if node.f < current_node.f:
                current_index = index
                current_node = node
        openList.pop(current_index)
        closedList.append(current_node)
        print(f'Closest node location {current_node.location}')

        if current_node.location == ending_node.location:
            print('Found the end')
            ending_path = []
            while current_node.parent is not None:
                ending_path.append(current_node.location)
                current_node = current_node.parent
            ending_path.append(current_node.location)
            return ending_path

        # Find children
        for coord in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            try:
            # board[current_node.location[0] + coord[0]][current_node.location[1] + coord[1]]
            # if (current_node.location[0] + coord[0] in range(len(board))
            #         and current_node.location[1] + coord[1] in range(len(board[current_node.location[1]]))):
                if board[current_node.location[0] + coord[0]][current_node.location[1] + coord[1]] != 1:
                    if (current_node.location[0] + coord[0]) >= 0 and (current_node.location[1] + coord[1]) >= 0:
                        child_node = (Node((current_node.location[0] + coord[0],
                                            current_node.location[1] + coord[1]), current_node))
                        child_node.g = current_node.g + 1
                        child_node.h = ((ending_node.location[0] - child_node.location[0] ** 2)
                                        + (ending_node.location[1] - child_node.location[1] ** 2))
                        child_node.f = child_node.g + child_node.h
                        if not child_in_list(child_node, openList):
                            if not child_in_list(child_node, closedList):
                                openList.append(child_node)
            except IndexError:
                pass
    return None


def main():

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start = (8, 0)
    end = (3, 6)

    path = a_star_pathing(board, start, end)
    if path is None:
        print('Could not find a path')
    else:
        print('Made final path')
        for coord in path:
            print(coord)


if __name__ == '__main__':
    main()

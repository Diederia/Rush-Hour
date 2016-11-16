
# class Position(object):
#
#     def __init__(self, x, y):
#
#         """
#         Initializes a position with coordiantes (x,y).
#         """
#         self.x = x
#         self.y = y
#
#     def getX(self):
#         return x
#     def getY(self):
#         return y
#     def getNewposition(self, direction, length):
#
#         old_x, old_y = self.getX(), self.getY()
#         if direction == 'left':
#             new_x = old_x - 1
#             new_y = old_y
#         elif direction == 'right':
#             new_x = old_x + 1
#             new_y = old_y
#         elif direction 'up':
#             new_y = old_y - 1
#             new_x = old_x
#         else direction == 'down':
#             new_y = old_y + 1
#             new_x = old_x
#         self.board[old_x][old_y] = 0
#         return Position(new_x, new_y)

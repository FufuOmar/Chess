import pygame
blockSize = 100
size = width, height = 800, 800
screen = pygame.display.set_mode((width, height))

class Piece:
    def __init__(self, image, pos, piece_type, color):
        self.image = pygame.transform.scale(image, (blockSize, blockSize))
        self.pos = pos
        self.type = piece_type
        self.color = color

    def draw(self, screen):
        screen.blit(self.image, (self.pos[0] * blockSize, self.pos[1] * blockSize))

    def actions(self, board):
        available_moves = []
        board.occupiedSpace()
        occupied_positions = [pos for pos, color in board.spaces] 
        if self.type == 'pawn':
            if self.color == 'black':
                # Normal Move
                move = (self.pos[0] , self.pos[1] + 1)
                if move not in occupied_positions:
                    available_moves.append(move)
                # Double move on first move
                if self.pos[1] == 1: 
                    move = (self.pos[0] , self.pos[1] + 2)
                    if move not in occupied_positions:
                        available_moves.append(move)
                # Capturing moves
                capture_moves = [(self.pos[0] - 1, self.pos[1] + 1), (self.pos[0] + 1, self.pos[1] + 1)]
                for capture_move in capture_moves:
                    if (capture_move, 'white') in board.spaces:
                        available_moves.append(capture_move)
            else: #If color is white
                # Normal Move
                move = (self.pos[0] , self.pos[1] - 1)
                if move not in occupied_positions:
                    available_moves.append(move)
                # Double move on first move
                if self.pos[1] == 6: 
                    move = (self.pos[0] , self.pos[1] - 2)
                    if move not in occupied_positions:
                        available_moves.append(move)
                # Capturing moves
                capture_moves = [(self.pos[0] - 1, self.pos[1] - 1), (self.pos[0] + 1, self.pos[1] - 1)]
                for capture_move in capture_moves:
                    if (capture_move, 'black') in board.spaces:
                        available_moves.append(capture_move)
        elif self.type == 'rook':
            if self.color == 'black':
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check up spaces
                            move[0] = move[0] + j
                            if move[0] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check down spaces
                            move[0] = move[0] - j
                            if move[0] < 0: # Break early if out of bounds
                                break
                        if i == 2: # Check right spaces
                            move[1] = move[1] + j
                            if move[1] > 7: # Break early if out of bounds
                                break
                        if i == 3: # Check left spaces
                            move[1] = move[1] - j
                            if move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'white') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'black') in board.spaces:
                                break
            else: # If color is white
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check up spaces
                            move[0] = move[0] + j
                            if move[0] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check down spaces
                            move[0] = move[0] - j
                            if move[0] < 0: # Break early if out of bounds
                                break
                        if i == 2: # Check right spaces
                            move[1] = move[1] + j
                            if move[1] > 7: # Break early if out of bounds
                                break
                        if i == 3: # Check left spaces
                            move[1] = move[1] - j
                            if move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'black') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'white') in board.spaces:
                                break
        elif self.type == 'knight':
            knight_moves = [
                    (2, 1), (2, -1), (-2, 1), (-2, -1),
                    (1, 2), (1, -2), (-1, 2), (-1, -2)
                ]
            if self.color == 'black':
                for move in knight_moves:
                    x = move[0] + self.pos[0]
                    y = move[1] + self.pos[1]
                    new_pos = (x, y)
                    # Normal Moves
                    if new_pos not in occupied_positions:
                        available_moves.append(new_pos)
                    # Capture Moves
                    elif (new_pos, 'white') in board.spaces:
                        available_moves.append(new_pos)
            else: #If color is white
                for move in knight_moves:
                    x = move[0] + self.pos[0]
                    y = move[1] + self.pos[1]
                    new_pos = (x, y)
                    # Normal Moves
                    if new_pos not in occupied_positions:
                        available_moves.append(new_pos)
                    # Capture Moves
                    elif (new_pos, 'black') in board.spaces:
                        available_moves.append(new_pos)        
        elif self.type == 'bishop':
            if self.color == 'black':
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check bottom right spaces
                            move[0] = move[0] + j
                            move[1] = move[1] + j
                            if move[0] > 7 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check top right spaces
                            move[0] = move[0] - j
                            move[1] = move[1] + j
                            if move[0] < 0 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 2: # Check bottom left spaces
                            move[0] = move[0] + j
                            move[1] = move[1] - j
                            if move[0] > 7 or move[1] < 0: # Break early if out of bounds
                                break
                        if i == 3: # Check top left spaces
                            move[0] = move[0] - j
                            move[1] = move[1] - j
                            if move[0] < 0 or move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'white') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'black') in board.spaces:
                                break
            else:
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check bottom right spaces
                            move[0] = move[0] + j
                            move[1] = move[1] + j
                            if move[0] > 7 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check top right spaces
                            move[0] = move[0] - j
                            move[1] = move[1] + j
                            if move[0] < 0 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 2: # Check bottom left spaces
                            move[0] = move[0] + j
                            move[1] = move[1] - j
                            if move[0] > 7 or move[1] < 0: # Break early if out of bounds
                                break
                        if i == 3: # Check top left spaces
                            move[0] = move[0] - j
                            move[1] = move[1] - j
                            if move[0] < 0 or move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'black') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'white') in board.spaces:
                                break
        elif self.type == 'queen':
            if self.color == 'black':
                #Straight moves
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check up spaces
                            move[0] = move[0] + j
                            if move[0] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check down spaces
                            move[0] = move[0] - j
                            if move[0] < 0: # Break early if out of bounds
                                break
                        if i == 2: # Check right spaces
                            move[1] = move[1] + j
                            if move[1] > 7: # Break early if out of bounds
                                break
                        if i == 3: # Check left spaces
                            move[1] = move[1] - j
                            if move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'white') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'black') in board.spaces:
                                break
                #Diagonial moves
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check bottom right spaces
                            move[0] = move[0] + j
                            move[1] = move[1] + j
                            if move[0] > 7 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check top right spaces
                            move[0] = move[0] - j
                            move[1] = move[1] + j
                            if move[0] < 0 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 2: # Check bottom left spaces
                            move[0] = move[0] + j
                            move[1] = move[1] - j
                            if move[0] > 7 or move[1] < 0: # Break early if out of bounds
                                break
                        if i == 3: # Check top left spaces
                            move[0] = move[0] - j
                            move[1] = move[1] - j
                            if move[0] < 0 or move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'white') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'black') in board.spaces:
                                break
            else:
                 #Straight moves
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check up spaces
                            move[0] = move[0] + j
                            if move[0] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check down spaces
                            move[0] = move[0] - j
                            if move[0] < 0: # Break early if out of bounds
                                break
                        if i == 2: # Check right spaces
                            move[1] = move[1] + j
                            if move[1] > 7: # Break early if out of bounds
                                break
                        if i == 3: # Check left spaces
                            move[1] = move[1] - j
                            if move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'black') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'white') in board.spaces:
                                break
                #Diagonial moves
                for i in range(4):
                    for j in range(1, 8):
                        move = list(self.pos)
                        if i == 0: # Check bottom right spaces
                            move[0] = move[0] + j
                            move[1] = move[1] + j
                            if move[0] > 7 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 1: # Check top right spaces
                            move[0] = move[0] - j
                            move[1] = move[1] + j
                            if move[0] < 0 or move[1] > 7: # Break early if out of bounds
                                break
                        if i == 2: # Check bottom left spaces
                            move[0] = move[0] + j
                            move[1] = move[1] - j
                            if move[0] > 7 or move[1] < 0: # Break early if out of bounds
                                break
                        if i == 3: # Check top left spaces
                            move[0] = move[0] - j
                            move[1] = move[1] - j
                            if move[0] < 0 or move[1] < 0: # Break early if out of bounds
                                break
                        if tuple(move) not in occupied_positions:
                                available_moves.append(tuple(move))
                            # Capture move
                        elif (tuple(move), 'black') in board.spaces:
                                available_moves.append(tuple(move))
                                break
                        elif (tuple(move), 'white') in board.spaces:
                                break
        elif self.type == 'king':
            king_moves = [
                (1, 0), (1, 1), (0, 1), (-1, 1),
                (-1, 0), (-1, -1), (0, -1), (1, -1)
            ]
            if self.color == 'black':
                for move in king_moves:
                    x = move[0] + self.pos[0]
                    y = move[1] + self.pos[1]
                    new_pos = (x, y)
                    # Normal Moves
                    if new_pos not in occupied_positions:
                        available_moves.append(new_pos)
                    # Capture Moves
                    elif (new_pos, 'white') in board.spaces:
                        available_moves.append(new_pos)
            else:
                 for move in king_moves:
                    x = move[0] + self.pos[0]
                    y = move[1] + self.pos[1]
                    new_pos = (x, y)
                    # Normal Moves
                    if new_pos not in occupied_positions:
                        available_moves.append(new_pos)
                    # Capture Moves
                    elif (new_pos, 'black') in board.spaces:
                        available_moves.append(new_pos)
        else:
            raise LookupError
        print(f"Avaiable moves:  {available_moves}")
        return available_moves



class Board:
    def __init__(self):
        # Initialize board state and pieces
        self.pieces = []
        self.spaces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)
        self.occupiedSpace()
        
    def draw(self, screen, selected_piece=None):
        drawGrid()
        if selected_piece:
            selected_spot = pygame.Rect(selected_piece.pos[0] * blockSize, selected_piece.pos[1] * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, (255, 255, 153), selected_spot, 0)
        for piece in self.pieces:
            piece.draw(screen)
      
    
    def occupiedSpace(self):
        self.spaces = [] #mvemvemomfoemfo
        for piece in self.pieces:
            position = tuple(piece.pos)
            color = piece.color
            self.spaces.append((position, color))
        print(f"Occupied spaces: {self.spaces}")  # Debugging line


    def move_piece(self, piece, new_pos):
        # Move piece and update board state
        #remove position in self.spaces once moved, and add new position
        moves_available = piece.actions(self)
        if new_pos in moves_available:
            for target_piece in self.pieces:
                if tuple(target_piece.pos) == new_pos and target_piece.color != piece.color:
                    self.remove_piece(target_piece)
                    break
            self.spaces.remove((tuple(piece.pos), piece.color))
            piece.pos = list(new_pos)
            self.spaces.append((tuple(new_pos), piece.color))
            print("Succesful move")
            return 0
        else:
            print("Failure move")
            return 1

def drawGrid():
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if (x // blockSize + y // blockSize) % 2 == 0:
                pygame.draw.rect(screen, (238, 238, 210), rect, 0)
            else:
                pygame.draw.rect(screen, (118, 150, 86), rect, 0)
import pygame

from chess import Piece, Board

pygame.init()
size = width, height = 800, 800
blockSize = 100 #Set the size of the grid block

screen = pygame.display.set_mode((width, height))

# Load the pieces
blackKing_image = pygame.image.load('chessPieces/bk.png')
blackQueen_image = pygame.image.load('chessPieces/bq.png')
blackBishop_image = pygame.image.load('chessPieces/bb.png')
blackKnight_image = pygame.image.load('chessPieces/bn.png')
blackRook_image = pygame.image.load('chessPieces/br.png')
blackPawn_image = pygame.image.load('chessPieces/bp.png')
whiteKing_image = pygame.image.load('chessPieces/wk.png')
whiteQueen_image = pygame.image.load('chessPieces/wq.png')
whiteBishop_image = pygame.image.load('chessPieces/wb.png')
whiteKnight_image = pygame.image.load('chessPieces/wn.png')
whiteRook_image = pygame.image.load('chessPieces/wr.png')
whitePawn_image = pygame.image.load('chessPieces/wp.png')
# Scale the pieces to fit the block size
bk = Piece(blackKing_image, [4,0], 'king', 'black')
bq = Piece(blackQueen_image, [3,0], 'queen', 'black')
bb1 = Piece(blackBishop_image, [2,0], 'bishop', 'black')
bn1 = Piece(blackKnight_image, [1,0], 'knight', 'black')
br1 = Piece(blackRook_image, [0,0], 'rook', 'black')
bb2 = Piece(blackBishop_image, [5,0], 'bishop', 'black')
bn2 = Piece(blackKnight_image, [6,0], 'knight', 'black')
br2 = Piece(blackRook_image, [7,0], 'rook', 'black')
bp1 = Piece(blackPawn_image, [0,1], 'pawn', 'black')
bp2 = Piece(blackPawn_image, [1,1], 'pawn', 'black')
bp3 = Piece(blackPawn_image, [2,1], 'pawn', 'black')
bp4 = Piece(blackPawn_image, [3,1], 'pawn', 'black')
bp5 = Piece(blackPawn_image, [4,1], 'pawn', 'black')
bp6 = Piece(blackPawn_image, [5,1], 'pawn', 'black')
bp7 = Piece(blackPawn_image, [6,1], 'pawn', 'black')
bp8 = Piece(blackPawn_image, [7,1], 'pawn', 'black')
wk = Piece(whiteKing_image, [4,7], 'king', 'white')
wq = Piece(whiteQueen_image, [3,7], 'queen', 'white')
wb1 = Piece(whiteBishop_image, [2,7], 'bishop', 'white')
wn1 = Piece(whiteKnight_image, [1,7], 'knight', 'white')
wr1 = Piece(whiteRook_image, [0,7], 'rook', 'white')
wb2 = Piece(whiteBishop_image, [5,7], 'bishop', 'white')
wn2 = Piece(whiteKnight_image, [6,7], 'knight', 'white')
wr2 = Piece(whiteRook_image, [7,7], 'rook', 'white')
wp1 = Piece(whitePawn_image, [0,6], 'pawn', 'white')
wp2 = Piece(whitePawn_image, [1,6], 'pawn', 'white')
wp3 = Piece(whitePawn_image, [2,6], 'pawn', 'white')
wp4 = Piece(whitePawn_image, [3,2], 'pawn', 'white')
wp5 = Piece(whitePawn_image, [4,6], 'pawn', 'white')
wp6 = Piece(whitePawn_image, [5,6], 'pawn', 'white')
wp7 = Piece(whitePawn_image, [6,6], 'pawn', 'white')
wp8 = Piece(whitePawn_image, [7,6], 'pawn', 'white')
#Setting up the board
board = Board()
board.add_piece(bk)
board.add_piece(bq)
board.add_piece(bb1)
board.add_piece(bn1)
board.add_piece(br1)
board.add_piece(bb2)
board.add_piece(bn2)
board.add_piece(br2)
board.add_piece(bp1)
board.add_piece(bp2)
board.add_piece(bp3)
board.add_piece(bp4)
board.add_piece(bp5)
board.add_piece(bp6)
board.add_piece(bp7)
board.add_piece(bp8)
board.add_piece(wk)
board.add_piece(wq)
board.add_piece(wb1)
board.add_piece(wn1)
board.add_piece(wr1)
board.add_piece(wb2)
board.add_piece(wn2)
board.add_piece(wr2)
board.add_piece(wp1)
board.add_piece(wp2)
board.add_piece(wp3)
board.add_piece(wp4)
board.add_piece(wp5)
board.add_piece(wp6)
board.add_piece(wp7)
board.add_piece(wp8)
def drawGrid():
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if (x // blockSize + y // blockSize) % 2 == 0:
                pygame.draw.rect(screen, (238, 238, 210), rect, 0)
            else:
                pygame.draw.rect(screen, (118, 150, 86), rect, 0)
#Main game loop
run = True
selected_piece = None
current_turn = 'white'  # White starts the game

while run:
    screen.fill((0, 0, 0))  # Clear the screen
    drawGrid()
    board.draw(screen, selected_piece)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            grid_x = mouse_pos[0] // blockSize
            grid_y = mouse_pos[1] // blockSize

            if selected_piece is None:
                # First click: select the piece
                for piece in board.pieces:
                    if piece.pos == [grid_x, grid_y] and piece.color == current_turn:
                        selected_piece = piece
                        break
            else:
                # Second click: move the selected piece
                if selected_piece.pos == list((grid_x, grid_y)): #If user clicks the same spot, go again
                    print("same spot")
                    selected_piece = None
                    break
                if board.move_piece(selected_piece, (grid_x, grid_y)) == 1: #If user makes a false move, go again
                    print("false move")
                    selected_piece = None
                    break
                else:
                    current_turn = 'black' if current_turn == 'white' else 'white'
                    selected_piece = None

    pygame.display.update()

pygame.quit()
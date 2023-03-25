#!/usr/bin/env python3

# chessValidator.py - This program takes a dictionary of chess board spaces and
# pieces and compares them to a standard chess board and piece set to determine
# if the given chess board dictionary is considered a valid chess board.
# A valid chess board will have exactly 1 black king, 1 white king, 32 pieces
# at most (16 for each player), at most 16 pawns (8 for each player), and all
# pieces must be on a valid space from '1a' to '8h'.
# Piece names begin with either a 'w' or a 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.


def is_valid_chess_board(dict):
    validChessBoard = {'1a':'wrook', '2a':'wknight', '3a':'wbishop', '4a':'wqueen', '5a':'wking', '6a':'wbishop', '7a':'wknight', '8a':'wrook',
                       '1b':'wpawn', '2b':'wpawn', '3b':'wpawn', '4b':'wpawn', '5b':'wpawn', '6b':'wpawn', '7b':'wpawn', '8b':'wpawn',
                       '1c':'', '2c':'', '3c':'', '4c':'', '5c':'', '6c':'', '7c':'', '8c':'',
                       '1d':'', '2d':'', '3d':'', '4d':'', '5d':'', '6d':'', '7d':'', '8d':'',
                       '1e':'', '2e':'', '3e':'', '4e':'', '5e':'', '6e':'', '7e':'', '8e':'',
                       '1f':'', '2f':'', '3f':'', '4f':'', '5f':'', '6f':'', '7f':'', '8f':'',
                       '1g':'bpawn', '2g':'bpawn', '3g':'bpawn', '4g':'bpawn', '5g':'bpawn', '6g':'bpawn', '7g':'bpawn', '8g':'bpawn',
                       '1h':'brook', '2h':'bknight', '3h':'bbishop', '4h':'bking', '5h':'bqueen', '6h':'bbishop', '7h':'bknight', '8h':'brook'}

    # Search for any invalid pieces in the given chess board dictionary.
    for piece in dict.values():
        if piece in validChessBoard.values():
            continue
        else:
            return False

    # Search for any invalid spaces in the given chess board dictionary.
    for space in dict.keys():
        if space in validChessBoard.keys():
            continue
        else:
            return False
    
    # Count if there are more than 32 pieces on the board.
    pieceList= []
    for piece in dict.values():
        if piece == '':
            continue
        else:
            pieceList.append(piece)

    if len(pieceList) > 32:
        return False

    # Check if there are more than 8 black or white pawns.
    whitePawns = [pawn for pawn in dict.values() if pawn == 'wpawn']
    blackPawns = [pawn for pawn in dict.values() if pawn == 'bpawn']

    if len(whitePawns) > 8:
        return False
    elif len(blackPawns) > 8:
        return False

    # Return a default True value if there are no issues with the given dictionary.
    return True


def main():
    validTestBoard = {'1a':'wrook', '2a':'wknight', '3a':'wbishop', '4a':'wqueen', '5a':'wking', '6a':'wbishop', '7a':'wknight', '8a':'wrook',
                       '1b':'wpawn', '2b':'wpawn', '3b':'wpawn', '4b':'wpawn', '5b':'wpawn', '6b':'wpawn', '7b':'wpawn', '8b':'wpawn',
                       '1c':'', '2c':'', '3c':'', '4c':'', '5c':'', '6c':'', '7c':'', '8c':'',
                       '1d':'', '2d':'', '3d':'', '4d':'', '5d':'', '6d':'', '7d':'', '8d':'',
                       '1e':'', '2e':'', '3e':'', '4e':'', '5e':'', '6e':'', '7e':'', '8e':'',
                       '1f':'', '2f':'', '3f':'', '4f':'', '5f':'', '6f':'', '7f':'', '8f':'',
                       '1g':'bpawn', '2g':'bpawn', '3g':'bpawn', '4g':'bpawn', '5g':'bpawn', '6g':'bpawn', '7g':'bpawn', '8g':'bpawn',
                       '1h':'brook', '2h':'bknight', '3h':'bbishop', '4h':'bking', '5h':'bqueen', '6h':'bbishop', '7h':'bknight', '8h':'brook'}

    invalidPiece = {'1a':'wrook', '2a':'wknight', '3a':'wbishop', '4a':'wqueen', '5a':'wking', '6a':'wbishop', '7a':'wknight', '8a':'wrook',
                       '1b':'epawn', '2b':'wpawn', '3b':'wpawn', '4b':'wpawn', '5b':'wpawn', '6b':'wpawn', '7b':'wpawn', '8b':'wpawn',
                       '1c':'', '2c':'', '3c':'', '4c':'', '5c':'', '6c':'', '7c':'', '8c':'',
                       '1d':'', '2d':'', '3d':'', '4d':'', '5d':'', '6d':'', '7d':'', '8d':'',
                       '1e':'', '2e':'', '3e':'', '4e':'', '5e':'', '6e':'', '7e':'', '8e':'',
                       '1f':'', '2f':'', '3f':'', '4f':'', '5f':'', '6f':'', '7f':'', '8f':'',
                       '1g':'bpawn', '2g':'bpawn', '3g':'bpawn', '4g':'bpawn', '5g':'bpawn', '6g':'bpawn', '7g':'bpawn', '8g':'bpawn',
                       '1h':'brook', '2h':'bknight', '3h':'bbishop', '4h':'bking', '5h':'bqueen', '6h':'bbishop', '7h':'bknight', '8h':'brook'}

    invalidSpace = {'1p':'wrook', '2a':'wknight', '3a':'wbishop', '4a':'wqueen', '5a':'wking', '6a':'wbishop', '7a':'wknight', '8a':'wrook',
                       '1b':'wpawn', '2b':'wpawn', '3b':'wpawn', '4b':'wpawn', '5b':'wpawn', '6b':'wpawn', '7b':'wpawn', '8b':'wpawn',
                       '1c':'', '2c':'', '3c':'', '4c':'', '5c':'', '6c':'', '7c':'', '8c':'',
                       '1d':'', '2d':'', '3d':'', '4d':'', '5d':'', '6d':'', '7d':'', '8d':'',
                       '1e':'', '2e':'', '3e':'', '4e':'', '5e':'', '6e':'', '7e':'', '8e':'',
                       '1f':'', '2f':'', '3f':'', '4f':'', '5f':'', '6f':'', '7f':'', '8f':'',
                       '1g':'bpawn', '2g':'bpawn', '3g':'bpawn', '4g':'bpawn', '5g':'bpawn', '6g':'bpawn', '7g':'bpawn', '8g':'bpawn',
                       '1h':'brook', '2h':'bknight', '3h':'bbishop', '4h':'bking', '5h':'bqueen', '6h':'bbishop', '7h':'bknight', '8h':'brook'}

    tooManyPieces = {'1a':'wrook', '2a':'wknight', '3a':'wbishop', '4a':'wqueen', '5a':'wking', '6a':'wbishop', '7a':'wknight', '8a':'wrook',
                       '1b':'wpawn', '2b':'wpawn', '3b':'wpawn', '4b':'wpawn', '5b':'wpawn', '6b':'wpawn', '7b':'wpawn', '8b':'wpawn',
                       '1c':'wrook', '2c':'', '3c':'', '4c':'', '5c':'', '6c':'', '7c':'', '8c':'',
                       '1d':'', '2d':'', '3d':'', '4d':'', '5d':'', '6d':'', '7d':'', '8d':'',
                       '1e':'', '2e':'', '3e':'', '4e':'', '5e':'', '6e':'', '7e':'', '8e':'',
                       '1f':'', '2f':'', '3f':'', '4f':'', '5f':'', '6f':'', '7f':'', '8f':'',
                       '1g':'bpawn', '2g':'bpawn', '3g':'bpawn', '4g':'bpawn', '5g':'bpawn', '6g':'bpawn', '7g':'bpawn', '8g':'bpawn',
                       '1h':'brook', '2h':'bknight', '3h':'bbishop', '4h':'bking', '5h':'bqueen', '6h':'bbishop', '7h':'bknight', '8h':'brook'}
    
    tooManyWhitePawns = {'1a':'wrook', '2a':'wknight', '3a':'wbishop', '4a':'wqueen', '5a':'wking', '6a':'wbishop', '7a':'wknight', '8a':'wrook',
                       '1b':'wpawn', '2b':'wpawn', '3b':'wpawn', '4b':'wpawn', '5b':'wpawn', '6b':'wpawn', '7b':'wpawn', '8b':'wpawn',
                       '1c':'wpawn', '2c':'', '3c':'', '4c':'', '5c':'', '6c':'', '7c':'', '8c':'',
                       '1d':'', '2d':'', '3d':'', '4d':'', '5d':'', '6d':'', '7d':'', '8d':'',
                       '1e':'', '2e':'', '3e':'', '4e':'', '5e':'', '6e':'', '7e':'', '8e':'',
                       '1f':'', '2f':'', '3f':'', '4f':'', '5f':'', '6f':'', '7f':'', '8f':'',
                       '1g':'bpawn', '2g':'bpawn', '3g':'bpawn', '4g':'bpawn', '5g':'bpawn', '6g':'bpawn', '7g':'bpawn', '8g':'bpawn',
                       '1h':'brook', '2h':'bknight', '3h':'bbishop', '4h':'bking', '5h':'bqueen', '6h':'bbishop', '7h':'bknight', '8h':'brook'}

    tooManyBlackPawns = {'1a':'wrook', '2a':'wknight', '3a':'wbishop', '4a':'wqueen', '5a':'wking', '6a':'wbishop', '7a':'wknight', '8a':'wrook',
                       '1b':'wpawn', '2b':'wpawn', '3b':'wpawn', '4b':'wpawn', '5b':'wpawn', '6b':'wpawn', '7b':'wpawn', '8b':'wpawn',
                       '1c':'', '2c':'', '3c':'', '4c':'', '5c':'', '6c':'', '7c':'', '8c':'',
                       '1d':'', '2d':'', '3d':'', '4d':'', '5d':'', '6d':'', '7d':'', '8d':'',
                       '1e':'', '2e':'', '3e':'', '4e':'', '5e':'', '6e':'', '7e':'', '8e':'',
                       '1f':'bpawn', '2f':'', '3f':'', '4f':'', '5f':'', '6f':'', '7f':'', '8f':'',
                       '1g':'bpawn', '2g':'bpawn', '3g':'bpawn', '4g':'bpawn', '5g':'bpawn', '6g':'bpawn', '7g':'bpawn', '8g':'bpawn',
                       '1h':'brook', '2h':'bknight', '3h':'bbishop', '4h':'bking', '5h':'bqueen', '6h':'bbishop', '7h':'bknight', '8h':'brook'}

    if is_valid_chess_board(validTestBoard):
        print("Valid board")
    else:
        print("Invalid baord")

    if is_valid_chess_board(invalidPiece):
        print("Valid board")
    else:
        print("Invalid board")
    
    if is_valid_chess_board(invalidSpace):
        print("Valid board")
    else:
        print("Invalid board")

    if is_valid_chess_board(tooManyPieces):
        print("Valid board")
    else:
        print("Invalid board")

    if is_valid_chess_board(tooManyWhitePawns):
        print("Valid board")
    else:
        print("Invalid board")

    if is_valid_chess_board(tooManyBlackPawns):
        print("Valid board")
    else:
        print("Invalid board")


if __name__ == "__main__":
    main()

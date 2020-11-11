# for storing info about the current state of the chess game
# responsible for determining the current move at the current
# keep the move logs

class GameState():
    def __init__(self):
        # second char represents the type of piece e.g bR is b,Rook
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', 'bp', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.moveFunctions = {'p': self.getPawnMoves,
                              'R': self.getRookMoves,
                              'N': self.getKnightMoves,
                              'B': self.getBishopMoves,
                              'Q': self.getQueenMoves,
                              'K':  self.getKingMoves}
        self.whiteToMove = True
        self.movelog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startcol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.movelog.append(move)
        self.whiteToMove = not self.whiteToMove

    ''' 
    undo the last move
    '''
    def undoMove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startRow][move.startcol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    '''
    all moves without considering checks
    '''
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):  # number of rows
            for c in range(len(self.board[r])):  # number of columns
                turn = self.board[r][c][0]
                if(turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves)  #calls the approrpriate move function based on piece type
        return moves

    '''
    get all the pawn moves for the pawn located at row,col and add these moves to the list
    '''
    def getPawnMoves(self, r, c, moves):
          if self.whiteToMove:  #white pawn moves
              if self.board[r - 1][c] == "--":  # 1 square pawn advance
                  moves.append(Move((r, c), (r-1, c), self.board))
                  if r == 6 and self.board[r - 2][c] == "--":  # 2square pawn advance
                      moves.append(Move((r, c), (r - 2, c), self.board))

                      #captures
                  if c - 1 >= 0:  #captures to the left
                      if self.board[r - 1][c - 1][0] == 'b':  #enemy to capture
                          moves.append(Move((r, c), (r - 1, c - 1), self.board))
                  if c + 1 <= 7:  #captures to the right
                      if self.board[r - 1][c + 1][0] == 'b':  #enemy piece to capture
                          moves.append(Move((r, c), (r - 1, c + 1), self.board))

          else:  #for the black pawns moves
              if self.board[r + 1][c] == "--":  #1 square move
                  moves.append(Move((r, c), (r + 1, c), self.board))
                  if r == 1 and self.board[r + 2][c] == "--":  #2 square move
                      moves.append(Move((r, c), (r+2, c), self.board))

              #captures
              if c - 1 >= 0:  #capture to left
                  if self.board[r + 1][c - 1][0] == "w":  #enemy to capture
                      moves.append(Move((r, c), (r + 1, c - 1), self.board))
                  if c + 1 <= 7:  #captures to the right
                      if self.board[r + 1][c + 1][0] == 'w':
                          moves.append(Move((r, c), (r + 1, c + 1), self.board))




    '''
      get all the rook moves for the pawn located at row,col and add these moves to the list
    '''

    def getRookMoves(self, r, c, moves):
        pass

    '''
      get all the knight moves for the pawn located at row,col and add these moves to the list
    '''
    def getKnightMoves(self, r, c, moves):
        pass

    '''
      get all the bishop moves for the pawn located at row,col and add these moves to the list
    '''
    def getBishopMoves(self, r, c, moves):
        pass

    '''
      get all the queen moves for the pawn located at row,col and add these moves to the list
    '''
    def getQueenMoves(self, r, c, moves):
        pass

    '''
      get all the king moves for the pawn located at row,col and add these moves to the list
    '''
    def getKingMoves(self, r, c, moves):
        pass

class Move():
    # maps keys to values
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startcol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startcol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startcol * 100 + self.endRow * 10 + self.endCol


    '''
    overriding the equals method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        # you can add to make it like a real chess notation
        return self.getRankFile(self.startRow, self.startcol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

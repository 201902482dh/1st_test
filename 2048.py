class Block:
    def __init__(self,col,row,value,combine=False):
        self.pos_x = col
        self.pos_y = row
        self.value = block_image[value]
        self.combine = combine
        
class Board:
    def __init__(self):
        self.board = [[None,None,None,None],
                      [None,None,None,None],
                      [None,None,None,None],
                      [None,None,None,None] ] #block객체들을 저장하는 게임판

    """
    def move(self):     #왼쪽 이동
        for row in range(4):
            for col in range(1,4):
                
                self.board[row][col]
    def rotate(self):   #게임판을 시계방향으로 90도 회전

    def compare(self):  #block의 왼쪽 block과 비교

    def combine(self):  #두 block소멸 및 결합된 블럭 생성

    def create(self):   #게임판에 새로운 블럭 생성
    
    """

board = Board()

#보드전체 프린트
for row in range(4):
    for col in range(4):
        print(board.board[row][col],end = ' ')
    print('')
    
print(1==None)


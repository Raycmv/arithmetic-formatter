import re


class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        board_string = ''
        for index, line in enumerate(self.board):
            row_list = []
            for index2, part in enumerate(line, start=1):
                row_square = ''.join(str(item) for item in part)
                row_list.extend(row_square)

            row_list = row_list[:-4]
            row = f'{"".join(row_list)}\n'
            row_empty = row.replace('A', ' ')
            board_string += row_empty   
        return board_string

def addCero(arr, le, sig = 'A'):
    a = ['A','A','A','A'] 
    while len(arr) < (le + 2):
        arr.insert(0, sig)
    arr.extend(a)
    return arr


def arithmetic_arranger(problems, show_answers=False):
    arrceld = []
    pri = []
    sec = []
    ter = []
    cua = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for x in  problems:
        
        if re.search('[a-zA-z]', x):
            return 'Error: Numbers must only contain digits.'
        else:
            
            if x.find('-') > 0 or x.find('+') > 0:
                
                if len(x[:x.find('-') - 1]) < 5 and len(x[x.find('-') + 2:]) < 5:
                    a1 = x[:x.find('-') - 1]
                    a2 = x[x.find('-') + 2:]
                    a1 = list(a1)
                    a2 = list(a2)
                    gn = []
                    res =list(str(int(x[:x.find('-') -1])-int(x[x.find('-') + 2:])))
                    le = len(a1) if len(a1) > len(a2) else len(a2)
                    a1 = addCero(a1,le)
                    a2 = addCero(a2,le)
                    res = addCero(res,le)
                    gn = addCero(gn,le,'-')
                    a2[0] = '-'
                    pri.extend(a1)
                    sec.extend(a2)
                    ter.extend(gn)
                    cua.extend(res)
                elif len(x[:x.find('+') - 1]) < 5 and len(x[x.find('+') + 2:]) < 5:
                    b1 = x[:x.find('+') - 1]
                    b2 = x[x.find('+') + 2:]
                    b1 = list(b1)
                    b2 = list(b2)
                    gn = []
                    res = list(str(int(x[:x.find('+') - 1])+int(x[x.find('+') + 2:])))
                    le = len(b1) if len(b1) > len(b2) else len(b2)
                    b1 = addCero(b1,le)
                    b2 = addCero(b2,le)
                    res = addCero(res,le)
                    gn = addCero(gn,le,'-')
                    b2[0] = '+'
                    pri.extend(b1)
                    sec.extend(b2)
                    ter.extend(gn)
                    cua.extend(res)
                else:
                    return 'Error: Numbers cannot be more than four digits.'
            else:
                return "Error: Operator must be '+' or '-'."
    if show_answers:
        arrceld.extend([pri, sec, ter, cua])
    else:
        arrceld.extend([pri, sec, ter])
    return Board(arrceld)
     

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 - 49"],True)}')

v = f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}'
# expected output
z = '    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----'

print(v)
print(z)
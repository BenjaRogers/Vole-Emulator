def create_num_list():
    nums = []
    for x in range(0, 16):
        if x < 10:
            x = str(x)
        elif x >= 10:
            if x == 10:
                x = 'A'
            if x == 11:
                x = 'B'
            if x == 12:
                x = 'C'
            if x == 13:
                x = 'D'
            if x == 14:
                x = 'E'
            if x == 15:
                x = 'F'
        for y in range(0, 16):
            if y < 10:
                y = str(y)
            elif y >= 10:
                if y == 10:
                    y = 'A'
                if y == 11:
                    y = 'B'
                if y == 12:
                    y = 'C'
                if y == 13:
                    y = 'D'
                if y == 14:
                    y = 'E'
                if y == 15:
                    y = 'F'
            nums.append(str(x + y))
    print(nums)
def create_memory():
    memory = dict()
    for x in range(0, 16):
        if x < 10:
            x = str(x)
        elif x >= 10:
            if x == 10:
                x = 'A'
            if x == 11:
                x = 'B'
            if x == 12:
                x = 'C'
            if x == 13:
                x = 'D'
            if x == 14:
                x = 'E'
            if x == 15:
                x = 'F'
        for y in range(0, 16):
            if y < 10:
                y = str(y)
            elif y >= 10:
                if y == 10:
                    y = 'A'
                if y == 11:
                    y = 'B'
                if y == 12:
                    y = 'C'
                if y == 13:
                    y = 'D'
                if y == 14:
                    y = 'E'
                if y == 15:
                    y = 'F'

            memory[str(x + y)] = '00'
    return memory
def create_register():
    register = dict()
    for x in range(0, 16):
        if x < 10:
            x = str(x)
        elif x >= 10:
            if x == 10:
                x = 'A'
            if x == 11:
                x = 'B'
            if x == 12:
                x = 'C'
            if x == 13:
                x = 'D'
            if x == 14:
                x = 'E'
            if x == 15:
                x = 'F'
        register[x] = '00'
    return register

def hex_to_binary(hex_num):
    if hex_num == '0':
        bin_num = '0000'
    if hex_num == '1':
        bin_num = '0001'
    if hex_num == '2':
        bin_num = '0010'
    if hex_num == '3':
        bin_num = '0011'
    if hex_num == '4':
        bin_num = '0100'
    if hex_num == '5':
        bin_num = '0101'
    if hex_num == '6':
        bin_num = '0110'
    if hex_num == '7':
        bin_num = '0111'
    if hex_num == '8':
        bin_num = '1000'
    if hex_num == '9':
        bin_num = '1001'
    if hex_num == 'A':
        bin_num = '1010'
    if hex_num == 'B':
        bin_num = '1011'
    if hex_num == 'C':
        bin_num = '1100'
    if hex_num == 'D':
        bin_num = '1101'
    if hex_num == 'E':
        bin_num = '1110'
    if hex_num == 'F':
        bin_num = '1111'
    return bin_num

def binary_to_hex(bin_num):
    if bin_num == '0000':
        hex_num = '0'
    if bin_num == '0001':
        hex_num = '1'
    if bin_num == '0010':
        hex_num = '2'
    if bin_num == '0011':
        hex_num = '3'
    if bin_num == '0100':
        hex_num = '4'
    if bin_num == '0101':
        hex_num = '5'
    if bin_num == '0110':
        hex_num = '6'
    if bin_num == '0111':
        hex_num = '7'
    if bin_num == '1000':
        hex_num = '8'
    if bin_num == '1001':
        hex_num = '9'
    if bin_num == '1010':
        hex_num = 'A'
    if bin_num == '1011':
        hex_num = 'B'
    if bin_num == '1100':
        hex_num = 'C'
    if bin_num == '1101':
        hex_num = 'D'
    if bin_num == '1110':
        hex_num = 'E'
    if bin_num == '1111':
        hex_num = 'F'
    return hex_num

def binary_arithmetic(bin_num1, bin_num2):
    result = []
    carries = ['0']
    bin_num1 = [bit for bit in bin_num1]
    bin_num2 = [bit for bit in bin_num2]

    for i in range(-1, -9, -1):
        add_list = [bin_num1[i], bin_num2[i], carries[-1]]
        count = add_list.count('1')
        if count == 0:
            result.append('0')
            carries.append('0')
        if count == 1:
            result.append('1')
            carries.append('0')
        if count == 2:
            result.append('0')
            carries.append('1')
        if count == 3:
            result.append('1')
            carries.append('1')
    result.reverse()
    return result




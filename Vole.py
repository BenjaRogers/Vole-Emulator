from STUFF import hex_to_binary, binary_to_hex

HEX_NUMBERS = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0A', '0B', '0C', '0D', '0E', '0F', '10', '11',
        '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C', '1D', '1E', '1F', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '2A', '2B', '2C', '2D', '2E', '2F', '30', '31', '32', '33', '34', '35',
        '36', '37', '38', '39', '3A', '3B', '3C', '3D', '3E', '3F', '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
        '5A', '5B', '5C', '5D', '5E', '5F', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B',
        '6C', '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A', '7B', '7C', '7D',
        '7E', '7F', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8A', '8B', '8C', '8D', '8E', '8F',
        '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9A', '9B', '9C', '9D', '9E', '9F', 'A0', 'A1',
        'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'B0', 'B1', 'B2', 'B3',
        'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5',
        'C6', 'C7', 'C8', 'C9', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
        'D8', 'D9', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
        'EA', 'EB', 'EC', 'ED', 'EE', 'EF', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'FA', 'FB',
        'FC', 'FD', 'FE', 'FF']

HEX_NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
class Vole:

    def __init__(self, program=['1C', '03', '2B', '03', '5A', 'BC', '3A', '00', 'C0', '00']):
        self.program = program
        self.register = {'0': '00', '1': '00', '2': '00', '3': '00', '4': '00', '5': '00', '6': '00', '7': '00',
                         '8': '00', '9': '00', 'A': '00', 'B': '00', 'C': '00', 'D': '00', 'E': '00', 'F': '00'}
        self.memory = {'00': '00', '01': '00', '02': '00', '03': '00', '04': '00', '05': '00', '06': '00', '07': '00',
                       '08': '00', '09': '00', '0A': '00', '0B': '00', '0C': '00', '0D': '00', '0E': '00', '0F': '00',
                       '10': '00', '11': '00', '12': '00', '13': '00', '14': '00', '15': '00', '16': '00', '17': '00',
                       '18': '00', '19': '00', '1A': '00', '1B': '00', '1C': '00', '1D': '00', '1E': '00', '1F': '00',
                       '20': '00', '21': '00', '22': '00', '23': '00', '24': '00', '25': '00', '26': '00', '27': '00',
                       '28': '00', '29': '00', '2A': '00', '2B': '00', '2C': '00', '2D': '00', '2E': '00', '2F': '00',
                       '30': '00', '31': '00', '32': '00', '33': '00', '34': '00', '35': '00', '36': '00', '37': '00',
                       '38': '00', '39': '00', '3A': '00', '3B': '00', '3C': '00', '3D': '00', '3E': '00', '3F': '00',
                       '40': '00', '41': '00', '42': '00', '43': '00', '44': '00', '45': '00', '46': '00', '47': '00',
                       '48': '00', '49': '00', '4A': '00', '4B': '00', '4C': '00', '4D': '00', '4E': '00', '4F': '00',
                       '50': '00', '51': '00', '52': '00', '53': '00', '54': '00', '55': 'C0', '56': '00', '57': '00',
                       '58': '00', '59': '00', '5A': '00', '5B': '00', '5C': '00', '5D': '00', '5E': '00', '5F': '00',
                       '60': '00', '61': '00', '62': '00', '63': '00', '64': '00', '65': '00', '66': '00', '67': '00',
                       '68': '00', '69': '00', '6A': '00', '6B': '00', '6C': '00', '6D': '00', '6E': '00', '6F': '00',
                       '70': '00', '71': '00', '72': '00', '73': '00', '74': '00', '75': '00', '76': '00', '77': '00',
                       '78': '00', '79': '00', '7A': '00', '7B': '00', '7C': '00', '7D': '00', '7E': '00', '7F': '00',
                       '80': '00', '81': '00', '82': '00', '83': '00', '84': '00', '85': '00', '86': '00', '87': '00',
                       '88': '00', '89': '00', '8A': '00', '8B': '00', '8C': '00', '8D': '00', '8E': '00', '8F': '00',
                       '90': '00', '91': '00', '92': '00', '93': '00', '94': '00', '95': '00', '96': '00', '97': '00',
                       '98': '00', '99': '00', '9A': '00', '9B': '00', '9C': '00', '9D': '00', '9E': '00', '9F': '00',
                       'A0': '00', 'A1': '00', 'A2': '00', 'A3': '00', 'A4': '00', 'A5': '00', 'A6': '00', 'A7': '00',
                       'A8': '00', 'A9': '00', 'AA': '00', 'AB': '00', 'AC': '00', 'AD': '00', 'AE': '00', 'AF': '00',
                       'B0': '00', 'B1': '00', 'B2': '00', 'B3': '00', 'B4': '00', 'B5': '00', 'B6': '00', 'B7': '00',
                       'B8': '00', 'B9': '00', 'BA': '00', 'BB': '00', 'BC': '00', 'BD': '00', 'BE': '00', 'BF': '00',
                       'C0': '00', 'C1': '00', 'C2': '00', 'C3': '00', 'C4': '00', 'C5': '00', 'C6': '00', 'C7': '00',
                       'C8': '00', 'C9': '00', 'CA': '00', 'CB': '00', 'CC': '00', 'CD': '00', 'CE': '00', 'CF': '00',
                       'D0': '00', 'D1': '00', 'D2': '00', 'D3': '00', 'D4': '00', 'D5': '00', 'D6': '00', 'D7': '00',
                       'D8': '00', 'D9': '00', 'DA': '00', 'DB': '00', 'DC': '00', 'DD': '00', 'DE': '00', 'DF': '00',
                       'E0': '00', 'E1': '00', 'E2': '00', 'E3': '00', 'E4': '00', 'E5': '00', 'E6': '00', 'E7': '00',
                       'E8': '00', 'E9': '00', 'EA': '00', 'EB': '00', 'EC': '00', 'ED': '00', 'EE': '00', 'EF': '00',
                       'F0': '00', 'F1': '00', 'F2': '00', 'F3': '00', 'F4': '00', 'F5': '00', 'F6': '00', 'F7': '00',
                       'F8': '00', 'F9': '00', 'FA': '00', 'FB': '00', 'FC': '00', 'FD': '00', 'FE': '00', 'FF': '00'}
        self.program_counter = '0001'
        self.instruction_register = ''
        self.counter = 0
        self.run = True
    def save_program_to_memory(self):
        for num in range(len(self.program)):
            address = HEX_NUMBERS[num]
            self.memory[address] = self.program[num]

    def fetch(self):
        # Retrieve the next instruction from memory(as indicated by the program counter) and then increment the program counter (pg. 109)

        # Break program counter into 2 unique addresses
        address1 = self.program_counter[:2]
        address2 = self.program_counter[2:]

        # retrieve instruction from address 1 & 2
        instruction1 = str(self.memory[address1])
        instruction2 = str(self.memory[address2])

        # provide the instructions to the instruction register
        self.instruction_register = instruction1 + instruction2

        # Increment the program counter
        for i in HEX_NUMBERS:
            if i == address2:
                self.program_counter = str(HEX_NUMBERS[self.counter + 1]) + str(HEX_NUMBERS[self.counter + 2])
            else:
                self.counter += 1
        self.counter = 0

    def decode(self):
        # Decode the instructions in the instruction register

        # Split instructions into op-code and operand field
        opcode = self.instruction_register[0]
        operand = self.instruction_register[1:]
        return opcode, operand

    def execute(self):
        # Perform the action required by the instruction in the instruction register

        opcode, operand = self.decode()

        if opcode == '1':
            self.load1(operand)
        if opcode == '2':
            self.load2(operand)
        if opcode == '3':
            self.store(operand)
        if opcode == '4':
            self.move(operand)
        if opcode == '5':
            self.add_compliment(operand)
        if opcode == '6':
            self.add_float(operand)
        if opcode == '7':
            self.or_gate(operand)
        if opcode == '8':
            self.and_gate(operand)
        if opcode == '9':
            self.xor(operand)
        if opcode == 'A':
            self.rotate(operand)
        if opcode == 'B':
            self.jump(operand)
        if opcode == 'C':
            self.halt(operand)

    def load1(self, operand):
        #RXY	LOAD the register R with the bit pattern found in the memory cell whose address is XY.
        register_address = operand[0]
        memory_address = operand[1:]
        self.register[register_address] = self.memory[memory_address]
        print(f"Load register {register_address} with the bit pattern found in memory cell {memory_address} ({self.memory[memory_address]})")

    def load2(self, operand):
        # RXY	LOAD the register R with the bit pattern XY.
        register_address = operand[0]
        bit_pattern = operand[1:]
        self.register[register_address] = bit_pattern
        print(f"Load register {register_address} with the bit pattern {bit_pattern}")

    def store(self, operand):
        # RXY	STORE the bit pattern found in register R in the memory cell whose address is XY.

        register_address = operand[0]
        memory_address = operand[1:]
        self.memory[memory_address] = self.register[register_address]
        print(f"Store the bit pattern ({self.register[register_address]}) found in register {register_address} in memory cell {memory_address}")

    def move(self, operand):
        # 0RS	MOVE the bit pattern found in register R to register S.
        register_address_original = operand[1]
        register_address_recipient = operand[2]
        self.register[register_address_recipient] = self.register[register_address_original]
        print(f"Move the bit pattern found at register {register_address_original} ({self.register[register_address_original]}) to register {register_address_recipient}")

    def add_compliment(self, operand):
        # RST	ADD the bit patterns in registers S and T as though they were two’s complement representations
        # and leave the result in register R.

        register_recipient_address = operand[0]
        register_1_address = operand[1]
        register_2_address = operand[2]

        # get hex numbers to convert
        register_1_hex_num = self.register[register_1_address]
        register_2_hex_num = self.register[register_2_address]

        # Convert hex numbers to binary
        register_1_bin = str(hex_to_binary(register_1_hex_num[0]) + hex_to_binary(register_1_hex_num[1]))
        register_2_bin = str(hex_to_binary(register_2_hex_num[0]) + hex_to_binary(register_2_hex_num[1]))

        # Perform arithmetic on binary numbers
        answer_byte = self.binary_arithmetic(register_1_bin, register_2_bin)

        # Convert List to hex byte
        answer_byte_bin = ''.join(answer_byte)
        nibble1_bin = answer_byte_bin[:4]
        nibble2_bin = answer_byte_bin[4:]
        nibble1_hex = binary_to_hex(nibble1_bin)
        nibble2_hex = binary_to_hex(nibble2_bin)
        answer_byte_hex = nibble1_hex + nibble2_hex

        # Leave answer byte in register
        self.register[register_recipient_address] = answer_byte_hex
        print(f"Add the bit patterns at register {register_1_address} and {register_2_address} and store in register {register_recipient_address}")

    def add_float(self, operand):
        pass

    def or_gate(self, operand):
        # OR the bit patterns in registers S and T and place the result in register R.

        register_recipient_address = operand[0]
        register_1_address = operand[1]
        register_2_address = operand[2]

        # get hex numbers to convert
        register_1_hex_num = self.register[register_1_address]
        register_2_hex_num = self.register[register_2_address]

        # Convert hex numbers to binary
        register_1_bin = str(hex_to_binary(register_1_hex_num[0]) + hex_to_binary(register_1_hex_num[1]))
        register_2_bin = str(hex_to_binary(register_2_hex_num[0]) + hex_to_binary(register_2_hex_num[1]))

        # Separate bin numbers into lists for comparison
        register_1_bin_list = [num for num in register_1_bin]
        register_2_bin_list = [num for num in register_2_bin]

        # Compare lists
        answer_byte = list()
        for i in range(8):
            if register_1_bin_list[i] == '1' or register_2_bin_list[i] == '1':
                answer_byte.append('1')
            else:
                answer_byte.append('0')
                # Convert List to hex byte
        answer_byte_bin = ''.join(answer_byte)
        nibble1_bin = answer_byte_bin[:4]
        nibble2_bin = answer_byte_bin[4:]
        nibble1_hex = binary_to_hex(nibble1_bin)
        nibble2_hex = binary_to_hex(nibble2_bin)
        answer_byte_hex = nibble1_hex + nibble2_hex
        self.register[register_recipient_address] = answer_byte_hex
        print(f"Or the bit patterns in register {register_1_address} and register {register_2_address} and store in {register_recipient_address}")
    def and_gate(self, operand):
        register_recipient_address = operand[0]
        register_1_address = operand[1]
        register_2_address = operand[2]

        # get hex numbers to convert
        register_1_hex_num = self.register[register_1_address]
        register_2_hex_num = self.register[register_2_address]

        # Convert hex numbers to binary
        register_1_bin = str(hex_to_binary(register_1_hex_num[0]) + hex_to_binary(register_1_hex_num[1]))
        register_2_bin = str(hex_to_binary(register_2_hex_num[0]) + hex_to_binary(register_2_hex_num[1]))

        # Separate bin numbers into lists for comparison
        register_1_bin_list = [num for num in register_1_bin]
        register_2_bin_list = [num for num in register_2_bin]

        # Compare lists
        answer_byte = list()
        for i in range(8):
            if register_1_bin_list[i] == '1' and register_2_bin_list[i] == '1':
                answer_byte.append('1')
            else:
                answer_byte.append('0')
                # Convert List to hex byte
        answer_byte_bin = ''.join(answer_byte)
        nibble1_bin = answer_byte_bin[:4]
        nibble2_bin = answer_byte_bin[4:]
        nibble1_hex = binary_to_hex(nibble1_bin)
        nibble2_hex = binary_to_hex(nibble2_bin)
        answer_byte_hex = nibble1_hex + nibble2_hex
        self.register[register_recipient_address] = answer_byte_hex
        print(f"And the bit patterns in register {register_1_address} and register {register_2_address} and store in {register_recipient_address}")

    def xor(self, operand):
        #RST	EXCLUSIVE OR the bit patterns in registers S and T and place the result in register R.

        register_recipient_address = operand[0]
        register_1_address = operand[1]
        register_2_address = operand[2]

        # get hex numbers to convert
        register_1_hex_num = self.register[register_1_address]
        register_2_hex_num = self.register[register_2_address]

        # Convert hex numbers to binary
        register_1_bin = str(hex_to_binary(register_1_hex_num[0]) + hex_to_binary(register_1_hex_num[1]))
        register_2_bin = str(hex_to_binary(register_2_hex_num[0]) + hex_to_binary(register_2_hex_num[1]))

        # Separate bin numbers into lists for comparison
        register_1_bin_list = [num for num in register_1_bin]
        register_2_bin_list = [num for num in register_2_bin]

        # Compare lists
        answer_byte = list()
        for i in range(8):
            if register_1_bin_list[i] != register_2_bin_list[i]:
                answer_byte.append('1')
            else:
                answer_byte.append('0')
                # Convert List to hex byte
        answer_byte_bin = ''.join(answer_byte)
        nibble1_bin = answer_byte_bin[:4]
        nibble2_bin = answer_byte_bin[4:]
        nibble1_hex = binary_to_hex(nibble1_bin)
        nibble2_hex = binary_to_hex(nibble2_bin)
        answer_byte_hex = nibble1_hex + nibble2_hex
        self.register[register_recipient_address] = answer_byte_hex
        print(f"Xor the bit patterns in register {register_1_address} and register {register_2_address} and store in {register_recipient_address}")

    def rotate(self, operand):
        # R0X	ROTATE the bit pattern in register R one bit to the right X times. Each time place the bit that
        # started at the low-order end at the high-order end.
        count = 0
        register_address = operand[0]
        moves_right = operand[2]

        # Get contents of register and convert to bits.
        byte = self.register[register_address]
        register_bin = str(hex_to_binary(byte[0]) + hex_to_binary(byte[1]))
        register_bin_list = [bit for bit in register_bin]

        # convert moves_right to actual int
        for num in range(len(HEX_NUMBER)):
            if HEX_NUMBER[num] == moves_right:
                moves_right = count
                break
            count += 1

        # Move bits to right.
        for i in range(moves_right):
            num = register_bin_list.pop()
            register_bin_list.insert(0, num)
        # Convert back to hex.
        answer_byte_bin = ''.join(register_bin_list)
        nibble1_bin = answer_byte_bin[:4]
        nibble2_bin = answer_byte_bin[4:]
        nibble1_hex = binary_to_hex(nibble1_bin)
        nibble2_hex = binary_to_hex(nibble2_bin)
        answer_byte_hex = nibble1_hex + nibble2_hex

        self.register[register_address] = answer_byte_hex
        print(f"Rotate the bit pattern in register {register_address} one bit to the right {count} times")
    def jump(self, operand):
        # JUMP to the instruction located in the memory cell at address XY if the bit pattern in register R
        # is equal to the bit pattern in register number 0. Otherwise, continue with the normal sequence of
        # execution.

        memory_address = operand[1:]
        register_address = operand[0]

        # Check condition for jump
        if self.register[register_address] == self.register['0']:
            for i in range(len(HEX_NUMBERS)):
                if HEX_NUMBERS[i] == memory_address:
                    jump_address = HEX_NUMBERS[i] + HEX_NUMBERS[i + 1]
        self.program_counter = jump_address
        print(f"Jump to the instruction located in the memory cell at address {memory_address} if the bit pattern in register {register_address} is equal to the bit pattern in register 0")
    def halt(self, operand):
        self.run = False
        print("Halt")
    def binary_arithmetic(self, bin_num1, bin_num2):
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
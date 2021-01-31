from Vole import Vole



def main():
    program = list()
    instruction = ''
    while instruction != 'X':
        instruction = input("Enter 2 byte instruction, enter X to run program: ").upper()
        program.append(instruction)
    vole = Vole(program)
    vole.save_program_to_memory()
    while vole.run == True:
        vole.fetch()
        vole.execute()
        print(vole.program_counter)
    print("register: ", vole.register)
    print("Memory:  ", vole.memory)


main()
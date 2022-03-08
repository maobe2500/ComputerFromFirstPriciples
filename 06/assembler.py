#!/usr/bin/env python3
import sys
import re
from code import Code
from symboltable import SymbolTable
from parser import Parser


class Assembler():
    def __init__(self, file):
        self.file = file
        self.st = SymbolTable()
        self.code = Code(self.st)
        self.p = Parser(self.file, self.st)
        self.out = self.p.out
        self.binaries = []
        self.instructions = {}              #instrucitons to be translated into machine code
        self.out_lines = self.p.out_lines   #lines to be written to out.asm

    def parse(self):
        self.p.clean()
        self.p.scan_for_labels()
        self.instructions = self.p.unpack_instructions()
        print('\ninstructions: \n')
        print(self.instructions)

    def translate(self):
        code = self.code

        print('\nOut lines: \n')
        print(self.out_lines)
        print('')
        instructions = self.instructions
        for key in instructions:                        #instructions = {i : [AorC, dest, comp, jump]}
            
            instruction_list = instructions[key]
            print(instruction_list)        #instructions = [AorC, dest, comp jump]
            AorC, *i_list = instruction_list     #index = i, AorC = AorC, i_list = [dest, comp, jump]
            
            if (AorC == 'a'):

                Ainstruction = i_list[0]                #needs to be a key to look up in table
                address = code.translateA(Ainstruction)
                print(f'A instruction: {address}')
                self.binaries.append(address)
            
            if (AorC == 'c'):
                
                Cinstruction = i_list
                binary = code.translateC(Cinstruction)
                print(f'C instruction: {binary}')
                self.binaries.append(binary)


    def write(self):
        with open(f'{sys.argv[2]}', 'w') as file:
            for line in self.binaries:
                file.write(line + '\n')





def main():
    assembler = Assembler(f'./{sys.argv[1]}')
    assembler.parse()
    assembler.translate()
    assembler.write()
    print('\nsymboltable:\n')
    print(assembler.st.table)
    print('')
    print(assembler.out_lines)

if __name__ == '__main__':
    main() 


 

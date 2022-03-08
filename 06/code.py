#!/usr/bin/env python3

class Code():
    def __init__(self, table):
        self.table = table
        self.n = 16
        self.dest_code = {'null' : '000', 'M' : '001', 'D' : '010', 'MD' : '011',
                            'A' :'100', 'AM' : '101', 'AD' : '110', 'AMD' : '111'}
        self.jump_code = {'null' : '000', 'JGT' : '001', 'JEQ' : '010', 'JGE' : '011',
                            'JLT' : '100', 'JNE' : '101', 'JLE' : '110', 'JMP' : '111'}
        self.comp_code = { '0':'0101010',  '1':'0111111',  '-1':'0111010', 'D':'0001100', 
                            'A':'0110000',  '!D':'0001101', '!A':'0110001', '-D':'0001111', 
                            '-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110', 
                            'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111', 
                            'D&A':'0000000','D|A':'0010101','M':'1110000','!M':'1110001', 
                            '-M':'1110011','M+1':'1110111', 'M-1':'1110010','D+M':'1000010',
                            'D-M':'1010011','M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101' }

    #translates A instructions
    def translateA(self, code):         #needs a key to look up in the table
        if (self.table.exists(code) and code.isalpha()):
            return self.table.get_address(code)
        else:
            dec_address = int(code)
        bin_address = bin(dec_address)[2:].zfill(16)
        return bin_address

    def translateC(self, codelist):
        op_code = '111'

        for i in range(len(codelist)):
            code = codelist[i]
            if ('\n' in code):
                codelist[i] = codelist[i].replace('\n', '')

        comp = self.comp_code[codelist[0]]
        dest = self.dest_code[codelist[1]]
        jump = self.jump_code[codelist[2]]
        return f'{op_code}{comp}{dest}{jump}'
        

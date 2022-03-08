#!/usr/bin/env python3
import re
class Parser():
    def __init__(self, file, table):
        self.file = file
        self.out = 'out.asm'
        self.st = table
        self.label_list = []
        self.out_lines = []

    #Reads the input file and appends each character to self.all_lines
    def clean(self):
        with open(self.file) as file:
            lines = file.readlines()
            all_lines = []

            for line in lines:
                new_line = ''
                for char in line:
                    if (char == '/'):
                        break
                    else:
                        new_line += char
                if (new_line != '\n' and new_line != ''):   #Mysterious line of code
                    all_lines.append(new_line.strip() + '\n')
        print(all_lines)
        
        for line in all_lines:
            line = line.replace(' ', '')
            self.out_lines.append(line)


    def scan_for_labels(self):

        #Scan for labels
        for index, line in enumerate(self.out_lines):
            
            while True:
                m = re.search(r'\(.*\)', self.out_lines[index])
                islabel = True if m != None else False
                if islabel:

                    self.out_lines.remove(self.out_lines[index])
                    self.st.add(m.group(0)[1:-1], index)
                
                else:
                    break

        with open(self.out, 'w') as writefile:
            #Write the de-labeled text to out.asm
            for new_line in self.out_lines:
                #if (new_line == '\n'):
                #    self.out_lines.remove(new_line)
                writefile.write(new_line)


    def unpack_instructions(self):
        with open(self.out) as file:
            lines = file.readlines()
            instructions = {}
            n = 16
            for i in range(len(lines)):
                if (lines[i][0] != '@' and lines[i].find('=') == -1):
                    #print('found' + str(lines[i]))
                    lines[i] = '=' + lines[i]
            for i in range(len(lines)):

                
                line = lines[i]
                a = re.search(r'@.*', line)
                d = re.search(r'^[^@^0-9][A-Za-z^]*',line)
                c = re.search(r'=[A-Z]*[^A-Z^a-z^0-9;]?[A-Z0-9]?', line)
                j = re.search(r';.*[A-Z]', line)

                #print(f'a: {a}c: {c}d: {d}j: {j}')

                if (a != None):
                    a_list = ['a']
                    a_key = a.group(0)[1:]

                    if (self.st.exists(a_key)):
                        a_key = self.st.get_address(a_key)
                    else:
                        if (not a_key.isnumeric()): #sometimes it is not onlly alpha !!!!!!!!!
                                                    #FIX TOMORROW CANT HANDLE PONG
                            self.st.add(a_key, n)
                            a_key = n
                            n+=1
                        else:

                            self.st.add(a_key, int(a_key))


                    a_list.append(a_key)
                    instructions[i] = a_list
                
                #if (c == None and d ==  None):
                #    c = d
                #    d = None
                
                if (c != None):
                    c_list = ['c']
                    
                    comp = c.group(0)[1:]
                    print(f'COMP: {comp}')
                    c_list.append(comp)

                    if (d != None):                        
                        dest = d.group(0)
                        if (dest[0] != '='):
                            c_list.append(dest)
                        else:
                            c_list.append('null')
                    else:
                        c_list.append('null')

                    #appends jump if it exists otherwise null
                    if (j != None):
                        jump = j.group(0)[1:]
                        c_list.append(jump)
                    else:
                        c_list.append('null')

                    instructions[i] = c_list
            
            return instructions

                
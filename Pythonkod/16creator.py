#!/usr/bin/env python3

with open('Mux16.hdl', 'a') as f:
	for i in range(16):
		f.write('\n')
		f.write('\t')
		for j in range(2):
			a = 'sel'
			b = f'b[{i}]'
			if (j == 0):
				a = f'a[{i}]'
				b = 'aout0'
			f.write(f'And(a={a}, b={b}, out=and{j}out{i});\n\t')
		f.write(f'Or(a=and0out{i}, b=and1out{i}, out=out[{i}]);\n');





#     Not(in=sel, out=aout0);
#
#     And(a=a[0], b=aout0, out=and0out0);
#     And(a=sel, b=b[0], out=and1out0);
#     Or(a=and0out0, b=and1out0, out=out[0]);
print('Automation Done!')

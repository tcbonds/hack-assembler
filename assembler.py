import sys
from parser import Parser
from code import Code 
from symbol_table import SymbolTable

assembly_file = sys.argv[1]

parser = Parser(assembly_file)
code = Code()
symbol_table = SymbolTable()

binary_code = []
has_more_commands = parser.hasMoreCommands()
while has_more_commands:
	command_type = parser.commandType()
	symbol = parser.symbol(command_type)
	dest = parser.dest(command_type)
	comp = parser.comp(command_type)
	jump = parser.jump(command_type)

	if command_type == 'C_COMMAND':
		bin_comp = code.comp(comp)
		bin_dest = code.dest(dest)
		bin_jump = code.jump(jump)

		bin_out = f'111{bin_comp}{bin_dest}{bin_jump}'

	elif command_type == 'A_COMMAND':
		bin_symbol = bin(int(symbol))[2:]
		while len(bin_symbol) < 15:
		    bin_symbol = f'0{bin_symbol}'
		bin_out = f'0{bin_symbol}'

	elif command_type == 'L_COMMAND':
		bin_out = 'None'
		# bin_out = f'0{bin_symbol}'

	binary_code.append(f'{bin_out}\n')

	print('command_type', command_type)
	print('symbol',symbol)
	print('dest', dest)
	print('comp', comp)
	print('jump', jump)
	print('bin_out', bin_out)

	parser.advance()
	has_more_commands = parser.hasMoreCommands()
	print('more commands',has_more_commands,'\n')


	


# with open(assembly_file, 'r') as assembly_code:
# 	line_list = []
# 	for line in assembly_code:
# 		line_list.append(line)

# print(line_list)

# Parse lines into parts

# Decode those parts


# After translating the program, write 
# the binary code to a .hack extension file. 

# binary_code = \
# ['1100000011111001\n',
#  '1011000001011111\n',
#  '1011111110111011\n',
#  '0011010110111000\n',
#  '1011001011010001\n',
#  '1000000101100011\n',
#  '1001000011010101\n',
#  '0011010001000111\n',
#  '1000101110011101\n',
#  '1100100101111111\n']

filename = assembly_file.split('.')[0]
with open(f'{filename}.hack', 'w') as output_file:
	for line in binary_code:
		output_file.write(line)
import sys
from parser import Parser
from code import Code 
from symbol_table import SymbolTable

def convert_to_binary(val, bit_num):
	bin_val = bin(int(val))[2:]
	bin_val = bin_val.zfill(bit_num)
	return bin_val

class Assembler:

	def __init__(self, assembly_file):
		self.code = Code()
		self.symbol_table = SymbolTable()

	def pass_1(self):
		'''
		Iterate through lines. When you find a label,
		record the line number.
		'''

		parser1 = Parser(assembly_file)
		
		code_line_ix = 0

		while parser1.hasMoreCommands():
			parser1.advance()

			command_type = parser1.commandType()
			print(command_type)
			if command_type == 'L_COMMAND':
				symbol = parser1.symbol(command_type)
				if not self.symbol_table.contains(symbol):
					bin_code_line_ix = convert_to_binary(code_line_ix, 15)
					self.symbol_table.add_entry(symbol, bin_code_line_ix)
					print(symbol, code_line_ix)
			else:
				code_line_ix += 1

	def pass_2(self):
		'''
		Iterate through lines again. When a symbolic 
		A-instruction is encountered, look in the symbol table
		and if it doesn't exist, add it with the next available 
		address.
		'''

		parser2 = Parser(assembly_file)
		ram_address = 16


		while parser2.hasMoreCommands():
			parser2.advance()

			command_type = parser2.commandType()
			print(command_type)
			if command_type == 'A_COMMAND':
				symbol = parser2.symbol(command_type)
				if not symbol.isnumeric() and not self.symbol_table.contains(symbol):
					bin_ram_address = convert_to_binary(ram_address, 15)
					self.symbol_table.add_entry(symbol, bin_ram_address)
					print(symbol, ram_address)
					ram_address +=1

	def pass_main(self):

		parser = Parser(assembly_file)
		binary_code = []

		while parser.hasMoreCommands():
			parser.advance()

			command_type = parser.commandType()
			symbol = parser.symbol(command_type)
			dest = parser.dest(command_type)
			comp = parser.comp(command_type)
			jump = parser.jump(command_type)

			if command_type == 'C_COMMAND':
				bin_comp = self.code.comp(comp)
				bin_dest = self.code.dest(dest)
				bin_jump = self.code.jump(jump)

				bin_out = f'111{bin_comp}{bin_dest}{bin_jump}'

			elif command_type == 'A_COMMAND':
				if symbol.isnumeric():
					bin_out = convert_to_binary(symbol, 16)
				else:
					bin_symbol = self.symbol_table.get_address(symbol)
					bin_out = f'0{bin_symbol}'

			if command_type != 'L_COMMAND':
				binary_code.append(f'{bin_out}\n')

			print('command_type', command_type)
			print('symbol',symbol)
			print('dest', dest)
			print('comp', comp)
			print('jump', jump)
			print('bin_out', bin_out)
			print('more commands',parser.hasMoreCommands(),'\n')


		filename = assembly_file.split('.')[0]
		with open(f'{filename}.hack', 'w') as output_file:
			for line in binary_code:
				output_file.write(line)

	def assemble(self):
		self.pass_1()
		self.pass_2()
		self.pass_main()


if __name__ == '__main__':

	# TODO: Add ability to open files in different directories
	assembly_file = sys.argv[1]

	assembler = Assembler(assembly_file)
	assembler.assemble()
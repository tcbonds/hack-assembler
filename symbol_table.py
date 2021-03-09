class SymbolTable:

	 def __init__(self):
	 	self.symbol_table = \
	 	{
	 		'SP':'000000000000000',
	 		'LCL':'000000000000001',
	 		'ARG':'000000000000010',
	 		'THIS':'000000000000011',
	 		'THAT':'000000000000100',
	 		'R0':'000000000000000',
	 		'R1':'000000000000001',
	 		'R2':'000000000000010',
	 		'R3':'000000000000011',
	 		'R4':'000000000000100',
	 		'R5':'000000000000101',
	 		'R6':'000000000000110',
	 		'R7':'000000000000111',
	 		'R8':'000000000001000',
	 		'R9':'000000000001001',
	 		'R10':'000000000001010',
	 		'R11':'000000000001011',
	 		'R12':'000000000001100',
	 		'R13':'000000000001101',
	 		'R14':'000000000001110',
	 		'R15':'000000000001111',
	 		'SCREEN':'100000000000000',
	 		'KBD':'110000000000000',
	 	}

	 def add_entry(self, symbol, address):
	 	self.symbol_table[symbol] = address

	 def contains(self, symbol):
	 	contains = self.symbol_table.get(symbol) != None

	 	return contains

	 def get_address(self, symbol):
	 	return self.symbol_table.get(symbol)

if __name__ == '__main__':
	st = SymbolTable()
	st.add_entry('yo','mama')
	print(st.symbol_table)
	print(st.contains('yo'))
	print(st.get_address('yo'))

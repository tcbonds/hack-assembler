class SymbolTable:

	 def __init__(self):
	 	self.symbol_table = dict()

	 def add_entry(self, symbol, address):
	 	self.symbol_table[symbol] = address

	 def contains(self, symbol):
	 	contains = self.symbol_table.get(symbol) != None

	 	return contains

	 def get_address(self, symbol):
	 	return self.symbol_table.get(symbol)

st = SymbolTable()
st.add_entry('yo','mama')
print(st.contains('yo'))
print(st.get_address('yo'))

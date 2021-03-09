class Parser:
	
	def __init__(self, assembly_file):
		self.line_list = []

		with open(assembly_file, 'r') as assembly_code:
			for line in assembly_code:
				self.line_list.append(line)

		self.current_line_ix = None
		self.current_line = None
		self.line_total = len(self.line_list)

	def hasMoreCommands(self):
		if self.current_line_ix != None:
			return self.current_line_ix < self.line_total - 1
		else:
			return True # Parser has not begun parsing hence current_line_ix = None

	def advance(self):
		if self.current_line_ix != None:
			self.current_line_ix += 1
		else:
			self.current_line_ix = 0

		self.current_line = self.line_list[self.current_line_ix]

		if '//' == self.current_line[:2] or '\n' == self.current_line :
			self.advance()
		else:
			comment_ix = self.current_line.find('//')
			if comment_ix != -1:
				self.current_line = self.current_line[:comment_ix]
			for char in ['\n','\r',' ']:
				self.current_line = self.current_line.replace(char, '')
			print(r"{}".format(self.current_line))

	def commandType(self):
		try:
			self.current_line 
		except:
			self.current_line = self.line_list[0]

		print('CURRENT LINE', self.current_line)	
		if '@' in self.current_line:
			return 'A_COMMAND'
		elif '(' in self.current_line and ')' in self.current_line:
			return 'L_COMMAND'
		else:
			return 'C_COMMAND'

	def symbol(self, commandType):
		if commandType == 'A_COMMAND':
			return self.current_line[1:]
		elif commandType == 'L_COMMAND':
			if self.current_line_ix == 0:
				return self.current_line[1:-2]
			else:
				return self.current_line[1:-1]
			print(self.current_line)
		else:
			return None

	def dest(self, commandType):
		if commandType == 'C_COMMAND':
			equal_sign_ix = self.current_line.find('=')
			if equal_sign_ix != -1:
				return self.current_line[:equal_sign_ix]
			else:
				return None
		else:
			return None

	def comp(self, commandType):
		if commandType == 'C_COMMAND':
			equal_sign_ix = self.current_line.find('=')
			semicolon_ix = self.current_line.find(';')
			if equal_sign_ix != -1 and semicolon_ix != -1:
				return self.current_line[equal_sign_ix+1:semicolon_ix]
			elif equal_sign_ix == -1 and semicolon_ix != -1:
				return self.current_line[:semicolon_ix]
			elif equal_sign_ix != -1 and semicolon_ix == -1:
				return self.current_line[equal_sign_ix+1:]
		else:
			return None

	def jump(self, commandType):
		if commandType == 'C_COMMAND':
			semicolon_ix = self.current_line.find(';')
			if semicolon_ix != -1:
				return self.current_line[semicolon_ix+1:]

		else:
			return None
	














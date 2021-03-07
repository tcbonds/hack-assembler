class Parser:
	
	def __init__(self, assembly_file):
		self.line_list = []

		with open(assembly_file, 'r') as assembly_code:
			for line in assembly_code:
				self.line_list.append(line)

		self.clean()

		self.current_line_ix = 0
		self.current_line = self.line_list[self.current_line_ix]
		self.line_total = len(self.line_list)

	def clean(self):
		print('Before', self.line_list, '\n')
		clean_line_list = []
		for line in self.line_list:
			if '//' not in line and '\n' != line:
				line = line.replace('\n','')
				line = line.replace(' ','')
				line = line.replace('\r','')
				print(r"{}".format(line))
				clean_line_list.append(line)
		self.line_list = clean_line_list
		print('After',self.line_list)

	def hasMoreCommands(self):
		self.line_total = len(self.line_list)
		return self.current_line_ix < self.line_total

	# def clean(self):
	# 	while '//' in self.current_line or '\n' == self.current_line:
	# 		self.line_total = len(self.line_list)
	# 		if self.current_line_ix < self.line_total-1:
	# 			del self.line_list[self.current_line_ix]
	# 			self.current_line = self.line_list[self.current_line_ix]
	# 		else:
	# 			break
	# 	self.current_line = self.current_line.replace(' ','').replace('\n','')
	# 	print('current_line', self.current_line)
	# 	print('current_line_ix', self.current_line_ix)

	def advance(self):
		self.current_line_ix += 1
		try:
			self.current_line = self.line_list[self.current_line_ix]
		except:
			pass
		
	def commandType(self):
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
	














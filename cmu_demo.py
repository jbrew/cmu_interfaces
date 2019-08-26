
"""
In this demo, we'll load the CMU
"""



with open('resources/cmu_dict.txt') as f:
	lines = f.readlines()

cmu = {}

for line in lines[56:]:		# ignore comments
	word, phones = line.split('  ')
	cmu[word.strip()] = phones.strip()

print(cmu['FONZIE'])
# expected: ''

print(cmu.get('AYYY'))
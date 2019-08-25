import re
import string

"""

The CMUdict is distributed as a raw textfile.

Each line has a word, then two spaces, then some space-separated phonemes.

Each phoneme is either:
	- a consonant (e.g. K, D, SH)
	- a vowel followed by a stress marker (e.g. EH0, IY1)

Sample line format:

	FONZIE  F AA1 N Z IY0
	FOOBAR  F UW1 B AA1 R

For words with more than one pronunciation, each alternate pronunciation
is listed on a seperate line, marked by parens:
	
	DR  D R AY1 V
	DR(1)  D AA1 K T ER0

http://www.speech.cs.cmu.edu/cgi-bin/cmudict

"""


def build_cmu_dict_from_text_file():
	
	"""
	Return format is a dictionary mapping words to a list of
	possible pronunciations, each of which is a string of
	space-seperated phones of the format:

		D AA1 K T ER0
	"""

	with open('resources/cmu_dict.txt') as f:
		lines = f.readlines()

	# ignore comments
	lines = [line for line in lines if not line[:3] == ';;;']
	print(len(lines))

	cmu_dict = {}

	for line in lines:

		# split on double space
		word, phones = line.split('  ')

		# remove newlines
		word = word.strip()
		phones = phones.strip()

		# ignore parens denoting alt pronunciations
		if re.match('\([0-9]*\)', word[-3:]):
			word = word[:-3]

		update_dictionary(
			cmu_dict, word, phones)

		update_dictionary_with_punctuation_removed(
			cmu_dict, word, phones)

	return cmu_dict


def update_dictionary(cmu_dict, word, phones):
	if word in cmu_dict:
		cmu_dict[word].append(phones)
	else:
		cmu_dict[word] = [phones]

def update_dictionary_with_punctuation_removed(cmu_dict, word, phones):
	exclude = set(string.punctuation)
	punct_removed = ''.join(ch for ch in word if ch not in exclude)

	if punct_removed in cmu_dict and not phones in cmu_dict[punct_removed]:
		cmu_dict[punct_removed].append(phones)
	else:
		cmu_dict[punct_removed] = [phones]

def percent_coverage(cmu_dict, target_list):
	
	"""
	Given a target list of words, returns what fraction of them is
	included in the cmu_dict.

		cmu_dict:		Iterable[str]
		target_list: 	Iterable[str]

		percent: 		float
	"""
	num_covered = 0
	for word in target_list:
		if word.upper() in cmu_dict:
			num_covered += 1
	return num_covered / len(target_list)



def show_oddballs(cmu_dict, target_list):

	to_return = ''

	for i, word in enumerate(target_list):
		if not word.upper() in cmu_dict:
			to_return += str(i+1) + '\t' + word + '\n'

	return to_return




if __name__ == '__main__':

	cmu = build_cmu_dict_from_text_file()

	with open('resources/count_1w.txt') as f:
		google_words = [line.split('\t')[0].strip() for line in f.readlines()]

	print(len(google_words))

	print(percent_coverage(cmu, google_words[:10000]))

	print(show_oddballs(cmu, google_words[:2000]))


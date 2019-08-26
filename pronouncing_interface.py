import pronouncing
import random
import string

"""
Accessing phonetic data using Allison Parrish's `pronouncing.py`
interface to the CMUdict.
"""

"""
In this demo we'll use an index to help us dynamically search a list of
lines by pronunciation. Goal: write rhyming course reviews.


Dataset source: Kaggle user Rohan Sharma

https://www.kaggle.com/roshansharma/coursera-course-reviews/notebook


*** DRAWBACKS ***

One issue with CMUdict (if you ask me) is its tendency to assign primary
stress markers to words that rarely carry it.

>>> print(pronouncing.phones_for_word('of'))
['AH1 V']

We can correct this by manually adding pronunciations to the dictionary.

The CMU is limited to English, with a focus on North American pronunciations.

"""



def phones_for_line(line):
	"""

	Get a list of phones for the given line.

	If the line contains an unknown word, return None

	"""
	line_phones = []
	exclude = set(string.punctuation)

	for word in line.split():
		
		word = ''.join(ch for ch in word if ch not in exclude)
		
		word_phones_options = pronouncing.phones_for_word(word)
		
		if len(word_phones_options) == 0:
			return None
		else:
			line_phones.extend(word_phones_options[0].split())		# just take the first pronunciation
	
	return " ".join(line_phones)


def lines_by_rhyme(line_phones_pairs):
	rhyme_dict = {}
	for line, line_phones in line_phones_pairs:
		rhyming_part = pronouncing.rhyming_part(line_phones)

		if rhyming_part in rhyme_dict:
			rhyme_dict[rhyming_part].add(line)
		else:
			rhyme_dict[rhyming_part] = set([line])

	return rhyme_dict


def group_by_key_function(line_phones_pairs, key_function):

	return_dict = {}
	for line, phones in line_phones_pairs:
		key = key_function(line)

		if key in return_dict:
			return_dict[key].add(line)
		else:
			return_dict[key] = set([line])
	return return_dict


def last_word(line):
	return remove_punctuation(line.split()[-1])


def remove_punctuation(word):
	exclude = set(string.punctuation)
	return ''.join(ch for ch in word if ch not in exclude)



if __name__ == '__main__':


	with open('resources/coursera_pos.txt') as f:
		lines = [line.strip() for line in f.readlines()]

	from direct_load import load_google

	google_words = set([w for w in load_google()[:30000] if len(w) > 4])

	for line in lines:
		acronym = ''.join([w[0] for w in line.split()]).lower()

		if acronym in google_words:
			print(acronym)
			print(line)



	stop = input('enter?')

	lines_and_phones = [(line, phones_for_line(line)) for line in lines]

	# ignore if phones_for_line returned None
	lines_and_phones = [pair for pair in lines_and_phones if pair[1]]

	by_rhyme = lines_by_rhyme(lines_and_phones)

	by_last_word = group_by_key_function(lines_and_phones, key_function=last_word)

	for i in range(5):
		print(random.choice(list(by_last_word.items())))



"""
def entries_longer_than(d, threshold):
	return {k: v for k, v in d.items() if len(v) >= threshold}

def entries_with_more_than_n_distinct_ends(d, threshold):
	return {k: v for k, v in d.items() if num_distinct_end_words(v) >= threshold}

def num_distinct_end_words(rhyme_set):
	distinct_end_words = {remove_punctuation(word.lower()) for word in list(rhyme_set)}
	return len(distinct_end_words)



### VOWEL MATCHING ###

def vowels_for_phones(phones):
	return [phone for phone in phones.split() if phone[-1] in '012']

def last_n_vowels_for_phones(phones, n):
	return vowels_for_phones(phones)[-n:]

def lines_by_last_n_vowels(line_phones_pairs, n):
	last_vowel_dict = {}
	for line, phones in line_phones_pairs:
		key = " ".join(last_n_vowels_for_phones(phones, n))
		
		if not key in last_vowel_dict:
			last_vowel_dict[key] = set([line])
		else:
			last_vowel_dict[key].add(line)
	return last_vowel_dict

### STRESSED VOWEL MATCHING ###

def stressed_vowels_for_phones(phones):
	return [phone for phone in phones.split() if phone[-1] == '1']	# key_change

def last_n_stressed_vowels_for_phones(phones, n):
	return stressed_vowels_for_phones(phones)[-n:]

def lines_by_last_n_stressed_vowels(line_phones_pairs, n):
	last_vowel_dict = {}
	for line, phones in line_phones_pairs:
		key = " ".join(last_n_stressed_vowels_for_phones(phones, n))
		
		if not key in last_vowel_dict:
			last_vowel_dict[key] = set([line])
		else:
			last_vowel_dict[key].add(line)
	return last_vowel_dict


"""


"""
	many_rhymes = entries_with_more_than_n_distinct_ends(rhyme_dict, 20)
	print(len(many_rhymes), 'rhyme sets with 20 distinct_end_words')

	rhyme_set = random.choice(list(many_rhymes.values()))

	for i in range(10):
		print(random.choice(list(rhyme_set)))
"""








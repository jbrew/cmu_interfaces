import nltk.corpus
from direct_load import percent_coverage, load_google

"""
Accessing the CMU via NLTK's built-in `corpus` package.
"""


def print_longest(cmu, n=10):
	"""
	Prints out the top n entries in the cmu, ranked by how
	many alternative pronunciations they have.
	"""

	sorted_by_length = sorted(cmu.items(), key=lambda x: len(x[1]), reverse=True)

	for k, v in sorted_by_length[:n]:
		print(k)
		for pron in v:
			print('\t' + " ".join(pron))
		print()


if __name__ == '__main__':

	cmu = nltk.corpus.cmudict.dict()

	#print(len(cmu))
	#google_words = load_google()

	#print(percent_coverage(cmu, google_words[:10000]))

	print(cmu['our'])

	import pronouncing

	print(pronouncing.phones_for_word('dr'))


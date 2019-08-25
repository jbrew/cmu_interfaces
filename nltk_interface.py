import nltk.corpus
from direct_load import percent_coverage, load_google

"""
Here's how to access the CMU via NLTK's built-in `corpus` package.


"""


def print_longest(cmu, num_longest=10):
	sorted_by_length = sorted(cmu.items(), key=lambda x: len(x[1]), reverse=True)

	for k, v in sorted_by_length[:num_longest]:
		print(k)
		for pron in v:
			print('\t' + " ".join(pron))
		print()


if __name__ == '__main__':

	cmu = nltk.corpus.cmudict.dict()

	print(len(cmu))
	google_words = load_google()

	print(percent_coverage(cmu, google_words[:10000]))


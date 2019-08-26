import sys
import csv
import nltk.data

csv.field_size_limit(sys.maxsize)


with open('resources/reviews.csv', newline='') as csv_file:
	csvreader = csv.reader(csv_file)

	lines = []

	for row in csvreader:
		text = row[1]
		rating = row[2]
		lines.append([text, rating])

	print(len(lines))

	lines_by_rating = {str(i): set([]) for i in range(1, 5+1)}

	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

	for text, rating in lines[1:]:

		sents = [str(sent) for sent in sent_detector.tokenize(text.strip())]
		rating_string = str(rating)

		for sent in sents:
			lines_by_rating[rating_string].add(sent)


	with open('resources/coursera_neg.txt', 'w') as f:
		f.write('\n'.join(list(lines_by_rating['1'])))
		f.write('\n')
		f.write('\n'.join(list(lines_by_rating['2'])))
		f.write('\n')
		f.write('\n'.join(list(lines_by_rating['3'])))

	with open('resources/coursera_pos.txt', 'w') as f:
		f.write('\n'.join(list(lines_by_rating['4'])))
		f.write('\n')
		f.write('\n'.join(list(lines_by_rating['5'])))




import random

filename = "data.txt"
file_object = open(filename)

def clean_str(s):
	return s.replace("!", "").replace("(", "").replace(")", "")

# read last words of each row
lines = file_object.readlines()
endings = []

for line in lines:
	if len(line) > 0:
		if len(line.split()) >0:
			ending = line.split()[-1].lower()
			ending = clean_str(ending)
			endings.append(ending)


print(len(endings))
print(len(set(endings)))

# read the whole file, transform into list of words
file_object = open(filename)

text = file_object.read().lower()
text = text.replace("\n", " LINEBREAK ")
text = clean_str(text)
text_list = text.split()

# generate dictionary of words with their corresponding
# lists of following words, eg. {"hello" -> ["world"]}
text_lookup = {}
total_words = len(text_list)
for ix, wd in enumerate(text_list):
	new_word = text_list[(ix - 1 + total_words) % total_words]
	if wd in text_lookup:
		new_lookup = text_lookup[wd] + [new_word]
		text_lookup[wd] = new_lookup
	else:
		text_lookup[wd] = [new_word]

# create line given the final word
def create_line(ending):
	def next(wd):
		potential = text_lookup[wd]
		p = len(potential) / (1 + len(potential))
		if random.uniform(0.0, 1.0) < p:
			return random.choice(potential)
		else:
			return random.choice(text_list)

	sen = ending
	current = ending
	while current != "LINEBREAK":
		new_current = next(current)
		sen = new_current + " " + sen
		current = new_current

	# add another line break if there would be one
	# this separates verses from each other
	if next(current) == "LINEBREAK":
		sen = " LINEBREAK " + sen
	return sen.strip()


# number of lines to be generated
rnds = 1000
sentence = ""
current_ending = random.choice(endings)

for i in range(0, rnds):
	print(current_ending)
	current_line = create_line(current_ending)
	sentence += current_line

	potential = []
	for ix, wd in enumerate(endings):
		if wd == current_ending:
			new_word = endings[(ix+1) % len(endings)]
			potential.append(new_word)

	p = len(potential) / (1 + len(potential))
	print(len(potential), p)
	if random.uniform(0.0, 1.0) < p:
		current_ending = random.choice(potential)
	else:
		print("WILD CARD")
		current_ending = random.choice(endings)

print(sentence)

sentences = sentence.split("LINEBREAK LINEBREAK")
for ix, sentence in enumerate(sentences[1:-1]):
	sentence = sentence.replace("LINEBREAK", "\n")

	# skip Twitter unfriendly verses and one/two line verses
	if len(sentence) < 280 and sentence.count("\n") > 2:
		print("Säkeistö " + str(ix), "(" + str(len(sentence)) + "char) :")
		for line in sentence.splitlines():
			print(line.strip().capitalize())
		print("\n")

import string
import math

#Google
p1 = {}
f1 = open('google.txt', 'r')
for line in f1:
	List = line.split()
	for word in List:
		fixed_word = word.translate(None, string.punctuation).lower()
		if len(fixed_word) > 0:
			if p1.has_key(fixed_word):
				p1[fixed_word] += 1
			else:
				p1[fixed_word] = 1

print(p1["google"])

wordcount1 = 0
for word in p1.keys():
	wordcount1 += p1[word]

print(wordcount1)

entropy1 = 0
for word in p1.keys():
	entropy1 += -(float(p1[word])/wordcount1)*math.log(float(p1[word])/wordcount1, 2)

print(entropy1)

#Apple
p2 = {}
f2 = open('apple.txt', 'r')
for line in f2:
	List = line.split()
	for word in List:
		fixed_word = word.translate(None, string.punctuation).lower()
		if len(fixed_word) > 0:
			if p2.has_key(fixed_word):
				p2[fixed_word] += 1
			else:
				p2[fixed_word] = 1

print(p2["mac"])

wordcount2 = 0
for word in p2.keys():
	wordcount2 += p2[word]

print(wordcount2)

entropy2 = 0
for word in p2.keys():
	entropy2 += -(float(p2[word])/wordcount2)*math.log(float(p2[word])/wordcount2, 2)

print(entropy2)

#Facebook
p3 = {}
f3 = open('facebook.txt', 'r')
for line in f3:
	List = line.split()
	for word in List:
		fixed_word = word.translate(None, string.punctuation).lower()
		if len(fixed_word) > 0:
			if p3.has_key(fixed_word):
				p3[fixed_word] += 1
			else:
				p3[fixed_word] = 1

print(p3["messenger"])

wordcount3 = 0
for word in p3.keys():
	wordcount3 += p3[word]

print(wordcount3)

entropy3 = 0
for word in p3.keys():
	entropy3 += -(float(p3[word])/wordcount3)*math.log(float(p3[word])/wordcount3, 2)

print(entropy3)


#Between Google and Apple
entropy = 0
for word in ((p1.keys() or p2.keys())):
	ptot = 0
	if p1.has_key(word):
		ptot += (float(p1[word])/wordcount1)/2.0
	if p2.has_key(word):
		ptot += (float(p2[word])/wordcount2)/2.0
	entropy += -ptot*math.log(ptot, 2)

print(entropy)


#Between Google and Facebook
entropy = 0
for word in ((p1.keys() or p3.keys())):
	ptot = 0
	if p1.has_key(word):
		ptot += (float(p1[word])/wordcount1)/2.0
	if p3.has_key(word):
		ptot += (float(p3[word])/wordcount3)/2.0
	entropy += -ptot*math.log(ptot, 2)

print(entropy)

#Between Apple and Facebook
entropy = 0
for word in ((p2.keys() or p3.keys())):
	ptot = 0
	if p2.has_key(word):
		ptot += (float(p2[word])/wordcount2)/2.0
	if p3.has_key(word):
		ptot += (float(p3[word])/wordcount3)/2.0
	entropy += -ptot*math.log(ptot, 2)

print(entropy)

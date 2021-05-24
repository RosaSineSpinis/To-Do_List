# write your code here
import re, sys, argparse, math

'''stage 5'''


def compute_ari(number_of_characters, number_of_words, number_of_sentences):
    coef_a = 4.71
    coef_b = 0.5
    cons_c = 21.43
    ari_score = (coef_a * number_of_characters / number_of_words) + (coef_b * number_of_words / number_of_sentences) - cons_c
    # print("score", math.ceil(score))
    return ari_score


def compute_fk(number_of_words, number_of_sentences, syllables):
    fk_a = 0.39
    fk_b = 11.8
    fk_c = 15.59
    fk_score = fk_a * number_of_words/number_of_sentences + fk_b * syllables/number_of_words - 15.59
    return fk_score


def compute_smog(polysyllables, number_of_sentences):
    smog_a = 1.043
    smog_b = 30
    smog_c = 3.1291
    smog_score = smog_a * math.sqrt(polysyllables * smog_b / number_of_sentences) + smog_c
    return smog_score


def compute_cl(words, sentences):
    cl_a = 0.0588
    cl_b = 0.296
    cl_c = 15.8

    counter_of_chars = 0
    counter_of_words = 0
    for idx, word in enumerate(words):
        val = re.findall(r'[\w,.!?()]', word)
        # print("word", word)
        # print("val", val)
        counter_of_chars += len(val)
        counter_of_words += 1

    print("counter_of_chars", counter_of_chars)
    print("counter_of_words", counter_of_words)

    cl_L = 100 * counter_of_chars / counter_of_words
    # print("cl_L", cl_L)

    counter_sentences = 0
    counter_of_words = 0
    for idx, sentence in enumerate(sentences):
        val = sentence.split(' ')
        if '' in val:
            val.remove('')
        # print("val, ", val)
        counter_of_words += len(val)
        counter_sentences += 1

    cl_S = 100 * counter_sentences / counter_of_words
    # print("cl_s", cl_S)

    cl_score = cl_a * cl_L - cl_b * cl_S - cl_c

    # print("(cl_a * cl_L)", cl_a * cl_L)
    # print("(cl_b * cl_S)", cl_b * cl_S)
    # print("cl_c", cl_c)
    # print("cl_score", cl_score)
    return cl_score


def difficult_words(words, longman_words_list, number_of_words):
    longman_number = 0
    for word in words:
        val = ''.join(re.findall('\w+', word)).lower()
        # print("val", val)
        for longman_word in longman_words_list:
            if longman_word == val:
                # print("val", val, longman_word)
                longman_number += 1

    longman_number = number_of_words - longman_number

    return longman_number


def compute_longman(number_of_words, number_of_sentences, num_diff_words):
    long_a = 0.1579
    long_b = 100
    long_c = 0.0496

    longman_score = long_a * num_diff_words / number_of_words * long_b + long_c * number_of_words / number_of_sentences
    # print("num_diff_words / number_of_words", num_diff_words / number_of_words)
    if num_diff_words / number_of_words > 0.05:
       longman_score += 3.6365
    return longman_score


parser = argparse.ArgumentParser()
parser.add_argument('--infile')
parser.add_argument('--words')

args = parser.parse_args()

with open(args.infile, 'r') as f:
    string_input = f.read()

with open(args.words, 'r') as f:
    longman_words_list = []
    longman_word = f.read().split()
    # print("type", type(longman_word))
    # while longman_word:
    #     longman_word = f.readline()
    #     print("longman_word", longman_word)
    #     longman_words_list.append(longman_word)
    for word in longman_word:
        longman_words_list.append(word)
    # print("longman_word", longman_word)

# print("len(longman_words_list)", len(longman_words_list))

# print("longman_words_list", longman_words_list)

# print("string_input\n", string_input)

sentences = re.findall(r'[\w ,()]+[.?!]+|[\w ]+\.?$', string_input)
# print("sentences\n", sentences)

words = re.findall(r'\w+[,.?!]*\w*|\w+$', string_input)
# print("words,", words)

chars = re.findall(r'[\w,.!?()]', string_input)
# print("chars\n", chars)
#

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
syllables = 0
polysyllables = 0
monosyllables = 0
for word in words:
    # val = re.findall(r'[aeiouyAEIOUY]*[B-DF-HJ-NP-TV-XZb-df-hj-np-tv-xz]+[aeiouyAEIOUY]+|[\wx]+$', word)
    val = re.findall(r'[aeiouyAEIOUY]+[B-DF-HJ-NP-TV-XZb-df-hj-np-tv-xz]+', word)
    # print("val", word, val)
    length = len(val)
    # print("length", length)
    if length == 1:
        monosyllables += 1
        syllables += 1
    elif length == 0:
        monosyllables += 1
        syllables += 1
    elif length == 2:
        syllables += length
    else:
        polysyllables += 1
        syllables += length


number_of_sentences = len(sentences)
number_of_words = len(words)
number_of_characters = len(chars)
num_diff_words = difficult_words(words, longman_words_list, number_of_words)

longman_score_dict = {
                4: 10,
                5: 12,
                6: 14,
                7: 16,
                8: 18,
                9: 24,
                10: 25
                }

grades = {
    1: 6,
    2: 8,
    3: 9,
    4: 10,
    5: 11,
    6: 12,
    7: 13,
    8: 14,
    9: 15,
    10: 16,
    11: 17,
    12: 18,
    13: 24,
    14: 25
 }

# grades = {
#     1: "5-6",
#     2: "7-8",
#     3: "7-9",
#     4: "9-10",
#     5: "10-11",
#     6: "11-12",
#     7: "12-13",
#     8: "13-14",
#     9: "14-15",
#     10: "15-16",
#     11: "16-17",
#     12: "17-18",
#     13: "18-24",
#     14: "25"
#  }

# print("math.ceil(score)", math.ceil(score))
# print(grades[math.ceil(score)])

print(
    f"Words: {number_of_words}\n\
Difficult words: {num_diff_words}\n\
Sentences: {number_of_sentences}\n\
Characters: {number_of_characters}\n\
Syllables: {syllables}\n\
Polysyllables: {polysyllables}\n\
Enter the score you want to calculate (ARI, FK, SMOG, CL, PB, all):"
    )

choice_input = input()


ari_score = compute_ari(number_of_characters, number_of_words, number_of_sentences)
ari_score = round(ari_score, 2)
ari_age = grades[math.ceil(ari_score)]

fk_score = compute_fk(number_of_words, number_of_sentences, syllables)
fk_score = round(fk_score, 2)
fk_age = grades[math.ceil(fk_score)]

smog_score = compute_smog(polysyllables, number_of_sentences)
smog_score = round(smog_score, 2)
smog_age = grades[math.ceil(smog_score)]

cl_score = compute_cl(words, sentences)
cl_score = round(cl_score, 2)
cl_age = grades[math.floor(cl_score)]

longman_score = round(compute_longman(number_of_words, number_of_sentences, num_diff_words), 2)
if longman_score >= 10:
    longman_age = 25
else:
    longman_age = longman_score_dict[math.floor(longman_score)]

average_age = round((ari_age + fk_age + smog_age + cl_age + longman_age) / 5, 0)
if choice_input == "ARI":
    print(f"Automated Readability Index: {ari_score}\
(about {grades[math.ceil(ari_score)]}-year-olds-old).")
elif choice_input == "FK":
    print(f"Flesch–Kincaid readability tests: {fk_score}\
(about {grades[math.ceil(fk_score)]}-year-olds-old).")
elif choice_input == "SMOG":
    print(f"Simple Measure of Gobbledygook: {smog_score}\
 (about {grades[math.ceil(smog_score)]}-year-olds-old).")
elif choice_input == "CL":
    print(f"Coleman–Liau index: {cl_score}\
 (about {grades[math.ceil(cl_score)]}-year-olds-old).")
elif choice_input == "all":
    print(f"Automated Readability Index: {ari_score} (about {ari_age}-year-olds-old).\n\
Flesch–Kincaid readability tests: {fk_score} (about {fk_age}-year-olds-year-old).\n\
Simple Measure of Gobbledygook: {smog_score} (about {smog_age}-year-olds-old).\n\
Coleman–Liau index: {cl_score} (about {cl_age}-year-olds-old).\n\
Probability-based score: {longman_score} (about {longman_age}-year-olds-old)\n\n\
This text should be understood in average by {average_age}-year-old."
)


'''stage 4'''
''' using argparse'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--infile')
# args = parser.parse_args()
#
# with open(args.infile, 'r') as f:
#     string_input = f.read()
# # print("string_input\n", string_input)
#
# # sentences = re.split(r'[.?!]', string_input)
# sentences = re.findall(r'[\w ,()]+[.?!]+|[\w ]+\.?$', string_input)
# # print("sentences\n", sentences)
#
# words = re.findall(r'\w+[,.?!]*\w*|\w+$', string_input)
# # print("words,", words)
#
# chars = re.findall(r'[\w,.!?()]', string_input)
# # print("chars\n", chars)
# #
#
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# syllables = 0
# polysyllables = 0
# monosyllables = 0
# for word in words:
#     # val = re.findall(r'[aeiouyAEIOUY]*[B-DF-HJ-NP-TV-XZb-df-hj-np-tv-xz]+[aeiouyAEIOUY]+|[\wx]+$', word)
#     val = re.findall(r'[aeiouyAEIOUY]+[B-DF-HJ-NP-TV-XZb-df-hj-np-tv-xz]+', word)
#     # print("val", word, val)
#     length = len(val)
#     # print("length", length)
#     if length == 1:
#         monosyllables += 1
#         syllables += 1
#     elif length == 0:
#         monosyllables += 1
#         syllables += 1
#     elif length == 2:
#         syllables += length
#     else:
#         polysyllables += 1
#         syllables += length
#
# number_of_sentences = len(sentences)
# number_of_words = len(words)
# number_of_characters = len(chars)
#
# grades = {
#     1: "5-6",
#     2: "7-8",
#     3: "7-9",
#     4: "9-10",
#     5: "10-11",
#     6: "11-12",
#     7: "12-13",
#     8: "13-14",
#     9: "14-15",
#     10: "15-16",
#     11: "16-17",
#     12: "17-18",
#     13: "18-24",
#     14: "25"
#  }
#
# # print("math.ceil(score)", math.ceil(score))
# # print(grades[math.ceil(score)])
#
# print(
#     f"Words: {number_of_words}\n\
# Sentences: {number_of_sentences}\n\
# Characters: {number_of_characters}\n\
# Syllables: {syllables}\n\
# Polysyllables: {polysyllables}\n\
# Enter the score you want to calculate (ARI, FK, SMOG, CL, all):"
#     )
#
# choice_input = input()
#
#
# def compute_ari(number_of_characters, number_of_words, number_of_sentences, syllables):
#     coef_a = 4.71
#     coef_b = 0.5
#     cons_c = 21.43
#     ari_score = (coef_a * number_of_characters / number_of_words) + (coef_b * number_of_words / number_of_sentences) - cons_c
#     # print("score", math.ceil(score))
#     return ari_score
#
#
# def compute_fk(number_of_words, number_of_sentences, syllables):
#     fk_a = 0.39
#     fk_b = 11.8
#     fk_c = 15.59
#     fk_score = fk_a * number_of_words/number_of_sentences + fk_b * syllables/number_of_words - 15.59
#     return fk_score
#
#
# def compute_smog(polysyllables, number_of_sentences):
#     smog_a = 1.043
#     smog_b = 30
#     smog_c = 3.1291
#     smog_score = smog_a * math.sqrt(polysyllables * smog_b / number_of_sentences) + smog_c
#     return smog_score
#
#
# def compute_cl(words, sentences):
#     cl_a = 0.0588
#     cl_b = 0.296
#     cl_c = 15.8
#
#     counter_of_chars = 0
#     counter_of_words = 0
#     for idx, word in enumerate(words):
#         val = re.findall(r'[\w,.!?()]', word)
#         # print("word", word)
#         # print("val", val)
#         counter_of_chars += len(val)
#         counter_of_words += 1
#
#     print("counter_of_chars", counter_of_chars)
#     print("counter_of_words", counter_of_words)
#
#     cl_L = 100 * counter_of_chars / counter_of_words
#     # print("cl_L", cl_L)
#
#     counter_sentences = 0
#     counter_of_words = 0
#     for idx, sentence in enumerate(sentences):
#         val = sentence.split(' ')
#         if '' in val:
#             val.remove('')
#         # print("val, ", val)
#         counter_of_words += len(val)
#         counter_sentences += 1
#
#     cl_S = 100 * counter_sentences / counter_of_words
#     # print("cl_s", cl_S)
#
#     cl_score = cl_a * cl_L - cl_b * cl_S - cl_c
#
#     # print("(cl_a * cl_L)", cl_a * cl_L)
#     # print("(cl_b * cl_S)", cl_b * cl_S)
#     # print("cl_c", cl_c)
#     # print("cl_score", cl_score)
#     return cl_score
#
#
# ari_score = compute_ari(number_of_characters, number_of_words, number_of_sentences, syllables)
# ari_score = round(ari_score, 2)
# fk_score = compute_fk(number_of_words, number_of_sentences, syllables)
# fk_score = round(fk_score, 2)
# smog_score = compute_smog(polysyllables, number_of_sentences)
# smog_score = round(smog_score, 2)
# cl_score = compute_cl(words, sentences)
# cl_score = round(cl_score, 2)
#
# if choice_input == "ARI":
#     print(f"Automated Readability Index: {ari_score}\
# (about {grades[math.ceil(ari_score)]}-year-olds).")
# elif choice_input == "FK":
#     print(f"Flesch–Kincaid readability tests: {fk_score}\
# (about {grades[math.ceil(fk_score)]}-year-olds).")
# elif choice_input == "SMOG":
#     print(f"Simple Measure of Gobbledygook: {smog_score}\
#  (about {grades[math.ceil(smog_score)]}-year-olds).")
# elif choice_input == "CL":
#     print(f"Coleman–Liau index: {cl_score}\
#  (about {grades[math.ceil(cl_score)]}-year-olds).")
# elif choice_input == "all":
#     print(f"Automated Readability Index: {ari_score} (about {grades[math.ceil(ari_score)]}-year-olds).\n\
# Flesch–Kincaid readability tests: {fk_score} (about {grades[math.ceil(fk_score)]}-year-olds).\n\
# Simple Measure of Gobbledygook: {smog_score} (about {grades[math.ceil(smog_score)]}-year-olds).\n\
# Coleman–Liau index: {cl_score} (about {grades[math.floor(cl_score)]}-year-olds)."
#           )

"""stage 3"""

# '''hard coded srgs reader'''
# '''
# full_cmd_arguments = sys.argv
# # print("full_cmd_arguments", full_cmd_arguments)
# argument_list = full_cmd_arguments[1:]
# # print("argument_list", argument_list)
# file_input = full_cmd_arguments[2]
# # print("file_input", file_input)
# '''
#
# ''' using argparse'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--infile')
# args = parser.parse_args()
#
# with open(args.infile, 'r') as f:
#     string_input = f.read()
# print("string_input\n", string_input)
#
# # sentences = re.split(r'[.?!]', string_input)
# sentences = re.findall(r'[\w ,()]+[.?!]+|[\w ]+\.?$', string_input)
# print("sentences\n", sentences)
#
# words = re.findall(r'\w+[,.?!]*\w*|\w+$', string_input)
# print("words,", words)
#
# chars = re.findall(r'[\w,.!?()]', string_input)
# # print("chars\n", chars)
# #
#
#
# number_of_sentences = len(sentences)
# number_of_words = len(words)
# number_of_characters = len(chars)
#
# coef_a = 4.71
# coef_b = 0.5
# cons_c = 21.43
#
# score = (coef_a * number_of_characters / number_of_words) + (coef_b * number_of_words / number_of_sentences) - cons_c
# # print("score", math.ceil(score))
#
# grades = {
#     1: "5-6",
#     2: "7-8",
#     3: "7-9",
#     4: "9-10",
#     5: "10-11",
#     6: "11-12",
#     7: "12-13",
#     8: "13-14",
#     9: "14-15",
#     10: "15-16",
#     11: "16-17",
#     12: "17-18",
#     13: "18-24",
#     14: "25"
#  }
#
# # print("math.ceil(score)", math.ceil(score))
# # print(grades[math.ceil(score)])
#
# print(
#     f"Words: {number_of_words}\n\
# Sentences: {number_of_sentences}\n\
# Characters: {number_of_characters}\n\
# The score is: {round(score, 2)}\n\
# This text should be understood by {grades[math.ceil(score)]}-year-olds."
#     )

"""stage 2"""
# string_input = input()
# sentences = re.findall(r'[\w ,]+[.?!]+|[\w ]+$', string_input)
#
# # print("sentences", sentences)
#
# lengths = []
# for sentence in sentences:
#     result = re.findall(r'\w+', sentence)
#     lengths.append(len(result))
#
# # print("lengths", lengths)
# average = sum(lengths)/len(lengths)
# # print("average", average)
#
# if average <= 10:
#     print("EASY")
# else:
#     print("HARD")


""""stage 1"""
# result = re.match('.{0,100}', string_input)
# result = result.span()[1]
#
# # print(result)
#
# if result < 100:
#     print("EASY")
# else:
#     print("HARD")

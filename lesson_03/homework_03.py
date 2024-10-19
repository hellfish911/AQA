"""
This module processes a text excerpt from 'The Adventures of Tom Sawyer'.

It performs various text manipulations and analyses, aimed at extracting
and counting specific elements within the text.
"""

adventures_of_tom_sawyer = '''\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
'Big Missouri' worked ....
and sweated
in the sun,
"the retired artist sat on a barrel in the .... shade close by, "
    "dangled his legs."
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
"By the time Ben was fagged out, Tom had traded the next chance "
     "to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.'''

# Task 01
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace('\n', ' ')

# Task 02
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace('....', ' ')

# Task 03
adventures_of_tom_sawyer = ' '.join(adventures_of_tom_sawyer.split())

# Task 04
h_count = adventures_of_tom_sawyer.lower().count('h')
print(f'Кількість літер "h": {h_count}')

# Task 05
capitalized_words = [
    word for word in adventures_of_tom_sawyer.split() if word[0].isupper()
]
print(f'Кількість слів з Великої літери: {len(capitalized_words)}')

# Task 06
second_tom_position = (
    adventures_of_tom_sawyer.lower().split().index('tom',
    adventures_of_tom_sawyer.lower().split().index('tom') + 1)
)
print(f'Позиція другого слова "Tom": {second_tom_position + 1}')

# Task 07
adventures_of_tom_sawyer_sentences = adventures_of_tom_sawyer.split('. ')

# Task 08
fourth_sentence = adventures_of_tom_sawyer_sentences[3].lower()
print(f'Четверте речення в нижньому регістрі: {fourth_sentence}')

# Task 09
starts_with_by_the_time = any(
    sentence.startswith('By the time')
    for sentence in adventures_of_tom_sawyer_sentences
)
print(
    f'Чи починається якесь речення з "By the time": {starts_with_by_the_time}',
)

# Task 10
last_sentence_word_count = len(adventures_of_tom_sawyer_sentences[-1].split())
print(f'Кількість слів в останньому реченні: {last_sentence_word_count}')

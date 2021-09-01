import re

# This block of code removes the text between EXERCISES
# and ADDITIONAL EXERCISES

text = ''
regex = re.compile('(?s)(?<=EXERCISES).*?(?=ADDITIONAL EXERCISES)')

with open('MergedText.txt', encoding='utf-8') as f:
    lines = [line.rstrip() for line in f.readlines()]

    for line in lines:
        text += line
        text += '\n'

modified_text = re.sub(regex, ' ', text)
# print(modified_text)

text_file = open("Merged_No_Exercises.txt", "w", encoding='utf-8')
text_file.write(modified_text)
text_file.close()

'''
After the above code is finished .. had to manually 
remove the last ADDITIONAL EXERCISE.

This:

EXERCISES ADDITIONAL EXERCISES ADDITIONAL EXERCISES ADDITIONAL EXERCISES ADDITIONAL EXERCISES ADDITIONAL EXERCISES ADDITIONAL EXERCISES ADDITIONAL EXERCISES ADDITIONAL EXERCISES
Suppose that the electric field part of an electromagnetic wave in
vacuum is E = {(3.1 N/C) cos [(1.8 rad/m) y + (5.4 × 106 rad/s)t]} î .
About 5% of the power of a 100 W light bulb is converted to visible
radiation. What is the average intensity of visible radiation
Assume that the radiation is emitted isotropically and neglect
reflection.
Use the formula λ m T = 0.29 cm K to obtain the characteristic
temperature ranges for different parts of the electromagnetic
spectrum. What do the numbers that you obtain tell you?
Given below are some famous numbers associated with
electromagnetic radiations in different contexts in physics. State
the part of the electromagnetic spectrum to which each belongs.
space).
levels in hydrogen; known as Lamb shift).
all space-thought to be a relic of the ‘big-bang’ origin of the
universe].
associated with a famous high resolution spectroscopic method
Answer the following questions:
Why? astronomy is possible only from satellites orbiting the earth.
Why? human survival. Why?
surface temperature be higher or lower than what it is now?
earth would be followed by a severe ‘nuclear winter’ with a
devastating effect on life on earth. What might be the basis of
this prediction?
'''

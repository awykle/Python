# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 6 pg 100 - Challenges
# hashtagallison - Practice 2019-04-08
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 6: CHALLENGES
#               - Official Answer Key: http://tinyurl.com/hapm4dx  (Don't look until you try for yourself!!)
#-------------------------------------------


#1. Print every character in the string "Camus."

c = "Camus."

print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
print(c[5])

#2. Write a program that collects two strings from a user, and inserts them into the string:
#   "Yesterday I wrote a [response_one]. I sent it to [response_two]!" and prints a new string

response_one = input("Something with words: ")
response_two = input("A person: ")

story = """Yesterday I wrote a {}. 
I sent it to {}!""".format(response_one, response_two)

print(story)

#3. Use a method to make the string "aldous Huxley was born in 1894." grammatically correct by 
#   capitalizing the first word in the sentence.

huxley = "aldous Huxley was born in 1894."
huxley = huxley[:1].capitalize() + huxley[1:]

print(huxley)

#4. Take the string "Where now?" "Who now?" "When now?" and call a method that returns it to
#   look like: ["Where now?", "Who now?", "When now?"]

www = '"Where now?" "Who now?" "When now?"'
www_list = www.split("\" \"")

www_list[1] = www_list[1].replace("W", "\"W")
www_list[2] = www_list[2].replace("W", "\"W")
www_list[0] = www_list[0].replace("?", "?\"")
www_list[1] = www_list[1].replace("?", "?\"")

print(www_list)

#5. Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a grammatically
#   correct string. There should be a space between each word, but no space between the word fence and the 
#   period that follows it. (Don't forget, you learned a method to turn a list of strings into a single string.)

fox_list = ["The", 
            "fox", 
            "jumped", 
            "over", 
            "the", 
            "fence", 
            "."]

fox_story = " ".join(fox_list)
fox_story = fox_story.replace(" .", ".")

print(fox_story)

#6. Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign.

scream = "A screaming comes across the sky."
scream = scream.replace("s", "$")

print(scream)

#7. Use a method to find the first index of the character "m" in the string "Hemingway".

hemingway = "Hemingway"

m = hemingway.index("m")

print(m)

#8. Find dialogue in your favorite book (containing quotes) and turn it into a string.

quote = """\"A good programmer is someone 
who always looks both ways 
before crossing a one way 
street.\" - Doug Linder"""

print(quote)

#9. Create the string "three three three" using concatenation, and then again using multiplication.

three = "three " + "three " + "three"

print(three)

three = ("three " * 3).strip()

print(three)

#10. Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only
#    include the characters before the comma.

april = "It was a bright cold day in April, and the clocks were striking thirteen."

april = april[:33]

print(april)
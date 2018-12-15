# ShabakChallengeDataScience1

first I created a zip cracker in python and generated a list of passwords (only digits like the instructions said)

Then I found that the password is "262626".

I got three files:
- something.txt
- clue.png
- clueTwo.jpg

## something.txt

This file is accually a python code for finding text in image
I made it alittle bit nicer and named it: "extract_code.py"

I then ran it on clue.png and clueTwo.jpg

## clue.png

after I ran the extract_code.py on this image I saw an image that said "Binary, Start 10,000 place, fibonacii"

## clueTwo.jpg

upon applyin gextract_code.py here I didnt find anything so i though this image itself is the clue

I openned this image in 010 editor and went to the 10,000 binary place in the file (which is hex((10,000) / 8)) ) -> 0x4e2 and 
found a string: "youbgdboxzmktx...(..iqr..(...(...t...(...(...(".

## Extracting the code

This part was taking the string and printing all every data that had an index from the fibonacii sequence:

"you got it"

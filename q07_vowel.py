# See the vowels in text
def vowel(data):
    vowel = 'aeiou'
    for char in data:
        if char in vowel:
            return(char)
            
# Count the no of vowels in a text           
def count_vowel(data):
    vowel = 'aeiou'
    count = 0
    for char in data:
        if char in vowel:
            count += 1
    return count

text = "education"
assert vowel("stacy") == "a"
assert count_vowel("stacy") == 1

print(count_vowel(text))
     
    

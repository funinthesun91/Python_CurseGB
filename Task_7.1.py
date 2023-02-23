def check_rhythm(text):
       vowels_count = {}    
    phrases = text.split()   
    for phrase in phrases:        
        phrase = phrase.replace('-', '').lower()        
        count = sum(1 for letter in phrase if letter in 'aeiouy')        
        if count in vowels_count:
            vowels_count[count] += 1
        else:
            vowels_count[count] = 1   
    return len(set(vowels_count.values())) == 1
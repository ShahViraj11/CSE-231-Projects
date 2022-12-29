words = input('Enter a word (\'quit\' to quit): \n').lower()
vowels = 'aeiou'

while True:
    end = ''
    if words == "quit".lower():
        break
    else:
        if words[0] in vowels:
           end = words + 'way'
        else:
            if len(words) <= 1:
                end = words +'ay'
            else:
                for i, let in enumerate(words):
                    if let in vowels:
                        end = words[i:]+words[:i]+'ay'
                        break
    print(end)
    words = input('Enter a word (\'quit\' to quit): \n').lower()

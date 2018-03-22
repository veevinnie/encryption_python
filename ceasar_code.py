alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

message = input('Enter a message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    new_position = (position + 3)%26
    new_character = alphabet[new_position]
    new_message += new_character
  else:
    new_message += character
    
print(new_message)    

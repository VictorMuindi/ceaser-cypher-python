alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text):
   #separate the text
  def split(word): 
    return [char for char in word]    
  
  letter_list = split(text)
  word_number_list = []
  shuffled_mess = []

  #shuffle the letters
  for i in range(len(alphabet)):
    # print(letter_list[i])
    for i in range(len(text)):
      #find the letter in the alphabet list and assign a number to it
      word_number_list.append(alphabet.index(letter_list[i]))
     
      #shift the numbers up by 3 then print out the position on the alphabet list
    for i in range(len(word_number_list)):
      word_number_list[i] += 3
      shuffled_mess.append(alphabet[word_number_list[i]])
    
    encrypted_mess = ''.join(shuffled_mess)
          
    return encrypted_mess

def decrypt(text):
  #separate the text
  def split(word): 
    return [char for char in word]    

  letter_list = split(text)
  word_number_list = []
  unshuffled_mess = []

  #unshuffle the letters
  for i in range(len(alphabet)):
    # print(letter_list[i])
    for i in range(len(text)):
      #find the letter in the alphabet list and assign a number to it
      word_number_list.append(alphabet.index(letter_list[i]))
     
      #shift the numbers up by 3 then print out the position on the alphabet list
    for i in range(len(word_number_list)):
      word_number_list[i] -= 3
      unshuffled_mess.append(alphabet[word_number_list[i]])
    
    decrypted_mess = ''.join(unshuffled_mess)
          
    return decrypted_mess
  
#another function that 

print("Hey this is a ceaser cypher.")
user_choice = input("1.Encrypt or 2.Decrypt: ")

if user_choice == "1":
  #separates a string into specific words, encrypts those
  ceaser_string = input("Lets encrypt:")
  ceaser_string_list = ceaser_string.split()
  encrypted_ceaser_string = []

  for i in range(len(ceaser_string_list)):
    encrypted_ceaser_string.append(encrypt(ceaser_string_list[i]))

  print(*encrypted_ceaser_string)
elif user_choice == "2":
  #separates a string into specific words, decrypts those
  ceaser_string = input("Lets decrypt:")
  ceaser_string_list = ceaser_string.split()
  decrypted_ceaser_string = []

  for i in range(len(ceaser_string_list)):
    decrypted_ceaser_string.append(decrypt(ceaser_string_list[i]))

  print(*decrypted_ceaser_string)

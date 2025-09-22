def is_valid_word(word, letters, required_letter, used_words):
  if word == "END": #Check if the guess is END
    return True

  if len(word) < 4: #Check if the word is at least 4 letters long
    print("Your word must be at least 4 letters long")
    return False

  if required_letter not in word:  #Check if the required letter is present in the word
    print(f"Your word must contain the letter {required_letter}")
    return False

  for char in word:  #Check if there are any letters that aren't on the list
    if char not in letters:
      print(f"{char} is not a letter you can use. The only letters you can use are {letters}")
      return False

  if word in used_words:  #to check if word has alredy been used
    print("Already used")
    return False


  return True      


word = "apple"
letters = ['a', 'p', 'l', 'e']
required_letter = 'a'
used_words = ['banana']
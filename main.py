def replace_o(word: str) -> str:
  if 'o' in word.lower():
    return word.lower().replace('o','%')
  else:
    return "Burts 'O' nav!"

if __name__ == "_main_":
  print(replace_o("123123"))

#Exercise_01
def slicing(list_num, k):
  for i in range(0, len(list_num) - k + 1):
    tmp_list = list_num[i:i+k]
    print(tmp_list, end = " = ")
    print(max(tmp_list))
  return

#Exercise_02
def count_char(str):
  my_dict = {}
  for i in range(len(str)):
    my_dict[str[i]] = str.count(str[i])
  print(my_dict)
  return

#Exercise_03
def word_count(file_path):
  with open(file_path, 'r') as file:
    content = file.read()
    words = content.split()
    word_count = {}
    for word in words:
      word_count[word] = words.count(word)
    #print(words)
    print(word_count)
  return
word_count(r"D:\Study_Document\P1_data.txt")

#Exercise_04

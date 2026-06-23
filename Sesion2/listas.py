# Lists
list_1 = ["bacon",23,"cheese",True]

list_2 = [
  "banana",
  "pasta",
  "kiwi",
  "mango",
  list_1
]

print(list_1[:2])
print(list_2.index("kiwi"))

# Dictionaries
dictionary_1 = {
  "Computer Program": "A series of instructions that can be executed by a computer",
  "Syntax": "The rules we create for computers and programmers to follow to avoid ambiguity and give strict meanings",
  "Programming Language": "A formal set of syntax for writing a computer program"

}

dictionary_2 = {
  "pilot": "James",
  "co-pilot": "Paul",
  "stewards": [
    "Peter",
    "Carol",
    "Jane"
  ],
  "breakfast": list_2,
  "passengers": 203
}

print(dictionary_1["Syntax"])
print(dictionary_2["stewards"][2])
 
# creating the first project of choosen question answers
questions =[
  ["A. what keyword is used to define a fuction in python ?", " def", "fun", "function", "define", 1],
  ["B. Which of the following is an immutable data type ?"," List", "Dictionary","Tuple ", "Set", 3],
  ["C. Which symbol is used to comment a single line in Python ?","//","#","<!-->","%",2 ],
  ["D. Which module is used for random number generation in python ?", " os", "random","numpy","math",2 ],
  ["E. Which keyword is used to handle exceptions?","exception","catch","try","throw",3 ],
  ["F. What data type is returned by the input() fuction ?","int","str","float","bool",2 ],
  ["G. How do you check the type of an object in python ?","type ()","isinstance()","type(),","object()",3 ],
  ["H. Which operator is used for exponentiation in python ?","^","*","**","pow",3 ],
  ["I. Which method is used to convert a string to lowercase ?","lower()","toLower()","casefold()","downcase()",1 ],
  ["J. Which library is commonly used for data visualization in python?","pandas","matplotlib","sklearn","scipy",2 ],
  ["K. What does the len() function do in python?","Finds maximum value","Calculates length", "Slices a squence","Check type", 2 ],
  ["L. Which method is used to add an element to a list?","append","add","insert","extend", 1]
  
]
amounts =[1000, 2000, 3000, 5000, 10000, 20000, 40000,80000,160000,320000, 50000,"1 Crore"]
earn = 0
for i in range (0, len(questions)):
  question = questions[i]
  print(" ")
  print(f"   Question for Rs. {amounts[i]}")
  print(f"{question[0]}\n")
  print(f"1. {question[1]}          2. {question[2]}")
  print(f"3. {question[3]}          4. {question[4]} \n")
  answer = int(input("Enter Your answer according to index: "))
  if(answer == question[-1]):
    print(f"Correct Answer, You have won Rs. {amounts[i]}")
    if(i == 2):
      earn = 3000
    elif(i == 5):
      earn = 20000
    elif(i == 8):
      earn = 160000
    elif(i == 11):
      earn = "1 crore"  
     
  else:
    print("Wrong Answer !")
    break
print(f"Your Earning Amount is {earn}")

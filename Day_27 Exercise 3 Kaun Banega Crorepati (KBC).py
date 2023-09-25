# Create a program capable of displaying questions to the user like KBC.
# Use list data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

a = ("***LET'S START KAUN BANEGA CROREPATI***")
print(a.center(50))
print("Rules:\n1: If you quit,you will get prize money you won in previous question.\n2: If you give wrong answer, you will get checkpoint money, if you lose between q1-q3 you will get nothing.\n\n       'CHALIYE SHURU KARTE HEIN DEVIYO AUR SAJJANO'\n")
questions =[[
  "Who is the Prime minister of India?", "N.Modi", "Rahul Gandhi", "Sonia Gandhi", "Lalu Yadav" , 1],
["Who is the President of India?", "Manmohan Singh" , "Abdul Kalam", "D.Murmu", "J.Nehru", 3],
["Who is the KBC Host?" , "SRK" , "Salman Khan" , "Govinda" , "Amitabh Bachhan", 4],
["What is the National Fruit of India ?", "Mango", "Apple", "Tomato", "Orange", 1],
["How may letters does English have?", "25", "23", "56", "26", 4],
["How many hours does a single day have ?", "34", "24" , "34", "56", 2],
[" Rainbow consist of __colours", "4", "5","7","2",3], ["Name the National song of india?", "Hiphop", "pop","Vande Mataram", "jazz", 3],
["Name the national game of India.", "Hockey", "cricket", "Football", "baseball", 1],
["Name the capital of India.", "Pune","Delhi", "Bihar","Ohio", 2],
["Twitter's new name is___", "Tesla","Mark","X","Social", 3],
["Which country is largest in terms of area", "Bihar", "Bhutan","China","Russia",4],
 ["Which language is this", "Python","Java", "C++", "C",1],
 ["Guess the x value, avogadro number = 6.022 * 10 to the power 'x'","22","45","46","23",4],
["Guess My age", "23","21","19","18",3],
 ["I can bench how many lbs ?","200","225","300","295",2]]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0,len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for Rs {levels[i]} : \n{question[i-i]}")
  print(f"1.{question[1]}           \n2.{question[2]}")
  print(f"3.{question[3]}           \n4.{question[4]}")
  answer = int(input("Enter the correct option(1-4) or  0 to quit: "))
  if(answer == 0):
    print(f" You QUIT ;but dont mind, You won Rs {levels[i-1]}")
    break
  elif(answer == question[-1]):
    print(f"Correct answer\nCONGRATS!!!  You have Won Rs {levels[i]} ")
    if(i ==4):
     money = 10000
    elif(i ==9):
     money = 320000
    elif(i ==14):
     money = 10000000
  else:
    print("Wrong Answer \nBETTER LUCK NEXT TIME")
    break

print("You won Rs", money , "in this participation")
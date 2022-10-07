def options(x,y,z):
    print("A) ",x)
    print("B) ",y)
    print("C) ",z)



print("ARE YOU READY TO ANSWER 10 Questions?\n")
print("LET US BEGIN\n")

score = 0

total_questions = 10

correct_ans = ["python","Charles Babbage","Steve Jobs","ALPHABET Inc.","Meta","Elon Musk","Larry the Bird","Bengaluru","Stack","Queue"]

correct_options = ["b","a","b","c","c","a","c","b","c","a"]



print("Question 1 -> Which one of the follwoing is an interpreted language ? ")
options("C++","Python","JAVA\n")

your_ans =  input()

if your_ans.lower() == correct_ans[0].lower() or your_ans.lower() == correct_options[0].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")



print("Question 2 -> Who is known as Father of Computers ? ")
options("Charles Babbage","Steve Jobs","Mark Zuckerberg\n")

your_ans =  input()

if your_ans.lower() == correct_ans[1].lower() or your_ans.lower() == correct_options[1].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")



print("Question 3 -> Who is the founder of APPLE Inc ? ")
options("Jeff Bezos","Steve Jobs","Mark Zuckerberg\n")

your_ans =  input()

if your_ans.lower() == correct_ans[2].lower() or your_ans.lower() == correct_options[2].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")



print("Question 4 -> What is the name of the Parent Company of GOOGLE ? ")
options("YAHOO","AMAZON","ALPHABET Inc.\n")

your_ans =  input()

if your_ans.lower() == correct_ans[3].lower() or your_ans.lower() == correct_options[3].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")




print("Question 5 -> What is the new name of Facebook ? ")
options("Instagram","Face_notebook","Meta\n")

your_ans =  input()

if your_ans.lower() == correct_ans[4].lower() or your_ans.lower() == correct_options[4].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")




print("Question 6 -> Name the person who recently bought Twitter ? ")
options("Elon Musk","Mukesh Ambani","Jeff Bezos\n")

your_ans =  input()

if your_ans.lower() == correct_ans[5].lower() or your_ans.lower() == correct_options[5].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")




print("Question 7 -> Name of the Bird we see in Twitter App logo ? ")
options("Harry the Bird","Barry the Bird","Larry the Bird\n")

your_ans =  input()

if your_ans.lower() == correct_ans[6].lower() or your_ans.lower() == correct_options[6].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")





print("Question 8 -> Name the city which is known as the SILICON VALLEY of INDIA ? ")
options("Kolkata","Bengaluru","New Delhi\n")

your_ans =  input()

if your_ans.lower() == correct_ans[7].lower() or your_ans.lower() == correct_options[7].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")





print("Question 9 -> Which of the following Data Structure use LIFO format ? ")
options("Queue","Tree","Stack\n")

your_ans =  input()

if your_ans.lower() == correct_ans[8].lower() or your_ans.lower() == correct_options[8].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")





print("Question 10 -> Which of the following Data Structure use FIFO format ? ")
options("Queue","Tree","Stack\n")

your_ans =  input()

if your_ans.lower() == correct_ans[9].lower() or your_ans.lower() == correct_options[9].lower():
    score = score + 1
    print("Your ans/option was",your_ans.upper(),"which is ABSOLUTELY CORRECT\n")

else:
    print("OOOPS!!! your answer/option was",your_ans.upper(),"but it is INCORRECT\n")



print("THE QUIZ HAS ENDED.....WELL PLAYED!!!!")
if(score < 5):
    print("It seems you scored",score,"/10. Next time prepare Well\n")
elif(score >= 5 and score<=7):
    print("It seems you scored",score,"/10. Well Done!!!!....Next Time set your sight on Gold!!!\n")
elif(score > 7):
    print("It seems you scored",score,"/10. Lets Go!!!!....You scored Amazingly\n")

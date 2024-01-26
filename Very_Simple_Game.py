questions = [
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
    ["which language was correct?","Bangla","English","Sanskrit","Arabic"],
]
# print(questions[-1])//last list
levels=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000]
ans=[1,2,3,4,1,2,3,4,1,2,3,4]
money=0
for i in range(len(questions)):
    question=questions[i]
    # print(question[-1])//Arabic
    print(f"\n{i+1}.(Qustion for BDT.{levels[i]})")
    print("Which Language is correct?")
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[3]}   d. {question[4]}")
    print("(## HINTS ## -->Just like a Circle.)")
    reply=int(input("Enter your answer (1-4) or 0 to Finish:"))
    if(reply==0):
        money=levels[i-1]
        break
    # if(reply==question[-1])://last index
    if(reply==ans[i]):
        print(f"Correct Answer,You have won BDT. {levels[i]}")
        if(i==2):
            money=3000
        elif(i==5):
            money=6000
        elif(i==8):
            money=9000
        elif(i==11):
            money=12000
    else:
        print("Wrong Answer!!!")
        break
else:
    print("Thank You...")
print(f"Your take home money is ={money}")

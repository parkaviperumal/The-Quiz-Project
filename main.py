from questions_model import Question
from data import question_data
from quiz_brain import Quizbrain
question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
   
quiz=Quizbrain(question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()
    
percentage=(quiz.score/len(question_bank))*100
print("\nquiz completed!")
print(f"your final score was:{quiz.score}/{len(question_bank)}")
print(f"your percentage is:{percentage}%")

if percentage>=50:
    print("Result:passed")
else:
    print("Result:failed")




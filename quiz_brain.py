class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, curr_ans):
        if user_ans.lower() == curr_ans.lower():
            print("You got it right!!")
            self.score += 1
        elif user_ans=="off":
            self.question_number=len(self.questions_list)
        else:
            print("You got it wrong")
        print(f"The correct answer was this {curr_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()

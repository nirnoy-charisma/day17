class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):

        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer_user = input(f"Q.{self.question_number}{current_question.text} (True/False)")
        self.check_answer(answer_user, current_question.answer)

    def check_answer(self, user_answer, right_answer):

        if user_answer.lower() == right_answer.lower():
            self.score = +1
            print("You got it right!")
        else:
            print("Thats wrong.")
        print(f"The Correct answer was :{right_answer}")
        print(f"Your Score is {self.score}/{self.question_number}")
        print("\n\n")

class TudorQuiz:

    QuestionList = ["How long did the Tudors reign for?", "Who was Henry 7th's dad?", "Who was the last Tudor?", "Who was Henry 7ths mum?", "What age was Henry when he died?"]
    AnswerList = ["118 years", "Edmund Tudor", "Elizabeth 1st", "Lady Margret Beaufort", "52"]

    def runQuestions(self):
        score = 0
        print ("Welcome to my quiz.")
        for QuestionNumber in range(len(self.QuestionList)):
            answer = input(self.QuestionList[QuestionNumber] + " ")
            if answer == self.AnswerList[QuestionNumber]:
                print ("Correct")
                score += 1
            else:
                print ("Rong")
        print ("Your score is: " + str(score))
        self.restart()

    def restart(self):
        answer = input("Do you want to play again? (Y/N) ")
        if answer == "Y":
            self.runQuestions()
        else:
            print ("Goodbye.")

TudorQuiz().runQuestions()

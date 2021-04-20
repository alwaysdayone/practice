# coding = utf-8
# author = mochacha
# date = 2020.12.15

from survey import AnonyousSurvey

question = "What language did you learn first to speak?"
my_survey = AnonyousSurvey(question)
my_survey.show_question()
print("Enter 'q' at any time  to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)
        
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
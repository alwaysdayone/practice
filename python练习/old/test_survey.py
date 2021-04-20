# coding = utf-8
# author = mochacha
# date = 2020.12.15

import unittest
from survey import AnonyousSurvey

# class TestAnonmousSurvey(unittest.TestCase):
#     def test_single_response(self):
#         question = "What language did you learn first to speak?"
#         my_survey = AnonyousSurvey(question)
#         my_survey.store_response('English')
        
#         self.assertIn('English', my_survey.responses)
    
#     def test_three_responses(self):
#         question = "What language did you learn first to speak?"
#         my_survey = AnonyousSurvey(question)
#         responses = ['English', 'spanish', 'chinese']
#         for response in responses:
#             my_survey.store_response(response)
        
#         for response in responses:
#             self.assertIn(response, my_survey.responses)
        
# if __name__ == "__main__":
#     unittest.main()

class TestAnonmousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you learn first to speak?"
        self.my_survey = AnonyousSurvey(question)
        self.responses = ['English', 'Spanish', 'Chinese']
        
    def test_single_response(self):
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)
        
    def test_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.responses)
        
if __name__ == "__main__":
    unittest.main()
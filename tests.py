import unittest
from montra import Montra

class TestAuthenticationMethods(unittest.TestCase):

    """  
    This unit tests depends on certain parameters to be executed (this must be improved!)
    Dependencies:
    - Montra most be running at http://127.0.0.1:8000
    - User admin with password=123456 must exists
    - api token de4611bcf0c6e393404fac095dab09fad01c1554 must be defined
    - questionnaire "Demo Observational" must exists  
    - questionnaire "Demo Observational" must have at least one fingerprint associated
    - questionnaire with acronym="ADC", questionnaireSlug="adcohort" must exist with more than one fingerprint,
        which should have at least one question with one answer
    """
    def test_basic_auth(self):
        user="admin"
        password="123456"
        montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
        #if the request fails a None is returned
        listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
        self.assertIsNotNone(listOfQuestionnaires)

    def test_token_auth(self):
        token = "de4611bcf0c6e393404fac095dab09fad01c1554"
        montra = Montra(url="http://127.0.0.1:8000", token=token, auth_type='token')
        #if the request fails a None is returned
        listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
        self.assertIsNotNone(listOfQuestionnaires)

    def test_search_dataset(self):
        user="admin"
        password="123456"
        montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
        # in this test we assume that the questionnaire 'Demo Observational' exists
        listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
        self.assertTrue(len(listOfQuestionnaires) > 0)

    def test_get_dataset(self):
        user="admin"
        password="123456"
        montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
        # in this test we assume that the questionnaire 'Demo Observational' exists
        listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
        questionnaireSlug = listOfQuestionnaires[0]["slug"]
        questionnaire = montra.get_dataset( questionnaireSlug=questionnaireSlug)
        # we assume that there's at least one entry at fingerprint_set
        fingerprintHash = questionnaire["fingerprint_set"][0]
        self.assertTrue( (len(listOfQuestionnaires) > 0) and (fingerprintHash is not None) )

    def test_get_dataentry_1_param(self):
        user="admin"
        password="123456"
        montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
        # in this test we assume that the questionnaire 'Demo Observational' exists
        listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
        questionnaireSlug = listOfQuestionnaires[0]["slug"]
        questionnaire = montra.get_dataset( questionnaireSlug=questionnaireSlug)
        # we assume that there's at least one entry at fingerprint_set
        fingerprintHash = questionnaire["fingerprint_set"][0]     
        fingerprintOp1 = montra.get_dataentry(fingerprintHash=fingerprintHash)
        self.assertIsNotNone(fingerprintOp1)

    def test_get_dataentry_2_param(self):
        user="admin"
        password="123456"
        montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
        fingerprintOp2 = montra.get_dataentry( acronym="ADC", questionnaireSlug="adcohort")
        self.assertTrue((fingerprintOp2 is not None) and (fingerprintOp2["fingerprint_hash"]) )

    def test_get_answers(self):
        user="admin"
        password="123456"
        montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
        fingerprintOp2 = montra.get_dataentry( acronym="ADC", questionnaireSlug="adcohort")
        answers = montra.list_answer(fingerprintHash=fingerprintOp2["fingerprint_hash"])
        self.assertTrue((answers is not None) and (len(answers) > 0))

    def test_post_new_answer(self):
        user="admin"
        password="123456"
        montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
        fingerprintOp2 = montra.get_dataentry( acronym="ADC", questionnaireSlug="adcohort")
        answers = montra.list_answer(fingerprintHash=fingerprintOp2["fingerprint_hash"])
        question = answers[0]["question"]
        newAnswer = montra.post_answer(fingerprintHash=fingerprintOp2["fingerprint_hash"], question=question, newAnswer="newAnswer")
        self.assertEquals(newAnswer['data'], "newAnswer")

if __name__ == '__main__':
    unittest.main()


# #Used to test locally during development
# user="admin"
# password="123456"
# token="de4611bcf0c6e393404fac095dab09fad01c1554s"

# #montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
# montra = Montra(url="http://127.0.0.1:8000", auth_type='token', token=token)

# print " -- search_datasets --"
# listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
# questionnaireSlug = listOfQuestionnaires[0]["slug"]
# print questionnaireSlug
# print " -- search_datasets done -- \n"


# print " -- get_dataset --"
# questionnaire = montra.get_dataset( questionnaireSlug=questionnaireSlug)
# print questionnaire
# fingerprintHash = questionnaire["fingerprint_set"][0]
# print fingerprintHash
# print " -- search_datasets done -- \n"


# print " -- get_dataentry 1 param--"
# fingerprintOp1 = montra.get_dataentry(fingerprintHash=fingerprintHash)
# print fingerprintOp1
# print " -- get_dataentry 1 param done -- \n"


# print " -- get_dataentry 2 param --"
# fingerprintOp2 = montra.get_dataentry(acronym="ADC", questionnaireSlug="adcohort")
# print fingerprintOp2
# fingerprintHash2 = fingerprintOp2["fingerprint_hash"]
# print fingerprintHash2
# print " -- get_dataentry 2 param done -- \n"

# print " -- list_answer --"
# answers = montra.list_answer(fingerprintHash=fingerprintHash2)
# print answers
# print " -- list_answer done --"

# print " -- get_answer --"
# question = answers[0]["question"]
# print question
# answer = montra.get_answer(fingerprintHash=fingerprintHash2, question=question)
# print answer
# print " -- get_answer done--"

# print " -- post_answer --"
# newAnswer = montra.post_answer(fingerprintHash=fingerprintHash2, question=question, newAnswer="newAnswer")
# print newAnswer
# print " -- post_answer done--"
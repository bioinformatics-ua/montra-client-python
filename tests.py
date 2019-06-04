import unittest
from montra import Montra

# class TestAuthenticationMethods(unittest.TestCase):

#     def test_basic_auth(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()


#Used to test locally during development
user="admin"
password="123456"
token="de4611bcf0c6e393404fac095dab09fad01c1554s"

#montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
montra = Montra(url="http://127.0.0.1:8000", auth_type='token', token=token)

print " -- search_datasets --"
listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
questionnaireSlug = listOfQuestionnaires[0]["slug"]
print questionnaireSlug
print " -- search_datasets done -- \n"


print " -- get_dataset --"
questionnaire = montra.get_dataset( questionnaireSlug=questionnaireSlug)
print questionnaire
fingerprintHash = questionnaire["fingerprint_set"][0]
print fingerprintHash
print " -- search_datasets done -- \n"


print " -- get_dataentry 1 param--"
fingerprintOp1 = montra.get_dataentry(fingerprintHash=fingerprintHash)
print fingerprintOp1
print " -- get_dataentry 1 param done -- \n"


print " -- get_dataentry 2 param --"
fingerprintOp2 = montra.get_dataentry(acronym="ADC", questionnaireSlug="adcohort")
print fingerprintOp2
fingerprintHash2 = fingerprintOp2["fingerprint_hash"]
print fingerprintHash2
print " -- get_dataentry 2 param done -- \n"

print " -- list_answer --"
answers = montra.list_answer(fingerprintHash=fingerprintHash2)
print answers
print " -- list_answer done --"

print " -- get_answer --"
question = answers[0]["question"]
print question
answer = montra.get_answer(fingerprintHash=fingerprintHash2, question=question)
print answer
print " -- get_answer done--"

print " -- post_answer --"
newAnswer = montra.post_answer(fingerprintHash=fingerprintHash2, question=question, newAnswer="newAnswer")
print newAnswer
print " -- post_answer done--"
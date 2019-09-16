import unittest
from montra import Montra

#Used to test locally during development
user="admin"
password="12345"
token="de4611bcf0c6e393404fac095dab09fad01c1554"

#montra = Montra(url="http://127.0.0.1:8000", username=user, password=password)
montra = Montra(url="http://127.0.0.1:8000", token=token)

print " -- search_datasets --"
listOfQuestionnaires = montra.search_datasets(questionnaire="Demo Observational")
questionnaireSlug = listOfQuestionnaires[0]["slug"]
print questionnaireSlug
print " -- search_datasets done -- \n"


print " -- get_dataset --"
questionnaire = montra.get_dataset(communityName="DEMO", questionnaireSlug=questionnaireSlug)
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

print " -- put_answer --"
newAnswer = montra.put_answer(fingerprintHash=fingerprintHash2, question=question, newAnswer="newAnswer")
print newAnswer
print " -- put_answer done--"

print " -- new_dataentry -- "
newDataenty = montra.new_dataentry(communityName="DEMO", questionnaireSlug=questionnaireSlug)
print newDataenty
newDataentyHash = newDataenty["fingerprint_hash"]
answers = montra.list_answer(fingerprintHash=newDataentyHash)
question = answers[0]["question"]
newAnswer = montra.put_answer(fingerprintHash=newDataentyHash, question=question, newAnswer="newAnswerInNewDataEntry")
#print newAnswer
print " -- new_dataentry done-- "
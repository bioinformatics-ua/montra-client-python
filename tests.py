from montra import Montra


#Used to test locally during development
user="admin"
password="12345"

montra = Montra(url="http://127.0.0.1:8000")

print(" -- search_datasets --")
listOfQuestionnaires = montra.search_datasets(user, password, questionnaire="Demo Observational")
questionnaireSlug = listOfQuestionnaires[0]["slug"]
print(questionnaireSlug)
print(" -- search_datasets done -- \n")


print(" -- get_dataset --")
questionnaire = montra.get_dataset(user, password, questionnaireSlug=questionnaireSlug)
print(questionnaire)
print(fingerprint)
print(" -- search_datasets done -- \n")


print(" -- get_dataentry 1 param--")
print(fingerprintOp1)
print(" -- get_dataentry 1 param done -- \n")


print(" -- get_dataentry 2 param --")
fingerprintOp2 = montra.get_dataentry(user, password, acronym="ADC", questionnaireSlug="adcohort")
print(fingerprintOp2)
fingerprintHash2 = fingerprintOp2["fingerprint_hash"]
print(fingerprintHash2)
print(" -- get_dataentry 2 param done -- \n")

print(" -- list_answer --")
answers = montra.list_answer(user, password, fingerprintHash=fingerprintHash2)
print(answers)
print(" -- list_answer done --")

print(" -- get_answer --")
question = answers[0]["question"]
print(question)
answer = montra.get_answer(user, password, fingerprintHash=fingerprintHash2, question=question)
print(answer)
print(" -- get_answer done--")

print(" -- post_answer --")
newAnswer = montra.post_answer(user, password, fingerprintHash=fingerprintHash2, question=question, newAnswer="newAnswer")
print(newAnswer)
print(" -- post_answer done--")
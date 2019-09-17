import unittest
import argparse
import sys
from montra import Montra
import time

_USER = 'admin'
_PASS = '123456'
_TOKEN = 'de4611bcf0c6e393404fac095dab09fad01c1111'
_URL = 'http://127.0.0.1:8000'
_DATASET = "demo-slug"
_COMM = "Test Comm"

def main():

    # global vars
    global _USER
    global _PASS
    global _TOKEN
    global _URL
    global _DATASET
    global _COMM

    # parse arguments
    parser = argparse.ArgumentParser(description='Run tests on montra client.')
    parser.add_argument('--url', help='Montra URL')
    parser.add_argument('--user', help='Montra Username')
    parser.add_argument('--password', help='Montra Password')
    parser.add_argument('--token', help='Montra Token')
    parser.add_argument('--dataset_slug', help='Existing dataset slug (the API doesn\' allow to create a dataset)')
    parser.add_argument('--comm', help='Existing community name (the API doesn\' allow to create a community)')
    args = parser.parse_args()

    # update global vars
    if args.url:
        _URL = args.url
        sys.argv.remove('--url')
        sys.argv.remove(args.url)
    if args.user:
        _USER = args.user
        sys.argv.remove('--user')
        sys.argv.remove(args.user)
    if args.password:
        _PASS = args.password
        sys.argv.remove('--password')
        sys.argv.remove(args.password)
    if args.dataset_slug:
        _DATASET= args.dataset_slug
        sys.argv.remove('--dataset_slug')
        sys.argv.remove(args.dataset_slug)
    if args.comm:
        _COMM= args.comm
        sys.argv.remove('--comm')
        sys.argv.remove(args.comm)
    if args.token:
        _TOKEN = args.token
        sys.argv.remove('--token')
        sys.argv.remove(args.token)

    # call unittest main function
    unittest.main()

class TestAuthenticationMethods(unittest.TestCase):


    def test_basic_auth(self):

        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # if the request fails a None is returned
        listOfQuestionnaires = montra.search_datasets(questionnaire="")
        self.assertIsNotNone(listOfQuestionnaires)


    def test_token_auth(self):
        
        montra = Montra(url=_URL, token=_TOKEN)
        
        # if the request fails a None is returned
        listOfQuestionnaires = montra.search_datasets(questionnaire="")
        self.assertIsNotNone(listOfQuestionnaires)


    def test_search_dataset(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # search for the configured dataset from any community
        listOfQuestionnaires = montra.search_datasets(questionnaire=_DATASET)
        self.assertTrue(len(listOfQuestionnaires) > 0)

        # search using first char
        listOfQuestionnaires = montra.search_datasets(questionnaire=_DATASET[:1])
        self.assertTrue(len(listOfQuestionnaires) > 0)

        # search using last char
        listOfQuestionnaires = montra.search_datasets(questionnaire=_DATASET[1:])
        self.assertTrue(len(listOfQuestionnaires) > 0)

        # search for any dataset on the specified community
        listOfQuestionnaires = montra.search_datasets(questionnaire="")
        self.assertTrue(len(listOfQuestionnaires) > 0)


    def test_get_dataset(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # get specified dataset from the specified community
        questionnaire = montra.get_dataset( communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone( questionnaire )


    def test_create_database(self):
       
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # add database 
        database_name = "Test" + str(time.time())
        dataentry = montra.new_dataentry( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(dataentry)


    def test_get_dataentry_1_param(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # add database
        database_name = "Test" + str(time.time())
        dataentry = montra.new_dataentry( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(dataentry)
        
        # get fingerprint by hash
        fingerprintOp1 = montra.get_dataentry(fingerprintHash=dataentry['fingerprint_hash'])
        self.assertIsNotNone(fingerprintOp1)


    def test_get_dataentry_2_param(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # add database
        database_name = "Test" + str(time.time())
        dataentry = montra.new_dataentry( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(dataentry)
        
        # get database by using its name
        fingerprintOp2 = montra.get_dataentry( database_name=database_name, communityName=_COMM)
        self.assertTrue((fingerprintOp2 is not None) and (fingerprintOp2["fingerprint_hash"]) )


    def test_list_answers(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        #create fingerprint
        database_name = "Test" + str(time.time())
        dataentry = montra.new_dataentry( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(dataentry)

        # get answers
        answers = montra.list_answer(fingerprintHash=dataentry["fingerprint_hash"])
        self.assertTrue((answers is not None) and (len(answers) > 0))

    
    def test_get_answer(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        #create fingerprint
        database_name = "Test" + str(time.time())
        dataentry = montra.new_dataentry( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(dataentry)

        # get answer
        answer = montra.get_answer(fingerprintHash=dataentry["fingerprint_hash"], question = 'email_PI')
        self.assertEquals(answer['question'], 'email_PI')


    def test_update_an_answer(self):

        montra = Montra(url=_URL, username=_USER, password=_PASS)

        #create fingerprint
        database_name = "Test" + str(time.time())
        dataentry = montra.new_dataentry( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(dataentry)

        # get answers
        answers = montra.list_answer(fingerprintHash=dataentry["fingerprint_hash"])
        self.assertTrue((answers is not None) and (len(answers) > 0))

        #edit answers
        # email
        question = 'email_PI'
        newAnswer = montra.put_answer(fingerprintHash=dataentry["fingerprint_hash"], question=question, newAnswer="pedrofreire@ua.pt")
        self.assertEquals(newAnswer['data'], "pedrofreire@ua.pt")
   
        # phone
        question = 'SC__phone'
        newAnswer = montra.put_answer(fingerprintHash=dataentry["fingerprint_hash"], question=question, newAnswer="+351933933933")
        self.assertEquals(newAnswer['data'], "+351933933933")

        # unknown question
        question = 'SC__phone99999'
        newAnswer = montra.put_answer(fingerprintHash=dataentry["fingerprint_hash"], question=question, newAnswer="+351933933933")
        self.assertIsNone(newAnswer)

    
    def test_update_an_answer_with_an_invalid_question(self):

        montra = Montra(url=_URL, username=_USER, password=_PASS)

        #create fingerprint
        database_name = "Test" + str(time.time())
        dataentry = montra.new_dataentry( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(dataentry)

        # get answers
        answers = montra.list_answer(fingerprintHash=dataentry["fingerprint_hash"])
        self.assertTrue((answers is not None) and (len(answers) > 0))

        #edit answers
        # unknown question
        question = 'SC__phone99999'
        newAnswer = montra.put_answer(fingerprintHash=dataentry["fingerprint_hash"], question=question, newAnswer="+351933933933")
        self.assertIsNone(newAnswer)


if __name__ == '__main__':
    main()

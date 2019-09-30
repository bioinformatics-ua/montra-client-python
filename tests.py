import unittest
import argparse
import sys
from montra import Montra
import time

_USER = 'admin'
_PASS = 'emif'
_TOKEN = '876a281ad0a1644d09df7f241346ea6fcbf2059b'
_URL = 'http://127.0.0.1:8000'
_DATASET = "ehden_final"
_COMM = "Community test"

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
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)

    def test_create_duplicated_databases(self):
       
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # add database 
        database_name = "TestDuplicated" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNone(database)

    def test_update_database(self):
       
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # add database 
        database_name = "Test" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)

        # update db
        database = montra.update_database( database['fingerprint_hash'], draft=False, description="Teste123")
        self.assertIsNotNone(database)
        self.assertTrue(database['description'] == 'Teste123')
        self.assertTrue(database['draft'] == False)


    def test_get_database_1_param(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # add database
        database_name = "Test" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)
        
        # get fingerprint by hash
        fingerprint = montra.get_database(fingerprintHash=database['fingerprint_hash'])
        self.assertIsNotNone(fingerprint)


    def test_get_database_2_param(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # add database
        database_name = "Test" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)
        
        # get database by using its name
        fingerprint = montra.get_database( database_name=database_name, communityName=_COMM)
        self.assertIsNotNone(fingerprint)

    def test_get_database_with_invalid_database_name(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        # get database by using its name
        fingerprint = montra.get_database( database_name='some_invalid_db_name', communityName=_COMM)
        self.assertIsNone(fingerprint)


    def test_list_answers(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        #create fingerprint
        database_name = "Test" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)

        # get answers
        answers = montra.list_answer(fingerprintHash=database["fingerprint_hash"])
        self.assertTrue((answers is not None) and (len(answers) > 0))

    
    def test_get_answer(self):
        
        montra = Montra(url=_URL, username=_USER, password=_PASS)
        
        #create fingerprint
        database_name = "Test" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)

        # get answer
        answer = montra.get_answer(fingerprintHash=database["fingerprint_hash"], question = 'email_PI')
        self.assertEquals(answer['question'], 'email_PI')


    def test_update_an_answer(self):

        montra = Montra(url=_URL, username=_USER, password=_PASS)

        #create fingerprint
        database_name = "Test" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)

        # get answers
        answers = montra.list_answer(fingerprintHash=database["fingerprint_hash"])
        self.assertTrue((answers is not None) and (len(answers) > 0))

        #edit answers
        # email
        question = 'email_PI'
        newAnswer = montra.put_answer(fingerprintHash=database["fingerprint_hash"], question=question, newAnswer="pedrofreire@ua.pt")
        self.assertEquals(newAnswer['data'], "pedrofreire@ua.pt")
   
        # phone
        question = 'SC__phone'
        newAnswer = montra.put_answer(fingerprintHash=database["fingerprint_hash"], question=question, newAnswer="+351933933933")
        self.assertEquals(newAnswer['data'], "+351933933933")

        # unknown question
        question = 'SC__phone99999'
        newAnswer = montra.put_answer(fingerprintHash=database["fingerprint_hash"], question=question, newAnswer="+351933933933")
        self.assertIsNone(newAnswer)

    
    def test_update_an_answer_with_an_invalid_question(self):

        montra = Montra(url=_URL, username=_USER, password=_PASS)

        #create fingerprint
        database_name = "Test" + str(time.time())
        database = montra.new_database( database_name=database_name, description="Teste", communityName=_COMM, questionnaireSlug=_DATASET)
        self.assertIsNotNone(database)

        # get answers
        answers = montra.list_answer(fingerprintHash=database["fingerprint_hash"])
        self.assertTrue((answers is not None) and (len(answers) > 0))

        #edit answers
        # unknown question
        question = 'SC__phone99999'
        newAnswer = montra.put_answer(fingerprintHash=database["fingerprint_hash"], question=question, newAnswer="+351933933933")
        self.assertIsNone(newAnswer)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'montra'
__version__ = '6.0'
__author__ = 'João Rafael Almeida'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2019, João Rafael Almeida, Universidade de Aveiro'
__url__ = 'https://github.com/bioinformatics-ua/montra-client-python'

__maintainer__ = 'João Rafael Almeida'
__email__ = 'joao.rafael.almeida@ua.pt'

__all__ = ()

import requests
from requests.auth import HTTPDigestAuth

URL = 'https://bioinformatics.ua.pt/ehden'
COMM = "ehden"
AUTH_TYPE = 'basic'
ERROR_MESSAGES = {
    "bad_auth_type": "Authentication type not valid. Authentication type should be set as 'basic' or 'token' ",
    "bad_auth_params": ("Authentication parameters are missing! Please provide valid credentials." 
                        "You can use either an username and password for a basic authentication or a valid API token using token authentication"),
    "bad_get_request_generic": "Something wrong with the request!"
}

class Montra:
    def __init__(self, url=URL, auth_type=AUTH_TYPE, username=None, password=None, token=None):

        #params validation
        if auth_type not in ['basic', 'token']:
            raise ValueError(ERROR_MESSAGES["bad_auth_type"])

        if ( auth_type == 'basic' and (username is None or password is None) ) \
            and ( auth_type == 'token' and token is None ):
            raise ValueError(ERROR_MESSAGES["bad_auth_params"])

        self.ENDPOINT = url
        self.USERNAME = username
        self.PASSWORD = password
        self.TOKEN = token
        self.AUTH_TYPE = auth_type

    def search_datasets(self, questionnaire=COMM):
        """
        Search for the questionnaires in all communities

        return: the list of questionnaires
        """
        url = self.ENDPOINT + "/api/questionnaires/?search=" + str(questionnaire)

        return self.__get_request(url=url)

    def get_dataset(self, questionnaireSlug=COMM):
        """
        Gets the dataset by the slug, which is the identifier

        return: json with the dataset (questionnaire)
        """
        url = self.ENDPOINT + "/api/questionnaires/" + str(questionnaireSlug)
        
        return self.__get_request(url=url)

    def get_dataentry(self, **args):
        if(len(args) == 1):
            return self.__get_dataentry_by_hash(args["fingerprintHash"])
        else:
            return self.__get_dataentry_by_acronym(args["acronym"], args["questionnaireSlug"])

    def __get_dataentry_by_hash(self, fingerprintHash):
        """
        Gets the fingerprint by the fingprint hash

        return: json with the fingerprint 
        """
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash)
        
        return self.__get_request(url=url)

    def __get_dataentry_by_acronym(self, acronym, questionnaireSlug=COMM):
        """
        Gets the fingerprint by the fingprint acronym and the questionnaire slug

        return: json with the fingerprint 
        """
        url = self.ENDPOINT + "/api/fingerprint-cslug-fslug/" + str(questionnaireSlug) + "/" + str(acronym)

        return self.__get_request(url=url)

    def list_answer(self, fingerprintHash):
        """
        Gets the list of available questions to get or update data of the fingerprint hash

        return: json with the fingerprint available questions (some types not available in the API)
        """
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash) + "/answers"

        return self.__get_request(url=url)

    def get_answer(self, fingerprintHash, question):
        """
        Gets the the question of the fingerprint hash

        return: json with question and answer
        """
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash) + "/answers/" + str(question)

        return self.__get_request(url=url)

    def post_answer(self, fingerprintHash, question, newAnswer):
        """
        Post a new answer in the question of the fingerprint hash

        return: json with question and answer
        """
        try:
            url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash) + "/answers/" + str(question) + "/"

            if self.AUTH_TYPE == 'basic':
                response = requests.put(url, auth=(self.USERNAME, self.PASSWORD), data={"data":newAnswer})
            elif self.AUTH_TYPE == 'token':
                response = requests.put(url, headers={'Authorization': 'Token ' + self.TOKEN}, data={"data":newAnswer})

            response.raise_for_status()

            return response.json()
        except requests.exceptions.HTTPError as err:
            print err
            sys.exit(1)

    def __get_request(self, url):
        try:
            if self.AUTH_TYPE == 'basic':
                response = requests.get(url, auth=(self.USERNAME, self.PASSWORD))
            elif self.AUTH_TYPE == 'token':
                response = requests.get(url, headers={'Authorization': 'Token ' + self.TOKEN})
            else:
                raise ValueError(ERROR_MESSAGES["bad_auth_type"])

            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print err
            sys.exit(1)
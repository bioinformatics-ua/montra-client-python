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

ERROR_MESSAGES = {
    "bad_arg": "The argments passed in the constructor are invalid! Please provide a token or the basic credentials using the parameters 'username' and 'password'",
    "bad_auth_type": "Authentication type not valid. Authentication type should be set as 'basic' or 'token' ",
    "bad_auth_params": ("Authentication parameters are missing! Please provide valid credentials." 
                        "You can use either an username and password for a basic authentication or a valid API token using token authentication"),
    "bad_get_request_generic": "Something wrong with the request!"
}

class Montra:
    def __init__(self, url=URL, **args):
        if "token" in args:
            self.token = args["token"]
            self.auth_type = 'token'
        elif "username" in args and "password" in args:
            self.username = args["username"]
            self.password = args["password"]
            self.auth_type = 'basic'
        else:
            raise ValueError(ERROR_MESSAGES["bad_arg"])
        self.ENDPOINT = url

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
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash) + "/answers/" + str(question) + "/"

        return self.__post_request(url=url, data={"data":newAnswer})

    def __get_request(self, url):
        try:
            if self.auth_type == 'basic':
                response = requests.get(url, auth=(self.username, self.password))
            elif self.auth_type == 'token':
                response = requests.get(url, headers={'Authorization': 'Token ' + self.token})
            else:
                raise ValueError(ERROR_MESSAGES["bad_auth_type"])
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print err
            sys.exit(1)

    def __post_request(self, url, data):
        try:
            if self.auth_type == 'basic':
                response = requests.put(url, auth=(self.username, self.password), data=data)
            elif self.auth_type == 'token':
                response = requests.put(url, headers={'Authorization': 'Token ' + self.token}, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print err
            return None

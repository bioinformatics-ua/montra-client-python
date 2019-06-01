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

class Montra:
    def __init__(self, url=URL):
        self.ENDPOINT = url

    def search_datasets(self, user, password, questionnaire=COMM):
        """
        Search for the questionnaires in all communities

        return: the list of questionnaires
        """
        url = self.ENDPOINT + "/api/questionnaires/?search=" + str(questionnaire)

        return self.__get_request(url=url, auth=(user, password))

    def get_dataset(self, user, password, questionnaireSlug=COMM):
        """
        Gets the dataset by the slug, which is the identifier

        return: json with the dataset (questionnaire)
        """
        url = self.ENDPOINT + "/api/questionnaires/" + str(questionnaireSlug)
        
        return self.__get_request(url=url, auth=(user, password))

    def get_dataentry(self, user, password, **args):
        if(len(args) == 1):
            return self.__get_dataentry_by_hash(user, password, args["fingerprintHash"])
        else:
            return self.__get_dataentry_by_acronym(user, password, args["acronym"], args["questionnaireSlug"])

    def __get_dataentry_by_hash(self, user, password, fingerprintHash):
        """
        Gets the fingerprint by the fingprint hash

        return: json with the fingerprint 
        """
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash)
        
        return self.__get_request(url=url, auth=(user, password))

    def __get_dataentry_by_acronym(self, user, password, acronym, questionnaireSlug=COMM):
        """
        Gets the fingerprint by the fingprint acronym and the questionnaire slug

        return: json with the fingerprint 
        """
        url = self.ENDPOINT + "/api/fingerprint-cslug-fslug/" + str(questionnaireSlug) + "/" + str(acronym)

        return self.__get_request(url=url, auth=(user, password))

    def list_answer(self, user, password, fingerprintHash):
        """
        Gets the list of available questions to get or update data of the fingerprint hash

        return: json with the fingerprint available questions (some types not available in the API)
        """
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash) + "/answers"

        return self.__get_request(url=url, auth=(user, password))

    def get_answer(self, user, password, fingerprintHash, question):
        """
        Gets the the question of the fingerprint hash

        return: json with question and answer
        """
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash) + "/answers/" + str(question)

        return self.__get_request(url=url, auth=(user, password))

    def post_answer(self, user, password, fingerprintHash, question, newAnswer):
        """
        Post a new answer in the question of the fingerprint hash

        return: json with question and answer
        """
        url = self.ENDPOINT + "/api/fingerprints/" + str(fingerprintHash) + "/answers/" + str(question) + "/"

        response = requests.put(url, auth=(user, password), data={"data":newAnswer})
        return response.json()

    def __get_request(self, url, auth):
        try:
            response = requests.get(url, auth=auth)
            return response.json()
        except:
            raise Exception("Something wrong with the request!")
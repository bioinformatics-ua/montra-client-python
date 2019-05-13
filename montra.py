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


class Montra:
    def __init__(self, url='https://bioinformatics.ua.pt/ehden'):
        self.ENDPOINT = url

    def search_questionnaire(self, questionnaire, user, password):
        auth=(user, password)
        pass

    def search_fingerprint(self, fingerprint, user, password):
        auth=(user, password)
        pass

    def get_answer(self, answer, user, password):
        auth=(user, password)
        pass

    def post_answer(self, answer, user, password):
        auth=(user, password)
        pass
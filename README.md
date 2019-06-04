# montra-client-python

Montra Webservices Wrapper for Python

## Getting Started

### Prerequisites

It must exist an instance of montra up and running. It's also necessary valid credentials to execute this client (user and password for basic authentication, or a token for token authentication).

### Initialize client
The client can be initialiazed using basic or token authentication. Bellow its listed examples for how to instanciate the client using the available authentications methods.

*Basic Authentication:
```python
montra = Montra(url="http://127.0.0.1:8000", username='username', password='password')

```

*Token Authentication:
```python
montra = Montra(url="http://127.0.0.1:8000", token='de4611bcf0c6e393404fac095dab09fad01c1554', auth_type='token' )

```
### Available Methods

1. search_datasets

*Example:
```python
list_of_datasets = montra.search_datasets(questionnaire="some questionnaire name")

```

2. get_dataset

*Example:
```python
dataset = montra.get_dataset(questionnaireSlug='someslug')

```

3. get_dataentry

*Example using 1 arg:
```python
database_entry = montra.get_dataentry(fingerprintHash='somefingerprinthash')

```

*Example using 2 args:
```python
database_entry = montra.get_dataentry(acronym="ADC", questionnaireSlug="adcohort")

```

4. list_answer

*Example:
```python
answers = montra.list_answer(fingerprintHash='somefingerprinthash')

```


5. get_answer

*Example:
```python
answer = montra.get_answer(fingerprintHash='somefingerprinthash', question='somequestion')

```

6. post_answer

*Example:
```python
newAnswer = montra.post_answer(fingerprintHash='somefingerprinthash', question='somequestion', newAnswer="newAnswer")

```

## Running the tests

In order to run tests, the following command should be run on the root folder of the project:

```
python test.py
```


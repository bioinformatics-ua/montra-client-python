# montra-client-python

Montra Webservices Wrapper for Python

## Getting Started

### Prerequisites

It must exist an instance of montra up and running. It's also necessary valid credentials to execute this client (user and password for basic authentication, or an API token for token authentication).

### Client initialization
The client can be initialiazed using basic or token authentication. Bellow its listed all the available arguments and also examples for how to instanciate the client using the available authentications methods.

#### Available parameters:
* **username** - Montra username
* **password** - Montra password
* **token** - An API token that can be obtained through 'API information' of montra. When using token authentication the auth_type must be set to 'token'.
* **auth_type** - Can be 'basic' or 'token'. The default value is 'basic' 

#### Examples
Basic Authentication:
```python
montra = Montra(url="http://127.0.0.1:8000", username='username', password='password')

```

Token Authentication:
```python
montra = Montra(url="http://127.0.0.1:8000", token='de4611bcf0c6e393404fac095dab09fad01c1554', auth_type='token' )

```
### Available Methods

* **Search Datasets**

    Parameters:
    * **questionnaire** - Search string with the  questionnaire slug or name
    
    Example:
    ```python
    list_of_datasets = montra.search_datasets(questionnaire="some questionnaire name")

    ```

* **Get Dataset**

    Parameters:
    * **questionnaireSlug** - Questionnaire slug

    Example:
    ```python
    dataset = montra.get_dataset(questionnaireSlug='someslug')

    ```

* **Get Dataentry**

    Parameters:
    * **questionnaireSlug** - Questionnaire slug
    * **acronym** - Fingerprint (database entry) acronym
    * **fingerprintHash** - Fingerprint (database entry) hash

    Example using 1 arg:
    ```python
    database_entry = montra.get_dataentry(fingerprintHash='somefingerprinthash')

    ```
    Example using 2 args:
    ```python
    database_entry = montra.get_dataentry(acronym="ADC", questionnaireSlug="adcohort")

    ```

* **List Answers**

    Parameters:
    * **fingerprintHash** - Fingerprint (database entry) hash


    Example:
    ```python
    answers = montra.list_answer(fingerprintHash='somefingerprinthash')

    ```
    
    **Note:**
    Only answers of the following types are available: 'open', 'open-textfield', 'comment', 'numeric', 'email' and 'url'


* **Get an Answer**

    Parameters:
    * **fingerprintHash** - Fingerprint (database entry) hash
    * **question** - Question slug

    Example:
    ```python
    answer = montra.get_answer(fingerprintHash='somefingerprinthash', question='somequestion')

    ```

* **Create an Answer**

    Parameters:
    * **fingerprintHash** - Fingerprint (database entry) hash
    * **question** - Question slug
    * **newAnswer** - String with the new answer

    Example:
    ```python
    newAnswer = montra.post_answer(fingerprintHash='somefingerprinthash', question='somequestion', newAnswer="newAnswer")

    ```

## Running the tests

In order to run tests, the following command should be run on the root folder of the project:

```
python test.py
```


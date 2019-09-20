# montra-client-python

Montra Webservices Wrapper for Python

## Getting Started

### Prerequisites

This wrapper can be used with any instance of up-to-date MONTRA up and running (e.g. localhost, EHDEN portal, etc). Its usage requires valid credentials to execute it (user and password for basic authentication, or an API token for token authentication).

### Installation

Install using pip:

```
pip install -e git://github.com/bioinformatics-ua/montra-client-python.git#egg=montra-client

```

### Usage

Import Montra either into your Python script or into shell if you make the API calls in command line:

```
from montra import Montra

```

### Client initialization
The client can be initialiazed using basic or token authentication. Bellow we list all the available arguments and some examples on how to instantiate the client using the available authentications methods. These examples assume there is a MONTRA installation running on localhost, port 8000.

#### Available parameters:
* **username** - Montra username
* **password** - Montra password
* **token** - An API token that can be obtained through 'API information' of montra

#### Examples
Basic Authentication:
```python
montra = Montra(url="http://127.0.0.1:8000", username='username', password='password')

```

Token Authentication:
```python
montra = Montra(url="http://127.0.0.1:8000", token='de4611bcf0c6e393404fac095dab09fad01c1554')

```
### Available Methods

* **Search Datasets**

    Parameters:
    * **questionnaire** - Search string with the questionnaire slug or name
    
    Example:
    ```python
    list_of_datasets = montra.search_datasets(questionnaire="some questionnaire name")

    ```

* **Get Dataset**

    Parameters:
    * **questionnaireSlug** - Questionnaire slug
    * **communityName** - Community name

    Example:
    ```python
    dataset = montra.get_dataset(communityName='Some community Name', questionnaireSlug='someslug')

    ```

* **Get Database**

    Parameters:
    * **questionnaireSlug** - Questionnaire slug
    * **database_name** - Fingerprint (database) name / acronym
    * **fingerprintHash** - Fingerprint (database) hash
    * **communityName** - Community name

    Example using fingerprint hash:
    ```python
    database = montra.get_database(fingerprintHash='somefingerprinthash')

    ```
    Example using database name and questionnaire slug:
    ```python
    database = montra.get_database(database_name="ABC", communityName="Some community name")

    ```

* **Create Database**

    Parameters:
    * **questionnaireSlug** - Questionnaire slug
    * **database_name** - Database name / acronym
    * **communityName** - Community name

    Example:
    ```python
    database = montra.new_database( database_name='somedbname', communityName='Some community Name', questionnaireSlug='Some questionnaire Slug')

    ```

* **Update Database**

    Parameters:
    * **draft** - Boolean
    * **fingerprintHash** - Fingerprint (database) hash

    Example:
    ```python
    database = montra.update_database(fingerprintHash='some_fingerprint_hash', draft=True)

    ```

* **List Answers**

    Parameters:
    * **fingerprintHash** - Fingerprint (database) hash


    Example:
    ```python
    answers = montra.list_answer(fingerprintHash='somefingerprinthash')

    ```
    
    **Note:**
    Only answers of the following types are supported: 'open', 'open-textfield', 'comment', 'numeric', 'email' and 'url'


* **Get Answer**

    Parameters:
    * **fingerprintHash** - Fingerprint (database) hash
    * **question** - Question slug

    Example:
    ```python
    answer = montra.get_answer(fingerprintHash='somefingerprinthash', question='somequestion')

    ```
    **Note:**
    In order to get all question slugs execute first the above method list_answer()

* **Update Answer**

    Parameters:
    * **fingerprintHash** - Fingerprint (database) hash
    * **question** - Question slug
    * **newAnswer** - String with the new answer

    Example:
    ```python
    newAnswer = montra.put_answer(fingerprintHash='somefingerprinthash', question='somequestion', newAnswer="newAnswer")

    ```
    **Note:**
    In order to get all question slugs execute first the above method list_answer()


## Running tests

In order to run tests, the following command should be run on the root folder of the project:

```
python tests.py --user <username> --password <password> --comm <community_name> --dataset_slug <questionnaire_slug> --token <token> --url <url_MONTRA_installation>
```


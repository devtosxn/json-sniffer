# JSON Sniffer
This program reads a JSON file and creates a schema based on the data types of the values in the `message` attribute if it exists. The schema includes a unique key for each attribute, the attribute's data type, and common fields like "tag", "description", and "required".

## Setup
1. Clone the repository

```
git clone https://github.com/devtosxn/json-sniffer.git
```
2. Switch into root directory

```
cd json-sniffer
```

3. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```
4. Install the requirements

```
pip3 install -r requirements.txt
```

## Running the Tests
To run the tests, navigate to the project directory and enter the command:

```
python3 -m unittest test_sniffer.py
```

## Running the Program
To run the program, navigate to the project directory and enter the command:

```
python3 main.py
```
By default, the program runs in `strict` mode which means that any data type that is not defined in the project specification will be returned as "undefined" based on the specified rules.

To run the program outside of `strict` mode, which adds additional data types to compensate for the undefined types as defined in this [screenshot](https://github.com/devtosxn/json-sniffer/blob/main/datatypes.png), enter the command:

```
python3 main.py nostrict
```


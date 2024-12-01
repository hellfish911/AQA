"""This module validates json files."""


import json
import logging


def validate_json_files(file_paths):
    """
    Validate a list of files to check if they contain valid JSON.

    Args:
        file_paths (list): List of file paths to validate.

    Logs:
        Errors for invalid JSON files to 'json__c.log'.
    """
    logging.basicConfig(
        filename='json__c.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                json.load(file)
        except json.JSONDecodeError as e:
            logging.error(f'Invalid JSON in file {file_path}: {e}')
        except FileNotFoundError as e:
            logging.error(f'File not found {file_path}: {e}')
        except Exception as e:
            logging.error(
                f'An unexpected error occurred for file {file_path}: {e}',
            )


validate_json_files([
    'localizations_en.json',
    'localizations_ru.json',
    'login.json',
    'swagger.json',
])

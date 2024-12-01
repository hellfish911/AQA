"""This module processes xml file."""


import xml.etree.ElementTree as ET
import logging


def search_and_log_xml_value(file_path):
    """
    Searches an XML file for 'group/number' and retrieves the value of
    'timingExbytes/incoming'. Logs the result at INFO level.

    Args:
        file_path (str): Path to the XML file.

    Logs:
        The retrieved value or an error message if not found.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        group_number = root.find(".//group/number")
        timing_incoming = root.find(".//timingExbytes/incoming")

        if group_number is not None and timing_incoming is not None:
            group_number_value = group_number.text
            timing_incoming_value = timing_incoming.text
            logging.info(f'Group/Number: {group_number_value}, TimingExbytes/Incoming: {timing_incoming_value}')
        else:
            missing_elements = []
            if group_number is None:
                missing_elements.append('group/number')
            if timing_incoming is None:
                missing_elements.append('timingExbytes/incoming')
            logging.error(f"Missing elements in XML: {', '.join(missing_elements)}")
    except ET.ParseError as e:
        logging.error(f'Failed to parse XML file {file_path}: {e}')
    except FileNotFoundError as e:
        logging.error(f'File not found {file_path}: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')


search_and_log_xml_value('groups.xml')

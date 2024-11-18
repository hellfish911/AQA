"""This module intended to test logger from the homework_10 module."""

import pytest
from unittest.mock import patch
import logging
from homework_10 import log_event


# Test for successful login
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_log_success(mock_basic_config, mock_get_logger):
    """Test for successful login."""
    mock_logger = mock_get_logger.return_value

    log_event('user1', 'success')

    mock_logger.info.assert_called_once_with(
        'Login event - Username: user1, Status: success',
    )


# Test for an outdated password
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_log_expired(mock_basic_config, mock_get_logger):
    """Test for an outdated password."""
    mock_logger = mock_get_logger.return_value

    log_event('user2', 'expired')

    mock_logger.warning.assert_called_once_with(
        'Login event - Username: user2, Status: expired',
    )


# Test for an incorrect password
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_log_failed(mock_basic_config, mock_get_logger):
    """Test for an incorrect password."""
    mock_logger = mock_get_logger.return_value

    log_event('user3', 'failed')

    mock_logger.error.assert_called_once_with(
        'Login event - Username: user3, Status: failed',
    )


# Test for unknown status
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_log_event_invalid_status(mock_basic_config, mock_get_logger):
    """Test for unknown status."""
    mock_logger = mock_get_logger.return_value

    log_event('user4', 'unknown')

    mock_logger.error.assert_called_once_with(
        'Login event - Username: user4, Status: unknown',
    )


# A test to check the message format
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_log_format(mock_basic_config, mock_get_logger):
    """A test to check the message format."""
    mock_logger = mock_get_logger.return_value

    log_event('user5', 'success')

    expected_message = 'Login event - Username: user5, Status: success'
    mock_logger.info.assert_called_once_with(expected_message)


# A test to check the level of logging for success
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_logging_level_for_success(mock_basic_config, mock_get_logger):
    """A test to check the level of logging for success."""
    mock_logger = mock_get_logger.return_value

    log_event('user6', 'success')

    mock_logger.info.assert_called_once()


# Test to check the logging level for expired
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_logging_level_for_expired(mock_basic_config, mock_get_logger):
    """Test to check the logging level for expired."""
    mock_logger = mock_get_logger.return_value

    log_event('user7', 'expired')

    mock_logger.warning.assert_called_once()


# Test to check the logging level for failed
@patch('logging.getLogger')
@patch('logging.basicConfig')
def test_logging_level_for_failed(mock_basic_config, mock_get_logger):
    """A test to check the logging level for failed."""
    mock_logger = mock_get_logger.return_value

    log_event('user8', 'failed')

    mock_logger.error.assert_called_once()

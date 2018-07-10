# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

import logging
import logging.handlers

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


def _create_logger():
    """ Setup logging configuration """

    # Console formatter, mention name
    cfmt = logging.Formatter(('%(name)s - %(levelname)s - %(message)s'))

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(cfmt)

    # Create the logger, adding the console handler
    log = logging.getLogger(__name__)
    log.addHandler(ch)


_create_logger()

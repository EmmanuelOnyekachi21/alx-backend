#!/usr/bin/env python3
"""Contains a function that returns the start and end number of a given page"""


def index_range(page, page_size):
    """Returns the start and end name number of a given page."""
    start_num = 0
    end_num = 0
    for pg in range(page):
        start_num = end_num
        end_num = start_num + page_size
    return (start_num, end_num)

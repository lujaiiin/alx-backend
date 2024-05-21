#!/usr/bin/env python3
"""modules"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range fun """

    beg: int = (page - 1) * page_size
    return (beg, beg + page_size)

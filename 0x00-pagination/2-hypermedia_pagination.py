#!/usr/bin/env python3
"""modules"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range fun"""

    beg: int = (page - 1) * page_size
    return (beg, beg + page_size)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page"""

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        book: List[List] = self.dataset()
        if start_index >= len(book):
            return []
        return book[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """get hyber"""

        data: List[List] = self.dataset()
        pages: int = math.ceil(len(data) / page_size)
        dic: Dict = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < pages else None,
            'prev_page': None if page == 1 else page - 1,
            'total_pages': pages
        }
        return dic

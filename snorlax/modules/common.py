from typing import List


def generate(response, selector: str):
    return [item.strip() for item in response.xpath(selector).extract()]


def is_numeric(items: List[str]):
    for i, item in enumerate(items):
        if item.isnumeric() is False:
            return False
    return True


def is_empty(items: List[str]):
    for i, item in enumerate(items):
        if not item:
            return False
        return True


def timestamp(date, hour, minute):
    return f'{date} {hour}:{minute}:00+01:00'

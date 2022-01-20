def generate_items(response, selector: str):
    return [item.strip() for item in response.xpath(selector).extract()]
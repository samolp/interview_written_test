import re


def credit_cared_validation(card_no):
    if (
            # Start with 4, 5, 6
            re.search('^[4-6]', card_no) and
            # 16 digits with optional -
            re.search(r'[\d]{16}|(\d{4}-){3}\d{4}', card_no) and
            # Find 4 or more consecutive digits
            not (re.search(r'(\d)\1{3,}', card_no))
    ):
        return True
    else:
        return False


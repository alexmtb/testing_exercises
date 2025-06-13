import datetime
import decimal
from functions.level_1.four_bank_parser import (
    BankCard, SmsMessage, Expense, parse_ineco_expense)


def test_parse_ineco_expense():
    """Test parsing a bank expense SMS."""
    sms = SmsMessage(
        '1357.00 RUB, 2891 01.06.25 13:57 AZS-57 authcode 59013',
        author='Ineco Bank',
        sent_at=datetime.datetime(2025, 6, 1, 13, 57)
    )
    cards = [
        BankCard(last_digits='2891', owner='Ineco Bank'),
        BankCard(last_digits='1753', owner='Ozon Bank')
    ]
    parsed_expence = Expense(
        amount=decimal.Decimal('1357.00'),
        card=BankCard(last_digits='2891', owner='Ineco Bank'),
        spent_in='AZS-57',
        spent_at=datetime.datetime(2025, 6, 1, 13, 57)
    )
    assert parse_ineco_expense(sms=sms, cards=cards) == parsed_expence
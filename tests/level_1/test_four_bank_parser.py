import datetime
import decimal
import pytest
from functions.level_1.four_bank_parser import (
    BankCard, SmsMessage, Expense, parse_ineco_expense)


@pytest.mark.parametrize(
    "sms,cards,expected_expense",
    [
        (
            SmsMessage(
                '1357.00 RUB, 2891 01.06.25 13:57 AZS-57 authcode 59013',
                author='Ineco Bank',
                sent_at=datetime.datetime(2025, 6, 1, 13, 57)
            ),
            [
                BankCard(last_digits='2891', owner='Ineco Bank'),
                BankCard(last_digits='1753', owner='Ozon Bank')
            ],
            Expense(
                amount=decimal.Decimal('1357.00'),
                card=BankCard(last_digits='2891', owner='Ineco Bank'),
                spent_in='AZS-57',
                spent_at=datetime.datetime(2025, 6, 1, 13, 57)
            )
        )
    ]
)
def test__parse_ineco_expense__returns_splitted_bank_expense_sms_into_custom_dataclass(
    sms, cards, expected_expense
):
    assert parse_ineco_expense(sms, cards) == expected_expense
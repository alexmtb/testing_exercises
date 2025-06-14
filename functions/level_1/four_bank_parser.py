import datetime
import decimal
from typing import NamedTuple


class BankCard(NamedTuple):
    last_digits: str
    owner: str


class SmsMessage(NamedTuple):
    text: str
    author: str
    sent_at: datetime.datetime


class Expense(NamedTuple):
    amount: decimal.Decimal
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime


def parse_ineco_expense(sms: SmsMessage, cards: list[BankCard]) -> Expense:
    raw_sum, raw_details = sms.text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    raw_card, raw_date, raw_time, spend_in = raw_details.split(' ', maxsplit=3)
    return Expense(
        amount=decimal.Decimal(raw_sum.split(' ')[-2]),
        card=[c for c in cards if c.last_digits == raw_card[-4:]][0],
        spent_in=spend_in,
        spent_at=datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M'),
    )


if __name__ == '__main__':
    # Function test
    test_sms = SmsMessage(
        '1357.00 RUB, 2801 01.06.25 13:57 AZS-57 authcode 59013',
        author='Ozon Bank',
        sent_at=datetime.datetime(2025, 6, 1, 13, 57)
    )
    test_cards = [
        BankCard(last_digits='2891', owner='Ozon Bank'),
        BankCard(last_digits='1753', owner='VBRR Bank')
    ]
    print(parse_ineco_expense(sms=test_sms, cards=test_cards))
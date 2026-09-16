def split_bill(bill_amount, tip_percent, people):
    tip_amount = bill_amount * tip_percent / 100
    grand_total = bill_amount + tip_amount
    each_person_share = grand_total / people

    return round(each_person_share, 2)

print(split_bill(100, 10, 2))
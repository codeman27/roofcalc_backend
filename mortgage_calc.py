#Run this function if given down payment price
def mortgage_calc(house_price, down_payment, interest_rate, loan_type):
    months_in_year = 12
    loan = house_price - down_payment
    monthly_rate = interest_rate/months_in_year
    num_pmts = loan_type * months_in_year

    mortgage = {}
    mortgage['monthly_payment'] = round(loan*(monthly_rate*(1 + monthly_rate)**num_pmts)/((1 + monthly_rate)**num_pmts - 1))
    mortgage['down_payment'] = down_payment
    mortgage['loan_amount'] = house_price - down_payment

    print(monthly_rate)
    print(((1 + monthly_rate)**num_pmts - 1))

    return mortgage

#Run this function if given down payment percent
def mortgage_calc_perc(house_price, down_payment_perc, interest_rate, loan_type):
    months_in_year = 12
    loan = house_price - (down_payment_perc * house_price)
    monthly_rate = interest_rate/months_in_year
    num_pmts = loan_type * months_in_year

    mortgage = {}
    mortgage['monthly_payment'] = round(loan*(monthly_rate*(1 + monthly_rate)**num_pmts)/((1 + monthly_rate)**num_pmts - 1))
    mortgage['down_payment'] = round(down_payment_perc * house_price)
    mortgage['loan_amount'] = house_price - (down_payment_perc * house_price)
    mortgage['down_payment_perc'] = down_payment_perc

    return mortgage


# print(mortgage_calc(273518, 54704, 0.03201, 30))
#print(mortgage_calc_perc(150000, 0.2, 0.045, 30))

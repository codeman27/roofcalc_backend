# 0.007365 of purchase price works from experience
# Percent lessens the more the house increases in price

def property_insurance(house_price):
    if house_price < 200000:
        insurance_rate = 0.007365
    else:
        insurance_rate = 0.004736

    insurance = {'type':'property'}
    insurance['yearly'] = round(house_price * insurance_rate)
    insurance['monthly'] = round(insurance['yearly'] / 12)

    return insurance

# Assume 1% of of the entire loan amount
def mortgage_insurance(loan, down_payment):
    pmi_rate = 0.01

    insurance = {'type':'mortgage'}
    insurance['yearly'] = round(loan * pmi_rate)
    insurance['monthly'] = round(insurance['yearly'] / 12)

    return insurance

#https://www.valuepenguin.com/flood-insurance/flood-zones-affect-insurance-premiums
def flood_insurance(house_price):
    insurance = {'type': 'flood'}
    insurance['yearly'] = round(house_price/100 * 0.29)
    insurance['monthly'] = round(insurance['yearly'] / 12)

    return insurance

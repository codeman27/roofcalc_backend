def property_management_perc(rent_estimate, perc = 0.1):
    property_management = {}

    property_management['type'] = 'property_management_perc'
    property_management['perc'] = perc
    property_management['amount'] = round(perc * rent_estimate)

    return property_management

def property_management_amt(amt, rent_estimate):
    property_management = {}

    property_management['type'] = 'property_management_amt'
    property_management['amount'] = amt
    property_management['perc'] = round(amt / rent_estimate, 4)

    return property_management

def vacancy(rent_estimate, perc = 0.1):
    vacancy = {}

    vacancy['type'] = 'vacancy'
    vacancy['perc'] = perc
    vacancy['amount'] = round(perc * rent_estimate)

    return vacancy

def repairs(rent_estimate, perc = 0.1):
    repairs = {}

    repairs['type'] = 'repairs'
    repairs['perc'] = perc
    repairs['amount'] = round(perc * rent_estimate)

    return repairs

def closing_costs_perc(mortgage, perc = 0.035):
    #Typically, home buyers will pay between about 2 to 5 percent of the purchase price of their home in closing fees.
    closing_costs = {}

    closing_costs['rate'] = perc
    closing_costs['closing_costs'] = round(closing_costs['rate'] * mortgage)

    return closing_costs

def closing_costs_amt(mortgage, closing_cost):
    closing_costs = {}

    closing_costs['rate'] = round(closing_cost / mortgage,4)
    closing_costs['closing_costs'] = closing_cost

    return closing_costs

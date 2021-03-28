from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from location import location
from search_results import search_results
from mortgage_rates import mortgage_rates
from mortgage_calc import mortgage_calc, mortgage_calc_perc
from property_taxes import property_taxes
from insurance import *
from expenses import *
from data_usa import data_usa

application = Flask(__name__)
CORS(application)

@application.route('/analysis', methods=['GET'])
def get_data():
    user_input = {
        'address': '445-San-Juan-St-Grand-Junction-CO-81504-USA'
    }
    user_input['address'] = request.args.get('address', default='')
    user_input['address'] = user_input['address'].replace(',', '').replace(' ', '-')

    loc = location(user_input['address'])
    address = loc['address'].replace(' ', '-')
    citystate = loc['city'] + '-' + loc['state']
    citystatezip = citystate +  '-'+ loc['zip']
    #
    data = {}
    data['zestimates'] = search_results(address, citystatezip)
    data['mortgage_rate'] = mortgage_rates('30-year fixed rate')
    data['monthly_mortgage'] = mortgage_calc_perc(data['zestimates']['zestimate'], 0.2, data['mortgage_rate']['rate'], data['mortgage_rate']['years'])
    data['taxes'] = property_taxes(loc['state'], loc['county'], data['zestimates']['zestimate'])
    data['pi'] = property_insurance(data['zestimates']['zestimate'])
    data['pmi'] = mortgage_insurance(data['zestimates']['zestimate'] - data['monthly_mortgage']['down_payment'], 0.2)
    data['fi'] = flood_insurance(data['zestimates']['zestimate'])
    data['pm'] = property_management_perc(0.1, data['zestimates']['rent_zestimate'])
    data['vacancy'] = vacancy(0.1, data['zestimates']['rent_zestimate'])
    data['repairs'] = repairs(0.1, data['zestimates']['rent_zestimate'])
    data['closing_costs'] = closing_costs_perc(data['monthly_mortgage']['loan_amount'])
    data['input_address'] = user_input['address']
    data['data_usa'] = data_usa(citystate.replace('-' , ', '))

    return jsonify(data)

@application.errorhandler(Exception)
def exception_handler(error):
    return '500'

if __name__ == '__main__':
    application.run(debug=False)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    wf = 0
    per_wash = 0
    result = None

    if request.method == "POST":
        wf = 0
        people = int(request.form['people'])
        average_shower = int(request.form['average_shower']) 

        if average_shower < 5:
            wf += 20
        elif average_shower >= 5 and average_shower <= 10:
            wf += 40
        elif average_shower >= 11 and average_shower <= 15:
            wf += 65
        else:
            wf += 75
        
        low_flow_shower = request.form['low_flow_shower']

        if low_flow_shower == 'Yes':
            wf -= (wf / 2)
        elif low_flow_shower == 'Some':
            wf -= (wf / 4)

        bath_frequency = int(request.form['bath_frequency']) 
        wf += bath_frequency * 35

        faucet_open = int(request.form['faucet_open']) 

        if faucet_open < 5:
            wf += 20
        elif faucet_open >= 5 and faucet_open <= 10:
            wf += 40
        elif faucet_open >= 11 and faucet_open <= 30:
            wf += 100
        else:
            wf += 150

        low_flow_bathroom_faucet = request.form['low_flow_bathroom_faucet']

        if low_flow_bathroom_faucet == 'Yes':
            wf -= wf * (19/100)
        elif low_flow_bathroom_faucet == 'Some':
            wf -= wf * (15/100)
    
        mellow = request.form['mellow']

        if mellow == 'Yes':
            wf += 9
        elif mellow == 'Sometimes':
            wf += 18
        else:
            wf += 25

        low_flow_toilets = request.form['low_flow_toilets']

        if low_flow_toilets == 'Yes':
            wf -= wf * (17/100)
        elif low_flow_toilets == 'Sometimes':
            wf -= wf * (8/100)
    
        kitchen_faucet_running = int(request.form['kitchen_faucet_running'])

        if kitchen_faucet_running < 5:
            wf += 20
        elif kitchen_faucet_running >= 5 and kitchen_faucet_running <= 20:
            wf += 65
        elif kitchen_faucet_running >= 21 and kitchen_faucet_running <= 45:
            wf += 165
        else:
            wf += 225

        low_flow_kitchen_faucet = request.form['low_flow_kitchen_faucet']

        if low_flow_kitchen_faucet == 'Yes':
            wf -= wf * (12/100)
    
        dish_wash_technique = request.form['dish_wash_technique']

        if dish_wash_technique == 'Old School Dishwasher':
            per_wash = 15
        elif dish_wash_technique == 'Water/Energy Efficient Dishwasher':
            per_wash = 4
        elif dish_wash_technique == 'With my own two hands':
            per_wash = 27
        elif dish_wash_technique == 'Trash them or eat out':
            per_wash = 5
    
        dish_wash_load = int(request.form['dish_wash_load'])

        wf += dish_wash_load * per_wash

        laundry_technique = request.form['laundry_technique']

        if laundry_technique == 'Old School Washing Machine':
            per_wash = 41
        elif laundry_technique == 'Water/Energy Efficient Washing Machine':
            per_wash = 20
        elif laundry_technique == 'Elbow Grease':
            per_wash = 25
        elif laundry_technique == 'Laundromat or pay someone else':
            per_wash = 38
    
        laundry_load = int(request.form['laundry_load'])

        wf += laundry_load * per_wash

        greywater_system = request.form['greywater_system']

        if greywater_system == 'Yes':
            wf -= 63

        wf *= people

        result = f"Your water footprint is: {wf} gallons"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
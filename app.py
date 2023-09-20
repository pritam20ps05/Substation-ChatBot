from os import environ
from bot import GPTapi
from time import sleep
from flask import Flask, render_template, request

app = Flask(__name__)
gptapi = GPTapi(api_key=environ['OPENAI_API_KEY'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/api/chatbot', methods=['POST'])
def chatbotapi():
    messages_context = request.get_json()
    # sleep(5);
    # resp = {'content': 'Maintenance in substations is crucial to ensure the reliable operation of electrical power systems. Here are some key points about maintenance in substations:\n\n1. Routine inspections: Regular inspections are conducted to identify any signs of wear and tear, loose connections, or damaged equipment. This helps in detecting potential issues before they lead to failures or accidents.\n\n2. Cleaning and lubrication: Substation equipment, such as breakers, switches, and contacts, require periodic cleaning and lubrication to remove dust, dirt, and moisture. This enhances the performance and reduces the risk of malfunctions.\n\n3. Testing and calibration: Various electrical tests are performed on substation equipment, including insulation resistance, power factor, and relay coordination tests. These tests ensure that the equipment is operating within specified parameters and provide data for maintenance decisions.\n\n4. Oil analysis: Transformers and circuit breakers often use oil for insulation and cooling. Regular oil analysis is performed to detect any contaminants, moisture, or degradation, which can indicate potential problems and the need for maintenance or replacement.\n\n5. Protective device maintenance: Relays, fuses, and other protective devices are inspected and tested to ensure proper operation. These devices play a crucial role in protecting the substation and the connected power system from faults and overloads.\n\n6. Grounding system maintenance: The grounding system in a substation needs to be regularly inspected and tested to maintain its integrity. Grounding faults can lead to safety hazards and damage to equipment.\n\n7. Record keeping: Comprehensive records of maintenance activities, testing results, and equipment history are maintained. These records help in tracking the maintenance history, identifying trends, and planning future maintenance activities.\n\n8. Training and safety: Maintenance personnel receive adequate training to ensure their safety and to perform maintenance tasks effectively. Safety protocols and procedures are strictly followed to minimize the risk of accidents during maintenance activities.\n\nIn summary, maintenance in substations involves routine inspections, cleaning, testing, and calibration of equipment, oil analysis, maintenance of protective devices and grounding systems, record keeping, and ensuring personnel safety through training and adherence to safety protocols.'}
    resp = gptapi.chatapi(messages_context)
    return resp

if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
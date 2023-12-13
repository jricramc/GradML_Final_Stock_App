from flask import Flask, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import stock_analysis
import vlc
import time

# Create a MediaPlayer with the MP4 file

app = Flask(__name__)
scheduler = BackgroundScheduler()

# Define a global variable to store the alert state
alert = False  # Initialize as False

def analyze_stocks():
    global alert  # Use the global variable
    result = stock_analysis.run_stock_analysis()
    alert = any(item['alert'] for item in result)  # Update the alert state
    if alert == True:
        player = vlc.MediaPlayer('sooth.mp3')

        # Start playing the MP4 file
        player.play()

        # Wait until the player has started before exiting
        time.sleep(1)  # Wait for 1 second to allow the player to start
        while player.is_playing():
            time.sleep(1)


# Schedule the `analyze_stocks` function to run every 10 seconds
scheduler.add_job(analyze_stocks, 'interval', seconds=15)
scheduler.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify({'alert': alert})  # Return alert state as JSON

@app.route('/run-algorithm', methods=['GET'])
def run_algorithm():
    global alert  # Make sure to use the global variable
    result = stock_analysis.run_stock_analysis()
    alert = any(item['alert'] for item in result)  # Update the alert state
    return jsonify({'result': result, 'alert': alert})

# Shut down the scheduler when exiting the app
@app.route('/shutdown', methods=['POST'])
def shutdown():
    scheduler.shutdown()
    return 'Scheduler shut down'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # Set use_reloader to False to avoid duplicate jobs

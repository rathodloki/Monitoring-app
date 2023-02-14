from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')
def get_system_resources():
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    ram_percent = virtual_memory.percent
    return f'CPU usage: {cpu_percent}%\nRAM usage: {ram_percent}%'

if __name__ == '__main__':
    app.run(debug=True)

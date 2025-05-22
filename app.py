from flask import Flask, render_template, request
import subprocess #run system commands like python


app = Flask(__name__)

def run_nmap_scan(target_ip):
    command = [r"C:\Program Files (x86)\Nmap\nmap.exe", "-Pn", "-sV", "-T4", "-F", target_ip]

    #command = ['nmap', target_ip]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Scan failed: {e}"
    


@app.route('/', methods=['GET', 'POST'])
def index():
    scan_output = ""
    if request.method == 'POST':
        target = request.form.get('target')
        if target:
            scan_output = run_nmap_scan(target)
    return render_template('index.html', scan_output=scan_output)

if __name__ == '__main__':
    app.run(debug=True)


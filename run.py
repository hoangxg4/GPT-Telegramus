import subprocess

# Chạy lệnh "flask run -h 0.0.0.0 -p 10000" bằng subprocess
flask_process = subprocess.Popen(["flask", "run", "-h", "0.0.0.0", "-p", "10000"])

# Chạy tập tin Python main.py bằng subprocess
main_process = subprocess.Popen(["python", "main.py"])

# Đợi cho cả hai tiến trình hoàn thành
flask_process.wait()
main_process.wait()

# Sử dụng image cơ sở Python 3.11
FROM python:3.11

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép các tệp cần thiết vào thư mục làm việc
COPY . .

# Cài đặt Flask
RUN pip install requirements.txt

# Chạy Flask app và main.py
CMD flask run -h 0.0.0.0 -p 10000 & python main.py

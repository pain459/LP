FROM ubuntu:22.04

RUN apt update && apt install -y \
    git build-essential cmake python3 python3-pip sqlite3 curl libcurl4-openssl-dev

RUN pip3 install fastapi uvicorn sqlite-utils pdfplumber

WORKDIR /app
RUN git clone https://github.com/ggerganov/llama.cpp.git
WORKDIR /app/llama.cpp
RUN mkdir build && cd build && cmake .. && cmake --build . --config Release

WORKDIR /app
COPY . .

EXPOSE 8000
CMD ["bash"]

FROM --platform=amd64 selenium/standalone-chrome:113.0

RUN sudo apt update && sudo apt install -y python3=3.8.2* \
    python3-pip=20.0.2* \
    wget=1.20.3* \ 
    zip=3.0* \ 
    && sudo rm -rf /var/lib/apt/lists/*
COPY . /root
WORKDIR /root
RUN sudo chmod 755 setup.sh && sudo ./setup.sh

RUN sudo python3 -m pip install -r requirements.txt

ENTRYPOINT [ "sudo", "python3", "lfi.py" ]
FROM --platform=amd64 selenium/standalone-chrome

RUN sudo apt update && sudo apt install -y python3 python3-pip wget zip gpg

COPY . /root
WORKDIR /root
RUN sudo chmod 755 setup.sh && sudo ./setup.sh

RUN sudo python3 -m pip install -r requirements.txt

ENTRYPOINT [ "sudo", "python3", "lfi.py" ]
# We're using Ubuntu 20.10
# Thanks to geez-Userbot
FROM vckyouuu/geezproject:buster


RUN git clone -b IndomieUserbot https://github.com/IndomieGorengSatu/IndomieUserbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/IndomieGorengSatu/indomieuserbot/indomieuserbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]

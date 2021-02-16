FROM python:3.5
COPY . /usr/src/mypython
WORKDIR /usr/src/mypython
ENTRYPOINT [ "python" ]
CMD [ "./hello.py" ]

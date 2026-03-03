FROM fedora:latest
RUN dnf install -y python3 && dnf clean all
WORKDIR /app
COPY . .
ENTRYPOINT ["python3", "main.py"]

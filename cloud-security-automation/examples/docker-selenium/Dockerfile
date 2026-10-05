FROM python:3.11-slim-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends chromium chromium-driver && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN pip install --no-cache-dir 'selenium>=4.33,<5'
COPY worker.py /app/worker.py
RUN useradd --create-home demo
USER demo
CMD ["python", "-u", "/app/worker.py"]

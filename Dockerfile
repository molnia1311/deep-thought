FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/molnia1311/deep-thought"
WORKDIR /app
RUN pip install --no-cache-dir openai
COPY app.py .
ENTRYPOINT ["python", "app.py"]

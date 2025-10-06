FROM python:3.11-slim
LABEL authors="Johannes Theissen-Lipp"

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY analysis.py .

# CMD ["python", "analysis.py"]
# Print log to file instead of console:
CMD ["bash", "-c", "python analysis.py > /app/output/analysis_log.txt 2>&1"]


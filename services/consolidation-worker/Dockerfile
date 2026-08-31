FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md /app/
COPY src /app/src
RUN pip install --no-cache-dir -e ".[api]"
ENV PYTHONPATH=/app/src
EXPOSE 8086
CMD ["uvicorn", "casops.memory.bootstrap:create_consolidation_app_from_env", "--factory", "--host", "0.0.0.0", "--port", "8086"]

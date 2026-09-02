FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md /app/
COPY src /app/src
COPY agents /app/agents
RUN pip install --no-cache-dir -e ".[api]"
ENV PYTHONPATH=/app/src
ENV CASOPS_AGENTS_ROOT=/app/agents
EXPOSE 18080
CMD ["uvicorn", "casops.api.control:create_app_from_env", "--factory", "--host", "0.0.0.0", "--port", "18080"]

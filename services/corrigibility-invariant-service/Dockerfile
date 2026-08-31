FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml README.md /app/
COPY src /app/src
RUN pip install --no-cache-dir -e ".[api]"

ENV PYTHONPATH=/app/src
ENV CASOPS_CORRIGIBILITY_DATA=/var/casops/corrigibility
ENV CASOPS_CORRIGIBILITY_KEY=/var/casops/corrigibility/keys/ed25519.pem
ENV CASOPS_ROLE=corrigibility

EXPOSE 8081
CMD ["uvicorn", "casops.corrigibility.bootstrap:create_app_from_env", "--factory", "--host", "0.0.0.0", "--port", "8081"]

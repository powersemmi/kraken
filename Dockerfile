FROM python:3.11-slim as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONBUFFERED=1 \
    PIP_NO_CACHE_DIR=OFF \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONPATH=/opt/app \
    PDM_VERSION=2.9.*

RUN pip install -U "pdm==$PDM_VERSION" "pip==23.2.1" && \
    pdm config venv.in_project false && \
    pdm config check_update false && \
    pdm config python.use_venv false

COPY pyproject.toml pdm.lock README.md /opt/app/

WORKDIR /opt/app

RUN mkdir __pypackages__ && pdm install -v --prod --no-lock --no-editable

FROM python:3.11-slim as runner

ENV PYTHONPATH=/opt/app/pkgs
COPY --from=builder /opt/app/__pypackages__/3.11/lib /opt/app/pkgs

WORKDIR /opt/app
COPY . .

CMD ["python", "-m", "kraken"]

FROM builder as tester

# Setup dev dependency
RUN pdm install --dev

CMD ["python"]
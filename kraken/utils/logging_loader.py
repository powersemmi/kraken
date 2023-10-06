import os
from pathlib import Path

import yaml


def init_logging(log_file: Path | str = "./logging.yaml") -> dict:
    """
    Функция для инициализации логирования из logging.yaml файла, лежащего в
     корне проекта.
    Логирование следует инициализировать перед запуском сервиса, в случае
     сервисов на fastapi
    следует передавать сгенерированный конфиг в unicorn
    """
    from logging import config as logging_config

    with open(os.path.normpath(log_file)) as stream:
        _config: dict = yaml.load(stream, Loader=yaml.FullLoader)

    logging_config.dictConfig(_config)
    return _config

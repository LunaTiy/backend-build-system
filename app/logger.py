import logging

import colorlog


def init_logger(
        name: str,
        handler: logging.Handler,
        log_level: int = logging.INFO
) -> logging.Logger:
    log = logging.getLogger(name)
    log.setLevel(log_level)
    formatter = colorlog.ColoredFormatter("%(asctime)s %(log_color)s[%(levelname)s] %(message)s")

    handler.setLevel(log_level)
    handler.setFormatter(formatter)

    log.addHandler(handler)
    return log


logger = init_logger("build-system", logging.StreamHandler())

import logging as log

FORMAT = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s'
DATEFMT = '%I:%M:%S %p'
LOGDEBUG = log.DEBUG

log.basicConfig(level=LOGDEBUG,
                format=FORMAT,
                datefmt=DATEFMT,
                filename='capa_datos.log',
                )

console = log.StreamHandler()
# https://docs.python.org/3/library/logging.html link documentation
formatter = log.Formatter(datefmt=DATEFMT, fmt=FORMAT)
console.setLevel(LOGDEBUG)
console.setFormatter(formatter)
log.getLogger('').addHandler(console)

if __name__ == '__main__':
    log.debug("Mesaje a nivel debug")
    log.info("Mensaje a nivel de info")
    log.warning("Mensaje a nivel de warning")
    log.error("Mensaje a nivel de error")
    log.critical("Mensaje a nivel critico")
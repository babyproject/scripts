import logging
import logging.config

#logging.config.fileConfig("logging.conf")
logging.basicConfig(filename="example.log", filemode="w", format="%(asctime)s %(levelname)s:%(message)s")

logger=logging.getLogger("kissme")
logger.setLevel(logging.DEBUG)

ins=logging.StreamHandler()
formatter=logging.Formatter("%(asctime)s #%(name)s# %(levelname)s:%(message)s")
ins.setFormatter(formatter)
logger.addHandler(ins)

logger.warning("this is the first line")
logger.error("something goes wrong")
logger.info("%s the hell you are %s", "what", "doing")

val=input("input anything: ")
if val==2:
    raise Warning("the value is invalid")
    val=input("input again: ")

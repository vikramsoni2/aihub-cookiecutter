import logging
import yaml

def getLogger(context):
    logging.basicConfig(
        level=logging.INFO, 
        format='%(levelname)s: %(asctime)s %(module)s.%(funcName)s:%(lineno)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return logging.getLogger(context)



def getConfig(config_file='../config.yaml'):
    yaml.warnings({'YAMLLoadWarning': False})
    with open(config_file, 'r') as conf_file:
        return yaml.load(conf_file)


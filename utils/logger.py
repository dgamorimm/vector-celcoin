from loguru import logger as log

def logger(level: str = 'INFO'):
    import sys
    log.remove()
    log.add(
        sys.stdout,
        level=level, 
        format="<green>{time:YYYY-MM-DD HH:mm:ss.ms Z}</green> - <cyan>{name}.{function}:L{line}</cyan> - [<level>{level}</level>] - <level>{message}</level>")
    
    return log
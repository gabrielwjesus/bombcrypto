from src.date import dateFormatted

import sys, yaml

stream = open("./config.yaml", 'r')
c = yaml.safe_load(stream)

last_log_is_progress = False

def logger(message, progress_indicator = False, color = 'default'):
    global last_log_is_progress

    formatted_datetime = dateFormatted()
    formatted_message = "[{}] => {}".format(formatted_datetime, message)

    if progress_indicator:
        if not last_log_is_progress:
            last_log_is_progress = True
            sys.stdout.write('Processing last action..')
            sys.stdout.flush()
        else:
            sys.stdout.write('.')
            sys.stdout.flush()
        return

    if last_log_is_progress:
        sys.stdout.write('\n - - - - - - \n')
        sys.stdout.flush()
        last_log_is_progress = False    

    print(formatted_message)

    if (c['save_log_to_file'] == True):
        logger_file = open("./logs/logger.log", "a", encoding='utf-8')
        logger_file.write(formatted_message + '\n')
        logger_file.close()

    return True

def loggerMapClicked():
    logger('New Map button clicked!')
    logger_file = open("./logs/new-map.log", "a", encoding='utf-8')
    logger_file.write(dateFormatted() + '\n')
    logger_file.close()

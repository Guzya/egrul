import os
import argparse
import logging
import datetime


def redecodig_file(source_file, dest_file):
    '''Перезаписываем файл'''
    buff_lines = []
    with open(source_file,'r',encoding='cp1251') as f:
        for line in f:
            if 'windows-1251' in line:
                line = line.replace('windows-1251','UTF-8')
            buff_lines.append(line)
    
    with open(dest_file,'w',encoding='utf8') as f:
        for line in buff_lines:
            f.write(line)




def main(source_dir, destination_dir):
    '''Основная функция'''

    # потом удалить
    #source_dir = '/home/guzya/python/EGRUL'
    #destination_dir = '/home/guzya/python/EGRUL/123'

    if not os.path.exists(source_dir):
        logger.error('Папки "{}" не существует.'.format(source_dir))
        logger.error('Скрипт завершает работу.')
        exit(1)
    
    if not os.path.exists(destination_dir):
        logger.info('Создаем папку "{}" .'.format(destination_dir))
        os.mkdir(destination_dir)
    

    xml_files = [file for file in os.listdir(source_dir) 
        if os.path.isfile(os.path.join(source_dir, file)) and (os.path.splitext(file)[1].upper() == '.XML') ]

    logger.info('Найдено файлов для обработки: {}'.format(len(xml_files)))

    for file in xml_files:
        logger.info('Начало обработки файла: {}'.format(file))
        redecodig_file(os.path.join(source_dir, file) ,os.path.join(destination_dir, file))
        logger.info('Окончание обработки файла: {}'.format(file))




if __name__ == "__main__":
    
    # Логер
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
	
    formatLogger = logging.Formatter('%(asctime)s: %(name)-12s: %(funcName)-17s: %(levelname)-8s: %(message)s')
    	
    filehandler = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'egrul_encoding-{}.log'.format(datetime.datetime.now().strftime("%Y.%m.%d_%H:%M"))))

    filehandler.setLevel(logging.INFO)
    filehandler.setFormatter(formatLogger)
	
    logger.addHandler(filehandler)
    
    # Парсер аргументов коммандной строки
    parser = argparse.ArgumentParser(description='Справка по аргументам!')
    parser.add_argument("--source", type=str, required=True, help="Папка с файлами для обработки")   
    parser.add_argument("--dest", type=str,required=True, help="Папка с результатами работы")
    parser.add_argument("--console", choices=["yes", "no"],
        default="no", type=str, help="Вывод лога в консоль, по умолчанию \"no\"")
    
    args = parser.parse_args()
    
    if args.console == 'yes':
        formatConsole = logging.Formatter('%(asctime)s: %(levelname)-6s: %(message)s')	
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatConsole)
        logger.addHandler(console)
    
    
    logger.info('Начало работы ------------------------------------- ')	
    startTime = datetime.datetime.now()

    main(args.source, args.dest)

    stopTime = datetime.datetime.now()    
    logger.info('Окончание работы ------------------------------------- ' )
    logger.info('Времы выполнения скрипта: ' + str(stopTime - startTime))
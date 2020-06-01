# egrul
Перекодирование XML-файлов ЕГРЮЛ из win-1251 в utf-8 со вставкой в файл encoding="UTF-8".



usage: egrul_encoding.py [-h] --source SOURCE --dest DEST [--console {yes,no}]

Справка по аргументам!

optional arguments: </br>
  -h, --help          show this help message and exit </br>
  --source SOURCE     Папка с файлами для обработки </br>
  --dest DEST         Папка с результатами работы </br>
  --console {yes,no}  Вывод лога в консоль, по умолчанию "no" </br></br>
  
  
  Пример использования скрипта:</br>
  
   python3 egrul_encoding.py --source /home/guzya/python/EGRUL --dest  /home/guzya/python/EGRUL/123 </br>
   Обработает все xml файлы из папки "/home/guzya/python/EGRUL" и положит результаты в папку "/home/guzya/python/EGRUL/123"
   </br>
   </br>
   python3 egrul_encoding.py --source /home/guzya/python/EGRUL --dest  /home/guzya/python/EGRUL/123 --console yes
   Дополнительно будет выводить лог в консоль.

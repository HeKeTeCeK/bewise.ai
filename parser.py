import csv
  
with open("test_data_copy.csv", encoding='utf-8') as r_file:
    
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    text    = []
    count   = 0
    count_m = 0
    dlg_id  = 0
    line_n  = 0
    
    # списки эталонных реплик менеджера
    greetings = ("Здравствуйте", "Добрый День")
    names     = ("Ангелина", "максим", "Анастасия")
    companies = ("Диджитал Бизнес", "КитоБизнес")
    goodbuys  = ("Всего Хорошего", "До Свидания", "Хорошего Вечера")
    
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print('ФайЛ СодержиТ СледующиЕ СтолБцЫ:')
            print(f'    {", ".join(row)}.')
            print()
            print('ФайЛ СодержиТ СледующиЕ РепликИ:')    
            
        #присваивание значения каждого столбца переменной с приведением к типу
        dlg_id = int(row["dlg_id"])
        line_n = int(row["line_n"])
        role   = str(row["role"])
        text.append(row["text"])
        
        # вывод необходимых реплик менеджера
        if role == "manager":
            #подсчёт и сбор всех реплик менеджеров
            count_m += 1
        count += 1
        
    # Вывод всех информационных строк
    print(f'    {text}.')
    print()
    print(f'ВсегО в ФайлЕ {count + 1} СтрокА, {dlg_id + 1} ДиалогоВ, ', end='')
    print(f'{count_m + 1} РепликИ МенеджерА.')

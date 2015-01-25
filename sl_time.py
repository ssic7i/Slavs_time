# coding: utf-8
__author__ = 'Serhii Sheiko sergy@sheyko.pp.ua'
# http://energodar.net/vedy/kalendar.html
# http://midgard-svaor.com/mernye-velichiny-nashix-predkov/
hours_ru = [(u'', u''),  # for start from 1-st hour
            (u'Паобедъ', u'начало нового дня'),
            (u'Вечиръ', u'появление звёздной росы на Небесах'),
            (u'Ничь', u'нечётное время 3-х Лун'),
            (u'Полничь', u'полный путь Лун'),
            (u'Заутра', u'звёздное утешение росы'),
            (u'Заура', u'звёздное сияние, заря'),
            (u'Заурнице', u'окончание звёздного сияния'),
            (u'Настя', u'утренняя роса'),
            (u'Сваор', u'восход Солнца'),
            (u'Утрось', u'успокоение росы'),
            (u'Поутрось', u'путь собирания успокоенной росы'),
            (u'Обестина', u'обедня, совместное собрание'),
            (u'Обед', u'трапеза'),
            (u'Подани', u'отдых после трапезы'),
            (u'Утдайни', u'время окончания деяний'),
            (u'Поудани', u'завершённый день')]

import datetime


def cur_conv_time(timezone):
    delta_time = datetime.timedelta(hours=timezone)
    cur_utc_time = datetime.datetime.utcnow() + delta_time
    cur_hour = int(cur_utc_time.hour)
    cur_minutes = int(cur_utc_time.minute)
    cur_sec = int(cur_utc_time.second)
    if cur_hour > 18:
        cur_hour = cur_hour - 18
    else:
        cur_hour =  cur_hour + 6
    #print(cur_hour)
    #print(cur_minutes)
    #print(cur_sec)
    c_secs = cur_hour * 60 * 60 + cur_minutes * 60 + cur_sec
    all_dol = c_secs * 34.56
    #print('Dolej: ' + str(all_dol))
    cov_hour = all_dol // (1296 * 144)
    #print('Hours:' + str(cov_hour))
    ost_chastey = all_dol % (1296 * 144)
    chastey = ost_chastey // 1296
    #print('Chastey:' + str(chastey))
    doley = ost_chastey % 1296
    #print('Doley:' + str(doley))
    return cov_hour, chastey, doley

#print(cur_conv_time(2))
#hour, doley, chastey = cur_conv_time(2)
#name, description = hours_ru[int(hour)]
#print(name)
#print(description)


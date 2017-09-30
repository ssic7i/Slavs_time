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

months_ru = [   u'',
                u'Рамахатъ',
                u'Айлетъ',
                u'Бейлетъ',
                u'Гейлетъ',
                u'Дайлетъ',
                u'Элетъ',
                u'Вэйлетъ',
                u'Хейлетъ',
                u'Тайлетъ'
            ]

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


def eval_day(timezone):
    __simple_year__ = 365
    __st_year__ = 369
    __one_round_years__ = __simple_year__ * 15 + __st_year__
    __one_round_life__ = __one_round_years__ * 9
    __one_svarogs_day__ = __one_round_life__ * 180

    # Days in Svarogs day before 23.09.2012
    # 23.09.2012 starts 3 of 4 parts of Svarogs day
    day_before_base = __one_svarogs_day__ / 2

    base_date = datetime.datetime(2012,9,23,18,0,0)
    corr_timezone = datetime.timedelta(hours=timezone)
    cur_date = datetime.datetime.utcnow()+corr_timezone
    days_between_dates = int((cur_date-base_date).days)

    if (days_between_dates + day_before_base) // __one_svarogs_day__ > 0:
        count_svarogs_days = (days_between_dates + day_before_base) // __one_svarogs_day__
        days_between_dates = __one_svarogs_day__ * count_svarogs_days - days_between_dates - day_before_base
        svarogs_days = count_svarogs_days
    else:
        svarogs_days = 0

    svarogs_days = svarogs_days + 1

    if days_between_dates // __one_round_life__ > 0:
        round_lifes = days_between_dates // __one_round_life__
        days_between_dates = days_between_dates % __one_round_life__
    else:
        round_lifes = 0

    round_lifes  = round_lifes + 1

    if days_between_dates // __one_round_years__ > 0:
        round_years = days_between_dates // __one_round_years__
        days_between_dates = days_between_dates % __one_round_years__
    else:
        round_years = 0

    round_years = round_years + 1

    if days_between_dates // (__simple_year__ * 15) > 0:
        # big year(16-th)
        days_between_dates = days_between_dates - (__simple_year__ * 15)
        year = 16
        month = days_between_dates // 41 + 1
        day = days_between_dates % 41
        return svarogs_days, round_lifes, round_years, year, month, day
    else:
        # simple year
        year = days_between_dates // __simple_year__
        corr_year = year + 1
        days_in_cur_year = (days_between_dates - (year * __simple_year__)) + 1
        days_in_cur_year = days_in_cur_year + 1 # because days_in_cur_year might be 0
        if days_in_cur_year > __simple_year__:
            corr_year += 1
            days_in_cur_year = days_in_cur_year - __simple_year__

        if days_in_cur_year in range(1, 41+1): # [1..41] 41
            month = 1
            date = days_in_cur_year
        elif days_in_cur_year in range(41+1, 41+1+40): # [42..81] 40
            month = 2
            date = days_in_cur_year - 41
        elif days_in_cur_year in range(41+1+40, 41+1+40+41): # [82..122] 41
            month = 3
            date = days_in_cur_year - 41 - 40
        elif days_in_cur_year in range(41+1+40+41, 41+1+40+41+40): # [123..162] 40
            month = 4
            date = days_in_cur_year - 41 - 40 - 41
        elif days_in_cur_year in range(41+1+40+41+40, 41+1+40+41+40+41): # [163..203] 41
            month = 5
            date = days_in_cur_year - 41 - 40 - 41 - 40
        elif days_in_cur_year in range(41+1+40+41+40+41, 41+1+40+41+40+41+40): # [204..243] 40
            month = 6
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41
        elif days_in_cur_year in range(41+1+40+41+40+41+40, 41+1+40+41+40+41+40+41): # [244..284] 41
            month = 7
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41 - 40
        elif days_in_cur_year in range(41+1+40+41+40+41+40+41, 41+1+40+41+40+41+40+41+40): # [285..324] 40
            month = 8
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41 - 40 - 41
        else: # range(41+1+40+41+40+41+40+41+40, 41+1+40+41+40+41+40+41+40+41) [325..365] 41
            month = 9
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41 - 40 - 41 - 40

        day = date
        return svarogs_days, round_lifes, round_years, corr_year, month, day

def cur_day(timezone):
    svarog_days, round_lifes, round_years, year, month, day = eval_day(timezone)
    year_in_round_life = (round_lifes-1) * (round_years-1) + year
    year_in_round_years = year
    month = month
    day = day
    return year_in_round_life, year_in_round_years, month, day

def year_cpsc(timezone):
    svarog_days, round_lifes, round_years, year, month, day = eval_day(timezone)
    return year + 7520


#print(cur_conv_time(2))
#hour, doley, chastey = cur_conv_time(2)
#name, description = hours_ru[int(hour)]
#print(name)
#print(description)

#print(cur_day(2))

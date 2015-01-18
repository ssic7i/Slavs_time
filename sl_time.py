__author__ = 'Serhii Sheiko sergy@sheyko.pp.ua'
# http://energodar.net/vedy/kalendar.html
# http://midgard-svaor.com/mernye-velichiny-nashix-predkov/


import datetime


def cur_conv_time(timezone):
    delta_time = datetime.timedelta(hours=timezone)
    cur_utc_time = datetime.datetime.utcnow() + delta_time
    cur_hour = int(cur_utc_time.hour)
    cur_minutes = int(cur_utc_time.minute)
    cur_sec = int(cur_utc_time.second)
    if cur_hour > 17:
        cur_hour = cur_hour - 18
    else:
        cur_hour =  cur_hour + 6
    #print(cur_hour)
    #print(cur_minutes)
    #print(cur_sec)
    c_secs = cur_hour * 60 * 60 + cur_minutes * 60 + cur_sec
    all_dol = c_secs * 34.5
    #print('Dolej: ' + str(all_dol))
    cov_hour = all_dol // 186624
    #print('Hours:' + str(cov_hour))
    ost_chastey = all_dol % 186624
    chastey = ost_chastey // 1296
    #print('Chastey:' + str(chastey))
    doley = ost_chastey % 1296
    #print('Doley:' + str(doley))
    return cov_hour, chastey, doley

cur_conv_time(2)

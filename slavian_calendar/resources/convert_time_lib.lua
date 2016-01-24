--
-- Created by IntelliJ IDEA.
-- User: sshejko
-- Date: 14.12.2015
-- Time: 11:33
-- To change this template use File | Settings | File Templates.
--
local months_ru = {[0] = '', [1] = 'Рамахатъ', [2] = 'Айлетъ', [3] = 'Бейлетъ', [4] = 'Гейлетъ', [5] = 'Дайлетъ', [6] = 'Элетъ', [7] = 'Вэйлетъ', [8] = 'Хейлетъ', [9] = 'Тайлетъ' }

function conv_time()
    local cur_hour = tonumber(os.date('%H'))
    local cur_minutes = tonumber(os.date('%M'))
    local cur_sec = tonumber(os.date('%S'))
    if cur_hour > 18 then
        cur_hour = cur_hour - 18
    else
        cur_hour =  cur_hour + 6
    end
    local c_secs = cur_hour * 60 * 60 + cur_minutes * 60 + cur_sec
    local all_dol = c_secs * 34.56
    local cov_hour = math.modf(all_dol / (1296 * 144))
    local ost_chastey = all_dol % (1296 * 144)
    local chastey = math.modf(ost_chastey / 1296)
    local doley = math.modf((ost_chastey % 1296)/1)
    return cov_hour, chastey, doley
end

function eval_day()
    local __simple_year__ = 365
    local __st_year__ = 369
    local __one_round_years__ = __simple_year__ * 15 + __st_year__
    local __one_round_life__ = __one_round_years__ * 9
    local __one_svarogs_day__ = __one_round_life__ * 180

    -- Days in Svarogs day before 23.09.2012
    -- 23.09.2012 starts 3 of 4 parts of Svarogs day
    local day_before_base = __one_svarogs_day__ / 2

    local base_date = tonumber(os.time{year=2012, month=9, day=23, hour=18, min=0, sec=0})
    local cur_date = tonumber(os.time())
    local temp_div_base, temp_div_ost = math.modf((cur_date-base_date)/86400)
    local days_between_dates = temp_div_base


    local svarogs_days = nil
    temp_div_base, temp_div_ost = math.modf((days_between_dates + day_before_base) / __one_svarogs_day__)
    if temp_div_base > 0 then
        temp_div_base, temp_div_ost = math.modf((days_between_dates + day_before_base) / __one_svarogs_day__)
        local count_svarogs_days = temp_div_base
        days_between_dates = __one_svarogs_day__ * count_svarogs_days - days_between_dates - day_before_base
        svarogs_days = count_svarogs_days
    else
        svarogs_days = 0
    end

    svarogs_days = svarogs_days + 1



    local round_lifes = nil
    temp_div_base, temp_div_ost = math.modf(days_between_dates / __one_round_life__)
    if temp_div_base > 0 then
        temp_div_base, temp_div_ost = math.modf(days_between_dates / __one_round_life__)
        round_lifes = temp_div_base
        days_between_dates = days_between_dates % __one_round_life__
    else
        round_lifes = 0
    end


    round_lifes  = round_lifes + 1

    local round_years = nil
    temp_div_base, temp_div_ost = math.modf(days_between_dates / __one_round_years__)
    if temp_div_base > 0 then
        temp_div_base, temp_div_ost = math.modf(days_between_dates / __one_round_years__)
        round_years = temp_div_base
        days_between_dates = days_between_dates % __one_round_years__
    else
        round_years = 0
    end

    round_years = round_years + 1


    local year = nil
    local month = nil
    local day = nil
    temp_div_base, temp_div_ost = math.modf(days_between_dates / (__simple_year__ * 15))


    if  temp_div_base > 0 then
        -- big year(16-th)
        days_between_dates = days_between_dates - (__simple_year__ * 15)
        year = 16
        temp_div_base, temp_div_ost = math.modf(days_between_dates / 41)
        month = temp_div_base + 1
        day = days_between_dates % 41
        return svarogs_days, round_lifes, round_years, year, month, day
    else
    -- simple year
        temp_div_base, temp_div_ost = math.modf(days_between_dates / __simple_year__)
        year = temp_div_base
        local corr_year = year + 1
        local days_in_cur_year = (days_between_dates - (year * __simple_year__)) + 1
        days_in_cur_year = days_in_cur_year + 1 -- because days_in_cur_year might be 0
        local date = nil
        if days_in_cur_year >= 1 and days_in_cur_year < 41+1 then -- [1..41] 41
            month = 1
            date = days_between_dates
        elseif days_in_cur_year >= 41+1 and days_in_cur_year < 41+1+40 then -- [42..81] 40
            month = 2
            date = days_in_cur_year - 41
        elseif days_in_cur_year >= 41+1+40 and days_in_cur_year < 41+1+40+41 then -- [82..122] 41
            month = 3
            date = days_in_cur_year - 41 - 40
        elseif days_in_cur_year >= 41+1+40+41 and days_in_cur_year < 41+1+40+41+40 then -- [123..162] 40
            month = 4
            date = days_in_cur_year - 41 - 40 - 41
        elseif days_in_cur_year >= 41+1+40+41+40 and days_in_cur_year < 41+1+40+41+40+41 then -- [163..203] 41
            month = 5
            date = days_in_cur_year - 41 - 40 - 41 - 40
        elseif days_in_cur_year >= 41+1+40+41+40+41 and days_in_cur_year < 41+1+40+41+40+41+40 then -- [204..243] 40
            month = 6
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41
        elseif days_in_cur_year >= 41+1+40+41+40+41+40 and days_in_cur_year < 41+1+40+41+40+41+40+41 then -- [244..284] 41
            month = 7
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41 - 40
        elseif days_in_cur_year >= 41+1+40+41+40+41+40+41 and days_in_cur_year < 41+1+40+41+40+41+40+41+40 then -- [285..324] 40
            month = 8
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41 - 40 - 41
        else -- range(41+1+40+41+40+41+40+41+40, 41+1+40+41+40+41+40+41+40+41) [325..365] 41
            month = 9
            date = days_in_cur_year - 41 - 40 - 41 - 40 - 41 - 40 - 41 - 40
        end

        day = date
        return svarogs_days, round_lifes, round_years, corr_year, month, day
    end
end

function cur_day()
    local svarog_days, round_lifes, round_years, year, month, day = eval_day()
    local year_in_round_life = (round_lifes-1) * (round_years-1) + year
    local year_in_round_years = year
    month = month
    day = day
    return year_in_round_life, year_in_round_years, month, day
end

function year_cpsc()
    local svarog_days, round_lifes, round_years, year, month, day = eval_day()
    return year + 7520
end

function get_current_day_name_digit()
    local base_date = tonumber(os.time{year=2012, month=9, day=23, hour=18, min=0, sec=0})
    local cur_date = tonumber(os.time())
    local diff_dates = (cur_date - base_date)
    local temp_div_base_d = 0
    local temp_div_ost_d = 0
    temp_div_base_d, temp_div_ost_d = math.modf((diff_dates/86400))
    local day_num = ((temp_div_base_d+1)%9) -- + 1 т.к. берётся целая часть, а её надо округлить вперёд(разница в секундах первый день делает нулевым, а он должен быть первым)
    return day_num + 1 -- +1 чтобы понедельник был 1-м а не нулевым
end
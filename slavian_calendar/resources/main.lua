-- Your app starts here!
require("convert_time_lib")

months_ru = {[0] = '', [1] = 'Рамахатъ', [2] = 'Айлетъ', [3] = 'Бейлетъ', [4] = 'Гейлетъ', [5] = 'Дайлетъ', [6] = 'Элетъ', [7] = 'Вэйлетъ', [8] = 'Хейлетъ', [9] = 'Тайлетъ' }

months_character_ru = {[0] = '', [1] = 'Сороковник Божественного Начала', [2] = 'Сороковник Новых Даров', [3] = 'Сороковник Белого Сияния и Покоя Мира', [4] = 'Сороковник Вьюг и Стужи', [5] = 'Сороковник Пробуждения Природы', [6] = 'Сороковник Посева и Наречения', [7] = 'Сороковник Ветров', [8] = '	Сороковник Получения Даров Природы', [9] = 'Сороковник Завершения' }

hours_caption_ru = {[0] = 'Поудани', [1] = 'Паобѣдъ', [2] = 'Вѣчиръ', [3] = 'Ничь', [4] = 'Полничь', [5] = 'Заутра', [6] = 'Заура', [7] = 'Заурнице', [8] = 'Настя', [9] = 'Сваор', [10] = 'Утрось', [11] = 'Поутрось', [12] = 'Обестина', [13] = 'Обед', [14] = 'Подани', [15] = 'Утдайни', [16] = 'Поудани' }

hours_description_ru = {[0] = 'завершённый день', [1] = 'начало нового дня', [2] = 'появление звёздной росы на Небесах', [3] = 'нечётное время 3-х Лун', [4] = 'полный путь Лун', [5] = 'звёздное утешение росы', [6] = 'звёздное сияние, заря', [7] = 'окончание звёздного сияния', [8] = 'утренняя роса', [9] = 'восход Солнца', [10] = 'успокоение росы', [11] = 'путь собирания успокоенной росы', [12] = 'обедня, совместное собрание', [13] = 'трапеза', [14] = 'отдых после трапезы', [15] = 'время окончания деяний', [16] = 'завершённый день' }

days_caption = {[0] = '', [1] = 'Понедельникъ', [2] = 'Вторникъ	', [3] = 'Третейникъ', [4] = 'Четверикъ', [5] = 'Пятница', [6] = 'Шестица', [7] = 'Седьмица', [8] = 'Осьмица', [9] = 'Неделя' }

days_desc = {[0] = '', [1] = 'день труда', [2] = 'день труда', [3] = 'день отдыха', [4] = 'день труда', [5] = 'день труда', [6] = 'день отдыха', [7] = 'день отдыха, пост', [8] = 'день труда', [9] = 'день гостей' }
--If using [QUICK] DeferRenderingOnStart=1 in app.icf, you must call this
--when your first scene is ready to draw.
director:startRendering()

bg = director:createSprite({x=0, y=0, xAnchor=0.5, yAnchor=0.5, xScale=2, yScale=2, source="bg.png"})

local fontText = director:createFont("fonts/arial_25.fnt")
local Cur_hour = director:createLabel({x=90, y=director.displayHeight-25, text=tostring(0), font=fontText, color=color.black})
local Cur_chastey = director:createLabel({x=90, y=director.displayHeight-50, text=tostring(0), font=fontText, color=color.black})
local Cur_doley = director:createLabel({x=90, y=director.displayHeight-75, text=tostring(0), font=fontText, color=color.black})
local Cur_caption_hour = director:createLabel({x=0, y=director.displayHeight-25, text="Часы", font=fontText, color=color.black})
local Cur_caption_chastey = director:createLabel({x=0, y=director.displayHeight-50, text="Части", font=fontText, color=color.black})
local Cur_caption_doley = director:createLabel({x=0, y=director.displayHeight-75, text="Доли", font=fontText, color=color.black})

local Cur_name_hour = director:createLabel({x=0, y=director.displayHeight-100, text="", font=fontText, color=color.black})
local Cur_description_hour = director:createLabel({x=0, y=director.displayHeight-145, text="", font=fontText, color=color.black})

local Cur_day = director:createLabel({x=65, y=director.displayHeight-190, text=tostring(0), font=fontText, color=color.black})
local Cur_caption_day = director:createLabel({x=0, y=director.displayHeight-190, text="День", font=fontText, color=color.black})
local Cur_day_name = director:createLabel({x=100, y=director.displayHeight-190, text="", font=fontText, color=color.black})
local Cur_day_descr = director:createLabel({x=0, y=director.displayHeight-215, text="", font=fontText, color=color.black})

local Cur_month = director:createLabel({x=230, y=director.displayHeight-250, text=tostring(0), font=fontText, color=color.black})
local Cur_caption_month = director:createLabel({x=0, y=director.displayHeight-250, text="Сороковник", font=fontText, color=color.black})
local Cur_text_month = director:createLabel({x=130, y=director.displayHeight-250, text="", font=fontText, color=color.black})
local Cur_text_month_character = director:createLabel({x=0, y=director.displayHeight-310, text="", font=fontText, color=color.black})

local Cur_year_in_round_years = director:createLabel({x=220, y=director.displayHeight-390, text=tostring(0), font=fontText, color=color.black})
local Cur_caption_year_in_round_years = director:createLabel({x=0, y=director.displayHeight-390, text="Лето в Круге Лет", font=fontText, color=color.black})

local Cur_year_in_round_life = director:createLabel({x=220, y=director.displayHeight-420, text=tostring(0), font=fontText, color=color.black})
local Cur_caption_year_in_round_life = director:createLabel({x=0, y=director.displayHeight-420, text="Лето в Круге Жизни", font=fontText, color=color.black})

local Cur_svarog_year = director:createLabel({x=180, y=director.displayHeight-450, text=tostring(0), font=fontText, color=color.black})
local Cur_caption_svarog_year = director:createLabel({x=0, y=director.displayHeight-450, text="Лето от С.М.З.Х.", font=fontText, color=color.black})



function update_labels()
  h, c, d = conv_time()
  year_in_round_life, year_in_round_years, month, day = cur_day()
  svarog_year = year_cpsc()
  day_num = get_current_day_name_digit()
  
  Cur_hour.text = tostring(h)
  Cur_chastey.text = tostring(c)
  Cur_doley.text = tostring(d)
  Cur_day.text = tostring(day)
  Cur_month.text = "("..tostring(month)..")"
  Cur_text_month.text = months_ru[month]
  Cur_text_month_character.text = months_character_ru[month]
  
  Cur_day_name.text = days_caption[day_num]
  Cur_day_descr.text = days_desc[day_num]
  
  Cur_name_hour.text = hours_caption_ru[h]
  Cur_description_hour.text = hours_description_ru[h]
  
  Cur_year_in_round_years.text = tostring(year_in_round_years)
  Cur_year_in_round_life.text = tostring(year_in_round_life)
  Cur_svarog_year.text = tostring(svarog_year)
end
system:addTimer(update_labels, 1, 0)

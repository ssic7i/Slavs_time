-- Your app starts here!
require("convert_time_lib")

months_ru = {[0] = '', [1] = 'Рамахатъ', [2] = 'Айлетъ', [3] = 'Бейлетъ', [4] = 'Гейлетъ', [5] = 'Дайлетъ', [6] = 'Элетъ', [7] = 'Вэйлетъ', [8] = 'Хейлетъ', [9] = 'Тайлетъ' }


--If using [QUICK] DeferRenderingOnStart=1 in app.icf, you must call this
--when your first scene is ready to draw.
director:startRendering()
--gem = director:createSprite({x=director.displayWidth/2, y=0, xAnchor=0.5, xAnchor=0.5, source="girl.png"})
--gem = director:createSprite({x=director.displayWidth/2, y=director.displayHeight/2, source="girl.png"})

local Cur_hour = director:createLabel(90, director.displayHeight-20, tostring(0))
local Cur_chastey = director:createLabel(90, director.displayHeight-40, tostring(0))
local Cur_doley = director:createLabel(90, director.displayHeight-60, tostring(0))
local Cur_caption_hour = director:createLabel(0, director.displayHeight-20, "Hours")
local Cur_caption_chastey = director:createLabel(0, director.displayHeight-40, "Chasty")
local Cur_caption_doley = director:createLabel(0, director.displayHeight-60, "Doly")

local Cur_day = director:createLabel(90, director.displayHeight-100, tostring(0))
local Cur_caption_day = director:createLabel(0, director.displayHeight-100, "Day")

local Cur_month = director:createLabel(90, director.displayHeight-120, tostring(0))
local Cur_caption_month = director:createLabel(0, director.displayHeight-120, "Month")

local Cur_year_in_round_years = director:createLabel(180, director.displayHeight-140, tostring(0))
local Cur_caption_year_in_round_years = director:createLabel(0, director.displayHeight-140, "Year in years")

local Cur_year_in_round_life = director:createLabel(180, director.displayHeight-160, tostring(0))
local Cur_caption_year_in_round_life = director:createLabel(0, director.displayHeight-160, "Year in Life")

local Cur_svarog_year = director:createLabel(160, director.displayHeight-180, tostring(0))
local Cur_caption_svarog_year = director:createLabel(0, director.displayHeight-180, "Svarog Year")



--local label1 = director:createLabel( {
--    hAlignment="right",vAlignment="middle",
--    text="Parent with borders",
--    color={0x80, 0xff, 0xff},
--    textBorderLeft=40,
--    textBorderRight=40,
--    textBorderTop=10,
--    textBorderBottom=18,
--    debugDraw=true,
--    font="Arial18.fnt"
--    } )
--

function update_labels()
  h, c, d = conv_time()
  year_in_round_life, year_in_round_years, month, day = cur_day()
  svarog_year = year_cpsc()
  
  Cur_hour.text = tostring(h)
  Cur_chastey.text = tostring(c)
  Cur_doley.text = tostring(d)
  Cur_day.text = tostring(day)
  Cur_month.text = tostring(month)
  Cur_year_in_round_years.text = tostring(year_in_round_years)
  Cur_year_in_round_life.text = tostring(year_in_round_life)
  Cur_svarog_year.text = tostring(svarog_year)
--  local Cur_hour = director:createLabel({x=10, y=20, w=200, y=100, font="fonts/Default.fnt", text=tostring(h), hAlignment="center", vAlignment="top"} )
--  local Cur_chastey = director:createLabel({x=10, y=40, w=200, y=100, font="fonts/Default.fnt", text=tostring(c), hAlignment="center", vAlignment="top"})
--  local Cur_doley = director:createLabel({x=10, y=26, w=200, y=100, font="fonts/Default.fnt", text=tostring(d), hAlignment="center", vAlignment="top"})
end
system:addTimer(update_labels, 1, 0)

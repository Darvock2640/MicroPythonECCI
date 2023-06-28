from pico_i2c_lcd import Screen

lcd = Screen(master_SCL=32, master_SDA=33, i2c_num_rows=4, i2c_num_cols=20)

lcd.lcd_str("Hola mundo", 0, 0)
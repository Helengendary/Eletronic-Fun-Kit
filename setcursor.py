def write_char(self, char):
        self._send_byte(ord(char), True)

    def set_cursor(self, col, row):
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        self._send_byte(0x80 | (col + row_offsets[row]))

# Configuração dos pinos
lcd = LCD(rs=14, e=13, d4=12, d5=11, d6=10, d7=9)

# Utilização do display
lcd.set_cursor(0, 0)  # Definir cursor para a coluna 0, linha 0
lcd.write_char('H')
def parse_verilog_number_literal(s):
    s = s.strip()
    if s[0] == '-':
        sign = True
        s = s[1:]
    else:
        sign = False

    if '0x' in s or '0X' in s:
        base = 16
        s = s.replace('0x', '').replace('0X', '')
    elif '0' in s and 'b' not in s:
        base = 8
        s = s.replace('0', '')
    else:
        base = 10

    value = int(s, base)
    bits = len(bin(value)[2:]) - 1

    return sign, bits, base, value

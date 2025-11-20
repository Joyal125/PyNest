int val = 0xCAFE;

/* 1. Test if last 4 bits have at least 3 bits ON */
((val & 0xF) >= 0x7);

/* 2. Reverse byte order -> 0xFECA */
((val >> 8) & 0xFF) | ((val & 0xFF) << 8);

/* 3. Rotate 4 bits -> 0xECAF */
((val << 4) | (val >> 12)) & 0xFFFF;

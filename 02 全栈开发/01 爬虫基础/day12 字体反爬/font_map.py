"""https://kekee000.github.io/fonteditor/  字体反爬
https://k.autohome.com.cn/5499#pvareaid=3454440   # 汽车之家

# code name 字体  换源安装
# pip install fontTools
# pip install pygame
# pip install ddddocr

a = {'': 7}
from fontTools.ttLib import TTFont
font = TTFont('03fa6bd5.woff')
font.saveXML('1.xml')"""

import os
import io

from lxml import etree

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from fontTools.ttLib import TTFont
import ddddocr


class GetFontMap(object):
    count = 0

    def __init__(self, font_path):
        self.font_path = font_path
        self.font_ocr = ddddocr.DdddOcr(show_ad=False)
        self.filename = "font"
        GetFontMap.count += 1
        pygame.init()

    def font_map(self):
        if not os.path.exists(self.filename):
            os.mkdir(self.filename)
        f = TTFont(self.font_path)
        f.saveXML(f"{self.filename}/{GetFontMap.count}.xml")
        xml_file = etree.parse(f"{self.filename}/{self.count}.xml")
        font = pygame.font.Font(self.font_path, 30)
        font_names = xml_file.xpath('//GlyphOrder/GlyphID/@name')
        code_dict = {}
        for i in font_names:
            a = i.replace('uni', '0x')
            try:
                word = chr(eval(a))
            except Exception as e:
                continue
            text = font.render(word, True, (0, 0, 0), (255, 255, 255))
            byte_io = io.BytesIO()
            pygame.image.save(text, byte_io)
            byte_arr = byte_io.getvalue()
            result = self.font_ocr.classification(byte_arr)
            code_dict[a] = result
        data_dict = {}
        for k, v in code_dict.items():
            key = k.replace("0x", '&#x') + ';'
            data_dict[key.lower()] = v
        return data_dict

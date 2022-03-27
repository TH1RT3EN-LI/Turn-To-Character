import os

import cv2
from PIL import Image


class TurnToCharacter():
    """
    把图片按灰度转换成字符
    """
    def __init__(self, path, multiple=2):
        self.path = path
        self.multiple = multiple

        self.img = Image.open(self.path)
        self.img_w, self.img_h = self.img.size
        self.compress = 'Turn To Character/compressed_img.png'


    def zoom_in(self):
        """放大图片"""
        self.img.thumbnail((self.img_w*self.multiple, self.img_h*self.multiple))
        self.img.save(self.compress)

    def zoom_out(self):
        """缩小图片"""
        self.img.thumbnail((self.img_w/self.multiple, self.img_h/self.multiple))
        self.img.save(self.compress)
    
    
    def turn_to_character(self, character_list, zoom_in=False, zoom_out=False):
        if zoom_in and not zoom_out:
            self.zoom_in()
            cv_img = cv2.imread(self.compress, cv2.IMREAD_GRAYSCALE)
            self.remove_compressed_img()
        if zoom_out and not zoom_in:
            self.zoom_out()
            cv_img = cv2.imread(self.compress, cv2.IMREAD_GRAYSCALE)
            self.remove_compressed_img()
        else:
            cv_img = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)

        s = ''
        for i in cv_img:
            for ii in i:
                # 默认八位灰度
                gray_level = int(ii // 32)
                s += character_list[gray_level]
            with open('Turn To Character/turn_to_character.txt', 'a') as f:
                f.write(s + '\n')
            s = ''
        print('处理完成！')
        

    def remove_compressed_img(self):
        os.remove(self.compress)
    

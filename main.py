from turn_to_character import TurnToCharacter
"""        ,----,       ,----,           
      ,/   .`|     ,/   .`|           
    ,`   .'  :   ,`   .'  : ,----..   
  ;    ;     / ;    ;     //   /   \  
.'___,/    ,'.'___,/    ,'|   :     : 
|    :     | |    :     | .   |  ;. / 
;    |.';  ; ;    |.';  ; .   ; /--`  
`----'  |  | `----'  |  | ;   | ;     
    '   :  ;     '   :  ; |   : |     
    |   |  '     |   |  ' .   | '___  
    '   :  |     '   :  | '   ; : .'| 
    ;   |.'      ;   |.'  '   | '/  : 
    '---'        '---'    |   :    /  
                           \   \ .'   
                            `---`     
                                      """
if __name__ == '__main__':
    # 供替换的字符，长度应小于等于灰度位数
    character_list = [
        '一',
        '二',
        '三',
        '四',
        '五',
        '六',
        '七',
        '八',
    ]
    character_list.reverse()
    # 图片路径
    path = r''
    # 缩放倍数
    multiple = 4
    # 实例化
    tc = TurnToCharacter(path, multiple)
    # 选择是否需要放大、缩小
    tc.turn_to_character(character_list, zoom_in=False, zoom_out=True)

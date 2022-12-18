import ybc_ai
import ybc_ui
import ybc_tools


a = ybc_ui.picker_button('选择一个小程序',['🐼动物识别','🤖️人机对话','🔍制作二维码'])
if a =='🐼动物识别':
    c = ybc_ui.picker_file()
    b = ybc_ai.animal_breed(c)
    ybc_ui.message(b,c)
if a == '🤖️人机对话':
    b = ybc_tools.record()
    c = ybc_ai.voice2text(b)
    d = ybc_ai.chat(c)
    ybc_ai.speak(d)
if a == '🔍制作二维码':
    c = ybc_ui.input('输入想要储存在二维码中的信息：')
    b = ybc_tools.qrcode(c)
    ybc_ui.message('二维码',b)

print('程序运行完毕')

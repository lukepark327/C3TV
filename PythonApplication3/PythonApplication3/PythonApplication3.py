    # _*_ coding: utf-8 _*_


from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import random

letters = '가나다라마거너더러머버서저고노도로모보소오조구누두루무부수우주바사아자하허호배'
numbers='0123456789'
W=520
H=110

font = ImageFont.truetype('C:\Windows\Fonts\FE-Font.ttf',size=83, encoding='unic')   

image_no=1

for i in range(3):
    image = Image.open(r'C:\Users\user\Desktop\background.png') #배경으로 쓸 이미지(번호판 양식) 
    
    N1=random.choice(numbers)
    N2=random.choice(numbers)
    N3=random.choice(numbers)
    
    L1= random.choice(letters)

    N4= random.choice(numbers)
    N5= random.choice(numbers)
    N6= random.choice(numbers)
    N7= random.choice(numbers)

    Fmessage=N1+N2+N3
    Mmessage=L1
    Lmessage=N4+N5+N6+N7
    message=Fmessage+Mmessage+Lmessage
    
    color = 'rgb(0,0,0)'

    draw = ImageDraw.Draw(image)
    w,h = draw.textsize(message,font=font)

    x,y=((W-w)/2),((H-h)/2-5)
    draw.text((x,y+5),Fmessage,fill=color,font=font)
    draw.text((220,y+20),Mmessage,fill=color,font=font)
    draw.text((270,y+5),Lmessage,fill=color,font=font)
    
   
    
    plt.imshow(image) # 만들어진 번호판 미리보기
    plt.show()
    name='license'+str(image_no)+'.PNG'
    image.save(name,'PNG')
    image_no+=1

# FE-font자체 문제때문에 프로그램 돌리면 한글이 ㅁ 형태로 나오는 문제는 아직 해결하지 못했습니다.
# FE-font 다운로드 주소: https://www.wfonts.com/font/fe-font



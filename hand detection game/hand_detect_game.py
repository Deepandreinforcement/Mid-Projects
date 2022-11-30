
import cv2
import time

import numpy as np
import pygame
import random


# burada elin yumruk şeklinde olması lazım

kamera= cv2.VideoCapture(0)
WIDTH=300
HEIGHT=300
FPS=30
score=0 

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
magenta=(255,0,255)
turuncu=(255,150,0)
turkuaz=(0,245,255)
pembe=(255,0,150)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20)) #20*20 genişliğinde bir obje oluşturduk ekranda gözkümesi için
        self.image.fill(blue) # bu objeyi maviye boyadık.
        self.rect=self.image.get_rect() # objeye rectangle özelliliği atadık. 
        self.rect.centerx=WIDTH/2 # objenin merkezinin x konumunu ayarladık.
        self.rect.bottom=HEIGHT-1
        self.speedx=0
    
    def update(self,gg=WIDTH/2):
        self.rect.centerx=gg
        if self.rect.left < 0:
            
            self.rect.left=0
            
        if self.rect.right > WIDTH:
            
            
            self.rect.right=WIDTH
#        
        
        
class Enemy(pygame.sprite.Sprite):
   
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((15,15)) 
        self.image.fill(red)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=30
        if score <10:
            
            self.speedx=0
        else:
            self.speedx=10
        self.speedy=5
    def update(self,gg=WIDTH/2):
        global score
        
        
        self.speedy=5+score*0.2
        print("hiz: ", self.speedy)
        
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        
        if self.rect.left < 0:
            
            self.speedx*=-1
        if self.rect.right > WIDTH:
            
            self.speedx*=-1
        
        if self.rect.bottom> HEIGHT or aa:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=30
            if not aa:
                
                score+=1
        

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")
clock=pygame.time.Clock()



all_sprite=pygame.sprite.Group() # sprite grubu ürettik
enemy=pygame.sprite.Group()
player=Player()
all_sprite.add(player) #player ı sprite grubuna ekledik
m1=Enemy()
m2=Enemy()
all_sprite.add(m1)
all_sprite.add(m2)
enemy.add(m1)
enemy.add(m2)




can=2
running=True
gg=WIDTH//2
aa=False # çarpma varsa score artmasın diye kullanılıyor
bb=True # enemy 3 için
cc=True # enemy 4 için
dd=True # enemy 5 için


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(turkuaz)
    font3=pygame.font.SysFont("Helvatica",40) # yazı fontu ve boyutu
    yazi3=font3.render("Başlamak için",1,pembe,white)
    yazi4=font3.render("sol yön tuşuna ",1,pembe,white)
    yazi5=font3.render("basınız. ",1,pembe,white)
    
    
    screen.blit(yazi3,(40,110))
    screen.blit(yazi4,(40,150))
    screen.blit(yazi5,(40,190))
    pygame.display.update()
    keystate=pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        
        break



while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            
            running=False
            
    ret,kare=kamera.read()
    kare=cv2.resize(kare,(300, 300))
    yuz=cv2.CascadeClassifier("fist.xml")
    gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    yuzler=yuz.detectMultiScale(gri,1.1,4)
    
    for (x,y,w,h,) in yuzler:
        gg=x+w//2
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("kamera",kare)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    
    # burada ölçeklendirme yapılıyor böylece sağa ya da sola gitmek daha etkili oluyor oyunda 
    if gg<90:
        gg=90
    if gg>210:
        gg=210
    gg=gg-90
    gg=2.5*gg
    all_sprite.update(WIDTH-gg) # bu gurptaki tüm nesnelere bu işlemi uygulıyoruz.
    # 300-gg olma sebebi ayna etkisi kameranın
    hits=pygame.sprite.spritecollide(player,enemy,False,pygame.sprite.collide_rect) 
    # player ile enemy grubu arasında çarpışma var mı yok mu buna bakarız. Çarpışma tipi circle
    # yani nesnenin etrafına çember çizer
    
    if hits: # çarpışma var ise
        can-=1
        
        
        aa=True #
        all_sprite.update(300-gg)
    aa=False
    print("can: ",can)
    print("score: ",score)
    
    if score==6 and bb:
        m3=Enemy()
        all_sprite.add(m3)
        enemy.add(m3)
        bb=False # bu sayede sadece bir kere enemy 3 üretiliyor.
    if score==15 and cc:
        m4=Enemy()
        all_sprite.add(m4)
        enemy.add(m4)
        cc=False
    if score==27 and dd:
        m5=Enemy()
        all_sprite.add(m5)
        enemy.add(m5)
        dd=False
    if can==0:
        running=False
        print("game over")
        screen.fill(turkuaz)
        
        
        font3=pygame.font.SysFont("Helvatica",60) # yazı fontu ve boyutu
        yazi3=font3.render("Game over",1,pembe,turkuaz)
        screen.blit(yazi3,(40,50)) #yazının x ve y konumu
        
        
        
        font4=pygame.font.SysFont("Helvatica",60) # yazı fontu ve boyutu
        yaz3="Score: "+str(score)
        yazi4=font4.render(yaz3,1,pembe,turkuaz)
        screen.blit(yazi4,(50,150)) #yazının x ve y konumu
        
        pygame.display.update()
        
        
        kamera.release()
        cv2.destroyAllWindows()
        
        time.sleep(5)
        
        pygame.quit()
        break
        
    screen.fill(green)
    
    
    font=pygame.font.SysFont("Helvatica",24) # yazı fontu ve boyutu
    yaz="score: "+str(score)
    yazi=font.render(yaz,1,red,white) 
    screen.blit(yazi,(0,0)) #yazının x ve y konumu
    
    all_sprite.draw(screen) # ekrana değişiklikleri çizdiriyoruz.
    
    
    yaz2="can: "+str(can)
    font2=pygame.font.SysFont("Helvatica",24) # yazı fontu ve boyutu
    yazi2=font2.render(yaz2,1,red,white)
    screen.blit(yazi2,(200,0)) #yazının x ve y konumu
    
    pygame.display.update()




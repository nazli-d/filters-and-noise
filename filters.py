import cv2
import numpy                                                             # Numpy kütüphanesi görüntünün matematiksel işlemlerini yapmak için kullanıldı. 
 
img = cv2.imread('foto.jpg', cv2.IMREAD_GRAYSCALE).astype('float32')     # foto okunup grayscale olarak yüklenir ve float32 veri tipine dönüştürülür.

# mean filter
mean = numpy.zeros_like(img, dtype=numpy.float32)
for i in range(1, img.shape[0] - 1):                                     # img.shape görüntünün boyutunu temsil ediyor.
    for j in range(1, img.shape[1] - 1):
        mean[i,j] = ( img[i-1,j-1] + img[i-1,j] + img[i-1,j+1] + img[i,j-1] + img[i,j]+
            img[i,j+1] + img[i+1,j-1] + img[i+1,j] + img[i+1,j+1] ) / 9.0
        
# median filter
median = numpy.zeros_like(img)
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        pixels = [ img[i-1,j-1], img[i-1,j], img[i-1,j+1],img[i,j-1], img[i,j],
            img[i,j+1],img[i+1,j-1], img[i+1,j], img[i+1,j+1] ]
        
        median[i,j] = numpy.median(pixels)
        
# gaussian filter
gaussian = numpy.zeros_like(img)
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        gaussian[i,j] = ( img[i-1,j-1] + 2*img[i-1,j] + img[i-1,j+1] +
            2*img[i,j-1] + 4*img[i,j] + 2*img[i,j+1] + img[i+1,j-1] + 
            2*img[i+1,j] + img[i+1,j+1] ) / 16

noise_img = img.copy()                                                  
noise_miktari  = 0.1                                                     # %10 luk gürültü
tuz_miktari   = int( noise_miktari * img.size * 0.5 )
biber_miktari = int( noise_miktari * img.size * 0.5 )

# for looplar, gürültü eklenmesi için tuz ve biber gürültüsü miktarını hesaplar ve 'random.randint' fonksiyonu kullanarak, rastgele bir piksele tuz ve biber ekler.  
for i in range( tuz_miktari ):
    x, y = numpy.random.randint( 0, img.shape[0]), numpy.random.randint(0, img.shape[1] )
    noise_img[x, y] = 255

for i in range( biber_miktari ):
    x, y = numpy.random.randint( 0, img.shape[0]), numpy.random.randint(0, img.shape[1] )
    noise_img[x, y] = 0

# Sonuçları ayrı pencerelerde açmak için imshow kullanıldı.
cv2.imshow('Orijinal goruntu', img.astype    ('uint8'))                  
cv2.imshow('Mean filter'    , mean.astype    ('uint8'))
cv2.imshow('Median filter'  , median.astype  ('uint8'))
cv2.imshow('Gaussian filter', gaussian.astype('uint8'))
cv2.imshow('Tuz ve Biber gurultusu', noise_img.astype('uint8'))

cv2.waitKey(0)
cv2.destroyAllWindows()

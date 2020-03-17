import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import cv2
import os

ia.seed(1)


# images = np.array(
#     [ia.quokka(size=(64, 64)) for _ in range(32)],
#     dtype=np.uint8
# )

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = BASE_DIR +"\license1.png"

print("load image " + img_path)

# load images GRAYSCALE
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


sometimes = lambda aug : iaa.Sometimes(0.5, aug)

sev_snow = 0 
sev_fog = 0
sev_rain = 0

# suppose that angle of cctv is 10 to -10 degree 
seq = iaa.Sequential(
    [
        iaa.Fliplr(0.5),
        sometimes(iaa.Affine(
            scale={"x" : (0.95, 1.15), "y" : (0.95,1.15)},
            translate_percent={"x": (-0.15, 0.15), "y" : (-0.15, 0.15)},
            shear=(-16, 16),
            rotate=(-10, 10),
        )),
        
        # degrade the quality of images
        # considering cctv quality
        iaa.JpegCompression(compression=(50, 85)),

        # give random four point perspective tranformations to plates
        sometimes(iaa.PerspectiveTransform(scale = (0.01, 0.15))),

        # using gaussian function, give natural Blur
        iaa.GaussianBlur(sigma = (0.0, 3.0)),

        # give fakes car plate movements
        # if cctv frame rate is low, then give bigger k
        # k determines the height and width of the kernal
        iaa.MotionBlur(k=10),


        # make digital noise.
        iaa.AdditiveGaussianNoise(scale=(0, 0.2*255)),

        iaa.OneOf([
            # adjust image contrast
            iaa.GammaContrast((0.5, 2.0)),
            # change brightness of images
            iaa.Multiply((0.5, 1.5)),
            ]
        ),

        # add Spatter
        sometimes(iaa.OneOf([
            iaa.imgcorruptlike.Spatter(severity=2),
            iaa.imgcorruptlike.Spatter(severity=1),
            iaa.imgcorruptlike.Spatter(severity=3),
            ]
        )),

        # # add Fog
        # # select severity of the fog
        # # default = 0
        # iaa.imgcorruptlike.Fog(severity = sev_fog),

        # # add Rain
        # # select severity of the rain 
        # # default = 0
        # iaa.Rain(severity = sev_rain),

        # # add snow
        # # select severity of the snow
        # # default = 0
        # iaa.imgcorruptlike.Snow(severity = sev_snow),
    ]
)

images_aug = seq(images=img)

# cv2.imwrite('aug_license1.png', images_aug)
cv2.imshow('gray', images_aug)
cv2.imwrite('aug_license1.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

ia.seed(1)

images = np.array(
    [ia.quokka(size=(64, 64)) for _ in range(32)],
    dtype=np.uint8
)

# set 50% for 
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
        sometimes(iaa.perspectiveTransform(scale = (0.01, 0.15))),

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
        # 
        sometimes(iaa.OneOf([
            iaa.Spatter(severity=1),
            iaa.Spatter(severity=2),
            iaa.Spatter(severity=3),
            ]
        )),

        # add Fog
        # select severity of the fog
        # default = 0
        iaa.Fog(severity = sev_fog),

        # add Rain
        # select severity of the rain 
        # default = 0
        iaa.Rain(severity = sev_rain),

        # add snow
        # select severity of the snow
        # default = 0
        iaa.Snow(severity = sev_snow),
    ]
)

images_aug = seq(images=images)
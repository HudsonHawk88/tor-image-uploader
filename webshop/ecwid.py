import requests
from uploader.uploader import Uploader

class Ecwid:
    def __init__(self, storeid, secrettoken):
        self.baseurl = "https://api.ecwid.com/api/v3/" + storeid
        self.uploader = Uploader()
        self.headers = { "Authorization": "Bearer " + secrettoken }
    # Get product id
    def uploadMainImage(self, productid, image):
        uploadUrl = self.baseurl + "/products/" + str(productid) + "/image/async"
        self.uploader.uploadMainImage(self.headers, uploadUrl, image)

    def uploadGalleryImage(self, productid, images):
        uploadUrl = self.baseurl + "/products/" + str(productid) + "/gallery/async"
        self.uploader.uploadGalleryImage(self.headers, uploadUrl, images)

    def bulkUpdateImages(self, productid,  mainimage, galleryimages):
        uploadUrl = self.baseurl + "/products/" + str(productid) + "/media"
        data = { "mainMedia": { "imageUrl": mainimage }, "galleryMedia": { "imageUrl": galleryimages } }
        #print("bulkUpdateImages: ", self.headers, uploadUrl, mainimage, galleryimages, data)
        requests.put(uploadUrl, headers=self.headers, data=data)

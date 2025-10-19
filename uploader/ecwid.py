from uploader import Uploader

class Ecwid:
    def __init__(self, storeid, secrettoken):
        self.baseurl = "https://api.ecwid.com/api/v3/" + storeid
        self.uploader = Uploader()
        self.headers = { "Authorization": "Bearer " + secrettoken }
    # Get product id
    def uploadMainImage(self, productid, image):
        uploadUrl = self.baseurl + "/products/" + productid + "/image"
        self.uploader.uploadMainImage(self.headers, uploadUrl, image)

    def uploadGalleryImage(self, productid, images):
        uploadUrl = self.baseurl + "/products/" + productid + "/image"
        self.uploader.uploadGalleryImage(self.headers, uploadUrl, images)

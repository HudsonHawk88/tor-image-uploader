import requests

class Uploader:

    def uploadMainImage(self, headers, url, image, methodtype = "POST"):
        #print("uploadMainImage: ", headers, url, image, methodtype)
        if methodtype == "GET":
            requests.get(url, headers=headers)
        else:
            requests.post(url, data=image, headers=headers)

    def uploadGalleryImage(self, headers, url, images, methodtype = "POST"):
        #print("uploadGalleryImage: ", headers, url, images, methodtype)
        if methodtype == "GET":
            requests.get(url, headers=headers)
        else:
            requests.post(url, data=images, headers=headers)
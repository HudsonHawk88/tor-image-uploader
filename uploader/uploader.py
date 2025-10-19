import requests

class Uploader:

    def uploadMainImage(self, headers, url, image, methodtype = "POST"):
        print("uploadMainImage: ", headers, url, image, methodtype)
        #if methodtype == "GET":
        #    requests.get(url, headers=headers)
        #else:
        #    requests.post(url, data=image, headers=headers)

    def uploadGalleryImage(self, headers, url, images, methodtype = "POST"):
        print("uploadMainImage: ", headers, url, images, methodtype)
        #if methodtype == "GET":
        #    requests.get(url, headers=headers)
        #else:
        #    requests.post(url, data=images, headers=headers)

    def uploadImageOther(self, url, headers, images, methodtype = "POST"):
        if methodtype == "GET":
            requests.get(url, headers=headers)
        else:
            requests.post(url, headers=headers, data=images)

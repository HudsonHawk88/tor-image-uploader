from webshop.ecwid import Ecwid

EcwidUploader = Ecwid("44059334", "secrettoken")
EcwidUploader.uploadMainImage(12, "https://a.com/a.jpg")
EcwidUploader.uploadGalleryImage(12, ["https://a.com/a.jpg", "https://b.com/b.jpg"])
EcwidUploader.bulkUpdateImages(12, "https://a.com/b.jpg", ["https://a.com/a.jpg", "https://b.com/b.jpg"])
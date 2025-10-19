from uploader.ecwid import Ecwid

EcwidUploader = Ecwid("44059334", "secrettoken")
EcwidUploader.uploadMainImage(12, "https://a.com/a.jpg")
EcwidUploader.uploadGalleryImage(12, ["https://a.com/a.jpg", "https://b.com/b.jpg"])
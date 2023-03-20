import qrcode

dimension = qrcode.QRCode(version = 1, box_size = 40, border = 5)

dimension.add_data("https://www.testsiteprojects.com/https://www.testsiteprojects.com/")
dimension.make(fit = True)
generate_image = dimension.make_image(fill_color = "black",back_color = "white")
generate_image.save("Mathsqrimage.png")


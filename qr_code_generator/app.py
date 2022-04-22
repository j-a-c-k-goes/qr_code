# - - - module imports - - -
import qrcode
import sys, time


def input_URL():
	url = str(input("enter the url you need to make a qr code for (use www.name.com) : "))
	http_prefix = "https://"
	full_url = f"{http_prefix}{url}"
	return full_url

def generate_qr(data, img_path=".", img_filename="qr_code"):
	# - - - make instance of qr - - -
	qr = qrcode.QRCode(
		version=1, 
		error_correction=qrcode.constants.ERROR_CORRECT_L, 
		box_size=15, 
		border=4)
	# - - - pass input text(hyperlink) into qr - - -
	qr.add_data(url)
	# - - - use entire dimension of qr code - - -
	qr.make(fit=True)
	# - - - convert into image file - - -
	qr_image = qr.make_image(fill_color="black", back_color="white")
	# - - - store file in current directory - - -
	qr_image.save(f"{img_path}/{img_filename}_{str(time.time())}.png")
	# - - - display data list of qr - - -
	print(qr.data_list)

if __name__ == "__main__":
	url = input_URL()
	generate_qr(url)






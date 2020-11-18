import os
import cv2
import pandas
import PySimpleGUI as sg
from PIL import Image


""" --- Objectives ---
1 - Load an image and display it on the window
2 - Offer options: delete image, create bouding box, zoom
3 - If delete image -> delete it and load next image
4 - If create bouding box -> save rectangle pos1 and pos2 in a .csv file using pandas
5 - Save image with the rectangle separately and load next image
"""

### Configs
x, y = 640, 480
icon = 'icon.ico' ###Icon made by Freepik -> https://www.flaticon.com/free-icon/picture_937456?term=image%20editing&page=1&position=48
font = 'Arial 14'
back = 'white'
text_color = 'black'

class BBM(object):
	def __init__(self):
		self.target_path = ''
		self.img_name = []
		self.window = self.create_interface()

		self.loop()

	def create_interface(self):
		layout = self.create_layout()

		return sg.Window('Bouding Box Maker', layout=layout, size=(x, y), icon=icon,
			             background_color=back, return_keyboard_events=True, font=font,
			             finalize=True)

	def create_layout(self):
		layout = [ [sg.Text('Select a folder with images', background_color=back, text_color=text_color, font=font)],
		           [sg.Input(key='folder_images'), sg.FolderBrowse(target='folder_images')],
		           [sg.Text('Select a folder to save your work', background_color=back, text_color=text_color, font=font)],
		           [sg.Input(key='folder_save'), sg.FolderBrowse(target='folder_save')], 
		           [sg.Text('First image', background_color=back, text_color=text_color, font=font)],
		           [sg.InputCombo(self.img_name, key='first_image', size=(15, 1))],
		           [sg.Button('START', key='start', pad=(150, 100)), sg.Button('STOP', key='stop')] ]

		return layout

	def show(self, img):
		img = cv2.imread(img)
		cv2.imshow('image', img)
		k = cv2.waitKey(0)
		if k == 27:
			cv2.destroyAllWindows()

	def loop(self):
		while True:

			event, values = self.window.read(timeout=50)

			### Close window
			if event in (None, 'Quit', 'Exit'):
				break

			if values['folder_images'] != self.target_path:
				self.target_path = values['folder_images']

				self.img_name = os.listdir(self.target_path)
				self.window.Element('first_image').update(values=self.img_name)

			if event == 'start':
				for img_name in self.img_name[self.img_name.index(values['first_image']): ]:
					img = self.target_path + '/' + img_name
					self.show(img)
			if event == 'stop':
				break

if __name__ == '__main__':
	bbm = BBM()

	bbm.window.close()
	cv2.destroyAllWindows()
	del bbm
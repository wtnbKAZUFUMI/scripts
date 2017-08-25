import cv2
import sys
import os
import numpy

args = sys.argv
dir_path =  args[1] + "/"
start = [int(args[2]) , int(args[3])]
end = [int(args[4]) , int(args[5])]
files = os.listdir(dir_path)
outdir_name = args[1].split("/")[-1] + "_cut"

def loadImages(dir_path):
	print "loading..."
	files_list = os.listdir(dir_path)
	if ".DS_Store" in files_list:
			files_list.remove(".DS_Store")
	images = [cv2.imread(dir_path + file) for file in files_list]
	return images
def trimingImages(images, start , end):
	print "trimminging..."
	cutimages = [image[start[1] : end[1] , start[0] : end[0]] for image in images]
	return cutimages
def writeImages(images, out_dir, dir_path):
	print "writing..."
	try:
		os.mkdir(out_dir)
	except OSError:
		None
	files_list = os.listdir(dir_path)
	if ".DS_Store" in files_list:
			files_list.remove(".DS_Store")
	[cv2.imwrite(out_dir + files_list[i] , images[i]) for i in range(len(files_list))]

images = loadImages(dir_path)
cutimages = trimingImages(images , start , end)
writeImages(cutimages, dir_path + "../" + outdir_name + "/", dir_path)
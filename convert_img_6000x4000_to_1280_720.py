from PIL import Image
import random

out_filename = "/path/to/orig/img_out.jpg"
filename = "/path/to/orig/img.jpg"
im = Image.open(filename)
imnew = Image.new("RGB", (1280, 720))

def getvals4(start_pos_x, start_pos_y):
	rr5, gg5, bb5 = im.getpixel((start_pos_x+4, start_pos_y+4))
	rr1 = random.randint(-21, 21) + rr5
	rr2 = random.randint(-21, 21) + rr5
	rr3 = random.randint(-21, 21) + rr5
	rr4 = random.randint(-21, 21) + rr5
	gg1 = random.randint(-21, 21) + gg5
	gg2 = random.randint(-21, 21) + gg5
	gg3 = random.randint(-21, 21) + gg5
	gg4 = random.randint(-21, 21) + gg5
	bb1 = random.randint(-21, 21) + bb5
	bb2 = random.randint(-21, 21) + bb5
	bb3 = random.randint(-21, 21) + bb5
	bb4 = random.randint(-21, 21) + bb5
	for xxx in range(4):
		for yyy in range(4):
			tr1, tg1, tb1 = im.getpixel((start_pos_x+xxx, start_pos_y+yyy))
			tr2, tg2, tb2 = im.getpixel((start_pos_x+xxx, start_pos_y+yyy+5))
			tr3, tg3, tb3 = im.getpixel((start_pos_x+xxx+5, start_pos_y+yyy))
			tr4, tg4, tb4 = im.getpixel((start_pos_x+xxx+5, start_pos_y+yyy+5))
			rr1 += tr1
			rr2 += tr2
			rr3 += tr3
			rr4 += tr4
			gg1 += tg1
			gg2 += tg2
			gg3 += tg3
			gg4 += tg4
			bb1 += tb1
			bb2 += tb2
			bb3 += tb3
			bb4 += tb4
	pattern_ab = random.choice("aaaa", "bbbb")
	if (pattern_ab == "aaaa"):
		tr, tg, tb = im.getpixel((start_pos_x,   start_pos_y+4))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x+2, start_pos_y+4))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+1))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+3))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x+1, start_pos_y+4))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+3, start_pos_y+4))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+6))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+8))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+5, start_pos_y+4))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+7, start_pos_y+4))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+2))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+6, start_pos_y+4))
		rr4 += tr
		gg4 += tg
		bb4 += tb
		tr, tg, tb = im.getpixel((start_pos_x+8, start_pos_y+4))
		rr4 += tr
		gg4 += tg
		bb4 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+5))
		rr4 += tr
		gg4 += tg
		bb4 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+7))
		rr4 += tr
		gg4 += tg
		bb4 += tb
	else:
		tr, tg, tb = im.getpixel((start_pos_x+1, start_pos_y+4))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x+3, start_pos_y+4))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+2))
		rr1 += tr
		gg1 += tg
		bb1 += tb
		tr, tg, tb = im.getpixel((start_pos_x,   start_pos_y+4))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+2, start_pos_y+4))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+5))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+7))
		rr2 += tr
		gg2 += tg
		bb2 += tb
		tr, tg, tb = im.getpixel((start_pos_x+6, start_pos_y+4))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+8, start_pos_y+4))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+1))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+3))
		rr3 += tr
		gg3 += tg
		bb3 += tb
		tr, tg, tb = im.getpixel((start_pos_x+5, start_pos_y+4))
		rr4 += tr
		gg4 += tg
		bb4 += tb
		tr, tg, tb = im.getpixel((start_pos_x+7, start_pos_y+4))
		rr4 += tr
		gg4 += tg
		bb4 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+6))
		rr4 += tr
		gg4 += tg
		bb4 += tb
		tr, tg, tb = im.getpixel((start_pos_x+4, start_pos_y+8))
		rr4 += tr
		gg4 += tg
		bb4 += tb
	return (rr1//21, gg1//21, bb1//21, rr2//21, gg2//21, bb2//21, rr3//21, gg3//21, bb3//21, rr4//21, gg4//21, bb4//21)

for xx in range(640):
	for yy in range(360):
		r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4 = getvals4((xx*9+120, yy*9+380))
		imnew.putpixel((xx*2, yy*2), (r1,g1,b1))
		imnew.putpixel((xx*2, yy*2+1), (r2,g2,b2))
		imnew.putpixel((xx*2+1, yy*2), (r3,g3,b3))
		imnew.putpixel((xx*2+1, yy*2+1), (r4,g4,b4))
imnew.save(out_filename)


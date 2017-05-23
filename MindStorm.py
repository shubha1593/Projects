## MindStorm with shapes, design using squares and circles ...

import turtle
import random

pixel = lambda: random.randint(0, 255)

def draw_square(tur, side) :
	for i in range(0, 4) :
		tur.forward(side)
		tur.right(90)


def draw_circle(tur, radius) :
	tur.circle(radius)

def draw_triangle(tur) :
	for i in range(0, 3) :
		tur.right(120)
		tur.forward(150)

def draw_art() :
	window = turtle.Screen()

	window.bgcolor("yellow")
	window.colormode(255)
	aang = turtle.Turtle()
	aang.shape("turtle")
	#aang.color("white")
	aang.speed(20)
	

	katara = turtle.Turtle()
	katara.shape("arrow")
	katara.speed(20)
	for j in range(1, 3) :
		if j == 1:
			aang.color("orange")
		else :
			aang.color("purple")
		for i in range(0, 36) :
			draw_square(aang, 60 + (50 * j))
			aang.right(10)
		for a in range(0, 4) :
			katara.right(90)
			for i in range(0, 36) :
				katara.color(pixel(), pixel(), pixel())
				draw_circle(katara, 60 + (60 * j)+ i)
	
	
	window.colormode(1)

	##sokka = turtle.Turtle()
	##sokka.shape("classic")
	##sokka.color("green")
	##sokka.speed(1)
	##draw_triangle(sokka)
	
	window.exitonclick()

draw_art()
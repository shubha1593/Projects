## Trying to make a flower, just for fun !!

import turtle
import random

## for generating values og r, g, b randomly
pixel = lambda: random.randint(0, 255)

def draw_square(tur, side) :
	for i in range(0, 4) :
		tur.forward(side)
		tur.right(90)

def draw_circle(tur, radius) :
	tur.circle(radius)

def draw_triangle(tur, length, angle) :
	for i in range(0, 3) :
		tur.right(angle)
		tur.forward(length)

def draw_art() :
	window = turtle.Screen()
	window.colormode(255)
	window.bgcolor(255, 255, 0)

	## create object of class Turtle
	katara = turtle.Turtle()
	katara.shape("arrow")
	katara.speed(20)
	for a in range(0, 4) :
		katara.right(90)
		for i in range(0, 36) :
			katara.color(pixel(), pixel(), pixel())
			draw_circle(katara, 120 + i)
	

	## create object of class Turtle
	aang = turtle.Turtle()
	aang.shape("turtle")
	aang.color(255, 102, 0)
	aang.speed(20)
	aang.pensize(2)
	for i in range(0, 36) :
			draw_square(aang, 110)
			aang.right(10)


	## create object of class Turtle
	sokka = turtle.Turtle()
	sokka.shape("classic")
	sokka.color(204, 0, 204)
	sokka.speed(15)
	sokka.pensize(3)
	for i in range(0, 24) :
		draw_triangle(sokka, 80, 120)
		sokka.right(15)
	
	
	window.colormode(1)
	
	window.exitonclick()

draw_art()
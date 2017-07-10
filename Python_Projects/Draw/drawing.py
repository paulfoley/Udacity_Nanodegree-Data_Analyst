## Different Drawings using Turtle

# Import
import turtle

# Functions
def draw_square(some_turtle):
	# Draws a Square
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_triangle(some_turtle):
	# Draws a Triangle
	for i in range(1,4):
		some_turtle.forward(150)
		some_turtle.right(120)

def draw_circle():
	# Draws a Circle
	window = turtle.Screen()
	window.bgcolor('Orange')

	angie = turtle.Turtle()
	angie.shape('arrow')
	angie.color('blue')
	angie.circle(100)

def draw_art():
	# Draws Art
	window = turtle.Screen()
	window.bgcolor('red')
	
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('green')
	brad.speed(10)

	for i in range(1,37):
		draw_triangle(brad)
		brad.right(10)

def draw_flower():
	window = turtle.Screen()
	window.bgcolor("blue")

	icon =turtle.Turtle()
	icon.shape("turtle")
	icon.color("orange")
	icon.speed(20)

	for i in range(1,37):
		icon.left(35)
		icon.forward(50)
		icon.right(35)
		icon.forward(50)
		icon.right(145)
		icon.forward(50)
		icon.right(35)
		icon.forward(50)
		icon.right(10)

	icon.seth(270)
	icon.forward(200)

	window.exitonclick()
"""Painting a scene of three trees, consisting of the components of the trunk, leaves, and branches."""

__author__ = "730482646"


from turtle import Turtle, colormode, done
from random import randint


def main() -> None:
    """Main function to create the image."""
    colormode(255)
    tree_placements = [-200, 0, 200]
    number = 2
    for x in tree_placements:
        draw_tree(x, 0, number)
        number -= 1
    done()


def draw_tree(x: int, y: int, number: int) -> None:
    """Draws a single tree."""
    tree = Turtle()
    tree.speed(0)
    tree.hideturtle()
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    draw_trunk(tree)
    tree.penup()
    tree.goto(x + 17, y + 150)
    tree.pendown()
    draw_leaves(tree)
    tree.penup()
    tree.goto(x + 13, y + 100) 
    tree.pendown()
    draw_branches(tree, number)


def draw_trunk(tree: Turtle) -> None:
    """Draws the trunk of a tree."""
    tree.color("brown")
    tree.begin_fill()
    i = 0
    while i < 2:
        tree.forward(40)
        tree.left(90)
        tree.forward(200)
        tree.left(90)
        i += 1
    tree.end_fill()


def draw_branch(tree: Turtle) -> None:
    """Draws a single branch."""
    random_branch = randint(50, 70)
    tree.forward(random_branch)
    tree.backward(random_branch)


def draw_branches(tree: Turtle, number: int) -> None:
    """Draws branches of a tree using recursion as well as the draw_branch function."""
    tree.color("brown")
    if number == 0:
        return
    else:
        draw_branch(tree)
        tree.left(120)
        draw_branches(tree, number - 1)
        tree.right(240)
        draw_branches(tree, number - 1)
        tree.left(120)


def draw_leaves(tree: Turtle) -> None:
    """Draws the leaves of a tree."""
    tree.penup()
    tree.pendown()
    tree.color("green")
    tree.begin_fill()
    tree.circle(80)
    tree.end_fill()


if __name__ == "__main__":
    main()
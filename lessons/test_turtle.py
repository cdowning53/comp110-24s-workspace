from turtle import Turtle, colormode, done
from random import randint

def main() -> None:
    """Main function to create the image."""
    colormode(255)
    tree_placements = [-200, 0, 200]
    for x in tree_placements:
        draw_tree(x, 0)
    done()

def draw_tree(x: int, y: int) -> None:
    """Draws a single tree."""
    tree = Turtle()
    tree.speed(0)
    tree.hideturtle()
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    draw_trunk(tree)
    tree.penup()
    tree.goto(x + 6, y + 150)
    tree.pendown()
    draw_leaves(tree)
    tree.penup()
    tree.goto(x, y - 2)
    tree.pendown()
    draw_branches(tree)

def draw_trunk(tree: Turtle) -> None:
    """Draws the trunk of a tree."""
    tree.color("brown")
    tree.begin_fill()
    for _ in range(2):
        tree.forward(40)
        tree.left(90)
        tree.forward(200)
        tree.left(90)
    tree.end_fill()

def draw_branch(tree: Turtle) -> None:
    """Draws a single branch."""
    random_branch = randint(40, 60)
    tree.forward(random_branch)
    tree.backward(random_branch)

def draw_branches(tree: Turtle) -> None:
    """Draws branches of a tree."""
    tree.color("brown")
    for _ in range(2):
        draw_branch(tree)
        tree.left(120)

def draw_leaves(tree: Turtle) -> None:
    """Draws the leaves of a tree."""
    tree.penup()
    tree.pendown()
    tree.color("green")
    tree.begin_fill()
    tree.circle(55)
    tree.end_fill()

if __name__ == "__main__":
    main()
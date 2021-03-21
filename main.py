
import numpy as np
import tkinter as tk
from graphs import DirectedGraph
from graph_canvas import GraphCanvas


def random_array(low, high, size):
    return np.random.uniform(low, high, size)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("easyflow")
    my_graph = DirectedGraph()

    my_canvas = GraphCanvas(window, width=800, height=800, background="white", graph_model=my_graph)
    my_canvas.grid(row=0, column=0)

    # Tkinter uses an eventhandler model. Below we bind callbacks to respond to user input events.

    my_canvas.bind('<Button-3>', my_canvas.add_node)
    my_canvas.bind('<Button-1>', my_canvas.draw_line)
    my_canvas.bind('<Double-Button-1>', my_canvas.create_edit)
    my_canvas.bind('<Motion>', my_canvas.draw_guide)

    my_canvas.tag_bind('node', '<Enter>', my_canvas.update_hover_item)
    my_canvas.tag_bind('node', '<Leave>', my_canvas.update_hover_item)
    my_canvas.tag_bind('edge', '<Enter>', my_canvas.update_hover_item)
    my_canvas.tag_bind('edge', '<Leave>', my_canvas.update_hover_item)

    window.mainloop()

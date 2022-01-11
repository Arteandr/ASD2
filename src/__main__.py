from tkinter import *
from linkedlist import LinkedList, Node

data = LinkedList()


def on_submit(event):
    if entry.get().strip(" ") == "":
        return
    data.add(Node(entry.get().strip(" ")))

    entry.delete(0, 'end')
    render(data, canvas)


root = Tk()
root.geometry("500x400")

frame = Frame(root, width=500, height=500)
frame.pack(fill=BOTH)

Label(frame,
      text="Разделить заданный список на два списка: в первый список включить элементы с четными значениями ключей, во второй - с нечетными.").pack()

entry_text = StringVar()


def on_change(entry_text):
    if len(entry_text.get()) > 4:
        entry_text.set(entry_text.get()[:-1])


entry_text.trace("w", lambda *args: on_change(entry_text))

input_frame = Frame(frame, height=100)

entry = Entry(input_frame, textvariable=entry_text)
entry.grid(row=0, column=0)
entry.bind("<Return>", on_submit)


def on_delete_submit():
    even, odd = separate(data)
    render(even, canvasEven)
    render(odd, canvasOdd)


button = Button(input_frame, text="Поделить списки", command=on_delete_submit)
button.grid(row=0, column=1, padx=10)

message = Label(input_frame, text="")
message.grid(row=1, column=0, columnspan=2, pady=10)

input_frame.pack(padx=20, pady=20)

canvas = Canvas(
    frame,
    width=10000,
    height=150,
    scrollregion=(0, 0, 10000, 10000)
)

odd_root = Tk()
odd_frame = Frame(odd_root, width=500, height=500)
odd_frame.pack(fill=BOTH)
canvasOdd = Canvas(
    odd_frame,
    width=10000,
    height=150,
    scrollregion=(0, 0, 10000, 10000)
)

even_root = Tk()
even_frame = Frame(even_root, width=500, height=500)
even_frame.pack(fill=BOTH)
canvasEven = Canvas(
    even_frame,
    width=10000,
    height=150,
    scrollregion=(0, 0, 10000, 10000)
)

hbar = Scrollbar(frame, orient=HORIZONTAL)

hbar.pack(side=BOTTOM, fill=X)
hbar.config(command=canvas.xview)

canvas.pack(side=LEFT, expand=False, padx=20, pady=20)
canvas.config(xscrollcommand=hbar.set)
canvasOdd.pack(side=LEFT, expand=False)
canvasOdd.config(xscrollcommand=hbar.set)
canvasEven.pack(side=LEFT, expand=False)
canvasEven.config(xscrollcommand=hbar.set)


def create_node(_canvas, offset_x=0, arrow=True, label=""):
    base_x = 50 + offset_x
    base_y = 50

    rectange_width = 50
    rectange_height = 50

    if arrow:
        arrow_length = 50

        _canvas.create_line(
            base_x + rectange_width,
            base_y + rectange_height // 2,
            base_x + rectange_width + arrow_length,
            base_y + rectange_height // 2,
            fill='black',
            width=5, arrow=LAST,
            activefill='gray',
            arrowshape="10 10 5"
        )

    _canvas.create_rectangle(
        base_x + 0,
        base_y + 0,
        base_x + rectange_width,
        base_y + rectange_height,
        fill='white', outline='black', width=3
    )

    _canvas.create_text(
        base_x + rectange_width // 2,
        base_y + rectange_height // 2,
        text=label,
        justify=CENTER,
        font="Verdana 14",
        width=rectange_width
    )


def render(linkedlist, _canvas):
    offset = 0
    _canvas.delete("all")
    node = linkedlist.head
    while node is not None:
        create_node(
            _canvas,
            offset_x=offset,
            arrow=(node.next is not None),
            label=node.data,
        )
        node = node.next

        offset += 100


data = LinkedList()

render(data, canvas)


def separate(linkedlist: LinkedList) -> tuple[LinkedList, LinkedList]:
    if len(linkedlist) < 3:
        message['text'] = "В списке недостаточно элементов!"
        return
    else:
        message['text'] = ""

    current = linkedlist.head

    evenlist = LinkedList()
    oddlist = LinkedList()

    while current:
        if int(current.data) % 2 == 0:
            evenlist.add(Node(current.data))
        else:
            oddlist.add(Node(current.data))
        current = current.next

    return evenlist, oddlist
    #
    # try:
    #     current.next.next.next
    #     message['text'] = ""
    # except AttributeError as e:
    #     message['text'] = "В списке недостаточно элементов!"
    #     return
    #
    # if current.next.next.next is None:
    #     dest = current.next.next
    #     del current.next
    #     del current
    #     linkedlist.head = dest
    #     return
    #
    # while current.next.next.next.next is not None:
    #     current = current.next
    #
    # dest = current.next.next.next
    #
    # del current.next.next
    # del current.next
    #
    # current.next = dest


root.mainloop()

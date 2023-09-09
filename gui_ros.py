import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from threading import Thread

class ChatterSubscriberNode(Node):

    def __init__(self, gui):
        super().__init__('chatter_subscriber_node')
        self.subscription = self.create_subscription(
            String,
            '/chatter',
            self.chatter_callback,
            10  # QoS profile depth
        )
        self.subscription  # prevent unused variable warning
        self.gui = gui

    def chatter_callback(self, msg):
        self.gui.update_text(msg.data)


class GUI(Thread):

    def __init__(self):
        super().__init__()
        self.text = ""
        self.node = None
        self.label = None  # Define label as an instance variable

    def run(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

        current_image_index = 0

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def update_image():
            global current_image_index
            if current_image_index == 0:
                canvas.itemconfig(image_1, image=image_image_2)
                current_image_index = 1
            else:
                canvas.itemconfig(image_1, image=image_image_1)
                current_image_index = 0
            window.after(1000, update_image)  # Change image every 1000 milliseconds (1 second)

        window = Tk()
        window.geometry("1024x600")
        window.configure(bg="#525050")

        canvas = Canvas(
            window,
            bg="#525050",
            height=600,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=855.0,
            y=24.0,
            width=152.0,
            height=79.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=854.0,
            y=134.0,
            width=152.0,
            height=79.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=854.0,
            y=244.0,
            width=152.0,
            height=79.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=854.0,
            y=354.0,
            width=152.0,
            height=79.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(f"button_5 clicked {self.text}"),
            relief="flat"
        )
        button_5.place(
            x=854.0,
            y=464.0,
            width=152.0,
            height=79.0
        )

        image_1 = canvas.create_image(
            644.0,
            300.0,
            image=image_image_1
        )

        # Create a label widget to display the text
        self.label = Label(
            window,
            text=self.text,
            bg="#525050",
            fg="white",
            font=("Helvetica", 18)
        )
        self.label.place(x=50, y=50)  # Adjust the position as needed

        window.resizable(False, False)
        window.after(2000, update_image)  # Start the image update loop
        window.mainloop()

    def update_text(self, text):
        self.text = text
        self.label.config(text=self.text)


def main(args=None):
    rclpy.init(args=args)
    gui_thread = GUI()
    node = ChatterSubscriberNode(gui_thread)

    try:
        gui_thread.start()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


import dearpygui.dearpygui as dpg

dependencies = ["window.py"]


def setup(ctx):
    ctx.log("e")
    dpg.add_text("Hello from window2.py")

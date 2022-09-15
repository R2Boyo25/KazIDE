import dearpygui.dearpygui as dpg
import threading

ctx = None


def startdpg():
    dpg.create_context()
    dpg.create_viewport(title='very basic Dear PyGui window')

    with dpg.window(tag="mainwindow"):
        dpg.add_text("Hello World!", pos=(
            dpg.get_viewport_width()/2, dpg.get_viewport_height()/2))

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("mainwindow", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


def setup(_ctx):
    global ctx

    ctx = _ctx

    ctx.log("Creating DPG window.")

    t = threading.Thread(target=startdpg)
    t.start()

    ctx.log("DPG window created.")

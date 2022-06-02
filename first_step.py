import dearpygui as d


def save_callback(sender, data):
    print("Save Clicked")


d.core.add_text("Hello, world")
d.core.add_button("Save", callback=save_callback)
d.core.add_input_text("string", default_value="Quick brown fox")
d.core.add_slider_float("float", default_value=0.273, max_value=1)

d.core.start_dearpygui()

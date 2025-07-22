import random
import tkinter as tk

window = tk.Tk()

window.title("Lottie Translator")
window.geometry("1280x720")
window.resizable(False, False)
window.configure(bg="#fec1d6")

# text at the top of the window
tk.Label(window, text="Lottie Translator", font=("Arial", 50), bg="#fec1d6", fg="black").pack(pady=15)

tk.Label(window, text="(yes lottish is a real language)", font=("Arial", 10), bg="#fec1d6", fg="black").pack(pady=2)

language_frame = tk.Frame(window, bg="#fec1d6")
language_frame.pack(pady=3)

language_left = tk.Label(language_frame, text="English", font=("Arial", 20), bg="#fec1d6", fg="black")
language_left.pack(side=tk.LEFT, padx=270) # 270 is middle 20 is together

language_right = tk.Label(language_frame, text="Lottish", font=("Arial", 20), bg="#fec1d6", fg="black")
language_right.pack(side=tk.LEFT, padx=270) # 270 is middle 20 is together 510 is google translate style

# pretty much just a div
entry_frame = tk.Frame(window, bg="#fec1d6")
entry_frame.pack(pady=3)

# text entry left
left_text = tk.Text(entry_frame, font=("Arial", 20), width=40, height=8)
left_text.pack(side=tk.LEFT, padx=10)

# text entry right
right_text = tk.Text(entry_frame, font=("Arial", 20), width=40, height=8)
right_text.pack(side=tk.LEFT, padx=10)

alphabet = {
    "a": "ll ",
    "b": "bb ",
    "c": "bl ",
    "d": "bbl ",
    "e": "lb ",
    "f": "blb ",
    "g": "bll ",
    "h": "bblb ",
    "i": "llb ",
    "j": "bbll ",
    "k": "blbb ",
    "l": "blbl ",
    "m": "bllb ",
    "n": "bblbb ",
    "o": "lbl ",
    "p": "bbllb ",
    "q": "bblbl ",
    "r": "blbbl ",
    "s": "blblb ",
    "t": "bllbb ",
    "u": "lbb ",
    "v": "blbll ",
    "w": "bllbl ",
    "x": "bblbbl ",
    "y": "bblblb ",
    "z": "bbllbb ",
    " ": "b ",
    "A": "LL ",
    "B": "BB ",
    "C": "BL ",
    "D": "BBL ",
    "E": "LB ",
    "F": "BLB ",
    "G": "BLL ",
    "H": "BBLB ",
    "I": "LLB ",
    "J": "BBLL ",
    "K": "BLBB ",
    "L": "BLBL ",
    "M": "BLLB ",
    "N": "BBLBB ",
    "O": "LBL ",
    "P": "BBLLB ",
    "Q": "BBLBL ",
    "R": "BLBBL ",
    "S": "BLBLB ",
    "T": "BLLBB ",
    "U": "LBB ",
    "V": "BLBLL ",
    "W": "BLLBL ",
    "X": "BBLBBl ",
    "Y": "BBLBLB ",
    "Z": "BBLLBB "
}

# Reverse alphabet dictionary
reverse_alphabet = {v.strip(): k + " " if k != " " else k for k, v in alphabet.items()}

# Track translation direction
is_normal_direction = True

def translate_string(input_string):
    result = []
    if is_normal_direction:
        for char in input_string:
            if char in alphabet:
                result.append(alphabet[char])
            else:
                result.append(char + " ")
        return ''.join(result)
    else:
        # Split input by spaces for reverse translation
        tokens = input_string.split()
        for token in tokens:
            if token in reverse_alphabet:
                result.append(reverse_alphabet[token].strip())
            else:
                result.append(token + " ")
        return ''.join(result)

def on_translate():
    input_text = left_text.get("1.0", tk.END).strip()
    translated_text = translate_string(input_text)
    right_text.delete("1.0", tk.END)
    right_text.insert("1.0", translated_text)

def on_switch_language():
    global is_normal_direction
    is_normal_direction = not is_normal_direction
    # Swap the language labels
    left_label_text = language_left.cget("text")
    right_label_text = language_right.cget("text")
    language_left.config(text=right_label_text)
    language_right.config(text=left_label_text)

translate_button = tk.Button(window, text="Translate", font=("Arial", 20), command=on_translate)
translate_button.pack(pady=20)

switch_button = tk.Button(window, text="Switch Language", font=("Arial", 16), command=on_switch_language)
switch_button.pack(pady=10)

def add_placeholder(text_widget, placeholder):
    text_widget.insert("1.0", placeholder)
    text_widget.config(fg="grey")
    def on_focus_in(event):
        if text_widget.get("1.0", "end-1c") == placeholder:
            text_widget.delete("1.0", "end")
            text_widget.config(fg="black")
    def on_focus_out(event):
        if not text_widget.get("1.0", "end-1c"):
            text_widget.insert("1.0", placeholder)
            text_widget.config(fg="grey")
    text_widget.bind("<FocusIn>", on_focus_in)
    text_widget.bind("<FocusOut>", on_focus_out)

add_placeholder(left_text, "Enter text here...")

add_placeholder(right_text, "Translation")

watermark = tk.Label(window, text="bllb ll bbl lb b bb bblblb b bllb llb bl lbl b :3", font=("Arial", 10), bg="#fec1d6", fg="black")
watermark.pack(side=tk.RIGHT, padx=35, pady=10)


window.mainloop()

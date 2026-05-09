from customtkinter import *



class Launcher(CTk):
    def __init__(self):
        super().__init__()

        self._setup_window()
        self._setup_ui()

        self.hue = 0.0
        self._animate()

        self.username = None
        self.host = None
        self.port = None

    def _setup_window(self):
        self.title("Agar.io Color Edition")
        self.geometry("500x700")
        self.configure(fg_color="#1e1e2e")

    def _setup_ui(self):
        self.main_container = CTkFrame(
            self,
            fg_color="#2b2b3b",
            corner_radius=25,
            border_width=4
        )
        self.main_container.pack(padx=30, pady=30, fill="both", expand=True)

        self.logo_label = CTkLabel(
            self.main_container,
            text="AGAR.IO",
            font=("Impact", 60)
        )
        self.logo_label.pack(pady=(30, 0))

        self.subtitle = CTkLabel(
            self.main_container,
            text="MULTI-COLOR EXPERIENCE",
            font=("Arial", 14, "italic"),
            text_color="#00ffcc"
        )
        self.subtitle.pack(pady=(0, 20))

        self.entry_nick = self._create_input(
            "ВАШ НІКНЕЙМ",
            "UltraPlayer_777",
            "#ff00ff"
        )

        self.entry_ip = self._create_input(
            "IP СЕРВЕРА",
            "agario.eu",
            "#00ffff"
        )

        self.entry_port = self._create_input(
            "ПОРТ",
            "8080",
            "#ffff00"
        )

        self.btn_login = CTkButton(
            self.main_container,
            text="ГРАТИ ЗАРАЗ",
            font=("Arial", 22, "bold"),
            height=60,
            corner_radius=15,
            fg_color="#ff4444",
            hover_color="#ff6666",
            text_color="white",
            border_width=2
        )
        self.btn_login.pack(padx=40, pady=(30, 20), fill="x")

        self.led_line = CTkFrame(
            self.main_container,
            height=5,
            fg_color="white"
        )
        self.led_line.pack(fill="x", padx=60, pady=10)

    def _create_input(self, label, placeholder, color):
        frame = CTkFrame(self.main_container, fg_color="transparent")
        frame.pack(padx=40, pady=8, fill="x")

        CTkLabel(
            frame,
            text=label,
            font=("Arial", 12, "bold"),
            text_color=color
        ).pack(anchor="w", padx=10)

        entry = CTkEntry(
            frame,
            placeholder_text=placeholder,
            height=45,
            border_width=2,
            corner_radius=12,
            fg_color="#353545",
            border_color="#444455",
            text_color="white"
        )
        entry.pack(fill="x", pady=2)

        return entry

    def _hsv_to_hex(self, h):
        h = h % 1.0
        i = int(h * 6)
        f = h * 6 - i

        v = 1.0
        p = 0.0
        q = 1 - f
        t = f

        i = i % 6

        if i == 0:
            r, g, b = v, t, p
        elif i == 1:
            r, g, b = q, v, p
        elif i == 2:
            r, g, b = p, v, t
        elif i == 3:
            r, g, b = p, q, v
        elif i == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q

        return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

    def _animate(self):
        main_color = self._hsv_to_hex(self.hue)
        second_color = self._hsv_to_hex((self.hue + 0.3) % 1.0)

        self.main_container.configure(border_color=main_color)
        self.logo_label.configure(text_color=second_color)
        self.led_line.configure(fg_color=main_color)
        self.btn_login.configure(border_color=second_color)

        self.hue = (self.hue + 0.007) % 1.0

        self.after(15, self._animate)

    def login(self):
        self.username = self._create_input.get()
        self.host = self.entry_ip.get()
        self.port = int(self.entry_port.get())

        self.destroy

if __name__ == "__main__":
    app = Launcher()
    app.mainloop()
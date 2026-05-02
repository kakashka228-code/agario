from customtkinter import *

# Світліша тема для бази
set_appearance_mode("dark")

class MegaRGBAgario(CTk):
    def __init__(self):
        super().__init__()

        self.title("Agar.io Color Edition")
        self.geometry("500x700")
        self.configure(fg_color="#1e1e2e") # Світліший темно-синій/фіолетовий фон

        self.hue = 0

        # Головна панель (світліша за фон)
        self.main_container = CTkFrame(self, fg_color="#2b2b3b", corner_radius=25, border_width=4)
        self.main_container.pack(padx=30, pady=30, fill="both", expand=True)

        # Яскравий заголовок
        self.logo_label = CTkLabel(self.main_container, text="AGAR.IO", 
                                   font=("Impact", 60))
        self.logo_label.pack(pady=(30, 0))
        
        self.subtitle = CTkLabel(self.main_container, text="MULTI-COLOR EXPERIENCE", 
                                 font=("Arial", 14, "italic"), text_color="#00ffcc")
        self.subtitle.pack(pady=(0, 20))

        # Створюємо поля з різними кольоровими акцентами
        self.entry_nick = self.create_fancy_input("ВАШ НІКНЕЙМ", "Наприклад:UltraPlayer_777", "#ff00ff")
        self.entry_ip = self.create_fancy_input("IP СЕРВЕРА", "agario.eu", "#00ffff")
        self.entry_port = self.create_fancy_input("ПОРТ", "Ваш порт...", "#ffff00")

        # Кнопка, яка сама по собі яскрава
        self.btn_login = CTkButton(self.main_container, 
                                   text="ГРАТИ ЗАРАЗ", 
                                   font=("Arial", 22, "bold"),
                                   height=60,
                                   corner_radius=15,
                                   fg_color="#ff4444", 
                                   hover_color="#ff6666",
                                   text_color="white",
                                   border_width=2,
                                   border_color="#ffffff")
        self.btn_login.pack(padx=40, pady=(30, 20), fill="x")

        # Додатковий декор - "світлодіодна стрічка"
        self.led_line = CTkFrame(self.main_container, height=5, fg_color="white")
        self.led_line.pack(fill="x", padx=60, pady=10)

        self.animate_rgb()

    def create_fancy_input(self, label_text, placeholder, accent_color):
        frame = CTkFrame(self.main_container, fg_color="transparent")
        frame.pack(padx=40, pady=8, fill="x")
        
        lbl = CTkLabel(frame, text=label_text, font=("Arial", 12, "bold"), text_color=accent_color)
        lbl.pack(anchor="w", padx=10)
        
        entry = CTkEntry(frame, 
                         placeholder_text=placeholder, 
                         height=45, 
                         border_width=2, 
                         corner_radius=12,
                         fg_color="#353545",
                         border_color="#444455",
                         text_color="white")
        entry.pack(fill="x", pady=2)
        return entry

    def hsv_to_hex(self, h):
        # Робимо кольори максимально насиченими
        h = float(h)
        s, v = 1.0, 1.0
        hi = int(h * 6)
        f = (h * 6) - hi
        p, q, t = v * (1 - s), v * (1 - s * f), v * (1 - s * (1 - f))
        r, g, b = [(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)][hi]
        return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

    def animate_rgb(self):
        # Основний колір анімації
        color_main = self.hsv_to_hex(self.hue)
        # Додатковий колір зі зміщенням (для різноманіття)
        color_secondary = self.hsv_to_hex((self.hue + 0.3) % 1.0)
        
        # Оновлюємо різні елементи різними кольорами
        self.main_container.configure(border_color=color_main)
        self.logo_label.configure(text_color=color_secondary)
        self.led_line.configure(fg_color=color_main)
        self.btn_login.configure(border_color=color_secondary)
        
        self.hue += 0.007 # Трохи швидше переливання
        if self.hue > 1: self.hue = 0
        
        self.after(15, self.animate_rgb)

if __name__ == "__main__":
    app = MegaRGBAgario()
    app.mainloop()
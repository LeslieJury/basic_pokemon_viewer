import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class PokemonCard:
    def __init__(self, name, card_type, rarity, image_path):
        self.name = name
        self.card_type = card_type
        self.rarity = rarity
        self.image_path = image_path

class CardRegistryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Card Registry")
        self.root.geometry("450x550")

        self.cards = [
            PokemonCard("Fuecoco", "Fire", "Common", "images/fuecoco.jpg"),
            PokemonCard("Kyurem", "Water", "Rare", "images/pokemoncard.jpg"),
            PokemonCard("Professor", "Trainer", "Rare", "images/profess.png")
        ]

        self.card_dict = {card.name: card for card in self.cards}
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Choose a Card:", font=("Arial", 12)).pack(pady=10)
        self.card_selector = ttk.Combobox(self.root, values=list(self.card_dict.keys()), state="readonly")
        self.card_selector.pack(pady=5)
        self.card_selector.bind("<<ComboboxSelected>>", self.display_card)

        self.name_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.name_label.pack(pady=5)

        self.type_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.type_label.pack(pady=5)

        self.rarity_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.rarity_label.pack(pady=5)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)

    def display_card(self, event):
        selected_name = self.card_selector.get()
        card = self.card_dict.get(selected_name)

        if card:
            self.name_label.config(text=f"Name: {card.name}")
            self.type_label.config(text=f"Type: {card.card_type}")
            self.rarity_label.config(text=f"Rarity: {card.rarity}")

            if os.path.exists(card.image_path):
                img = Image.open(card.image_path)
                img = img.resize((200, 280))
                self.photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=self.photo)
                self.image_label.image = self.photo
            else:
                self.image_label.config(text="Image not found", image="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CardRegistryApp(root)
    root.mainloop()

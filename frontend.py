import tkinter as tk
from tkinter import messagebox
from isbn_bnf_lookup import get_bnf_data, save_results

def rechercher():
    """Récupère les ISBN entrés par l'utilisateur et effectue la recherche."""
    isbn_input = entry.get()
    isbns = [isbn.strip() for isbn in isbn_input.split(',') if isbn.strip()]
    
    if not isbns:
        messagebox.showwarning("Erreur", "Veuillez entrer au moins un ISBN.")
        return
    
    results = {}
    for isbn in isbns:
        results[isbn] = get_bnf_data(isbn)
    
    save_results(results)
    messagebox.showinfo("Succès", "Recherche terminée ! Résultats sauvegardés dans bnf_results.json")

def create_gui():
    """Crée l'interface graphique avec Tkinter."""
    root = tk.Tk()
    root.title("Recherche ISBN - BNF")
    root.geometry("400x200")
    
    tk.Label(root, text="Entrez les ISBN (séparés par des virgules) :").pack(pady=10)
    
    global entry
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    
    search_button = tk.Button(root, text="Rechercher", command=rechercher)
    search_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    try:
        create_gui()
    except ModuleNotFoundError as e:
        messagebox.showerror("Erreur", f"Module manquant : {e}. Assurez-vous que Tkinter est bien installé.")

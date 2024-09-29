Tady je přehledný **cheat sheet** pro používání Gitu a GitHubu, který ti pomůže s nejčastějšími příkazy:

---

### **1. Nastavení Git**
Nastavení Git uživatele (pouze jednou při první instalaci Gitu):
```bash
git config --global user.name "Jáchym Urban"
git config --global user.email "tvůj@email.com"
```

### **2. Inicializace nového Git repozitáře**
Vytvoření nového repozitáře v aktuálním adresáři:
```bash
git init
```

### **3. Přidání souborů do staging oblasti**
Přidání konkrétního souboru do staging:
```bash
git add název_souboru.py
```

Přidání všech změn (nové, upravené, smazané soubory):
```bash
git add .
```

### **4. Vytvoření commitu**
Commitování změn s popisem:
```bash
git commit -m "Popis změn"
```

### **5. Kontrola stavu repozitáře**
Zobrazí stav (co je změněné, co je přidané do stagingu):
```bash
git status
```

### **6. Zobrazení historie commitů**
Zobrazení seznamu commitů:
```bash
git log
```

Kratší log s jedním řádkem na commit:
```bash
git log --oneline
```

### **7. Připojení vzdáleného repozitáře (GitHub)**
Přidání vzdáleného repozitáře:
```bash
git remote add origin https://github.com/tvuj-uzivatel/tvuj-repozitar.git
```

### **8. Pushnutí změn na GitHub**
Pushnutí lokálních změn na vzdálený repozitář:
```bash
git push -u origin master
```

Pokud používáš větev `main` místo `master`:
```bash
git push -u origin main
```

### **9. Stažení změn z GitHubu**
Stažení změn z GitHubu do lokálního repozitáře:
```bash
git pull origin master
```

### **10. Vytvoření nové větve**
Vytvoření nové větve a přepnutí na ni:
```bash
git checkout -b název-vetve
```

Přepnutí na existující větev:
```bash
git checkout název-vetve
```

### **11. Sloučení větví (merge)**
Sloučení změn z jiné větve do aktuální větve:
```bash
git merge název-vetve
```

### **12. Klonování repozitáře**
Stažení kopie existujícího repozitáře z GitHubu:
```bash
git clone https://github.com/tvuj-uzivatel/tvuj-repozitar.git
```

### **13. Odstranění souboru z Git**
Smazání souboru z Git (a zároveň z disku):
```bash
git rm název_souboru.py
```

Odstranění souboru z Git bez smazání z disku:
```bash
git rm --cached název_souboru.py
```

### **14. Zobrazení rozdílů mezi změnami**
Zobrazení změn ve srovnání s posledním commitem:
```bash
git diff
```

---

Tento cheat sheet pokrývá základní příkazy, které ti pomohou efektivně pracovat s Git a GitHubem.
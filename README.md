# ZK_JachymCernik

Caesar cypher: 
Tento kód implementuje Caesarovu šifru,  kde je každé písmeno v otevřeném textu posunuto o určitý počet míst v abecedním indexu. V této šifře se posun a velikost posunu (key) určuje podle zadání uživatele. Funkce 'crypting' se stará o posun písmen, zatímco funkce 'printMenu' se stará o interakci s uživatelem. Hlavní skript vše spojuje dohromady. V kódu se nacházejí  2 globální proměnné 'encrypting' a 'decrypting' k určení, zda se má zpráva zašifrovat nebo dešifrovat. Tyto proměnné jsou nastaveny v hlavním skriptu na základě volby uživatele.

password generator: 
 Kód obsahuje několik funkcí, které vybírají znaky z předdefinovaných seznamů a přidávají je do prázdného seznamu hesel. Pick letter, number a další. Poté je seznam hesel sloučen do řetězce pomocí funkce mergeList. Funkce randomizer přijímá délku hesla jako parametr a zajišťuje, že heslo bude obsahovat alespoň jeden znak z každého typu. Kód také používá modul random k vygenerování náhodných indexů a čísel

from services.perpustakaan_service import PerpustakaanService
from ui.console_menu import UI

def main():
    print("=========================================")
    print("     SISTEM INFORMASI PERPUSTAKAAN       ")
    print("=========================================\n")
    
    #untuk service perpustakaan
    service = PerpustakaanService()
    #untuk menu 
    menu_aplikasi = UI(service=service)
    
    try:
        menu_aplikasi.jalankan()
    except KeyboardInterrupt:
        print("\n\n[INFO] Program dihentikan paksa. Sampai jumpa!")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan pada sistem: {e}")

if __name__ == "__main__":
    main()
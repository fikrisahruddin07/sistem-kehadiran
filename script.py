import os

def test():
    filename = "index.html"

    # Semak kewujudan fail HTML
    if os.path.exists(filename):
        print("Fail index.html wujud.")

        # Baca kandungan fail
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

            # Semak kewujudan fungsi alert()
            if "alert(" in content:
                print("Fungsi alert() dijumpai dalam index.html.")
            else:
                print("Fungsi alert() TIDAK dijumpai.")
    else:
        print("Fail index.html TIDAK wujud.")

# Panggil fungsi
test()
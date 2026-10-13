"""Sitenin dışarıya verdiği kaynak kod adresi — TEK yerde durur.

build.py ve guide.py buradan okur (guide.py build.py tarafından içe
aktarıldığı için sabit build.py'de tutulamaz: döngüsel içe aktarma olurdu).
Depo taşınırsa yalnız bu satır değişir, sonra `python3 build.py`.
"""

GITHUB = "https://github.com/sekuvo/sekuvo"

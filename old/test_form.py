from fdfgen import forge_fdf
import subprocess

# pkgs_1, pkgs_2, pkgs_3, description_1, description_2, description_3, invoice_no, PO_no, RR_no,
# freight, quantity_1, quantity_2, quantity_3, rate_1, rate_2, rate_3, unit_1, unit_2, unit_3,
# amount_1, amount_2, amount_3, paise_1, paise_2, paise_3, total, total_paise,

fields = [('invoice_no','1'),('PO_no','1'), ('description_1','Some long item description'),('quantity_1','12'),('amount_1','23234'),('paise_1','1'),('unit_1','per kg'),('quantity_1','21'),('total','12321')]
fdf = forge_fdf("",fields,[],[],[])
fdf_file = open("data.fdf","wb")
fdf_file.write(fdf)
fdf_file.close()


subprocess.run(['pdftk', 'test.pdf', 'fill_form', 'data.fdf', 'output', 'output.pdf', 'flatten'])

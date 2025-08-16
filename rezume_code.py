from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Sarlavha
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Rezyume", ln=True, align="C")

# Shaxsiy ma'lumotlar
pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(0, 10, "Shaxsiy Ma'lumotlar:", ln=True)
pdf.cell(0, 10, "Ism-sharif: Mutalov Abdulaziz", ln=True)
pdf.cell(0, 10, "Tug'ilgan sana: 12-04-2008", ln=True)
pdf.cell(0, 10, "Telefon raqami: +99891120826", ln=True)
pdf.cell(0, 10, "Email: mtosh662@gmail.com", ln=True)
pdf.multi_cell(0, 10, "Yashash manzili: Shayxontohur tuman, Komolon mahallasi, Gulirano prayezi 8")

# Kasbiy maqsad
pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Kasbiy Maqsad:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Yo'nalish: Dasturchi", ln=True)
pdf.cell(0, 10, "Lavozim: Mvjud emas", ln=True)

# Ta'lim
pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Ta'lim:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "O'quv yurti: O'zbekiston", ln=True)
pdf.cell(0, 10, "O'qish boshlangan: Fevral, 2025", ln=True)
pdf.cell(0, 10, "O'qish tugagan: Sentabr, 2025", ln=True)
pdf.cell(0, 10, "Mutaxassislik: Juni (junior dasturchi)", ln=True)

# Tajriba
pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Ish Tajribasi:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Tajriba: Mavjud emas", ln=True)

# Ko‘nikmalar
pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Ko'nikmalar:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Kompyuter dasturlari: Python", ln=True)
pdf.cell(0, 10, "Til bilimi: Rus tili (B2), Ingliz tili (A2)", ln=True)
pdf.cell(0, 10, "Boshqa ko'nikmalar: Hozircha mavjud emas", ln=True)

# Faylni saqlash
pdf.output("Mutalov_Abdulaziz_Rezyume.pdf")

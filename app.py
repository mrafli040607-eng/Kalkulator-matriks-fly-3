import streamlit as st
import numpy as np
import pandas as pd


# =========================================================
# KONFIGURASI
# =========================================================

st.set_page_config(
    page_title="Kalkulator Matriks",
    page_icon="🔢",
    layout="centered"
)


# =========================================================
# JUDUL
# =========================================================

st.title("🔢 Kalkulator Matriks")

st.write(
    "Kalkulator matriks menggunakan Python, "
    "NumPy, Pandas, dan Streamlit."
)

st.divider()


# =========================================================
# FUNGSI FORMAT ANGKA
# =========================================================

def format_angka(nilai):

    if abs(nilai - round(nilai)) < 1e-10:
        return str(int(round(nilai)))

    return f"{nilai:.4f}"


# =========================================================
# FUNGSI INPUT MATRIKS
# =========================================================

def input_matriks(nama, baris, kolom, key):

    st.subheader(nama)

    data_awal = np.zeros(
        (baris, kolom),
        dtype=float
    )

    data = pd.DataFrame(
        data_awal,
        index=[
            f"Baris {i + 1}"
            for i in range(baris)
        ],
        columns=[
            f"Kolom {j + 1}"
            for j in range(kolom)
        ]
    )

    hasil_input = st.data_editor(
        data,
        key=key,
        use_container_width=True,
        num_rows="fixed"
    )

    return hasil_input.to_numpy(dtype=float)


# =========================================================
# FUNGSI MENAMPILKAN MATRIKS
# =========================================================

def tampilkan_matriks(A):

    df = pd.DataFrame(
        A,
        index=[
            f"Baris {i + 1}"
            for i in range(A.shape[0])
        ],
        columns=[
            f"Kolom {j + 1}"
            for j in range(A.shape[1])
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )


# =========================================================
# FUNGSI LANGKAH PENJUMLAHAN
# =========================================================

def langkah_penjumlahan(A, B):

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Setiap elemen pada Matriks A dijumlahkan "
        "dengan elemen Matriks B pada posisi yang sama."
    )

    for i in range(A.shape[0]):

        for j in range(A.shape[1]):

            hasil = A[i, j] + B[i, j]

            st.write(
                "C[{},{}] = {} + {} = {}".format(
                    i + 1,
                    j + 1,
                    format_angka(A[i, j]),
                    format_angka(B[i, j]),
                    format_angka(hasil)
                )
            )


# =========================================================
# FUNGSI LANGKAH PENGURANGAN
# =========================================================

def langkah_pengurangan(A, B):

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Setiap elemen pada Matriks A dikurangi "
        "dengan elemen Matriks B pada posisi yang sama."
    )

    for i in range(A.shape[0]):

        for j in range(A.shape[1]):

            hasil = A[i, j] - B[i, j]

            st.write(
                "C[{},{}] = {} - {} = {}".format(
                    i + 1,
                    j + 1,
                    format_angka(A[i, j]),
                    format_angka(B[i, j]),
                    format_angka(hasil)
                )
            )


# =========================================================
# FUNGSI LANGKAH PERKALIAN
# =========================================================

def langkah_perkalian(A, B):

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Setiap elemen hasil diperoleh dari "
        "perkalian baris Matriks A dengan kolom Matriks B."
    )

    hasil = A @ B

    for i in range(A.shape[0]):

        for j in range(B.shape[1]):

            bagian = []

            for k in range(A.shape[1]):

                bagian.append(
                    "({} × {})".format(
                        format_angka(A[i, k]),
                        format_angka(B[k, j])
                    )
                )

            ekspresi = " + ".join(bagian)

            st.write(
                "C[{},{}] = {} = {}".format(
                    i + 1,
                    j + 1,
                    ekspresi,
                    format_angka(hasil[i, j])
                )
            )


# =========================================================
# FUNGSI LANGKAH TRANSPOSE
# =========================================================

def langkah_transpose(A):

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Transpose dilakukan dengan mengubah setiap "
        "baris menjadi kolom."
    )

    st.write(
        "Ukuran awal Matriks A: {} × {}".format(
            A.shape[0],
            A.shape[1]
        )
    )

    st.write(
        "Ukuran setelah transpose: {} × {}".format(
            A.shape[1],
            A.shape[0]
        )
    )


# =========================================================
# FUNGSI DETERMINAN 2x2
# =========================================================

def determinan_2x2(A):

    a = A[0, 0]
    b = A[0, 1]
    c = A[1, 0]
    d = A[1, 1]

    hasil = (a * d) - (b * c)

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Untuk matriks 2 × 2 digunakan rumus:"
    )

    st.write(
        "det(A) = (a × d) - (b × c)"
    )

    st.write(
        "det(A) = ({} × {}) - ({} × {})".format(
            format_angka(a),
            format_angka(d),
            format_angka(b),
            format_angka(c)
        )
    )

    st.write(
        "det(A) = {} - {}".format(
            format_angka(a * d),
            format_angka(b * c)
        )
    )

    st.write(
        "det(A) = {}".format(
            format_angka(hasil)
        )
    )

    return hasil


# =========================================================
# FUNGSI DETERMINAN 3x3
# =========================================================

def determinan_3x3(A):

    a = A[0, 0]
    b = A[0, 1]
    c = A[0, 2]

    d = A[1, 0]
    e = A[1, 1]
    f = A[1, 2]

    g = A[2, 0]
    h = A[2, 1]
    i = A[2, 2]

    bagian1 = a * ((e * i) - (f * h))
    bagian2 = b * ((d * i) - (f * g))
    bagian3 = c * ((d * h) - (e * g))

    hasil = bagian1 - bagian2 + bagian3

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Menggunakan ekspansi kofaktor baris pertama."
    )

    st.write(
        "det(A) = a(ei − fh) − b(di − fg) + c(dh − eg)"
    )

    st.write(
        "Bagian pertama = {}".format(
            format_angka(bagian1)
        )
    )

    st.write(
        "Bagian kedua = {}".format(
            format_angka(bagian2)
        )
    )

    st.write(
        "Bagian ketiga = {}".format(
            format_angka(bagian3)
        )
    )

    st.write(
        "det(A) = {} − {} + {} = {}".format(
            format_angka(bagian1),
            format_angka(bagian2),
            format_angka(bagian3),
            format_angka(hasil)
        )
    )

    return hasil


# =========================================================
# FUNGSI INVERS 2x2
# =========================================================

def invers_2x2(A):

    a = A[0, 0]
    b = A[0, 1]
    c = A[1, 0]
    d = A[1, 1]

    det = (a * d) - (b * c)

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Rumus invers matriks 2 × 2:"
    )

    st.write(
        "A⁻¹ = 1/(ad − bc) × "
        "[ d  −b ; −c  a ]"
    )

    st.write(
        "det(A) = ({} × {}) − ({} × {}) = {}".format(
            format_angka(a),
            format_angka(d),
            format_angka(b),
            format_angka(c),
            format_angka(det)
        )
    )

    if abs(det) < 1e-10:

        st.error(
            "Determinan = 0. Matriks tidak mempunyai invers."
        )

        return None

    hasil = np.linalg.inv(A)

    st.write(
        "Karena determinan tidak sama dengan 0, "
        "maka matriks mempunyai invers."
    )

    st.write("Hasil invers:")

    tampilkan_matriks(hasil)

    return hasil


# =========================================================
# PILIH OPERASI
# =========================================================

operasi = st.selectbox(
    "⚙️ Pilih Operasi",
    [
        "Penjumlahan",
        "Pengurangan",
        "Perkalian",
        "Transpose",
        "Determinan",
        "Invers",
        "Rank",
        "Trace"
    ]
)


# =========================================================
# MATRIKS A
# =========================================================

st.divider()

st.header("Matriks A")

col_a1, col_a2 = st.columns(2)

with col_a1:

    baris_a = st.number_input(
        "Baris A",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )

with col_a2:

    kolom_a = st.number_input(
        "Kolom A",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )


A = input_matriks(
    "Masukkan nilai Matriks A",
    int(baris_a),
    int(kolom_a),
    "matriks_A"
)


# =========================================================
# MATRIKS B
# =========================================================

B = None

if operasi in [
    "Penjumlahan",
    "Pengurangan",
    "Perkalian"
]:

    st.divider()

    st.header("Matriks B")

    col_b1, col_b2 = st.columns(2)

    with col_b1:

        baris_b = st.number_input(
            "Baris B",
            min_value=1,
            max_value=10,
            value=2,
            step=1
        )

    with col_b2:

        kolom_b = st.number_input(
            "Kolom B",
            min_value=1,
            max_value=10,
            value=2,
            step=1
        )

    B = input_matriks(
        "Masukkan nilai Matriks B",
        int(baris_b),
        int(kolom_b),
        "matriks_B"
    )


# =========================================================
# TOMBOL HITUNG
# =========================================================

st.divider()

hitung = st.button(
    "🔢 HITUNG",
    type="primary",
    use_container_width=True
)


# =========================================================
# PERHITUNGAN
# =========================================================

if hitung:

    # -----------------------------------------------------
    # PENJUMLAHAN
    # -----------------------------------------------------

    if operasi == "Penjumlahan":

        if A.shape != B.shape:

            st.error(
                "Penjumlahan tidak dapat dilakukan."
            )

            st.write(
                "Ukuran A = {} × {}".format(
                    A.shape[0],
                    A.shape[1]
                )
            )

            st.write(
                "Ukuran B = {} × {}".format(
                    B.shape[0],
                    B.shape[1]
                )
            )

            st.warning(
                "Syarat: ukuran Matriks A dan B harus sama."
            )

        else:

            hasil = A + B

            st.success(
                "Penjumlahan berhasil!"
            )

            st.subheader("📊 Hasil")

            tampilkan_matriks(hasil)

            langkah_penjumlahan(A, B)


    # -----------------------------------------------------
    # PENGURANGAN
    # -----------------------------------------------------

    elif operasi == "Pengurangan":

        if A.shape != B.shape:

            st.error(
                "Pengurangan tidak dapat dilakukan."
            )

            st.warning(
                "Syarat: ukuran Matriks A dan B harus sama."
            )

        else:

            hasil = A - B

            st.success(
                "Pengurangan berhasil!"
            )

            st.subheader("📊 Hasil")

            tampilkan_matriks(hasil)

            langkah_pengurangan(A, B)


    # -----------------------------------------------------
    # PERKALIAN
    # -----------------------------------------------------

    elif operasi == "Perkalian":

        if A.shape[1] != B.shape[0]:

            st.error(
                "Perkalian tidak dapat dilakukan."
            )

            st.write(
                "Jumlah kolom A = {}".format(
                    A.shape[1]
                )
            )

            st.write(
                "Jumlah baris B = {}".format(
                    B.shape[0]
                )
            )

            st.warning(
                "Syarat perkalian: "
                "jumlah kolom A harus sama "
                "dengan jumlah baris B."
            )

        else:

            hasil = A @ B

            st.success(
                "Perkalian berhasil!"
            )

            st.subheader("📊 Hasil")

            tampilkan_matriks(hasil)

            st.write(
                "Ukuran hasil = {} × {}".format(
                    hasil.shape[0],
                    hasil.shape[1]
                )
            )

            langkah_perkalian(A, B)


    # -----------------------------------------------------
    # TRANSPOSE
    # -----------------------------------------------------

    elif operasi == "Transpose":

        hasil = A.T

        st.success(
            "Transpose berhasil!"
        )

        st.subheader("📊 Hasil")

        tampilkan_matriks(hasil)

        langkah_transpose(A)


    # -----------------------------------------------------
    # DETERMINAN
    # -----------------------------------------------------

    elif operasi == "Determinan":

        if baris_a != kolom_a:

            st.error(
                "Determinan hanya dapat dihitung "
                "untuk matriks persegi."
            )

        elif baris_a == 2:

            hasil = determinan_2x2(A)

            st.subheader("📊 Hasil")

            st.write(
                "det(A) = {}".format(
                    format_angka(hasil)
                )
            )

        elif baris_a == 3:

            hasil = determinan_3x3(A)

            st.subheader("📊 Hasil")

            st.write(
                "det(A) = {}".format(
                    format_angka(hasil)
                )
            )

        else:

            hasil = np.linalg.det(A)

            st.subheader("📊 Hasil")

            st.write(
                "det(A) = {}".format(
                    format_angka(hasil)
                )
            )

            st.info(
                "Untuk matriks lebih dari 3 × 3, "
                "perhitungan dilakukan menggunakan NumPy."
            )


    # -----------------------------------------------------
    # INVERS
    # -----------------------------------------------------

    elif operasi == "Invers":

        if baris_a != kolom_a:

            st.error(
                "Invers hanya dapat dihitung "
                "untuk matriks persegi."
            )

        elif baris_a == 2:

            hasil = invers_2x2(A)

            if hasil is not None:

                st.subheader("📊 Hasil")

                tampilkan_matriks(hasil)

        else:

            determinan = np.linalg.det(A)

            if abs(determinan) < 1e-10:

                st.error(
                    "Matriks tidak mempunyai invers "
                    "karena determinannya = 0."
                )

            else:

                hasil = np.linalg.inv(A)

                st.subheader("📊 Hasil Invers")

                tampilkan_matriks(hasil)

                st.subheader(
                    "📖 Langkah Penyelesaian"
                )

                st.write(
                    "Matriks lebih dari 2 × 2 dihitung "
                    "menggunakan metode numerik."
                )


    # -----------------------------------------------------
    # RANK
    # -----------------------------------------------------

    elif operasi == "Rank":

        hasil = np.linalg.matrix_rank(A)

        st.subheader("📊 Hasil")

        st.write(
            "Rank(A) = {}".format(hasil)
        )

        st.subheader(
            "📖 Langkah Penyelesaian"
        )

        st.write(
            "Rank adalah jumlah maksimum baris "
            "atau kolom yang bebas linear."
        )

        st.write(
            "Pada aplikasi ini Rank dihitung "
            "menggunakan metode numerik NumPy."
        )


    # -----------------------------------------------------
    # TRACE
    # -----------------------------------------------------

    elif operasi == "Trace":

        if baris_a != kolom_a:

            st.error(
                "Trace hanya dapat dihitung "
                "untuk matriks persegi."
            )

        else:

            hasil = np.trace(A)

            st.subheader("📊 Hasil")

            st.write(
                "Tr(A) = {}".format(
                    format_angka(hasil)
                )
            )

            st.subheader(
                "📖 Langkah Penyelesaian"
            )

            st.write(
                "Trace diperoleh dengan menjumlahkan "
                "semua elemen pada diagonal utama."
            )

            diagonal = []

            for i in range(int(baris_a)):

                diagonal.append(
                    format_angka(A[i, i])
                )

            ekspresi = " + ".join(diagonal)

            st.write(
                "Tr(A) = {}".format(
                    ekspresi
                )
            )

            st.write(
                "Tr(A) = {}".format(
                    format_angka(hasil)
                )
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Kalkulator Matriks | "
    "Python + Streamlit + NumPy + Pandas"
    )warning(
                "Ukuran kedua matriks harus sama."
            )

        else:

            hasil = A + B

            st.success(
                "Penjumlahan berhasil!"
            )

            st.subheader("📊 Hasil")

            tampilkan_matriks(hasil)

            langkah_penjumlahan(A, B)


    # =====================================================
    # PENGURANGAN
    # =====================================================

    elif operasi == "Pengurangan":

        if A.shape != B.shape:

            st.error(
                "Pengurangan tidak dapat dilakukan."
            )

            st.warning(
                "Ukuran kedua matriks harus sama."
            )

        else:

            hasil = A - B

            st.success(
                "Pengurangan berhasil!"
            )

            st.subheader("📊 Hasil")

            tampilkan_matriks(hasil)

            langkah_pengurangan(A, B)


    # =====================================================
    # PERKALIAN
    # =====================================================

    elif operasi == "Perkalian":

        if A.shape[1] != B.shape[0]:

            st.error(
                "Perkalian tidak dapat dilakukan."
            )

            st.write(
                f"Kolom A = {A.shape[1]}"
            )

            st.write(
                f"Baris B = {B.shape[0]}"
            )

            st.warning(
                "Syarat perkalian: "
                "kolom A = baris B."
            )

        else:

            hasil = A @ B

            st.success(
                "Perkalian berhasil!"
            )

            st.subheader("📊 Hasil")

            tampilkan_matriks(hasil)

            langkah_perkalian(A, B)


    # =====================================================
    # TRANSPOSE
    # =====================================================

    elif operasi == "Transpose":

        hasil = A.T

        st.success(
            "Transpose berhasil!"
        )

        st.subheader("📊 Hasil Transpose")

        tampilkan_matriks(hasil)

        st.subheader("📖 Langkah Penyelesaian")

        st.write(
            "Transpose dilakukan dengan menukar "
            "baris menjadi kolom."
        )

        st.write(
            f"Ukuran awal: "
            f"{A.shape[0]} × {A.shape[1]}"
        )

        st.write(
            f"Ukuran setelah transpose: "
            f"{hasil.shape[0]} × {hasil.shape[1]}"
        )


    # =====================================================
    # DETERMINAN
    # =====================================================

    elif operasi == "Determinan":

        if baris_a != kolom_a:

            st.error(
                "Determinan hanya dapat dihitung "
                "untuk matriks persegi."
            )

        elif baris_a == 2:

            hasil = langkah_determinan_2x2(A)

        elif baris_a == 3:

            hasil = langkah_determinan_3x3(A)

        else:

            hasil = np.linalg.det(A)

            st.subheader("📊 Hasil")

            st.write(
                f"det(A) = {hasil:.6f}"
            )

            st.info(
                "Untuk matriks lebih dari 3 × 3, "
                "hasil dihitung menggunakan NumPy. "
                "Versi berikutnya dapat kita tambahkan "
                "langkah eliminasi atau ekspansi kofaktor."
            )


    # =====================================================
    # INVERS
    # =====================================================

    elif operasi == "Invers":

        if baris_a != kolom_a:

            st.error(
                "Invers hanya dapat dihitung "
                "untuk matriks persegi."
            )

        elif baris_a == 2:

            langkah_invers_2x2(A)

        else:

            det = np.linalg.det(A)

            if abs(det) < 1e-10:

                st.error(
                    "Matriks tidak memiliki invers "
                    "karena determinannya = 0."
                )

            else:

                hasil = np.linalg.inv(A)

                st.subheader("📊 Hasil Invers")

                tampilkan_matriks(hasil)

                st.subheader(
                    "📖 Langkah Penyelesaian"
                )

                st.write(
                    "Matriks lebih dari 2 × 2 "
                    "dihitung menggunakan metode "
                    "invers numerik."
                )


    # =====================================================
    # RANK
    # =====================================================

    elif operasi == "Rank":

        hasil = np.linalg.matrix_rank(A)

        st.subheader("📊 Hasil")

        st.write(
            f"Rank(A) = {hasil}"
        )

        st.subheader(
            "📖 Langkah Penyelesaian"
        )

        st.write(
            "Rank matriks ditentukan berdasarkan "
            "jumlah baris atau kolom yang bebas linear."
        )

        st.write(
            "Pada implementasi ini, Rank dihitung "
            "menggunakan algoritma numerik NumPy."
        )


    # =====================================================
    # TRACE
    # =====================================================

    elif operasi == "Trace":

        if baris_a != kolom_a:

            st.error(
                "Trace hanya dapat dihitung "
                "untuk matriks persegi."
            )

        else:

            hasil = np.trace(A)

            st.subheader("📊 Hasil")

            st.write(
                f"Tr(A) = {angka(hasil)}"
            )

            st.subheader(
                "📖 Langkah Penyelesaian"
            )

            diagonal = []

            for i in range(baris_a):

                diagonal.append(
                    angka(A[i, i])
                )

            ekspresi = " + ".join(diagonal)

            st.latex(
                rf"""
                Tr(A) = {ekspresi}
                """
            )

            st.latex(
                rf"""
                Tr(A) = {angka(hasil)}
                """
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Kalkulator Matriks | "
    "Python + Streamlit + NumPy + Pandas"
    st.subheader("📖 Langkah Penyelesaian")

st.write(
    "Trace diperoleh dengan menjumlahkan "
    "elemen pada diagonal utama."
)

diagonal = []

for i in range(int(baris_a)):
    diagonal.append(
        angka(A[i, i])
    )

ekspresi = " + ".join(diagonal)

st.latex(
    rf"Tr(A) = {ekspresi}"
)

st.latex(
    rf"Tr(A) = {angka(hasil)}"
    )
    )

    elemen = [
        A[i, i] for i in range(n)
    ]

    operasi = " + ".join(
        fmt(x) for x in elemen
    )

    hasil = np.trace(A)

    st.latex(
        rf"\operatorname{{Tr}}(A)"
        rf" = {operasi}"
    )

    st.latex(
        rf"\operatorname{{Tr}}(A)"
        rf" = {fmt(hasil)}"
    )


# =========================================================
# PILIH OPERASI
# =========================================================

operasi = st.selectbox(
    "Pilih Operasi Matriks",
    [
        "Penjumlahan",
        "Pengurangan",
        "Perkalian",
        "Transpose",
        "Determinan",
        "Invers",
        "Rank",
        "Trace"
    ]
)


# =========================================================
# UKURAN MATRIKS A
# =========================================================

st.divider()

st.header("Matriks A")

col_a1, col_a2 = st.columns(2)

with col_a1:

    baris_a = st.number_input(
        "Jumlah Baris A",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )

with col_a2:

    kolom_a = st.number_input(
        "Jumlah Kolom A",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )


# =========================================================
# INPUT MATRIKS A
# =========================================================

A = buat_matriks(
    "Input Matriks A",
    int(baris_a),
    int(kolom_a),
    "input_A"
)


# =========================================================
# MATRIKS B
# =========================================================

B = None

if operasi in [
    "Penjumlahan",
    "Pengurangan",
    "Perkalian"
]:

    st.divider()

    st.header("Matriks B")

    col_b1, col_b2 = st.columns(2)

    with col_b1:

        baris_b = st.number_input(
            "Jumlah Baris B",
            min_value=1,
            max_value=10,
            value=2,
            step=1
        )

    with col_b2:

        kolom_b = st.number_input(
            "Jumlah Kolom B",
            min_value=1,
            max_value=10,
            value=2,
            step=1
        )

    # -----------------------------------------------------
    # Informasi syarat operasi
    # -----------------------------------------------------

    if operasi == "Penjumlahan":

        st.info(
            "Syarat penjumlahan: ukuran Matriks A "
            "dan Matriks B harus sama."
        )

    elif operasi == "Pengurangan":

        st.info(
            "Syarat pengurangan: ukuran Matriks A "
            "dan Matriks B harus sama."
        )

    elif operasi == "Perkalian":

        st.info(
            "Syarat perkalian: jumlah kolom A harus "
            "sama dengan jumlah baris B."
        )

    # -----------------------------------------------------
    # INPUT MATRIKS B
    # -----------------------------------------------------

    B = buat_matriks(
        "Input Matriks B",
        int(baris_b),
        int(kolom_b),
        "input_B"
    )


# =========================================================
# TOMBOL HITUNG
# =========================================================

st.divider()

hitung = st.button(
    "🔢 HITUNG",
    type="primary",
    use_container_width=True
)


# =========================================================
# PERHITUNGAN
# =========================================================

if hitung:

    # =====================================================
    # PENJUMLAHAN
    # =====================================================

    if operasi == "Penjumlahan":

        if A.shape != B.shape:

            st.error(
                f"Penjumlahan tidak dapat dilakukan. "
                f"Ukuran A = {A.shape[0]}×{A.shape[1]}, "
                f"sedangkan ukuran B = "
                f"{B.shape[0]}×{B.shape[1]}."
            )

        else:

            langkah_penjumlahan(A, B)

            hasil = A + B

            st.success("Penjumlahan berhasil!")

            st.subheader("Hasil A + B")

            st.dataframe(
                tampilkan_matriks(hasil),
                use_container_width=True,
                hide_index=True
            )


    # =====================================================
    # PENGURANGAN
    # =====================================================

    elif operasi == "Pengurangan":

        if A.shape != B.shape:

            st.error(
                f"Pengurangan tidak dapat dilakukan. "
                f"Ukuran A = {A.shape[0]}×{A.shape[1]}, "
                f"sedangkan ukuran B = "
                f"{B.shape[0]}×{B.shape[1]}."
            )

        else:

            langkah_pengurangan(A, B)

            hasil = A - B

            st.success("Pengurangan berhasil!")

            st.subheader("Hasil A - B")

            st.dataframe(
                tampilkan_matriks(hasil),
                use_container_width=True,
                hide_index=True
            )


    # =====================================================
    # PERKALIAN
    # =====================================================

    elif operasi == "Perkalian":

        if A.shape[1] != B.shape[0]:

            st.error(
                "Perkalian tidak dapat dilakukan."
            )

            st.warning(
                f"Kolom A = {A.shape[1]}, "
                f"sedangkan baris B = {B.shape[0]}."
            )

            st.write(
                "Syarat perkalian adalah:"
            )

            st.latex(
                r"\text{kolom A} = \text{baris B}"
            )

        else:

            langkah_perkalian(A, B)

            hasil = A @ B

            st.success("Perkalian berhasil!")

            st.subheader("Hasil A × B")

            st.dataframe(
                tampilkan_matriks(hasil),
                use_container_width=True,
                hide_index=True
            )

            st.write(
                f"Ukuran hasil: "
                f"{hasil.shape[0]} × {hasil.shape[1]}"
            )


    # =====================================================
    # TRANSPOSE
    # =====================================================

    elif operasi == "Transpose":

        langkah_transpose(A)

        hasil = A.T

        st.success("Transpose berhasil!")

        st.subheader("Hasil Transpose Matriks A")

        st.dataframe(
            tampilkan_matriks(hasil),
            use_container_width=True,
            hide_index=True
        )

        st.write(
            f"Ukuran awal: "
            f"{A.shape[0]} × {A.shape[1]}"
        )

        st.write(
            f"Ukuran transpose: "
            f"{hasil.shape[0]} × {hasil.shape[1]}"
        )


    # =====================================================
    # DETERMINAN
    # =====================================================

    elif operasi == "Determinan":

        if baris_a != kolom_a:

            st.error(
                "Determinan hanya dapat dihitung "
                "untuk matriks persegi."
            )

            st.write(
                f"Ukuran Matriks A sekarang: "
                f"{int(baris_a)} × {int(kolom_a)}"
            )

        else:

            langkah_determinan(A)

            hasil = np.linalg.det(A)

            st.success(
                "Determinan berhasil dihitung!"
            )

            st.subheader("Hasil Determinan Matriks A")

            st.latex(
                rf"\det(A) = {hasil:.4f}"
            )


    # =====================================================
    # INVERS
    # =====================================================

    elif operasi == "Invers":

        if baris_a != kolom_a:

            st.error(
                "Invers hanya dapat dihitung "
                "untuk matriks persegi."
            )

        else:

            determinan = np.linalg.det(A)

            if abs(determinan) < 1e-10:

                st.error(
                    "Matriks A tidak mempunyai invers "
                    "karena determinannya = 0."
                )

            else:

                langkah_invers(A)

                hasil = np.linalg.inv(A)

                st.success(
                    "Invers Matriks A berhasil dihitung!"
                )

                st.subheader("Hasil A⁻¹")

                st.dataframe(
                    tampilkan_matriks(hasil),
                    use_container_width=True,
                    hide_index=True
                )


    # =====================================================
    # RANK
    # =====================================================

    elif operasi == "Rank":

        langkah_rank(A)

        hasil = np.linalg.matrix_rank(A)

        st.success("Rank berhasil dihitung!")

        st.subheader("Hasil Rank Matriks A")

        st.latex(
            rf"\operatorname{{rank}}(A) = {hasil}"
        )


    # =====================================================
    # TRACE
    # =====================================================

    elif operasi == "Trace":

        if baris_a != kolom_a:

            st.error(
                "Trace hanya dapat dihitung "
                "untuk matriks persegi."
            )

        else:

            langkah_trace(A)

            hasil = np.trace(A)

            st.success("Trace berhasil dihitung!")

            st.subheader("Hasil Trace Matriks A")

            st.latex(
                rf"\operatorname{{Tr}}(A) = {hasil:g}"
            )


# =========================================================
# INFORMASI APLIKASI
# =========================================================

st.divider()

st.caption(
    "Kalkulator Matriks | Python + Streamlit + NumPy + Pandas"
){{Tr}}(A) = {hasil:g}"
            )


# =========================================================
# INFORMASI APLIKASI
# =========================================================

st.divider()

st.caption(
    "Kalkulator Matriks | Python + Streamlit + NumPy + Pandas"
)

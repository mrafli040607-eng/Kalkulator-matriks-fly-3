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

st.title("🔢 Kalkulator Matriks")

st.write(
    "Kalkulator matriks berbasis Python untuk menghitung "
    "operasi matriks dan menampilkan langkah penyelesaian."
)

st.divider()


# =========================================================
# FUNGSI INPUT MATRIKS
# =========================================================

def buat_matriks(nama, baris, kolom, key):

    st.subheader(nama)

    data_awal = np.zeros((baris, kolom))

    nama_baris = [
        f"Baris {i + 1}"
        for i in range(baris)
    ]

    nama_kolom = [
        f"Kolom {j + 1}"
        for j in range(kolom)
    ]

    dataframe_awal = pd.DataFrame(
        data_awal,
        index=nama_baris,
        columns=nama_kolom
    )

    data = st.data_editor(
        dataframe_awal,
        key=key,
        use_container_width=True,
        num_rows="fixed"
    )

    return data.to_numpy(dtype=float)


# =========================================================
# FUNGSI FORMAT ANGKA
# =========================================================

def angka(nilai):

    if abs(nilai - round(nilai)) < 1e-10:
        return str(int(round(nilai)))

    return f"{nilai:.4f}"


# =========================================================
# FUNGSI MENAMPILKAN MATRIKS
# =========================================================

def tampilkan_matriks(matriks):

    df = pd.DataFrame(
        matriks,
        index=[
            f"Baris {i + 1}"
            for i in range(matriks.shape[0])
        ],
        columns=[
            f"Kolom {j + 1}"
            for j in range(matriks.shape[1])
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
        "Penjumlahan dilakukan dengan menjumlahkan "
        "elemen yang berada pada posisi yang sama."
    )

    for i in range(A.shape[0]):

        for j in range(A.shape[1]):

            hasil = A[i, j] + B[i, j]

            st.write(
                f"C[{i+1},{j+1}] = "
                f"{angka(A[i,j])} + {angka(B[i,j])} "
                f"= {angka(hasil)}"
            )


# =========================================================
# FUNGSI LANGKAH PENGURANGAN
# =========================================================

def langkah_pengurangan(A, B):

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Pengurangan dilakukan dengan mengurangkan "
        "elemen yang berada pada posisi yang sama."
    )

    for i in range(A.shape[0]):

        for j in range(A.shape[1]):

            hasil = A[i, j] - B[i, j]

            st.write(
                f"C[{i+1},{j+1}] = "
                f"{angka(A[i,j])} - {angka(B[i,j])} "
                f"= {angka(hasil)}"
            )


# =========================================================
# FUNGSI LANGKAH PERKALIAN
# =========================================================

def langkah_perkalian(A, B):

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Perkalian matriks dilakukan dengan mengalikan "
        "setiap baris Matriks A dengan setiap kolom Matriks B."
    )

    hasil = A @ B

    for i in range(A.shape[0]):

        for j in range(B.shape[1]):

            bagian = []

            for k in range(A.shape[1]):

                bagian.append(
                    f"({angka(A[i,k])} × {angka(B[k,j])})"
                )

            ekspresi = " + ".join(bagian)

            st.write(
                f"C[{i+1},{j+1}] = "
                f"{ekspresi} "
                f"= {angka(hasil[i,j])}"
            )


# =========================================================
# FUNGSI DETERMINAN 2×2
# =========================================================

def langkah_determinan_2x2(A):

    a = A[0, 0]
    b = A[0, 1]
    c = A[1, 0]
    d = A[1, 1]

    hasil = (a * d) - (b * c)

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Untuk matriks 2 × 2:"
    )

    st.latex(
        r"""
        A =
        \begin{bmatrix}
        a & b\\
        c & d
        \end{bmatrix}
        """
    )

    st.latex(
        r"\det(A) = (a\times d)-(b\times c)"
    )

    st.latex(
        rf"""
        \det(A)
        =
        ({angka(a)}\times{angka(d)})
        -
        ({angka(b)}\times{angka(c)})
        """
    )

    st.latex(
        rf"""
        = {angka(a*d)} - {angka(b*c)}
        """
    )

    st.latex(
        rf"""
        = \boxed{{{angka(hasil)}}}
        """
    )

    return hasil


# =========================================================
# FUNGSI DETERMINAN 3×3
# =========================================================

def langkah_determinan_3x3(A):

    a = A[0, 0]
    b = A[0, 1]
    c = A[0, 2]

    d = A[1, 0]
    e = A[1, 1]
    f = A[1, 2]

    g = A[2, 0]
    h = A[2, 1]
    i = A[2, 2]

    hasil = (
        a * (e*i - f*h)
        - b * (d*i - f*g)
        + c * (d*h - e*g)
    )

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Menggunakan ekspansi kofaktor baris pertama:"
    )

    st.latex(
        r"""
        \det(A)
        =
        a(ei-fh)
        -
        b(di-fg)
        +
        c(dh-eg)
        """
    )

    st.latex(
        rf"""
        =
        {angka(a)}
        ({angka(e)}\times{angka(i)}
        -
        {angka(f)}\times{angka(h)})
        -
        {angka(b)}
        ({angka(d)}\times{angka(i)}
        -
        {angka(f)}\times{angka(g)})
        +
        {angka(c)}
        ({angka(d)}\times{angka(h)}
        -
        {angka(e)}\times{angka(g)})
        """
    )

    st.latex(
        rf"""
        \boxed{{\det(A)={angka(hasil)}}}
        """
    )

    return hasil


# =========================================================
# FUNGSI INVERS 2×2
# =========================================================

def langkah_invers_2x2(A):

    a = A[0, 0]
    b = A[0, 1]
    c = A[1, 0]
    d = A[1, 1]

    det = (a * d) - (b * c)

    st.subheader("📖 Langkah Penyelesaian")

    st.write(
        "Rumus invers matriks 2 × 2:"
    )

    st.latex(
        r"""
        A^{-1}
        =
        \frac{1}{ad-bc}
        \begin{bmatrix}
        d & -b\\
        -c & a
        \end{bmatrix}
        """
    )

    st.latex(
        rf"""
        \det(A)
        =
        ({angka(a)}\times{angka(d)})
        -
        ({angka(b)}\times{angka(c)})
        =
        {angka(det)}
        """
    )

    if abs(det) < 1e-10:

        st.error(
            "Determinan = 0, sehingga matriks "
            "tidak memiliki invers."
        )

        return None

    hasil = np.linalg.inv(A)

    st.latex(
        rf"""
        A^{{-1}}
        =
        \frac{{1}}{{{angka(det)}}}
        \begin{{bmatrix}}
        {angka(d)} & {-angka(b)}\\
        {-angka(c)} & {angka(a)}
        \end{{bmatrix}}
        """
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


A = buat_matriks(
    "Masukkan Matriks A",
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

    B = buat_matriks(
        "Masukkan Matriks B",
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
# PROSES PERHITUNGAN
# =========================================================

if hitung:

    # =====================================================
    # PENJUMLAHAN
    # =====================================================

    if operasi == "Penjumlahan":

        if A.shape != B.shape:

            st.error(
                "Penjumlahan tidak dapat dilakukan."
            )

            st.write(
                f"Ukuran A = {A.shape[0]} × {A.shape[1]}"
            )

            st.write(
                f"Ukuran B = {B.shape[0]} × {B.shape[1]}"
            )

            st.warning(
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
    )emen pada diagonal utama."
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

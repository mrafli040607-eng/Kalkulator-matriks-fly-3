import streamlit as st
import numpy as np
import pandas as pd

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================

st.set_page_config(
    page_title="Kalkulator Matriks",
    page_icon="🔢",
    layout="centered"
)

st.title("🔢 Kalkulator Matriks")
st.write(
    "Aplikasi untuk menghitung operasi dasar matriks "
    "menggunakan Python."
)

st.divider()


# =========================================================
# FUNGSI MEMBUAT INPUT MATRIKS
# =========================================================

def buat_matriks(nama, baris, kolom, key):

    st.subheader(nama)

    # Membuat matriks awal berisi angka 0
    data_awal = np.zeros((baris, kolom))

    # Nama baris dan kolom
    nama_baris = [f"Baris {i + 1}" for i in range(baris)]
    nama_kolom = [f"Kolom {j + 1}" for j in range(kolom)]

    dataframe_awal = pd.DataFrame(
        data_awal,
        index=nama_baris,
        columns=nama_kolom
    )

    # Tabel yang dapat diedit
    data = st.data_editor(
        dataframe_awal,
        key=key,
        use_container_width=True,
        num_rows="fixed"
    )

    return data.to_numpy(dtype=float)


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
                f"sedangkan ukuran B = {B.shape[0]}×{B.shape[1]}."
            )

        else:

            hasil = A + B

            st.success("Penjumlahan berhasil!")

            st.subheader("Hasil A + B")

            st.dataframe(
                pd.DataFrame(hasil),
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
                f"sedangkan ukuran B = {B.shape[0]}×{B.shape[1]}."
            )

        else:

            hasil = A - B

            st.success("Pengurangan berhasil!")

            st.subheader("Hasil A - B")

            st.dataframe(
                pd.DataFrame(hasil),
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

            hasil = A @ B

            st.success("Perkalian berhasil!")

            st.subheader("Hasil A × B")

            st.dataframe(
                pd.DataFrame(hasil),
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

        hasil = A.T

        st.success("Transpose berhasil!")

        st.subheader("Transpose Matriks A")

        st.dataframe(
            pd.DataFrame(hasil),
            use_container_width=True,
            hide_index=True
        )

        st.write(
            f"Ukuran awal: {A.shape[0]} × {A.shape[1]}"
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

            hasil = np.linalg.det(A)

            st.success(
                "Determinan berhasil dihitung!"
            )

            st.subheader("Determinan Matriks A")

            st.write(
                f"Ukuran A = "
                f"{int(baris_a)} × {int(kolom_a)}"
            )

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

                hasil = np.linalg.inv(A)

                st.success(
                    "Invers Matriks A berhasil dihitung!"
                )

                st.subheader("A⁻¹")

                st.dataframe(
                    pd.DataFrame(hasil),
                    use_container_width=True,
                    hide_index=True
                )


    # =====================================================
    # RANK
    # =====================================================

    elif operasi == "Rank":

        hasil = np.linalg.matrix_rank(A)

        st.success("Rank berhasil dihitung!")

        st.subheader("Rank Matriks A")

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

            hasil = np.trace(A)

            st.success("Trace berhasil dihitung!")

            st.subheader("Trace Matriks A")

            st.latex(
                rf"\operatorname{{Tr}}(A) = {hasil:g}"
            )


# =========================================================
# INFORMASI APLIKASI
# =========================================================

st.divider()

st.caption(
    "Kalkulator Matriks | Python + Streamlit + NumPy + Pandas"
    ):

    # =====================================================
    # PENJUMLAHAN
    # =====================================================

    if operasi == "Penjumlahan":

        if A.shape != B.shape:

            st.error(
                "Penjumlahan tidak dapat dilakukan "
                "karena ukuran matriks berbeda."
            )

        else:

            hasil = A + B

            st.success(
                "Penjumlahan berhasil!"
            )

            st.subheader(
                "📚 Langkah Perhitungan"
            )

            latex_matrix(A, "A")
            latex_matrix(B, "B")

            st.write(
                "Setiap elemen A dijumlahkan "
                "dengan elemen B yang bersesuaian."
            )

            for i in range(A.shape[0]):

                for j in range(A.shape[1]):

                    st.latex(
                        rf"c_{{{i+1},{j+1}}}"
                        rf"="
                        rf"{fmt(A[i,j])}"
                        rf"+"
                        rf"{fmt(B[i,j])}"
                        rf"="
                        rf"{fmt(hasil[i,j])}"
                    )

            st.subheader("Hasil")

            latex_matrix(
                hasil,
                "A+B"
            )


    # =====================================================
    # PENGURANGAN
    # =====================================================

    elif operasi == "Pengurangan":

        if A.shape != B.shape:

            st.error(
                "Pengurangan tidak dapat dilakukan "
                "karena ukuran matriks berbeda."
            )

        else:

            hasil = A - B

            st.success(
                "Pengurangan berhasil!"
            )

            st.subheader(
                "📚 Langkah Perhitungan"
            )

            latex_matrix(A, "A")
            latex_matrix(B, "B")

            for i in range(A.shape[0]):

                for j in range(A.shape[1]):

                    st.latex(
                        rf"c_{{{i+1},{j+1}}}"
                        rf"="
                        rf"{fmt(A[i,j])}"
                        rf"-"
                        rf"{fmt(B[i,j])}"
                        rf"="
                        rf"{fmt(hasil[i,j])}"
                    )

            st.subheader("Hasil")

            latex_matrix(
                hasil,
                "A-B"
            )


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

            st.latex(
                r"""
                \text{Kolom A}
                \neq
                \text{Baris B}
                """
            )

        else:

            hasil = A @ B

            st.success(
                "Perkalian berhasil!"
            )

            st.subheader(
                "📚 Langkah Perhitungan"
            )

            st.write(
                f"A berukuran "
                f"{A.shape[0]} × {A.shape[1]}"
            )

            st.write(
                f"B berukuran "
                f"{B.shape[0]} × {B.shape[1]}"
            )

            st.write(
                "Setiap elemen hasil diperoleh "
                "dari perkalian baris A dengan "
                "kolom B."
            )

            for i in range(A.shape[0]):

                for j in range(B.shape[1]):

                    bagian = []

                    for k in range(A.shape[1]):

                        bagian.append(
                            f"({fmt(A[i,k])})"
                            f"({fmt(B[k,j])})"
                        )

                    persamaan = "+".join(
                        bagian
                    )

                    st.latex(
                        rf"c_{{{i+1},{j+1}}}"
                        rf"="
                        rf"{persamaan}"
                        rf"="
                        rf"{fmt(hasil[i,j])}"
                    )

            st.subheader("Hasil")

            latex_matrix(
                hasil,
                "AB"
            )


    # =====================================================
    # TRANSPOSE
    # =====================================================

    elif operasi == "Transpose":

        hasil = A.T

        st.success(
            "Transpose berhasil!"
        )

        st.subheader(
            "📚 Langkah Perhitungan"
        )

        latex_matrix(A, "A")

        st.write(
            "Transpose dilakukan dengan "
            "mengubah baris menjadi kolom."
        )

        for i in range(A.shape[0]):

            for j in range(A.shape[1]):

                st.latex(
                    rf"a_{{{i+1},{j+1}}}"
                    rf"\rightarrow"
                    rf"a^T_{{{j+1},{i+1}}}"
                    rf"="
                    rf"{fmt(A[i,j])}"
                )

        st.subheader("Hasil")

        latex_matrix(
            hasil,
            "A^T"
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

        else:

            n = A.shape[0]

            st.subheader(
                "📚 Langkah Perhitungan"
            )

            latex_matrix(A, "A")

            # -------------------------------------------------
            # 1 x 1
            # -------------------------------------------------

            if n == 1:

                hasil = A[0, 0]

                st.latex(
                    rf"\det(A)={fmt(hasil)}"
                )

            # -------------------------------------------------
            # 2 x 2
            # -------------------------------------------------

            elif n == 2:

                a = A[0, 0]
                b = A[0, 1]
                c = A[1, 0]
                d = A[1, 1]

                st.latex(
                    r"""
                    \det(A)=ad-bc
                    """
                )

                st.latex(
                    rf"""
                    \det(A)
                    =
                    ({fmt(a)})({fmt(d)})
                    -
                    ({fmt(b)})({fmt(c)})
                    """
                )

                hasil = (
                    a*d -
                    b*c
                )

                st.latex(
                    rf"""
                    ={fmt(a*d)}
                    -
                    {fmt(b*c)}
                    =
                    {fmt(hasil)}
                    """
                )

            # -------------------------------------------------
            # 3 x 3
            # -------------------------------------------------

            elif n == 3:

                a, b, c = A[0]
                d, e, f = A[1]
                g, h, i = A[2]

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

                bagian1 = e*i - f*h
                bagian2 = d*i - f*g
                bagian3 = d*h - e*g

                st.latex(
                    rf"""
                    =
                    ({fmt(a)})({fmt(bagian1)})
                    -
                    ({fmt(b)})({fmt(bagian2)})
                    +
                    ({fmt(c)})({fmt(bagian3)})
                    """
                )

                hasil = (
                    a*bagian1
                    -
                    b*bagian2
                    +
                    c*bagian3
                )

                st.latex(
                    rf"\det(A)={fmt(hasil)}"
                )

            # -------------------------------------------------
            # > 3 x 3
            # -------------------------------------------------

            else:

                hasil = np.linalg.det(A)

                st.write(
                    "Untuk matriks berukuran "
                    "lebih dari 3 × 3, digunakan "
                    "eliminasi Gauss."
                )

                U, langkah = gauss_elimination(A)

                tampilkan_langkah(
                    langkah
                )

                diagonal = np.diag(U)

                st.write(
                    "Setelah matriks berada dalam "
                    "bentuk segitiga atas:"
                )

                latex_matrix(
                    U
                )

                st.write(
                    "Determinan diperoleh dari "
                    "perkalian elemen diagonal "
                    "utama, dengan memperhatikan "
                    "pertukaran baris."
                )

                st.latex(
                    rf"\det(A)={fmt(hasil)}"
                )

            st.success(
                f"Determinan = {fmt(hasil)}"
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

            det = np.linalg.det(A)

            st.subheader(
                "📚 Langkah Perhitungan"
            )

            latex_matrix(A, "A")
#==========================================================
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
    )
(
    
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

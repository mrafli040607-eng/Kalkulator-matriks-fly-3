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
)

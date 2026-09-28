import streamlit as st
import numpy as np
import pandas as pd

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Kalkulator Matriks",
    page_icon="🔢",
    layout="centered"
)

st.title("🔢 Kalkulator Matriks")
st.write("Masukkan nilai matriks pada tabel di bawah.")

st.divider()


# ==========================================
# FUNGSI INPUT MATRIKS
# ==========================================

def buat_matriks(nama, baris, kolom, key):

    st.subheader(nama)

    # Membuat matriks awal berisi angka 0
    data_awal = np.zeros((baris, kolom))

    # Nama kolom
    nama_kolom = [f"Kolom {j+1}" for j in range(kolom)]

    # Nama baris
    nama_baris = [f"Baris {i+1}" for i in range(baris)]

    df_awal = pd.DataFrame(
        data_awal,
        index=nama_baris,
        columns=nama_kolom
    )

    # Tabel yang bisa diedit
    data = st.data_editor(
        df_awal,
        key=key,
        use_container_width=True,
        num_rows="fixed"
    )

    return data.to_numpy(dtype=float)


# ==========================================
# PILIH OPERASI
# ==========================================

operasi = st.selectbox(
    "Pilih Operasi",
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


# ==========================================
# UKURAN MATRIKS A
# ==========================================

st.subheader("Ukuran Matriks A")

col1, col2 = st.columns(2)

with col1:
    baris_a = st.number_input(
        "Jumlah Baris",
        min_value=1,
        max_value=6,
        value=2,
        step=1
    )

with col2:
    kolom_a = st.number_input(
        "Jumlah Kolom",
        min_value=1,
        max_value=6,
        value=2,
        step=1
    )


# ==========================================
# MATRIKS A
# ==========================================

A = buat_matriks(
    "Matriks A",
    int(baris_a),
    int(kolom_a),
    "matriks_A"
)


# ==========================================
# MATRIKS B
# ==========================================

B = None

if operasi in [
    "Penjumlahan",
    "Pengurangan",
    "Perkalian"
]:

    st.divider()

    st.subheader("Matriks B")

    if operasi == "Perkalian":

        st.info(
            "Untuk perkalian A × B, "
            "jumlah kolom A harus sama dengan "
            "jumlah baris B."
        )

        baris_b = int(kolom_a)

        kolom_b = st.number_input(
            "Jumlah Kolom B",
            min_value=1,
            max_value=6,
            value=2,
            step=1
        )

    else:

        baris_b = int(baris_a)
        kolom_b = int(kolom_a)

    B = buat_matriks(
        "Matriks B",
        baris_b,
        int(kolom_b),
        "matriks_B"
    )


# ==========================================
# TOMBOL HITUNG
# ==========================================

st.divider()

if st.button(
    "🔢 HITUNG",
    type="primary",
    use_container_width=True
):

    # ======================================
    # PENJUMLAHAN
    # ======================================

    if operasi == "Penjumlahan":

        hasil = A + B

        st.success("Perhitungan berhasil!")

        st.subheader("Hasil A + B")

        st.dataframe(
            hasil,
            use_container_width=True
        )


    # ======================================
    # PENGURANGAN
    # ======================================

    elif operasi == "Pengurangan":

        hasil = A - B

        st.success("Perhitungan berhasil!")

        st.subheader("Hasil A - B")

        st.dataframe(
            hasil,
            use_container_width=True
        )


    # ======================================
    # PERKALIAN
    # ======================================

    elif operasi == "Perkalian":

        if A.shape[1] != B.shape[0]:

            st.error(
                "Perkalian tidak dapat dilakukan. "
                "Jumlah kolom A harus sama dengan "
                "jumlah baris B."
            )

        else:

            hasil = A @ B

            st.success("Perhitungan berhasil!")

            st.subheader("Hasil A × B")

            st.dataframe(
                hasil,
                use_container_width=True
            )


    # ======================================
    # TRANSPOSE
    # ======================================

    elif operasi == "Transpose":

        hasil = A.T

        st.success("Transpose berhasil!")

        st.subheader("Transpose Matriks A")

        st.dataframe(
            hasil,
            use_container_width=True
        )


    # ======================================
    # DETERMINAN
    # ======================================

    elif operasi == "Determinan":

        if baris_a != kolom_a:

            st.error(
                "Determinan hanya dapat dihitung "
                "pada matriks persegi."
            )

        else:

            hasil = np.linalg.det(A)

            st.success("Determinan berhasil dihitung!")

            st.subheader("Hasil Determinan")

            st.write(
                f"**det(A) = {hasil:.4f}**"
            )


    # ======================================
    # INVERS
    # ======================================

    elif operasi == "Invers":

        if baris_a != kolom_a:

            st.error(
                "Invers hanya dapat dihitung "
                "pada matriks persegi."
            )

        else:

            determinan = np.linalg.det(A)

            if abs(determinan) < 1e-10:

                st.error(
                    "Matriks tidak memiliki invers "
                    "karena determinannya = 0."
                )

            else:

                hasil = np.linalg.inv(A)

                st.success("Invers berhasil dihitung!")

                st.subheader("A⁻¹")

                st.dataframe(
                    hasil,
                    use_container_width=True
                )


    # ======================================
    # RANK
    # ======================================

    elif operasi == "Rank":

        hasil = np.linalg.matrix_rank(A)

        st.success("Rank berhasil dihitung!")

        st.subheader("Rank Matriks A")

        st.write(
            f"**Rank(A) = {hasil}**"
        )


    # ======================================
    # TRACE
    # ======================================

    elif operasi == "Trace":

        if baris_a != kolom_a:

            st.error(
                "Trace hanya dapat dihitung "
                "pada matriks persegi."
            )

        else:

            hasil = np.trace(A)

            st.success("Trace berhasil dihitung!")

            st.subheader("Trace Matriks A")

            st.write(
                f"**Tr(A) = {hasil}**"
            )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Kalkulator Matriks | Python + Streamlit + NumPy"
)

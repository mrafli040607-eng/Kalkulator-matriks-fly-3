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
    "Aplikasi Kalkulator Matriks dengan langkah-langkah "
    "penyelesaian menggunakan Python."
)

st.divider()


# =========================================================
# FUNGSI MEMBUAT INPUT MATRIKS
# =========================================================

def buat_matriks(nama, baris, kolom, key):

    st.subheader(nama)

    data_awal = np.zeros((baris, kolom))

    nama_baris = [f"Baris {i + 1}" for i in range(baris)]
    nama_kolom = [f"Kolom {j + 1}" for j in range(kolom)]

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

def fmt(x):
    if abs(x) < 1e-10:
        x = 0

    if float(x).is_integer():
        return str(int(x))

    return f"{x:.4f}"


# =========================================================
# FUNGSI MENAMPILKAN MATRIKS
# =========================================================

def tampilkan_matriks(M):
    return pd.DataFrame(
        [[fmt(x) for x in row] for row in M]
    )


# =========================================================
# FUNGSI LANGKAH PENJUMLAHAN
# =========================================================

def langkah_penjumlahan(A, B):

    st.subheader("📌 Langkah-Langkah Penjumlahan")

    st.write(
        "Penjumlahan matriks dilakukan dengan menjumlahkan "
        "elemen yang berada pada posisi yang sama."
    )

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):

            st.latex(
                rf"C_{{{i+1}{j+1}}}"
                rf" = {fmt(A[i,j])} + {fmt(B[i,j])}"
                rf" = {fmt(A[i,j] + B[i,j])}"
            )


# =========================================================
# FUNGSI LANGKAH PENGURANGAN
# =========================================================

def langkah_pengurangan(A, B):

    st.subheader("📌 Langkah-Langkah Pengurangan")

    st.write(
        "Pengurangan matriks dilakukan dengan mengurangkan "
        "elemen yang berada pada posisi yang sama."
    )

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):

            st.latex(
                rf"C_{{{i+1}{j+1}}}"
                rf" = {fmt(A[i,j])} - {fmt(B[i,j])}"
                rf" = {fmt(A[i,j] - B[i,j])}"
            )


# =========================================================
# FUNGSI LANGKAH PERKALIAN
# =========================================================

def langkah_perkalian(A, B):

    st.subheader("📌 Langkah-Langkah Perkalian")

    st.write(
        "Perkalian matriks dilakukan dengan mengalikan setiap "
        "baris Matriks A dengan setiap kolom Matriks B."
    )

    hasil = A @ B

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):

            bagian = []

            for k in range(A.shape[1]):
                bagian.append(
                    f"({fmt(A[i,k])} × {fmt(B[k,j])})"
                )

            operasi = " + ".join(bagian)

            nilai = []

            for k in range(A.shape[1]):
                nilai.append(
                    A[i,k] * B[k,j]
                )

            penjumlahan = " + ".join(
                fmt(x) for x in nilai
            )

            st.latex(
                rf"C_{{{i+1}{j+1}}}"
                rf" = {operasi}"
                rf" = {penjumlahan}"
                rf" = {fmt(hasil[i,j])}"
            )


# =========================================================
# FUNGSI LANGKAH TRANSPOSE
# =========================================================

def langkah_transpose(A):

    st.subheader("📌 Langkah-Langkah Transpose")

    st.write(
        "Transpose dilakukan dengan mengubah baris menjadi "
        "kolom dan kolom menjadi baris."
    )

    for i in range(A.shape[1]):

        isi = " , ".join(
            fmt(A[j, i]) for j in range(A.shape[0])
        )

        st.latex(
            rf"\text{{Kolom {i+1} menjadi Baris {i+1}: }}"
            rf"\quad [{isi}]"
        )


# =========================================================
# FUNGSI LANGKAH DETERMINAN
# =========================================================

def langkah_determinan(A):

    n = A.shape[0]

    st.subheader("📌 Langkah-Langkah Determinan")

    if n == 1:

        st.latex(
            rf"\det(A) = {fmt(A[0,0])}"
        )

    elif n == 2:

        st.write("Untuk matriks 2 × 2:")

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
            rf"\det(A) = (a \times d) - (b \times c)"
        )

        st.latex(
            rf"\det(A) = "
            rf"({fmt(A[0,0])} \times {fmt(A[1,1])})"
            rf" - "
            rf"({fmt(A[0,1])} \times {fmt(A[1,0])})"
        )

        st.latex(
            rf"\det(A) = {fmt(A[0,0] * A[1,1])}"
            rf" - {fmt(A[0,1] * A[1,0])}"
        )

        st.latex(
            rf"\det(A) = {fmt(np.linalg.det(A))}"
        )

    else:

        st.write(
            "Untuk matriks berukuran lebih dari 2 × 2, "
            "determinan dihitung menggunakan ekspansi kofaktor."
        )

        for j in range(n):

            minor = np.delete(
                np.delete(A, 0, axis=0),
                j,
                axis=1
            )

            tanda = (-1) ** j

            st.latex(
                rf"C_{{1,{j+1}}}"
                rf" = (-1)^{{1+{j+1}}}"
                rf"\det(M_{{1,{j+1}}})"
            )

        st.write(
            "Perhitungan lengkap menghasilkan:"
        )

        st.latex(
            rf"\det(A) = {fmt(np.linalg.det(A))}"
        )


# =========================================================
# FUNGSI LANGKAH INVERS
# =========================================================

def langkah_invers(A):

    n = A.shape[0]

    st.subheader("📌 Langkah-Langkah Invers Matriks")

    st.write(
        "Invers matriks dihitung menggunakan metode "
        "Gauss-Jordan."
    )

    st.write("Langkah 1: Bentuk matriks augmented [A | I].")

    identitas = np.eye(n)

    augmented = np.hstack((A, identitas))

    st.dataframe(
        tampilkan_matriks(augmented),
        use_container_width=True,
        hide_index=True
    )

    st.write(
        "Langkah 2: Lakukan operasi baris elementer "
        "hingga bagian kiri menjadi matriks identitas."
    )

    M = augmented.astype(float)

    for i in range(n):

        pivot = M[i, i]

        if abs(pivot) < 1e-10:

            for r in range(i + 1, n):

                if abs(M[r, i]) > 1e-10:

                    M[[i, r]] = M[[r, i]]
                    break

        pivot = M[i, i]

        if abs(pivot) < 1e-10:
            continue

        # Membuat pivot menjadi 1
        M[i] = M[i] / pivot

        st.write(
            f"Pivot baris {i+1} dibuat menjadi 1."
        )

        st.dataframe(
            tampilkan_matriks(M),
            use_container_width=True,
            hide_index=True
        )

        # Membuat elemen lain pada kolom pivot menjadi 0
        for r in range(n):

            if r != i:

                faktor = M[r, i]

                if abs(faktor) > 1e-10:

                    M[r] = M[r] - faktor * M[i]

                    st.write(
                        f"Baris {r+1} dikurangi "
                        f"({fmt(faktor)}) × Baris {i+1}"
                    )

                    st.dataframe(
                        tampilkan_matriks(M),
                        use_container_width=True,
                        hide_index=True
                    )

    st.write(
        "Langkah 3: Bagian kanan dari matriks augmented "
        "merupakan matriks invers."
    )

    invers = M[:, n:]

    st.dataframe(
        tampilkan_matriks(invers),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# FUNGSI LANGKAH RANK
# =========================================================

def langkah_rank(A):

    st.subheader("📌 Langkah-Langkah Rank")

    st.write(
        "Rank matriks ditentukan berdasarkan jumlah baris "
        "atau kolom yang bebas secara linear setelah "
        "dilakukan eliminasi baris."
    )

    M = A.astype(float).copy()

    baris, kolom = M.shape

    rank = 0

    for col in range(kolom):

        pivot = None

        for row in range(rank, baris):

            if abs(M[row, col]) > 1e-10:
                pivot = row
                break

        if pivot is None:
            continue

        M[[rank, pivot]] = M[[pivot, rank]]

        M[rank] = M[rank] / M[rank, col]

        for row in range(baris):

            if row != rank:

                faktor = M[row, col]

                M[row] = M[row] - faktor * M[rank]

        rank += 1

        st.write(
            f"Setelah eliminasi kolom {col+1}:"
        )

        st.dataframe(
            tampilkan_matriks(M),
            use_container_width=True,
            hide_index=True
        )

        if rank == baris:
            break

    st.latex(
        rf"\operatorname{{rank}}(A) = {rank}"
    )


# =========================================================
# FUNGSI LANGKAH TRACE
# =========================================================

def langkah_trace(A):

    n = A.shape[0]

    st.subheader("📌 Langkah-Langkah Trace")

    st.write(
        "Trace adalah jumlah seluruh elemen pada diagonal utama."
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

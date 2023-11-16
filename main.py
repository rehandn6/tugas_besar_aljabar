import streamlit as st
import numpy as np
import pandas as pd


st.title("Aplikasi Input Output")
with st.container():
    st.write("Analisis Input-Ouput (I-O) adalah suatu model matematis untuk menganalisis keterkaitan antar sektor dalam suatu perekonomian. ")
    st.write("Tujuan aplikasi ini untuk menghitung permintaan akhir agar dapat terpenuhi berdasarkan sektor-sektor yang telah ditentukan maka harus memproduksi barang/ output berturut-turut senilai berapa rupiah.")


st.write("---")    
menentukan  = st.selectbox("Silahkan pilih jumlah sektor", ["3 sektor", "6 sektor", "9 sektor"])

identitas6x6 = np.array([   [1, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 1]])

identitas9x9 = np.array([   [1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1]
                        ])

matrix_a = np.array([       [0.0366, 0.0000, 0.1766, 0.0000, 0.0000, 0.0159, 0.0010, 0.0000, 0.0045],
                            [0.0001, 0.0989, 0.0257, 0.0049, 0.1719, 0.0013, 0.0023, 0.0018, 0.0025],
                            [0.0079, 0.0135, 0.0479, 0.0038, 0.0394, 0.0248, 0.0216, 0.0045, 0.0191],
                            [0.0002, 0.0053, 0.0089, 0.3783, 0.0019, 0.0141, 0.0122, 0.0016, 0.0274],
                            [0.0040, 0.0161, 0.0012, 0.0045, 0.0363, 0.0108, 0.0049, 0.0247, 0.0059],
                            [0.0101, 0.0203, 0.0544, 0.0239, 0.0383, 0.0221, 0.0571, 0.0079, 0.0596],
                            [0.0031, 0.0515, 0.0210, 0.0119, 0.0183, 0.0386, 0.0766, 0.0248, 0.0678],
                            [0.0039, 0.0317, 0.0083, 0.0318, 0.0318, 0.0375, 0.0241, 0.0350, 0.0241],
                            [0.0013, 0.0014, 0.0041, 0.0043, 0.0015, 0.0032, 0.0202, 0.0058, 0.0098]
                        ])


def input_matrix3x3(label):
    matrix = np.zeros((3, 3))
    columns = st.columns(3)
    for i in range(3):
        for j in range(3):
            matrix[i][j] = columns[j].number_input(f' ({i+1}, {j+1})', value=0.0, format="%.4f", key=f'{label}-{i}-{j}')
    return matrix

def input_permintaan3x3(label):
    matrix = np.zeros((3, 1))
    for i in range(3):
        for j in range(1):
            matrix[i][j] = st.number_input(f'Masukan nilai permintaan akhir {i+1}', value=0.0, format="%.2f", key=f'{label}-{i}-{j}')
    return matrix

def input_matrix6x6(label):
    matrix = np.zeros((6, 6))
    columns = st.columns(6)
    for i in range(6):
        for j in range(6):
            matrix[i][j] = columns[j].number_input(f' ({i+1}, {j+1})', value=0.0, format="%.4f", key=f'{label}-{i}-{j}')
    return matrix

def input_permintaan6x6(label):
    matrix = np.zeros((6, 1))
    for i in range(6):
        for j in range(1):
            matrix[i][j] = st.number_input(f'Masukan nilai permintaan akhir {i+1}', value=0.0, format="%.2f", key=f'{label}-{i}-{j}')
    return matrix

def input_permintaan9x9(label):
    matrix = np.zeros((9, 1))
    for i in range(9):
        for j in range(1):
            matrix[i][j] = st.number_input(f'Masukan nilai permintaan akhir {i+1}', value=0.0, format="%.2f", key=f'{label}-{i}-{j}')
    return matrix

def main3x3():
    st.header("Matriks Koefisien Teknis 3 Sektor:")
    matrix_a = input_matrix3x3("A")
    identity_matrix = np.eye(3)
    result_matrix = identity_matrix - matrix_a
    inverse_matrix = np.linalg.inv(result_matrix)
    st.write("Matriks Input Anda")
    st.write(matrix_a)
    st.write("---")
    st.header("Permintaan Akhir")
    demand_matrix = input_permintaan3x3("D")
    st.write("---")
    st.header("Hasil : ")
    final_result = np.dot(inverse_matrix, demand_matrix)
    # st.write(final_result)

    col1, col2 = st.columns(2)
    with col1 :
        chart_data = pd.DataFrame(final_result, columns=[" "])
        st.bar_chart(chart_data)
    with col2 :
        st.write(" 0 = Sektor 1" )
        st.write(" 1 = Sektor 2" )
        st.write(" 2 = Sektor 3" )
    
    a =final_result[0]
    st.write(f"Sektor 1 harus memproduksi barang/output senilai Rp. {a} Juta ")
    b =final_result[1]
    st.write(f"Sektor 2 harus memproduksi barang/output senilai Rp. {b} Juta")
    c =final_result[2]
    st.write(f"Sektor 3 harus memproduksi barang/output senilai  Rp. {c} Juta" )
    
def main6x6():
    st.header("Matriks Koefisien Teknis 6 Sektor:")
    matrix_a = input_matrix6x6("A")
    result_matrix =identitas6x6 - matrix_a
    inverse_matrix = np.linalg.inv(result_matrix)

    st.write("Matriks Input Anda")
    st.write(matrix_a)

    st.write("---")
    st.header("Permintaan Akhir")
    demand_matrix = input_permintaan6x6("D")

    st.write("---")
    st.header("Hasil : ")
    final_result = np.dot(inverse_matrix, demand_matrix)
    # st.write(final_result)

    col1, col2 = st.columns(2)
    with col1 :
        chart_data = pd.DataFrame(final_result, columns=[" "])
        st.bar_chart(chart_data)
    with col2 :
        st.write(" 0 = Sektor 1" )
        st.write(" 1 = Sektor 2" )
        st.write(" 2 = Sektor 3" )
        st.write(" 3 = Sektor 4" )
        st.write(" 4 = Sektor 5" )
        st.write(" 5 = Sektor 6" )

    a =final_result[0]
    st.write(f"Sektor 1 harus memproduksi barang/output senilai Rp. {a} Juta ")
    b =final_result[1]
    st.write(f"Sektor 2 harus memproduksi barang/output senilai Rp. {b} Juta")
    c =final_result[2]
    st.write(f"Sektor 3 harus memproduksi barang/output senilai  Rp. {c} Juta" )
    d =final_result[3]
    st.write(f"Sektor 4 harus memproduksi barang/output senilai Rp. {d} Juta ")
    e =final_result[4]
    st.write(f"Sektor 5 harus memproduksi barang/output senilai Rp. {e} Juta")
    f =final_result[5]
    st.write(f"Sektor 6 harus memproduksi barang/output senilai  Rp. {f} Juta" )
    

def main9x9():
    st.header("Matriks Koefisien Teknis 9 Sektor:")
    result_matrix =identitas9x9  - matrix_a
    inverse_matrix = np.linalg.inv(result_matrix)
    st.write("Matriks Input")
    st.write(matrix_a)
    st.write("---")
    st.header("Permintaan Akhir")
    demand_matrix = input_permintaan9x9("D")
    st.write("---")
    st.header("Hasil : ")
    final_result = np.dot(inverse_matrix, demand_matrix)
    # st.write(final_result)
    col1, col2 = st.columns(2)
    with col1 :
        chart_data = pd.DataFrame(final_result, columns=[" "])
        st.bar_chart(chart_data)
    with col2 :
        st.write(" 0 = Sektor 1" )
        st.write(" 1 = Sektor 2" )
        st.write(" 2 = Sektor 3" )
        st.write(" 3 = Sektor 4" )
        st.write(" 4 = Sektor 5" )
        st.write(" 5 = Sektor 6" )
        st.write(" 6 = Sektor 7" )
        st.write(" 7 = Sektor 8" )
        st.write(" 8 = Sektor 9" )

    st.write(final_result)


# if __name__ == "__main__":
#     main()
if menentukan == "9 sektor":
    main9x9()

if menentukan == "6 sektor":
    main6x6()

if menentukan == "3 sektor":
    main3x3()



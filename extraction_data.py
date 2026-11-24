import pandas as pd

def extraction_data_Z_matrix(Z):
    df = pd.read_csv(Z, sep='\t', header=None)

    # === EXTRACTION OF COLUMN INDICES (C1:KUG1 and C2:KUG2) ===
    col_index_1 = df.iloc[0, 2:7989].values
    col_index_2 = df.iloc[1, 2:7989].values
    multi_col_index = pd.MultiIndex.from_arrays([col_index_1, col_index_2])

    # === LINE INDICATOR EXTRACTION (A4:A7990 and B4:B7990) ===
    row_index_1 = df.iloc[3:7990, 0].values  # Colonne A
    row_index_2 = df.iloc[3:7990, 1].values  # Colonne B
    multi_row_index = pd.MultiIndex.from_arrays([row_index_1, row_index_2])

    # === DATA EXTRACTION (C4:KUG7990) ===
    data = df.iloc[3:7990, 2:7989]

    # === DATAFRAME CREATION WITH MULTI-LEVEL INDICES ===
    df_final = pd.DataFrame(data.values, index=multi_row_index, columns=multi_col_index)
    return df_final


def extraction_data_Y_matrix(Y):
    df = pd.read_csv(Y, sep='\t', header=None)

    # === EXTRACTION OF COLUMN INDICES (C1:MG1 and C2:MG2) ===
    col_index_1 = df.iloc[0, 2:345].values
    col_index_2 = df.iloc[1, 2:345].values
    multi_col_index = pd.MultiIndex.from_arrays([col_index_1, col_index_2])

    # === LINE INDICATOR EXTRACTION (A4:A7990 and B4:B7990) ===
    row_index_1 = df.iloc[3:7990, 0].values  # Colonne A
    row_index_2 = df.iloc[3:7990, 1].values  # Colonne B
    multi_row_index = pd.MultiIndex.from_arrays([row_index_1, row_index_2])

    # === DATA EXTRACTION (C4:MG7990) ===
    data = df.iloc[3:7990, 2:345]

    # === DATAFRAME CREATION WITH MULTI-LEVEL INDICES ===
    df_final = pd.DataFrame(data.values, index=multi_row_index, columns=multi_col_index)
    return df_final


def extraction_data_x_matrix(x):
    df = pd.read_csv(x, sep='\t', header=None)

    # === LINE INDICATOR EXTRACTION (A2:A7988 and B2:B7988) ===
    row_index_1 = df.iloc[1:7988, 0].values  # Colonne A
    row_index_2 = df.iloc[1:7988, 1].values  # Colonne B
    multi_row_index = pd.MultiIndex.from_arrays([row_index_1, row_index_2])

    # === DATA EXTRACTION (C2:C7988) ===
    data = df.iloc[1:7988, 2]

    # === DATAFRAME CREATION WITH MULTI-LEVEL INDICES ===
    df_final = pd.DataFrame(data.values, index=multi_row_index, columns=['indout'])
    return df_final


def extraction_data_F_water_matrix(F):
    df = pd.read_csv(F, sep='\t', header=None)

    # === EXTRACTION OF COLUMN INDICES (B1:KUF1 and B2:KUF2) ===
    col_index_1 = df.iloc[0, 1:7989].values
    col_index_2 = df.iloc[1, 1:7989].values
    multi_col_index = pd.MultiIndex.from_arrays([col_index_1, col_index_2])

    # === LINE INDICATOR EXTRACTION (A4:A197) ===
    row_index_1 = df.iloc[3:197, 0].values  # Colonne A
    

    # === DATA EXTRACTION (C4:KUG7990) ===
    data = df.iloc[3:197, 1:7989]

    # === DATAFRAME CREATION WITH MULTI-LEVEL INDICES ===
    df_final = pd.DataFrame(data.values, index=row_index_1, columns=multi_col_index)
    return df_final


def extraction_data_F_airem_matrix(F):
    df = pd.read_csv(F, sep='\t', header=None)

    # === EXTRACTION OF COLUMN INDICES (B1:KUF1 and B2:KUF2) ===
    col_index_1 = df.iloc[0, 1:7989].values
    col_index_2 = df.iloc[1, 1:7989].values
    multi_col_index = pd.MultiIndex.from_arrays([col_index_1, col_index_2])

    # === LINE INDICATOR EXTRACTION (A4:A197) ===
    row_index_1 = df.iloc[3:421, 0].values  # Colonne A
    

    # === DATA EXTRACTION (C4:KUG7990) ===
    data = df.iloc[3:421, 1:7989]

    # === DATAFRAME CREATION WITH MULTI-LEVEL INDICES ===
    df_final = pd.DataFrame(data.values, index=row_index_1, columns=multi_col_index)
    return df_final

def extraction_data_F_land_matrix(F):
    df = pd.read_csv(F, sep='\t', header=None)

    # === EXTRACTION OF COLUMN INDICES (B1:KUF1 and B2:KUF2) ===
    col_index_1 = df.iloc[0, 1:7989].values
    col_index_2 = df.iloc[1, 1:7989].values
    multi_col_index = pd.MultiIndex.from_arrays([col_index_1, col_index_2])

    # === LINE INDICATOR EXTRACTION (A4:A197) ===
    row_index_1 = df.iloc[3:35, 0].values  # Colonne A
    

    # === DATA EXTRACTION (C4:KUG7990) ===
    data = df.iloc[3:35, 1:7989]

    # === DATAFRAME CREATION WITH MULTI-LEVEL INDICES ===
    df_final = pd.DataFrame(data.values, index=row_index_1, columns=multi_col_index)
    return df_final


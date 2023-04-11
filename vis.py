import pandas as pd  # dataframe library

filename = 'csv/kdrama_data.csv'
# filename = r"C:\Users\John Kim\Desktop\kdrama_data.csv"

df = pd.read_csv(filename)
df = df[['title', 'description', 'keywords',
         'genres', 'actors', 'director', 'screenwriter']]


def remove_chars(string):
    if isinstance(string, str) == False:
        return string
    remove_list = ["[", "]", "'"]
    for remove in remove_list:
        string = string.replace(remove, "")
    return string


def get_info(title):
    df = pd.read_csv(filename)
    fill_na()
    index = search_kdrama(title)

    row = df.loc[index]
    dicti = row.to_dict()
    # removes unnecessary characters
    columns = ['keywords', 'genres', 'actors']
    for column in columns:
        dicti[column] = remove_chars(dicti[column])
    return dicti


def get_desc_word_count(desc):
    word_list = desc.split(' ')
    word_count = len(word_list)
    return word_count


def get_titles():
    np_titles = df['title'].to_numpy()
    title_list = np_titles.tolist()
    return title_list


def kdrama_exists(title, klist):
    if title is None:
        return False
    for kdrama in klist:
        if title.lower() == kdrama.lower():
            return True
    return False


def fill_na():
    """replaces na values with an empty string"""
    df.replace("N/A", "")
    for label in df.columns:
        df[label] = df[label].fillna('')  # fills N/A values with ""


def get_indices():
    indices = pd.Series(df.index, index=df['title'])
    return indices[~indices.index.duplicated(keep='last')]


def search_kdrama(kdrama_name):
    """searches for kdrama with matching name and returns top result"""
    # return get_indices()[get_indices().index.str.contains(kdrama_name, regex=False, na=False)][0]
    return get_indices()[get_indices().index.str.contains(kdrama_name.lower(), case=False, regex=False, na=False)][0]

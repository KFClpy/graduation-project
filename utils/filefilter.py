def is_csv(filename):
    return '.' in filename and get_filetype(filename) == 'csv'


def get_filetype(filename):
    return filename.rsplit('.', 1)[1]

import dropbox

from get_enviroment import DROPBOX_KEY


class TransferData:
    def __init__(self):
        self.dbx = dropbox.Dropbox(DROPBOX_KEY)

    def uploadFile(self, file):
        with open('files/' + file, 'rb') as f:
            self.dbx.files_upload(f.read(), '/' + file, mode=dropbox.files.WriteMode.overwrite)

    def downloadFile(self, file):
        self.dbx.files_download_to_file('files/' + file, '/' + file)

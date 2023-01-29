import sys
from pathlib import Path

IMAGES = []
AUDIO = []
VIDEO = []
ARCHIVES = []
DOCUMENTS = []
OTHER = []

REGISTER_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'BMP': IMAGES,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'PDF': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # convert file extension to folder name .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # If it is a folder, then add it from the FOLDERS list and go to the next item in the folder
        if item.is_dir():
            # check that the folder is not the one where we already put files
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                # scan this subfolder - recursion
                scan(item)
            # go to the next item in the scanned folder
            continue

        # Work with a file
        ext = get_extension(item.name)  # take extension
        fullname = folder / item.name  # take full path to the file
        if not ext:  # if the file has no extension, add to unknown
            OTHER.append(fullname)
        else:
            try:
                # take a list of where to put the full path to the file
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # If we did not register the extension in REGISTER_EXTENSIONS, then add to another
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == '__main__':

    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images: {IMAGES}')
    print(f'Audio: {AUDIO}')
    print(f'Archives: {ARCHIVES}')
    print(f'Documents: {DOCUMENTS}')
    print(f'Video: {VIDEO}')

    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')

    print(FOLDERS[::-1])
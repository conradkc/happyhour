import argparse
import io, os
from datetime import datetime
from google.cloud import vision
from google.cloud.vision import types
from django.conf import settings





def ImageToStringTimeDuration(path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\CENTRIXSuser\\Happy Hour-f63bfc3b397d.json'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content= image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        block_strings = []
        time_strings = []
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            block_strings.append(format(block_text))
            time_indicators = ('AM','PM',':','am','pm')
            if any(s in format(block_text) for s in time_indicators):
                time_strings.append(format(block_text))
            print('Block Content: {}'.format(block_text))
            #print('Block Bounds:\n {}'.format(block.bounding_box))

    timestart, duration = ConvertToStartDuration(time_strings)

    return '\n'.join(block_strings),timestart,duration

def ConvertToStartDuration(time_strings):
    format = '%I:%M%p'
    timestart = []
    duration = []
    for timerange in time_strings:
        startstring = timerange.split('-')[0]
        timestart.append(datetime.strptime(startstring,format))
        endstring = timerange.split('-')[1]
        timeend = datetime.strptime(endstring, format)
        duration.append(timeend-datetime.strptime(startstring,format))

    return timestart,duration


# settings.configure()
# root_path = settings.BASE_DIR
# path = os.path.join(root_path,'happyhour','media','Fete Hawaii.jpg')
# print(ImageToStringTimeDuration(path))
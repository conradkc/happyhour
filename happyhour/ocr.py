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
            #print('Block Content: {}'.format(block_text))
            #print('Block Bounds:\n {}'.format(block.bounding_box))

    #timestart, duration = ConvertToStartDuration(time_strings)

    return '\n'.join(block_strings)


def timerange_to_start_duration(timerange):
    for separator in ('-', 'till', 'Till', 'TILL'):
        try:
            # get times and split by '-' eg. 2:30pm-5:30pm -> 2:30pm start and 5:30pm end
            start_string = timerange.split(separator)[0]
            #print(start_string)
            end_string = timerange.split(separator)[1]
            #print(end_string)
            # get am or pm from second time e.g. 2-5pm -> 2pm-5pm
            if start_string[-1:] != 'm' or 'M':
               start_string = start_string + end_string[-2:]
            # convert to datetime field
            start_time = try_parsing_time(start_string)
            end_time = try_parsing_time(end_string)
            duration = end_time - start_time
            return start_time, duration
        except IndexError:
            pass
    raise ValueError('time range does not fit any format')




def try_parsing_time(text):
    for fmt in ('%I:%M%p', '%I%p'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid time format found in: ' + text)

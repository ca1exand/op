def remove_lines_w_urls(line):
    if (re.match('.*http.*',line) or re.match('.*www\..*',line)):
        return None
    return line

def remove_replies(line):
    line = re.sub('@[^\s]*\s','',line)
    return line

def only_letters(line):
    line = re.sub('[^a-z\s]','',line)
    return line
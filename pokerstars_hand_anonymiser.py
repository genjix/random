import glob, re, random, functools, time, logging
"""Requires an input directory filled with HHs called hands/ and an output directory called complete/"""
nickname="genjix"
replacement_nickname="XXXXXXXXXXX"
fake_date="2008/01/01 5:00:00 WET [2008/01/01 0:00:00 ET]\n"

random.seed(time.time())

check_header = re.compile(".?PokerStars Game #\d+:  [a-zA-Z' ]+ \(\$[0-9./]+\$[0-9./]+ [A-Z]{3,4}\) - \d{4}\/\d{2}\/\d{2} \d{1,2}:\d{2}:\d{2}")
find_game_type = re.compile(":  [a-zA-Z' ]+ \(\$[0-9./]+\$[0-9./]+ [A-Z]{3,4}\) - ")

kill_your_cards = re.compile("\[[AKQJT2-9][shcd] [AKQJT2-9][shcd]\]")

def new_output_file():
    return open("complete/" + str(round(random.random()*20))+".txt", "a")
current_output_filehandle = None

handtext_buffer = None
logging.basicConfig(level=logging.INFO)

# find all .txt files in current directory
handhistory_filenames = glob.glob("hands/*.txt")
for filename in handhistory_filenames:
    logging.info("%s ...", filename)
    with open(filename,mode="rb") as input_hh_filehandle:
        for binaryline in input_hh_filehandle:
            try:
                line = binaryline.decode()
            except UnicodeDecodeError:
                logging.warning("Skipping hand due to read error...")
                handtext_buffer = None
                continue
            if nickname in line:
                line = line.replace(nickname,replacement_nickname)
                line = kill_your_cards.sub("[7s 2c]", line)
            elif "Tournament" in line:
                handtext_buffer = None
            elif check_header.match(line):
                if handtext_buffer is not None:
                    with new_output_file() as output_filehandle:
                        try:
                            output_filehandle.write(handtext_buffer)
                        except UnicodeEncodeError:
                            logging.error("Skipping write on line: %s", line)
                handtext_buffer = ""
                game_type = find_game_type.search(line).group()
                random_game_number = \
                    functools.reduce(
                        lambda s, n: s + str(round(random.random()*9)),
                        range(11), "#")
                line = "PokerStars Game "+random_game_number+game_type+fake_date
            if handtext_buffer is not None:
                handtext_buffer += line

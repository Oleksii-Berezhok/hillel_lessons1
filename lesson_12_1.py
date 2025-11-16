import codecs 
def delete_html_tags(html_file, result_file='cleaned.txt'):
    inside_tag = False
    previous_empty = False

    with codecs.open(html_file, 'r', 'utf-8') as file, \
         codecs.open(result_file, 'w', 'utf-8') as cleaned:

        for line in file:
            cleaned_line = ""
            i = 0

            while i < len(line):
                char = line[i]

                if char == '<':
                    inside_tag = True

                if inside_tag:
                    if char == '>':
                        inside_tag = False
                    i += 1
                    continue
                cleaned_line += char
                i += 1
                cleaned_line = cleaned_line.strip()

            if cleaned_line == "":
                if previous_empty:  # пропускаємо, бо вже був порожній
                    continue
                previous_empty = True
            else:
                previous_empty = False

            cleaned.write(cleaned_line.strip() + "\n")

delete_html_tags("draft.html")
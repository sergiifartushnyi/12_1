import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_content = re.sub(r'<[^>]*>', '', html)

    cleaned_lines = [line.strip() for line in cleaned_content.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(cleaned_lines))


    print(f"Очищений текст успішно записано у файл '{result_file}'")

delete_html_tags('draft.html')

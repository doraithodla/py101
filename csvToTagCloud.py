import csv


def read_csv(filename="freq.csv"):
    """
    reads a csv file and returns the object
    :param filename: csv file to be read
    :return: csv object
    """
    csv_content = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for rows in csv_reader:
            csv_content.append(rows)
    return csv_content


def format_html(tags):
    """
    converts tags into html form
    :param tags: word and it's frequency
    :return: html content
    """
    html = "<html><head>HTML Word Cloud</head><body>"
    html += """<div id="my_favorite_latin_words" style="width: 550px; height: 350px; border: 1px solid #ccc;"></div>"""
    html += """</body><style>/** * Tooltip Styles */ /* Add this attribute to the element that needs a tooltip */ [data-tooltip] { position: relative; z-index: 9999999; cursor: pointer; } /* Hide the tooltip content by default */ [data-tooltip]:before, [data-tooltip]:after { visibility: hidden; -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)"; filter: progid: DXImageTransform.Microsoft.Alpha(Opacity=0); opacity: 0; pointer-events: none; } /* Position tooltip above the element */ [data-tooltip]:before { position: absolute; bottom: 80%; left: 50%; margin-bottom: 5px; margin-left: -30px; padding: 7px; width: 60px; -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; background-color: #000; background-color: hsla(0, 0%, 20%, 0.9); color: #fff; content: attr(data-tooltip); text-align: center; font-size: 14px; line-height: 1.2; } /* Triangle hack to make tooltip look like a speech bubble */ [data-tooltip]:after { position: absolute; bottom: 80%; left: 50%; margin-left: 1px; width: 0; border-top: 5px solid #000; border-top: 5px solid hsla(0, 0%, 20%, 0.9); border-right: 5px solid transparent; border-left: 5px solid transparent; content: " "; font-size: 0; line-height: 0; } /* Show tooltip content on hover */ [data-tooltip]:hover:before, [data-tooltip]:hover:after { visibility: visible; -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)"; filter: progid: DXImageTransform.Microsoft.Alpha(Opacity=100); opacity: 1; z-index: 9999999; } </style>"""
    html += """ <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>"""
    html += """ <script src="https://cdnjs.cloudflare.com/ajax/libs/jqcloud/1.0.4/jqcloud-1.0.4.min.js"></script>"""

    html += """<script>var word_list = ["""
    for tag in tags:
        word = tag[0]
        freq = tag[1]
        html += """{text: " """ + word + """ ", weight: """ + freq + """, html: {"data-tooltip": " """ + freq + """ "}},"""
    html += """]; $(function() { $("#my_favorite_latin_words").jQCloud(word_list, { shape: "rectangular", autoResize: true }); });"""
    html += "</script>"
    html += "</html>"

    return html


def save_to_file(filename, html):
    """
    saves text to a html file
    :return: None
    """
    with open(filename, "w") as f:
        f.write(html)


if __name__ == '__main__':
    csv_content = read_csv()
    html = format_html(csv_content[1:])
    save_to_file("freq.html", html)

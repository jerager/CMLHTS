def methodJ(self, word, width=80, lines=25):
    """
        Print concordance lines given the query word.
        :param word: The target word
        :type word: str
        :param lines: The number of lines to display (default=25)
        :type lines: int
        :param width: The width of each line, in characters (default=80)
        :type width: int
        :param save: The option to save the concordance.
        :type save: bool
    """
    concordance_list = self.find_concordance(word, width, lines)

    if not concordance_list:
        print("no matches")
    else:
        lines = min(lines, len(concordance_list))
        print("Displaying {} of {} matches:".format(lines,len(concordance_list)))
        for i, concordance_line in enumerate(concordance_list[:lines]):
            print(concordance_line.line)

nltk.text.ConcordanceIndex.print_concordance = methodJ

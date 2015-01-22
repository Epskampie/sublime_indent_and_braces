import sublime
import sublime_plugin

def get_indentation_on_line(view, point):
    pt = view.line(point).begin()
    result = ''
    while True:
        c = view.substr(pt)
        if c == " " or c == "\t":
            pt += 1
            result += c
        else:
            break

    return result

class IndentAndBracesCommand(sublime_plugin.TextCommand):
    def run(self, edit, from_cursor = None, opening_brace = '{', closing_brace = '}'):
        sel = self.view.sel()
        for r in tuple(reversed(sel)):
            if from_cursor == None:
                # from_cursor not set, determine it intelligently
                from_cursor = (r.begin() == self.view.line(r.begin()).end())

            region_end = self.view.line(r.end()).end()
            if self.view.classify(r.end()) & sublime.CLASS_LINE_START:
                region_end = r.end() - 1

            if from_cursor:
                region = sublime.Region(r.begin(), region_end)
            else:
                region = sublime.Region(self.view.line(r.begin()).begin(), region_end)

            indent = get_indentation_on_line(self.view, region.begin())
            if from_cursor:
                insert_start = opening_brace
            else:
                insert_start = indent + opening_brace + "\n"
            insert_end = '\n' + indent + closing_brace

            self.view.insert(edit, region.begin(), insert_start)
            self.view.insert(edit, region.end() + len(insert_start), insert_end)

            indent_region = sublime.Region(region.begin() + len(insert_start) + 1, region.end() + len(insert_start))
            num_lines_indented = len(self.view.lines(indent_region))

            self.view.sel().clear()
            self.view.sel().add(indent_region)
            self.view.run_command('indent')

            sel.clear()
            settings = self.view.settings()
            if from_cursor:
                # Move cursor to beyond last brace
                pt = region.end() + len(insert_start) + len(insert_end) + num_lines_indented * (settings.get('tab_size') if settings.get('translate_tabs_to_spaces') else 1)
            else:
                pt = region.begin() + len(indent)
            sel.add(sublime.Region(pt, pt))
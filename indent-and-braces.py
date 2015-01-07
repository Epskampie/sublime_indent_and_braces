import sublime
import sublime_plugin
import copy

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
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        # self.view.run_command('indent')
        sel = self.view.sel()
        # print(sel[0].a)
        for r in copy.deepcopy(sel):
            region = sublime.Region(self.view.line(r.begin()).begin(), self.view.line(r.end()).end())
            # content = view.substr(region)
            
            indent = get_indentation_on_line(self.view, region.begin())
            
            insert_start = indent + "{\n"
            insert_end = "\n" + indent + '}'
            
            self.view.insert(edit, region.begin(), insert_start)
            self.view.insert(edit, region.end() + len(insert_start), insert_end)
            
            sel.clear()
            sel.add(sublime.Region(region.begin() + len(insert_start), region.end() + len(insert_start)))
            self.view.run_command('indent')
            
            sel.clear()
            pt = region.begin() + len(indent)
            sel.add(sublime.Region(pt, pt))